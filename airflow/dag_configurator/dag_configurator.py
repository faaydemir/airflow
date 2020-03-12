import json
"""
write given config to 
"""
class ConfigWriter:
    
    def write(self,path:str,config:str) -> None:
        config = {
            'value1': config,
            'value2': 1,
        }

        with open(path +'.json', 'w') as json_file:
            json.dump(config, json_file)
    