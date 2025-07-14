#在终端输入streamlit run + 文件名可以运行streamlit

#输入streamlit hello可以打开streamlit
#control c 可以停止streamlit运行
import streamlit as st
import pandas as pd


st.title('K first Streamlit app')  #设置网页标题
st.write('Hello Streamlit!') #在网页上显示文本内容

st.image("/Users/kevin.w/Desktop/computing/AI python/0_2 10.22.51.jpg", width=200) #在网页上显示图片，需要复制路径

表格 = pd.DataFrame({"学号": [1, 2, 3],
                   "姓名": ["张三", "李四", "王五"],
                   "成绩": [90, 85, 88]})  #创建一个DataFrame
st.dataframe(表格)  #在网页上显示DataFrame(交互式表格)
st.divider()  #添加分割线
st.table(表格)  #在网页上显示DataFrame(静态表格)


