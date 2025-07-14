import streamlit as st 

name = st.text_input("请输入你的名字： ") # 创建一个文本输入框，提示用户输入名字

if name:  # 如果用户输入了名字
    st.write(f"你好，{name}")  # 显示你好➕用户输入的名字
    
st.divider()  # 添加分割线

password = st.text_input("请输入密码： ", type="password")  # 创建一个密码输入框，提示用户输入密码

st.divider()  

paragraph = st.text_area("请输入一段自我介绍：") # 创建一个大的文本输入框

st.divider()  

age = st.number_input("请输入你的年龄： ", min_value=0, max_value=120, value = 0)  # 创建一个数字输入框，限制年龄范围,默认0

st.divider()

check = st.checkbox("我同意条款和条件")  # 创建一个复选框，提示用户同意条款和条件
if check:  # 如果用户同意条款和条件
    st.write("感谢你同意")  # 显示感谢信息
if not check:  # 如果用户同意条款和条件
    st.write("必须给我同意")  # 显示感谢信息
    
st.divider()

submit = st.botton("提交")  # 创建一个提交按钮
if submit:  # 如果用户点击提交按钮
    st.write("提交成功")  # 显示提交成功信息