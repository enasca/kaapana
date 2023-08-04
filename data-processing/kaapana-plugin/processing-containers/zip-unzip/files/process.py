import os
import glob
import pathlib
import zipfile
from shutil import copy2
from os.path import join, relpath, basename, dirname, exists

processed_count = 0


def unzip_file(zip_path, target_path):
    global processed_count

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(target_path)
    processed_count += 1


def zip_dir(zip_dir_path, target_file):
    global processed_count

    print(f"# Zipping {zip_dir_path} --> {target_file}")

    zipf = zipfile.ZipFile(target_file, "w", zipfile.ZIP_DEFLATED)
    whitelist_files = os.getenv("WHITELIST_FILES", "NONE").split(",")
    whitelist_files = None if whitelist_files[0] == "NONE" else whitelist_files
    blacklist_files = os.getenv("BLACKLIST_FILES", "NONE").split(",")
    blacklist_files = None if blacklist_files[0] == "NONE" else blacklist_files
    # info_files = os.getenv("INFO_FILES", "NONE").split(",")
    # info_files = None if info_files[0] == "NONE" else info_files
    # target_dir = dirname(target_file)
    print("#")
    print(f"# whitelist_files: {whitelist_files}")
    print(f"# blacklist_files: {blacklist_files}")
    print("#")

    for root, dirs, files in os.walk(zip_dir_path):
        for file in files:
            skip_file = None

            print("#")
            print(f"# Checking file {file}")

            # if info_files != None:
            #     for info_file in info_files:
            #         info_file = info_file.replace("*", "")
            #         index_found = file.find(info_file)
            #         if index_found != -1 and index_found + len(info_file) == len(file):
            #             target_info_file_path = join(target_dir, basename(file))
            #             info_file = join(root, file)
            #             print(f"# Found info-file: {info_file}")
            #             print(f"# Target: {target_info_file_path}")
            #             copy2(info_file, target_info_file_path)

            if blacklist_files != None:
                skip_file = False
                for blacklist_file in blacklist_files:
                    blacklist_file = blacklist_file.replace("*", "")
                    index_found = file.find(blacklist_file)
                    if index_found != -1 and index_found + len(blacklist_file) == len(
                        file
                    ):
                        print(f"# blacklist skip: {blacklist_file}")
                        skip_file = True
                        break

            if skip_file != None and skip_file:
                continue

            if whitelist_files != None:
                skip_file = True
                for whitelist_file in whitelist_files:
                    whitelist_file = whitelist_file.replace("*", "")
                    index_found = file.find(whitelist_file)
                    if index_found != -1 and index_found + len(whitelist_file) == len(
                        file
                    ):
                        print(f"# whitelist add {whitelist_file}")
                        skip_file = False
                        break

            if skip_file == None or not skip_file:
                print(f"# Adding: {file}")
                zipf.write(
                    join(root, file),
                    relpath(join(root.replace(zip_dir_path, ""), file), "/.."),
                )
                processed_count += 1
            else:
                print(f"# skipping: {file}")
            print("#")

    print("#")
    print("# ZIPPING DONE")
    print("#")

    zipf.close()


if __name__ == "__main__":
    target_filename = os.getenv("TARGET_FILENAME", "NONE")
    target_filename = None if target_filename == "NONE" else target_filename
    subdir = os.getenv("SUBDIR", "NONE")
    subdir = "" if subdir == "NONE" else subdir
    mode = os.getenv("MODE", "unzip").lower().strip()
    batch_level = True if os.getenv("BATCH_LEVEL", "False").lower() == "true" else False

    print("##################################################")
    print("#")
    print("# Starting ZIP-UNZIP ...")
    print("#")
    print(f"# mode:        {mode}")
    print(f"# batch_level: {batch_level}")
    print("#")

    batch_folders = sorted(
        [
            f
            for f in glob.glob(
                join("/", os.environ["WORKFLOW_DIR"], os.environ["BATCH_NAME"], "*")
            )
        ]
    )

    if mode.lower() == "zip":
        print(f"# target_filename: {target_filename}")

        if not batch_level:
            for batch_element_dir in batch_folders:
                target_dir = join(batch_element_dir, os.environ["OPERATOR_OUT_DIR"])
                pathlib.Path(target_dir).mkdir(parents=True, exist_ok=True)
                zip_target = join(target_dir, target_filename)
                zip_dir_path = join(
                    batch_element_dir, os.environ["OPERATOR_IN_DIR"], subdir
                )
                zip_dir(zip_dir_path=zip_dir_path, target_file=zip_target)

        else:
            target_dir = join(
                "/", os.environ["WORKFLOW_DIR"], os.environ["OPERATOR_OUT_DIR"]
            )
            pathlib.Path(target_dir).mkdir(parents=True, exist_ok=True)
            zip_target = join(target_dir, target_filename)

            zip_dir_path = join(
                "/", os.environ["WORKFLOW_DIR"], os.environ["OPERATOR_IN_DIR"], subdir
            )
            zip_dir(zip_dir_path=zip_dir_path, target_file=zip_target)

    elif mode.lower() == "unzip":
        if not batch_level:
            for batch_element_dir in batch_folders:
                element_input_dir = join(
                    batch_element_dir, os.environ["OPERATOR_IN_DIR"]
                )
                element_output_dir = join(
                    batch_element_dir, os.environ["OPERATOR_OUT_DIR"]
                )
                pathlib.Path(element_output_dir).mkdir(parents=True, exist_ok=True)

                print(f"Search dir: {element_input_dir}")
                zip_files = glob.glob(join(element_input_dir, "*.zip"), recursive=True)
                print(f"Files found: {zip_files}")
                for zip_file in zip_files:
                    unzip_file(zip_path=zip_file, target_path=element_output_dir)

        else:
            batch_input_dir = join(
                "/", os.environ["WORKFLOW_DIR"], os.environ["OPERATOR_IN_DIR"]
            )
            batch_output_dir = join(
                "/", os.environ["WORKFLOW_DIR"], os.environ["OPERATOR_OUT_DIR"]
            )
            pathlib.Path(batch_output_dir).mkdir(parents=True, exist_ok=True)

            zip_files = glob.glob(join(batch_input_dir, "*.zip"), recursive=True)
            for zip_file in zip_files:
                unzip_file(zip_path=zip_file, target_path=batch_output_dir)

    else:
        print("##################################################")
        print("#")
        print(f"# MODE: {mode} is not supported.")
        print("# ABORT")
        print("#")
        print("##################################################")
        exit(1)

if processed_count == 0:
    print("#")
    print("##################################################")
    print("#")
    print("#################  ERROR  #######################")
    print("#")
    print("# ----> NO FILES HAVE BEEN PROCESSED!")
    print("#")
    print("##################################################")
    print("#")
    exit(1)
