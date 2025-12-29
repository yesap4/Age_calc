# sample streamlit python code
import streamlit as st
import time

st.set_page_config(page_title="Setup Test App", layout="centered")

st.title("🧪 Streamlit Setup Test")

st.write("If you can see this page, Streamlit is running correctly.")

# Session state test
if "count" not in st.session_state:
    st.session_state.count = 0

st.subheader("🔘 Button Test")
if st.button("Click me"):
    st.session_state.count += 1
    st.success(f"Button clicked {st.session_state.count} times")

# Time test
st.subheader("⏱️ Time Test")
st.write("Current timestamp:")
st.code(time.time())

# Input test
st.subheader("⌨️ Input Test")
name = st.text_input("Enter your name")

if name:
    st.info(f"Hello, {name}! 👋")

st.divider()
st.caption("✅ If buttons, input, and text work — your environment is ready.")