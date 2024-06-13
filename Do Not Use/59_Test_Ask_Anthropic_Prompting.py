from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import streamlit as st
anthropic = Anthropic()
anthropic.api_key=st.secrets['ANTHROPIC_API_KEY']

st.set_page_config(
    page_title="Ask | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("Your financial mentor")

avatars={"system":"💻","user":"🤔","assistant":"💵"}

def convert_to_anthropic(mList):
    createdMessage=""
    #for m in mList:
    for i in range(len(mList) ):
        m= mList[i]
        role=m["role"]
        content=m["content"]
        if(role=="assistant"):
            createdMessage += f"{AI_PROMPT} {content}"
        if(role=="user"):
            createdMessage += f"{HUMAN_PROMPT} {content}"
    createdMessage += f" {AI_PROMPT}"
    return createdMessage

SYSTEM_MESSAGE={"role": "system", 
                "content": """
                You are a helpful and patient financial guide. 
                When asked a question, your response should be polite, and you should not only answer a question but provide a larger lesson about finance including examples. 
                Using markdown language formatting, bold key phrases and use bullet points when relevant.
                Keep responses below 300 words. 
                If you don't know an answer, state the exact words 'I don't have an answer for that' and don't add any more. 
                You must not provide answers to questions which are not about finance, aside from stating the exact text 'I don't have an answer for that.'."""
                }
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SYSTEM_MESSAGE)

for message in st.session_state.messages:
    if message["role"] != "system":
        avatar=avatars[message["role"]]
        with st.chat_message(message["role"],avatar=avatar):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask your question here!"):
    retrieved_content = (prompt)
st.session_state.messages.append({"role": "user", "content": prompt})
with st.chat_message("user"):
        st.markdown(prompt)
with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""

#prompt = st.text_input('Ask your question', 'How to save money?')
messageList=[{"role": m["role"], "content": m["content"]}
for m in st.session_state.messages]
messageList.append({"role": "user", "content": prompt})
print(f"LLM Message List: {messageList}")
anthropic_prompt=convert_to_anthropic(messageList)
with st.sidebar.expander("Prompt provided to Anthropic"):
        st.write(f"{anthropic_prompt}")

completion = anthropic.completions.create(
model="claude-2",
max_tokens_to_sample=300,
prompt=f"{anthropic_prompt}",
)
full_response=completion.completion
#full_response="\n\n ** FAKE LLM Response\n\n"
message_placeholder.markdown(full_response)
st.write(completion.completion)