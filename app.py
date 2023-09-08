import streamlit as st
import pandas as pd
import openai

#title the page
st.title("Personal Finance Chatbot")
#display a subheader
st.subheader("Personal finance, personalized.")
#display an image
st.image("/content/money.png")

#create two tabs and add elements to each
asktab, learntab = st.tabs(["Ask", "Learn"])
asktab.write("**This is a chatbot. Ask it anything!**")
learntab.write("**Scroll through and learn.**")

with learntab.expander("Learn more about stocks:"):
    st.write("""
        Investing in stocks means owning parts of a company.
        more stuff about investing, ...
    """)

learntab.video("https://www.ted.com/talks/oliver_elfenbaum_how_does_the_stock_market_work?language=en", format="video/mp4")



openai.api_key = st.secrets["database"]["OPENAI_API_KEY"]
st.write(openai.api_key)

#Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.chat_message("Ask any finance question")

# Accept user input
if prompt := st.chat_input("Ask any finance question"):
   #  Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
     #Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

for response in openai.ChatCompletion.create(
        model=st.session_state["openai_model"],
        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
        stream=True,
    ):
        full_response += response.choices[0].delta.get("content", "")
        message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
st.session_state.messages.append({"role": "assistant", "content": full_response})