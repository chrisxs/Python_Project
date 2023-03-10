import openai
import re
import time

# 在这里填写您的OpenAI API密钥
openai.api_key = "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"

# GPT-3 模型ID
model_engine = "text-davinci-002"

# 历史对话记录
history = []

# 开始对话
print("欢迎使用ChatGPT！输入'exit'退出。")

while True:
    # 获取用户输入
    user_input = input("You: ")
    
    # 如果用户输入“exit”，则退出程序
    if user_input.lower() == "exit":
        print("ChatGPT: 再见！")
        break
    
    # 如果历史记录长度超过最大值，则删除第一个元素
    if len(history) >= 20:
        history.pop(0)
    
    # 添加用户输入到历史记录中
    history.append("用户: " + user_input)
    
    # 将历史记录组合成单个字符串，并将其发送到GPT-3进行生成
    prompt = "\n".join(history)
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    message = response.choices[0].text
    
    # 从生成的响应中提取文本
    message = message.strip()
    message = re.sub(r"\s+", " ", message)
    
    # 如果生成的响应为空，则等待一秒钟再次尝试
    if not message:
        time.sleep(1)
        continue
    
    # 将生成的响应添加到历史记录中
    #history.append("ChatGPT: " + message)
    
    # 打印生成的响应
    print(message)
