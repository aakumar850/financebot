import streamlit as st
import anthropic
anthropic.api_key=st.secrets['ANTHROPIC_API_KEY']

st.set_page_config(
    page_title="Create | Your Portico Wellness Marketing Assistant",
    page_icon="Portico care logo.png",
)
(column1,column2)=st.columns([2,8])
column1.image("Portico care logo.png", width=100)
column2.title("Your Marketing Assistant")
st.markdown("""
\n **:green[Marketing strategy guidance:]** I will offer you a step-by-step guidance on creating a marketing plan tailored to your CAI practice, including setting goals, identifying target audiences, and choosing the right marketing channels. 
\n **If you have any existing content for me to review, you may paste it so I can tailor it to your specific needs.**
\n **You may ask follow up questions so we can personalize the plan specifically for your business.**
""")

avatars={"system":"💻","user":"🤔","assistant":"💵"}
print("my avatars"+avatars["assistant"])
def send_request_and_process(full_response:str):       
    print("st session state messages: ", st.session_state.messages)
    for response in anthropic.Anthropic().messages.create(
        model="claude-3-opus-20240229"
        ,max_tokens=1024
        ,system= """
        You are a helpful and patient marketing executive for Complementary & Integrative Care practice.
        Your tone is professional, concise, and courteous. 
        In reviewing the input, you look for inaccuracies, as well as understanding the user's intent.
        If the input is not marketing related then respond: "I can only answer marketing related content."
        If you are not sure about how to respond then say: "I'm sorry I do not know the answer to that."
        For everything else, use the appropriate output format based on the type of content you are creating:
        Marketing Strategy Plan Template:
        1. Executive Summary
        2. Business Overview
        - Company description
        - Products/services offered
        - Unique selling proposition (USP)
        3. Market Analysis
        - Target market and customer personas
        - Competitor analysis
        - Industry trends and growth potential
        4. Marketing Goals and Objectives
        - SMART (Specific, Measurable, Achievable, Relevant, Time-bound) goals
        - Key performance indicators (KPIs)
        5. Marketing Strategies
        - Positioning and branding
        - Content marketing plan
        - Social media marketing plan
        - Email marketing plan
        - Advertising and promotional strategies
        - Partnership and collaboration opportunities
        6. Budget and Resource Allocation
        7. Implementation Timeline
        8. Evaluation and Monitoring
        - Tracking and reporting on KPIs
        - Adjusting strategies based on performance
        """
        ,messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        ,stream=True
        ):
            print(f"response Event {type(response)}, {response.type}")
            if (response.type == 'content_block_start'):
                full_response += response.content_block.text
            if (response.type == 'content_block_delta'):
                full_response += response.delta.text
            if (response.type == 'content_block_stop'):
                print(f"full_response B", full_response)
                break
    #for display on UI
    message_placeholder.markdown(full_response)
    #for passing to anthropic
    st.session_state.messages.append({"role": "assistant", "content": full_response})
    
if "messages" not in st.session_state:
    st.session_state.messages = []
    print(f"AK 33")
    
for message in st.session_state.messages:
    if message["role"] != "system":
        avatar=avatars[message["role"]]
        print(f"AK 50", message["role"])
        with st.chat_message(message["role"],avatar=avatar):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask your question here!"):
    new_message={"role": "user", "content": prompt}
    st.session_state.messages.append(new_message)
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        print("ak 51 FR", full_response)
        try: 
            send_request_and_process(full_response)
        except Exception as err:
            print("!! Request failed!", err)
            st.markdown("Internal error. Pls contact the administrator.")
    

#RawMessageStartEvent
#RawContentBlockStartEvent(content_block=TextBlock(text='', type='text')
#RawContentBlockDeltaEvent(delta=TextDelta(text='Here', type='text_delta')
#RawContentBlockStopEvent(index=0, type='content_block_stop')
#RawMessageDeltaEvent(delta=Delta(stop_reason='end_turn', stop_sequence=None), type='message_delta', usage=MessageDeltaUsage(output_tokens=253))
#RawMessageStopEvent(type='message_stop')