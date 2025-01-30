from tools.tool import Base_Tool
import requests

class Get_Weather(Base_Tool):
    def __init__(self):
        self._wrap_output = False
        self._config = {
            'type': 'function',
            'function': {
                'name': 'getweather',
                'description': 'Get weather from a place',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'place': {'type': 'string', 'description': 'The place you want the weather of'},
                    },
                    'required': ['place'],
                },
            },
        }
        self._function_name = self._config['function']['name']

    @property
    def config(self):
        return self._config
    
    @property
    def wrap_output(self):
        return self._wrap_output
    
    @property
    def function_name(self):
        return self._function_name
    
    def call(self, arguments):
        place = arguments.get('place', '').lower()
        url = f"https://wttr.in/{place}"
        print("Calling weather function for:", place)
        response = requests.get(url)
        return response.text
