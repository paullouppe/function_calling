from tools.weather import Get_Weather
from tools.news import Get_News
from tools.agenda.agenda import AgendaHandler
from tools.agenda.agenda_tool import *
from model_interaction.ollama import call_model
from tools.tools_manager import ToolsManager

def main():
    # handlers
    agenda_handler = AgendaHandler()

    # tools
    news_tool = Get_News()
    weather_tool = Get_Weather()
    agenda_add_meeting_tool = Agenda_Add_Meeting(agenda_handler)
    agenda_remove_tool = Agenda_Remove_Meeting(agenda_handler)
    agenda_view_complete_tool = Agenda_View_Complete(agenda_handler)
    agenda_meeting_list_tool = Agenda_View_Meeting_List(agenda_handler)

    manager = ToolsManager([
        news_tool,
        weather_tool,
        agenda_add_meeting_tool,
        agenda_remove_tool, 
        agenda_view_complete_tool, 
        agenda_meeting_list_tool
    ]);
    
    tools_config = manager.get_all_configs()

    m = input("Your question : ")
    messages = [
        {'role': 'user', 'content': m}
    ]

    response = call_model(messages, tools_config)
    print("First response from the model:\n", response['message'])

    tool_calls = response['message'].get('tool_calls', [])
    if tool_calls:
        for tool_call in tool_calls:
            tool_name = tool_call['function']['name']
            arguments = tool_call['function']['arguments']

            if manager.has_tool(tool_name):
                
                function_response = manager.call_tool(tool_name, arguments)
                
                messages.append({'role': 'tool', 'content': function_response})
                
                if manager.is_wrap_output(tool_name):
                    final_response = call_model(messages, tools_config)
                    print("Final response from the model:\n", final_response['message']['content'])
                else:
                    print("Function response:", function_response)
            else:
                print(f"Unknown tool name: {tool_name}")
    else:
        final_response = call_model(messages, tools_config)
        print("Final response from the model:\n", 
              final_response['message']['content'])

if __name__ == "__main__":
    main()
