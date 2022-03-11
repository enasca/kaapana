import random
from datetime import datetime, timedelta

from airflow.utils.dates import days_ago
from airflow.models import DAG
from airflow.models import Variable

from kaapana.operators.LocalWorkflowCleanerOperator import LocalWorkflowCleanerOperator
from federated_setup_node_test.LocalFedartedSetupNodeTestOperator import LocalFedartedSetupNodeTestOperator
from federated_setup_node_test.LocalFederatedSetupSkipTestOperator import LocalFederatedSetupSkipTestOperator

ui_forms = {
    "workflow_form": {
        "type": "object",
        "properties": {
            "task": {
                "title": "Test federated setup",
                "description": "This is just a test",
                "type": "string",
                "default": "Test",
                "required": True
            }
        }
    }
}
args = {
    'ui_visible': False,
    'ui_forms': ui_forms,
    'owner': 'kaapana',
    'start_date': days_ago(0),
    'retries': 0,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    dag_id='federated-setup-node-test',
    default_args=args,
    concurrency=4,
    max_active_runs=4,
    schedule_interval=None
)

federated_setup_node_test = LocalFedartedSetupNodeTestOperator(dag=dag)
federated_setup_skip_test = LocalFederatedSetupSkipTestOperator(dag=dag)
clean = LocalWorkflowCleanerOperator(dag=dag, clean_workflow_dir=False)
federated_setup_node_test >> federated_setup_skip_test >> clean