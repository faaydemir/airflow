import json
"""
write given config to 
"""
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