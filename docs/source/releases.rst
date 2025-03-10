
#########
Changelog
#########

.. _release-0.2.2:

-------------------------

********************
Release Notes v0.2.2
********************

July 26, 2023

-------------------------

Bug fixes
---------

* Installation of certificates
* Access to Traefik routes for users with no admin rights

.. _release-0.2.1:

-------------------------

********************
Release Notes v0.2.1
********************

July 19, 2023

-------------------------

New features
------------

* Major restructuring and update of the documentation
* Added experimental persistent layer as extension for data management
* Updated landing page layout
* RTStruct and segmentation support in Gallary View

Bug fixes
---------

* Redirect for Minio and Keycloak
* Update of constraints file
* Fix of TypeError: cannot pickle '_thread.lock' object in Airflow
* Muliplte fixes in Kaapana-Backend
* Fixes in Trivy vulnerability scanner
* Fixes in the server_installation.sh
* Muliplte fixes in Kube-Helm backend
* Introducing a smaller GPU base image
* Fixes in scheduling of workflows
* Fix of Prometheus and Grafana error
* Fix in data upload
* Removal of not ready extensions from collections chart
* Fix of Tensorboard logs
* Fix of nnU-Net ensemble workflow
* Fix of radiomics federated workflow

Upcoming
--------

* Maintenance UI for UI-based platform management and maintenance 
* Multi Instance support for different Kaapana deployments within a single K8S Cluster
* New persistence layer for Kapaana

.. _release-0.2.0:

-------------------------

********************
Release Notes v0.2.0
********************

May 18, 2023

-------------------------

New Features
============

.. figure:: https://www.kaapana.ai/kaapana-downloads/kaapana-docs/stable/img/datasets.png
   :align: center
   :alt: New Dataset UI


Datasets
--------

* Added intuitive Gallery-style view visualizing thumbnails and (configurable) metadata of DICOM Series
* Added Multiselect which allows performing actions on multiple series at once including add/removing to/from a dataset, executing workflows on individual series or creating new datasets based on the selection
* Added configurable side panel metadata dashboard allowing the exploration of metadata distributions (based on selections)
* Introduced intuitive shortcut based tagging functionality allowing fast and convenient annotation and categorization of series
* (Full-text) search to filter for items based on metadata
* Added option to open a series in a side panel visualizing the DICOM using (an adjusted) OHIF Viewer-v3 next to all Metadata of the specific series.

Workflow Management System:
---------------------------

* Introduction of Kaapana Object "Workflow"
* Workflows semantically bind together multiple jobs, the data on which the jobs are running on and the orchestrating/triggering and the runner instances of the jobs Workflow Execution
* Only location to trigger executable jobs on Kaapana platform
* Directly accessible from Datasets view
* Remote/federated workflow execution on connected remote Kaapana instances more built-in

Workflow List:

* Visualizes all workflows which are or were running on the platform including
* Information regarding the workflow specification live status updates of workflow's jobs
* Workflow actions to abort, restart or delete workflows including all their jobs
* Information regarding the job specification
* Live updates of the job's status
* Redirect links to the job's airflow DAG run
* Job actions to abort, restart or delete jobs

Instance Overview:

* Visualization of the local and remote Kaapana instance
* Connection of remote Kaapana instances
* Information regarding the instance specification


Extension Upload / Data Upload mechanism
----------------------------------------
* Introduction of new NIfTI + DICOM upload (NIfTIs will be converted to DICOM + incl. segmentation support)
* Easily importing the uploaded images into PACS via available workflows
* New chart (.tgz) and container (.tar) upload feature which enables users to upload their own extensions into the platform
* Importing container .tar files directly into the microk8s container runtime


Results page
------------
* A new results page has been introduced which allows users to explore results of their workflows by visualizing HTMLs 

MISC:
-----

* New NIfTI + DICOM upload (NIfTIs will be converted to DICOM + incl. segmentation support)
* New extension and container upload & import features
* Improved landing-page navigation to make workflows more present and more intuitive to interact with
* git-describe-based versioning for Kaapana
* Switch to `persistent-volumes <https://kubernetes.io/docs/concepts/storage/persistent-volumes/>`_ for better security and better cloud provider support 
* Security vulnerability improvements
* Included `Trivy <https://trivy.dev//>`_ container scanning for automatic CVE detection + SBOM creation in the build system
* Improved security check for all ingress requests
* Improved Keycloak initialization & password policy for production mode
* Introduced Black code formatter for Kaapana
* Introduction of a dark mode to the landing page
* Introduction of new base images for better dependency management and security handling (also smaller and more efficient)
* Improved Airflow scheduling for Kubernetes jobs
* Split of Airflow scheduler and webserver in separate PODs for better stability and robustness
* Automatic thumbnail generation for RTSTRUCTs and DICOM SEGs
* Improved annotation-metadata detection for SEG and RTSTRUCT
* Improved Kaapana build-system to better support external resources and platform creation
* Better support for offline installation & VM creation (upcoming)
* Many other smaller bug-fixes, improvements and adjustments

