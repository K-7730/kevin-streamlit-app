import streamlit as st 


# 选项列表, 单选
gender = st.radio("你的性别是什么？",
        ["男性", "女性", "其他"], 
        index=None)  # 默认选项的索引，None表示没有默认选项

st.divider()  # 添加分割线


# 选项列表, 单选
contact = st.selectbox("你喜欢的联系方式是什么？",
                       ["微信", "QQ", "电话", "电子邮件"],  
                       index = None)
if contact == "微信":
    st.text_input("请输入你的微信号：")  # 如果选择了微信，显示一个文本输入框
if contact == "QQ":
    st.text_input("请输入你的QQ号：")  # 如果选择了QQ
if contact == "电话":
    st.text_input("请输入你的电话号码：")  # 如果选择了电话
if contact == "电子邮件":
    st.text_input("请输入你的电子邮件地址：")  # 如果选择了电子邮件


st.divider()  # 添加分割线


# 选项列表, 多选
fruits = st.multiselect("你喜欢的水果有哪些？",
                          ["苹果", "香蕉", "橙子", "葡萄", "草莓"])  
for fruit in fruits:  # 遍历用户选择的水果
    st.write(f"你选择了：{fruit}")  # 显示用户选择的水果
    

st.divider()  # 添加分割线


# 选项列表, 滑块
height = st.slider("你的身高是多少？", min_value=0, max_value=250, value=100, step=1)