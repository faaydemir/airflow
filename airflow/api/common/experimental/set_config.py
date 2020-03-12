import json
import logging
from sqlalchemy import or_
from airflow import models
from airflow.exceptions import DagNotFound
from airflow.models import DagModel, TaskFail
from airflow.models.serialized_dag import SerializedDagModel
from airflow.settings import STORE_SERIALIZED_DAGS
from airflow.utils.session import provide_session

log = logging.getLogger(__name__)


@provide_session
def set_config(dag_id: str) -> int:

    configWriter = ConfigWriter()
    configWriter.write("test","1")
    return 0



class ConfigWriter:
    
    def write(self,fileName:str,config:str) -> None:
        pathhelper = PathHelper()
        path = pathhelper.GetConfigPath()
        config = {
            'value1': config,
            'value2': 1,
        }
        d = DagBuilder()
        dagstring = d.build("test")

        with open(path+'/'+fileName +'.py', 'w') as dagFile:
            dagFile.write(dagstring)

        with open(path+'/'+fileName +'.json', 'w') as json_file:
            json.dump(config, json_file)
    
class PathHelper:
  
    def GetDagPath(self) -> str:
        return 'tmp'

    def GetAirFlowPath(self) -> str:
        return 'tmp'


class DagBuilder:
    def build(self,id) ->str:

        dag ="""
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
args = {
    'owner': 'airflow',
    'start_date': days_ago(2),
}
dag = DAG(
    dag_id='example_bash_operator',
    default_args=args,
    schedule_interval='0 0 * * *',
    dagrun_timeout=timedelta(minutes=60),
    tags=['example']
)
run_this_last = DummyOperator(
    task_id='run_this_last',
    dag=dag,
)
# [START howto_operator_bash]
run_this = BashOperator(
    task_id='run_after_loop',
    bash_command='echo 1',
    dag=dag,
)
# [END howto_operator_bash]
run_this >> run_this_last
for i in range(3):
    task = BashOperator(
        task_id='runme_' + str(i),
        bash_command='echo "{{ task_instance_key_str }}" && sleep 1',
        dag=dag,
    )
    task >> run_this
# [START howto_operator_bash_template]
also_run_this = BashOperator(
    task_id='also_run_this',
    bash_command='echo "run_id={{ run_id }} | dag_run={{ dag_run }}"',
    dag=dag,
)
# [END howto_operator_bash_template]
also_run_this >> run_this_last
if __name__ == "__main__":
    dag.cli()
        """

        return dag