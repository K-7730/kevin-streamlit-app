import streamlit as st 

name = st.text_input("请输入你的名字： ") # 创建一个文本输入框，提示用户输入名字

if name:  # 如果用户输入了名字
    st.write(f"这是你吗，{name}")  # 显示你好➕用户输入的名字 
    st.image("5a11f109b61a3ce298bafd95cecc98d2.jpg", width=200)  #一定要相对路径，显示一张图片
    
st.divider()  # 添加分割线

password = st.text_input("请输入密码： ", type="password")  # 创建一个密码输入框，提示用户输入密码

st.divider()  

#paragraph = st.text_area("请输入一段自我介绍：") # 创建一个大的文本输入框
# 选项列表, 滑块
height = st.slider("你的身高是多少？", min_value=0, max_value=250, value=100, step=1)


st.divider()  

age = st.number_input("请输入你的年龄： ", min_value=0, max_value=120, value = 0)  # 创建一个数字输入框，限制年龄范围,默认0

st.divider()

check = st.checkbox("改成是否同意波比最帅行了吧👍")  # 创建一个复选框，提示用户同意条款和条件
if check:  # 如果用户同意条款和条件
    st.write("我就知道")  # 显示感谢信息
if not check:  # 如果用户同意条款和条件
    st.write("必须给我同意")  # 显示感谢信息
    
st.divider()

if check:
    submit = st.button("自愿提交")  # 创建一个提交按钮
    if submit:  # 如果用户点击提交按钮
        st.write("提交成功")  # 显示提交成功信息
        st.image("9737fa712f8f98dfc8992d3e54e8bb0c.jpg")
        
        
        
# 如果要对原链接进行更新
#1:  git add .
#2： git commit -m "更新内容"
#3  git push origin main