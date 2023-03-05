import openai

MODEL = "gpt-3.5-turbo"

def get_chatgpt_response(messages, temperature=0):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
    )
    return response

def add_message(messages, role, content):
    messages.append({
        "role": role,
        "text": content
    })
    return messages

def add_user_message(content, messages=[]):
    return add_message(messages, "user", content)

def add_system_message(content, messages=[]):
    return add_message(messages, "system", content)

def add_assistant_message(content, messages=[]):
    return add_message(messages, "assistant", content)