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

        with open(path+'/'+fileName +'.json', 'w') as json_file:
            json.dump(config, json_file)
    
class PathHelper:
    @classmethod
    def GetDagPath(self) -> str:
        return '/'

    @classmethod
    def GetAirFlowPath(self) -> str:
        return '/'