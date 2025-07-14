from openai import OpenAI
client = OpenAI(api_key="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")
response = client.chat.completions.create( #创建一个聊天完成请求
    model="gpt-3.5-turbo", #要使用的模型
    messages=[
        {"role":"user" , "content":"What is the capital of France?"}, #role 可以是user用户输入, assistant Ai助手输入, system 系统输入
    ],
    max_tokens=50, #最大token数为50
    temperature=0.7, #温度参数控制输出的随机性，0.7表示适度随机，范围可以在0-2， 越高越随机
)
print(response.choices[0].message.content) # 输出: Paris

#或者可以用 'platform.openai.com/playground',点击右上角的view code就有code了


