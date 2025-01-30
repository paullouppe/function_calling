from tools.tool import Base_Tool
import requests

class Get_News(Base_Tool):
    def __init__(self):
        self._wrap_output = True
        self._config = {
            'type': 'function',
            'function': {
                'name': 'getnews',
                'description': 'Get recent news from a country',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'country': {'type': 'string', 'description': 'The name of the country'},
                    },
                    'required': ['country'],
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
        country = arguments.get('country', '').lower().strip()
        country_map = {
            'france': 'fr',
            'india': 'in',
            'usa': 'us',
            'australia': 'au',
            'russia': 'ru',
            'united kingdom': 'gb',
        }
        country_code = country_map.get(country, 'fr')  # Default to 'fr'
        if country_code == 'fr' and country not in country_map:
            print("Unknown country:", country)

        url = f"https://saurav.tech/NewsAPI/top-headlines/category/general/{country_code}.json"
        print("Calling news function for:", country)
        response = requests.get(url)
        news_data = response.json()
        if 'articles' in news_data and news_data['articles']:
            article = news_data['articles'][0]
            return f"{article['title']}: {article['content']}"
        return "No news available for the given country."
