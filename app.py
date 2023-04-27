import streamlit as st

if not "count" in st.session_state:
    st.session_state.count = 1

if st.button("click", key = "click", type = "primary"):
    st.session_state.count += 1

if st.session_state.count % 3 == 0 or "3" in str(st.session_state.count):
    st.write("(｡∀゜)<"+str(st.session_state.count)+"!!")
else:
    st.write("ಠ▃ಠ<"+str(st.session_state.count))