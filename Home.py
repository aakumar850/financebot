import streamlit as st
import pandas as pd
import openai

st.set_page_config(
    page_title="Home | Your Portico Wellness Marketing Assistant",
    page_icon="portico_bug.svg",
)
#AK test
#title page
#display an image
st.image("Portico-logo-color.svg", width=400)

st.title("About the website")
st.write("""
         **:green[Welcome to Portico Wellness Marketing Assistant!]** Here, we hope to help you take charge of your company's brand 
         through our interactive marketing chat assistant. 
         
         - With the **:green[Learn]** page, you can learn or refresh key marketing concepts.
         - With the **:green[Strategize]** page, you can paste in your company profile, rough drafts and we will tailor marketing strategy plan for your business. Strategy that you can use to build brand awareness, promote your business or drive engagement.
         - With the **:green[Plan]** page, you can learn key ways to plan your campaign strategy. Strategy that you can use for social media, email promotions and advertising campaigns. 
         - With the **:green[Create]** page, you can paste in your company profile, rough drafts and we will create usable marketing content that you can use for creating a strong brand. Content that can go on your website, for ad campaigns, brochures, flyers, social media and many more.
         - With the **:green[Generate Image]** page, you can provide a prompt and we will create a suitable image, which you can use on your website, for ad campaigns, brochures, flyers, social media posts and many more.
         """)



#create two tabs and add elements to each
# asktab, learntab = st.tabs(["Ask", "Learn"])
# asktab.write("**This is a chatbot. Ask it anything!**")
# learntab.write("**Scroll through and learn.**")

# with learntab.expander("Learn more about stocks:"):
#     st.write("""
#         Investing in stocks means owning parts of a company.
#         more stuff about investing, ...
#     """)

# learntab.video("https://www.ted.com/talks/oliver_elfenbaum_how_does_the_stock_market_work?language=en", format="video/mp3")


# openai.api_key = st.secrets["database"]["OPENAI_API_KEY"]

# message_placeholder = st.empty()
# full_response = ""

# #Set a default model
# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"

# # Initialize chat history
# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     #st.session_state.messages.append({"role": "system", "content": "Please provide the user good financial advice"})


# # Display chat messages from history on app rerun
# for message in st.session_state.messages:
#     with asktab.chat_message(message["role"]):
#         asktab.markdown(message["content"])

# asktab.chat_message("Ask any finance question")

# # Accept user input
# if prompt := st.chat_input("Ask any finance question"):
#    #  Add user message to chat history
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     # Display user message in chat message container
#     with asktab.chat_message("user"):
#         asktab.markdown(prompt)
#      #Display assistant response in chat message container

#     with st.chat_message("assistant"):
#         for response in openai.ChatCompletion.create(
#         model=st.session_state["openai_model"],
#         messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#         stream=True,
#     ):
#         full_response += response.choices[0].delta.get("content", "")
#         message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
    
#     message_placeholder = st.empty()
#         full_response = ""
#         for response in openai.ChatCompetion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         ):
#             full_response += response.choices[0].delta.get("content", "")
#             message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
    
#     for response in openai.ChatCompletion.create(
#         model=st.session_state["openai_model"],
#         messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
#         stream=True,
#     ):
#         full_response += response.choices[0].delta.get("content", "")
#         message_placeholder.markdown(full_response + "▌")
#         message_placeholder.markdown(full_response)
#     st.session_state.messages.append({"role": "assistant", "content": full_response})
