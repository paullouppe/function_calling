from tools.tool import Base_Tool
from tools.agenda.agenda import AgendaHandler

class Agenda_Add_Meeting(Base_Tool):
    def __init__(self, agenda_handler: AgendaHandler):
        self._agenda_handler = agenda_handler
        self._wrap_output = False
        self._config = {
            'type': 'function',
            'function': {
                'name': 'agendaaddmeeting',
                'description': 'Add a meeting to the agenda',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string', 'description': 'The title of the meeting.'},
                        'date': {'type': 'string', 'description': 'The date of the meeting in the YYYY-MM-DD format'},
                        'time': {'type': 'string', 'description': 'The time of the meeting in the HH:MM format'},
                    },
                    'required': ['title', 'date', 'time'],
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
        print("arguments", arguments)
        return self._agenda_handler.add_meeting(
            arguments.get('title', '').lower(), 
            arguments.get('date', '').lower(), 
            arguments.get('time', '').lower()
        )
    
class Agenda_Remove_Meeting(Base_Tool):
    def __init__(self, agenda_handler: AgendaHandler):
        self._agenda_handler = agenda_handler
        self._wrap_output = False
        self._config = {
            'type': 'function',
            'function': {
                'name': 'agendaremovemeeting',
                'description': 'Remove a meeting from the agenda',
                'parameters': {
                    'type': 'object',
                    'properties': {
                        'title': {'type': 'string', 'description': 'The title of the meeting.'},
                    },
                    'required': ['title'],
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
        return self._agenda_handler.remove_meeting(arguments.get('title', '').lower())

class Agenda_View_Meeting_List(Base_Tool):
    def __init__(self, agenda_handler: AgendaHandler):
        self._agenda_handler = agenda_handler
        self._wrap_output = False
        self._config = {
            'type': 'function',
            'function': {
                'name': 'agendaviewmeetinglist',
                'description': 'Show the complete meeting list of the agenda.',
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
        return self._agenda_handler.view_meeting_list()

class Agenda_View_Complete(Base_Tool):
    def __init__(self, agenda_handler: AgendaHandler):
        self._agenda_handler = agenda_handler
        self._wrap_output = False
        self._config = {
            'type': 'function',
            'function': {
                'name': 'agendashowcompleteagenda',
                'description': 'Show the complete agenda of every days there is at least one meetings.',
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
        return self._agenda_handler.view_complete_agenda()
