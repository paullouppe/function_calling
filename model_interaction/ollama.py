import ollama

def call_model(messages, tools):
    return ollama.chat(model='qwen2.5', messages=messages, tools=tools)