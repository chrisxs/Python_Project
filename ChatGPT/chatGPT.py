import openai

# 设置 OpenAI GPT API 的访问密钥
openai.api_key = '访问密钥'

# 定义与 AI 进行对话的函数
def chat_with_ai(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None
    )

    if len(response.choices) > 0:
        return response.choices[0].text.strip()
    else:
        return None

# 与用户进行对话
print("AI: 你好！我是 AI，有什么我可以帮助你的吗？")

while True:
    user_input = input("用户: ")

    if user_input.lower() == '退出':
        print("AI: 再见！")
        break

    ai_response = chat_with_ai("用户：" + user_input + "\nAI:")

    if ai_response:
        print("AI:", ai_response)
    else:
        print("AI: 对不起，我无法理解你的问题。")
