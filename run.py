import streamlit as st
import mypkg.mymod as mymod

with st.sidebar:
	n = st.slider("label")


st.write(mymod.a)
