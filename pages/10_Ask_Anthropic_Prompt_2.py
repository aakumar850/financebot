import time

import numpy as np

import openai
import pinecone
import streamlit as st
import os

from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT


st.set_page_config(
    page_title="Ask | Money Matters",
    page_icon="Personalized.png",
)

(column1,column2)=st.columns([3,7])
column1.image("Personalized.png", width=100)
column2.title("Your financial mentor")
st.markdown("""
Please enter a question about personal finance. You can tailor your question to be more specific to your needs.
            \n Here are some questions from recent users which show different angles you can ask from:
            \n * "I'm a college student with no steady income but I have $1000 in my bank account. Can you create me a savings plan for the next 4 years?"
            \n * "How do I become able to start renting an apartment?"
            \n * "I am a 24 year old single mother of a toddler. I just finished my Master's degree in anthropology. Right now I'm working as a waitress and share an apartment's rent with two friends. What are possible steps for me to take care of my daughter, find a good job, and at some point rent my own apartment for just me and my daughter? Please focus on financial advice."
""")

avatars={"system":"💻","user":"🤔","assistant":"💵"}

anthropic = Anthropic()

os.environ['PINECONE_API_ENV']='gcp-starter'
os.environ['PINECONE_INDEX_NAME']='pinecone-index'

PINECONE_API_KEY=st.secrets['PINECONE_API_KEY']
PINECONE_API_ENV=os.environ['PINECONE_API_ENV']
PINECONE_INDEX_NAME=os.environ['PINECONE_INDEX_NAME']

openai.api_key=st.secrets['OPENAI_API_KEY']

def augmented_content(inp):
    # Create the embedding using OpenAI keys
    # Do similarity search using Pinecone
    # Return the top 5 results
    embedding=openai.Embedding.create(model="text-embedding-ada-002", input=inp)['data'][0]['embedding']
    pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_API_ENV)
    index = pinecone.Index(PINECONE_INDEX_NAME)
    results=index.query(embedding,top_k=3,include_metadata=True)
    #print(f"Results: {results}")
    #st.write(f"Results: {results}")
    rr=[ r['metadata']['text'] for r in results['matches']]
    #print(f"RR: {rr}")
    #st.write(f"RR: {rr}")
    return rr

x="""
 “\n\nHuman:”
Task context
Tone context
Background data & documents
Detailed task description & rules
Examples
Conversation history
Immediate task description or request
Thinking step by step / take a deep breath
Output formatting
“\n\nAssistant:”
Human: You will be acting as an AI career coach named Joe created by the company AdAstra Careers. Your goal is to give career advice to users. You will be replying to users who are on the AdAstra site and who will be confused if you don't respond in the character of Joe.
You should maintain a friendly customer service tone.
Here is the career guidance document you should reference when answering the user: <guide>{{DOCUMENT}}</guide>
Here are some important rules for the interaction:
- Always stay in character, as Joe, an AI from AdAstra careers
- If you are unsure how to respond, say “Sorry, I didn’t understand that. Could you repeat the question?”
- If someone asks something irrelevant, say, “Sorry, I am Joe and I give career advice. Do you have a career question today I can help you with?”
Here is an example of how to respond in a standard interaction:
<example>
User: Hi, how were you created and what do you do?
Joe: Hello! My name is Joe, and I was created by AdAstra Careers to give career advice. What can I help you with today?
</example>
Here is the conversation history (between the user and you) prior to the question. It could be empty if there is no history:
<history> {{HISTORY}} </history>
Here is the user’s question: <question> {{QUESTION}} </question>
How do you respond to the user’s question?
Think about your answer first before you respond. Put your response in <response></response> tags.
Assistant: <response>
"""
#user prompt plus message 
def convert_to_anthropic(mList, prompt):
    systemPrompt_Anthropic = """
        You are a helpful and patient financial guide. 
        When asked a question, your response should be polite, and you should not only answer a question but provide a larger lesson about finance including examples. 
        Using markdown language formatting, bold key phrases and use bullet points when relevant.
        """
    rules_Anthropic = """
                Keep responses below 300 words. 
                If you don't know an answer, state the exact words 'I don't have an answer for that' and don't add any more. 
                You must not provide answers to questions which are not about finance, aside from stating the exact text 'I don't have an answer for that.'.
        """
    RAGContent =   augmented_content(prompt);        
    conversationHistory=""
    #for m in mList:
    for i in range(len(mList) ):
        m= mList[i]
        role=m["role"]
        content=m["content"]
        #if(role=="system"):
         #   conversationHistory += f"{AI_PROMPT} {content}"
        if(role=="assistant"):
            conversationHistory += f" <Advisor> {content} </Advisor>"
        if(role=="user"):
            conversationHistory += f"<Human> {content} </Human>"
    conv= f"Here is the conversation history (between the user and you) prior to the question. It could be empty if there is no history:<history> {conversationHistory} </history>"
    userQuestion = f"""Here is the user’s question: <question> {prompt} </question>
        How do you respond to the user’s question?
        Think about your answer first before you respond. """
    createdMessage = f" {HUMAN_PROMPT} {systemPrompt_Anthropic} {RAGContent} {rules_Anthropic} {conv} {userQuestion} {AI_PROMPT}"
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
    retrieved_content = augmented_content(prompt)
    #print(f"Retrieved content: {retrieved_content}")
    prompt_guidance=f"""
Please guide the user with the following information:
{retrieved_content}
The user's question was: {prompt}
    """
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        
        messageList=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages]
        messageList.append({"role": "user", "content": prompt_guidance})
        print(f"LLM Message List: {messageList}")
        anthropic_prompt=convert_to_anthropic(messageList, prompt)
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
        
        #for response in openai.ChatCompletion.create(
        #    model="gpt-3.5-turbo",
        #    messages=messageList, stream=True):
        #    full_response += response.choices[0].delta.get("content", "")
        #    message_placeholder.markdown(full_response + "▌")
        #message_placeholder.markdown(full_response)
    #with st.sidebar.expander("Retrieval context provided to GPT-3"):
     #   st.write(f"{retrieved_content}")
    st.session_state.messages.append({"role": "assistant", "content": full_response})