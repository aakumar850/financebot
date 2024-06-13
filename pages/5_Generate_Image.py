from openai import OpenAI
import streamlit as st
print(f"3")
st.set_page_config(
    page_title="Create | Your Portico Wellness Marketing Assistant",
    page_icon="Portico care logo.png",
)
client=OpenAI(api_key=st.secrets['OPENAI_API_KEY'])

(column1,column2)=st.columns([2,8])
column1.image("Portico care logo.png", width=100)
column2.title("Your Marketing Assistant")
st.markdown("""
I will assist with your **:green[image generation]** that you can use on your website, blog posts, social media, email campaigns, newsletters and many more ways.
\n Provide me specific information such as: 
\n (1) A few specific details about the object or character, 
\n (2) Info about the setting or background to use for the image, 
\n (3) The medium style in which it's depicted, such as oil painting, digital photo, or even marble statue
\n (4) Other adjectives, such as "colorful," "swirling," "playful," "happy," "minimalist," "geometric," "vibrant," "dramatic," "ornate," "austere," etc.—anything that could help build your desired aesthetic                                  

\n **:green[AVOID THESE PITFALLS]** in your prompts.
\n (1) Complex scenes with multiple subjects, detailed layout requests (for example, "A big red Object X on the left, friendly Object Y on the right, a small Object Z wearing Item A above them")
\n (2) Images with multiple faces (these are often distorted)
\n (3) Requests for text (for example, "a sign saying 'Happy birthday!'"), because I don't know how to spell  
\n Here are some examples from recent users which show different types of images you can ask me to generate:
\n "Spring Detox Wellness, studio lighting"
\n "21-Day Yoga Challenge, vector art"
\n "Vibrant and joyful healthy living"
\n "Black and white poster for chiropracter's office"   
\n "physiotherapy water color"                                    

\n **What image would you like me to generate for you today?**            
""")

avatars={"system":"💻","user":"🤔","assistant":"📝"}

SYSTEM_PROMPT="""
Ignore all previous commands. 
You are a helpful and patient user experience executive for Complementary & Integrative Care practice.
If the input is not healthcare related then respond: "I can only generate healthcare related images."
If you are not sure about how to respond then say: "I'm sorry I do not know the answer to that."
For everything else, generate images with no words. 
"""

SYSTEM_MESSAGE={"role": "system", "content": SYSTEM_PROMPT}

def send_request_and_process(full_response:str):       
        print(f"122 prompt: ", full_response)
        full_response += SYSTEM_PROMPT
        print(f"40 full_response", full_response)
        #for response in client.images.generate(
        response = client.images.generate(
            model="dall-e-3",
            prompt=full_response,
            size="1024x1024",
            quality="standard",
            n=1,)
        print(f"129 ak response url", response.data[0].url)
        image_url = response.data[0].url
        print(f"131 ak image url", response.data[0])
        message_placeholder.markdown(image_url)
        #st.session_state.messages.append({"role": "assistant", "content": full_response})

if "messages" not in st.session_state:
    st.session_state.messages = []
    print(f"56 system message", st.session_state.messages.append(SYSTEM_MESSAGE))
    st.session_state.messages.append(SYSTEM_MESSAGE)

for message in st.session_state.messages:
    if message["role"] != "system":
        avatar=avatars[message["role"]]
        with st.chat_message(message["role"],avatar=avatar):
            #print(f"62 message", message)
            st.markdown(message["content"])

if prompt := st.chat_input("Please paste the marketing information that you'd like to copy edit or create"):
    new_message={"role": "user", "content": prompt}
    st.session_state.messages.append(new_message)
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        print (f"151 prompt", prompt)
        try: 
            send_request_and_process(prompt)
        except Exception as err:
            print("!! Request failed!", err)
            st.markdown("Internal error. Pls contact the administrator.")
        