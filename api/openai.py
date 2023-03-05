import openai

MODEL = "gpt-3.5-turbo"

def get_chatgpt_response(messages, temperature=0):
    print(messages)
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=temperature,
        max_tokens=100,
    )
    # only show the text completion
    return response["choices"][0]["message"]["content"]

def add_message(messages, role, content):
    messages.append({
        "role": role,
        "content": content
    })
    return messages

def add_user_message(content, messages=[]):
    return add_message(messages, "user", content)

def add_system_message(content, messages=[]):
    return add_message(messages, "system", content)

def add_assistant_message(content, messages=[]):
    return add_message(messages, "assistant", content)