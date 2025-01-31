
class ToolsManager():
    def __init__(self, tools):
        self.tools = {tool.function_name: tool for tool in tools}

    def has_tool(self, tool_name):
        return tool_name in self.tools

    def call_tool(self, tool_name, arguments):
        return self.tools[tool_name].call(arguments)
    
    def is_wrap_output(self, tool_name):
        return self.tools[tool_name].wrap_output

    def get_all_configs(self):
        return [tool.config for tool in self.tools.values()]
