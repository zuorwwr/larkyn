# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import streamlit as st
st.title('我的小程序')
name = st.text_input('输入你的名字：')
if name:
    st.write(f'你好呀，{name}！欢迎加入！！')
    st.balloons()