New Workflows
-------------

* `TotalSegmentator <https://github.com/wasserth/TotalSegmentator>`_ incl. all sub-tasks
* RTSTRUCT support for nnUNet training
* nnU-Net federated
* Radiomics federated

Updated Components
------------------

* Kubernetes v1.26/stable
* Helm v3.10
* Airflow v2.5.3
* Keycloak v21.0.1
* Traefik v2.9.9
* Grafana v9.4.7
* Kubernetes Dashboard v2.7.0
* OHIF v4.12.26
* Prometheus v2.34.0
* Alertmanager v0.25.0
* Auth2-proxy v7.4.0
* metrics-scraper : v1.0.9
* kube-state-metrics: v2.8.2
* OpenSearch Dashboards: 2.6.0
* OpenSearch: v2.6.0


New Extensions
--------------

* 3D Slicer
* Model-Hub
* RateMe


Upcoming
--------

* Maintenance UI for UI-based platform management and maintenance 
* Multi Instance support for different Kaapana deployments within a single K8S Cluster
* New persistence layer for Kapaana

.. _release-0.1.3:

---------

********************
Release Notes v0.1.3
********************

Date: July 31, 2022

---------

Changelog
---------

* Updated microk8s to v1.23/stable
    * latest stable version
    * API adjustments within all deployments

* Server and platform installation improvements
    * new certificate installation incl. random cert generator
    * easy offline installation method (no registry needed)
    * introduction of a helm namespace for separate deployment tracking
    * support for custom DNS servers
    * better proxy support (incl. no_proxy configuration)
    * improved security by RBAC cluster support
    * support for AlmaLinux as a replacement for CentOS 8

* Extensions
    * simplification of extension collections

* New build-system
    * improved build-time (~1h for the kaapana-platform)
    * improved dependency checks
    * build-tree visualization
    * container tarball export for offline installation
    * platform filters (to only build specific ones)
    * ability to include external repositories into the build-tree
    * Podman support as Docker alternative
    * direct microk8s injection
    * stats on used / unused resources
    * better logs
* ability to separate platforms in a registry using prefixes

* New processing scheduling system
    * improved robustness
    * multi GPU support
    * multi job per GPU support
    * utilizes Airflow pools as a transparent and consistent solution

* New Auth-Proxy → now OAuth2-proxy (Louketo has been deprecated)
* No additional port for Keycloak needed anymore
* Support for http → https redirect for arbitrary ports
* New development method within running pipelines
    * live container-debugging during workflow execution
    * Front-end for build-in IDE within the platform

* Bug-fixes
    * Fixed misbehaving “Delete-Series-From-Platform” workflow
    * Re-Index workflow
    * Increased timeout for process incoming dcm when called from CTP
    * Fixed bug in DICOM reindexation polluting the data directory
    * Fixed bugs in install script to make it location agnostic

* General Improvements
    * More robust un-deployment of the platform
    * Up to date Zenodo metadata
    * New tagging system allowing the deletion of tags and a faster processing
    * Adjustments of the landing page design
    * The dcmsend processing container reties sending of images up to 5 times making it more robust
    * Add Monitoring support for airflow
    * New Grafana Dashboards for Airlfow, Kubernetes and Traefik

* Documentation
    * Adjusted tutorials
    * New Operator docs
    * New Guides (Write Dockerfiles for Kaapana, Automatic Triggering, Send images to platform, Building the Platform, How does the Build System Work, Provide Workflow as Extension, How Kaapana uses Helm Charts, How to stop and restart a workflow, How to remove data from the platform, How to backup a Kaapana instance, How to install TLS certificates)
    * FAQ extension
    * New examples for workflows and processing containers
    
* many other smaller bug-fixes and adjustments

Incompatible Changes
--------------------

* Kubernetes v1.19 is not supported anymore

Updated Components
------------------

* Airflow v2.2.5
* Dcm4chee v5.26.0
* Keycloak v19.0.3
* Traefik v2.6
* Kubernetes Dashboard v2.5.1
* OHIF v4.12.26
* MinIO v2022.03.26
* Grafana v8.4.4
* Prometheus v2.34.0
* Alertmanager v0.24.0
* CTP v0.1.3
* kube-state metrics v2.5.0

Extensions
----------

New integrations:

* openEDC 
* doccano-image-tagging
* Federated learning extension

Updated extensions:

* Jupyterlab v3.3.2
* Code-Server v4.2.0
* Tensorboard v2.8.0
* Mitk-Workbench v2022.04


0.1.3-beta
==========

Date: May 30, 2022

0.1.2
=====

Date: May 15, 2022

* Last release with support for kubernetes v1.19 

0.1.0
=====

Date: Oct 24, 2020

* Initial release of Kaapana

