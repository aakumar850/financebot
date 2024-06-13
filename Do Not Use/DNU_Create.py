import anthropic
import streamlit as st

st.set_page_config(
    page_title="Create | Your Portico Wellness Marketing Assistant",
    page_icon="Portico care logo.png",
)

(column1,column2)=st.columns([2,8])
column1.image("Portico care logo.png", width=100)
column2.title("Your Marketing Assistant")
st.markdown("""
I will assist with your content creation that you can use on your website, blog posts, social media, email campaigns, newsletters and many more ways. Please enter your draft, your company overview, products and services info and I will copy edit and generate marketing content for you.          
\n For example: 
\n **Marketing strategy guidance:** I will offer you a step-by-step guidance on creating a marketing plan tailored to your CAI practice, including setting goals, identifying target audiences, and choosing the right marketing channels. 
\n **Content creation support:** You provide your draft or overview of your company's product and services, and I will offer tips as well as create engaging content for blog posts, social media updates, newsletters, and promotional materials. 
\n **Email marketing tools:** Provide templates and best practices for creating effective email campaigns, managing subscriber lists, and analyzing campaign performance. 
\n **Analytics and reporting:** Help track and analyze key marketing metrics, such as website traffic, social media engagement, and conversion rates, providing insights and recommendations for improvement. 
\n **Advertising guidance:** Offer advice on creating and managing online advertising campaigns, including platform selection (e.g., Google Ads, Facebook Ads), targeting, and budget optimization. 
\n **What marketing content would you like me to create for you today? If you have any existing content for me to review and copy edit you may paste it.**
""")

avatars={"system":"💻","user":"🤔","assistant":"📝"}

SYSTEM_PROMPT="""
You are a helpful and patient marketing executive for Complementary & Integrative Care practice.
Your tone is professional, concise, and courteous. 
In reviewing the input, you look for inaccuracies, as well as understanding the user's intent.
If the input is not marketing related then respond: "I can only answer marketing related content."
If you are not sure about how to respond then say: "I'm sorry I do not know the answer to that."
For everything else, start all responses with: "Here is my response:"
Use the appropriate output format base on the type of content you are creating:
Content Creation Templates:

1. Blog Post Template
   - Attention-grabbing headline
   - Introduction with a hook
   - Subheadings for main points
   - Relevant images or videos
   - Call-to-action (CTA) at the end
   - Meta title and description for SEO

2. Social Media Post Templates
   - Platform-specific image sizes and formats
   - Engaging caption with relevant hashtags
   - Call-to-action or question to encourage interaction
   - Tagging relevant accounts or partners
   - Tracking links or UTM parameters for analytics

3. Email Newsletter Template
   - Compelling subject line
   - Personalized greeting
   - Featured content (e.g., blog post, success story, tip of the month)
   - Promotions or special offers
   - Upcoming events or webinars
   - Social media and contact information
   - Unsubscribe link and privacy policy

4. Case Study Template
   - Client overview and challenges
   - Services provided and solution implemented
   - Results and benefits achieved
   - Client testimonial
   - Call-to-action to learn more or request a consultation

5. Press Release Template
   - Attention-grabbing headline
   - Subheadline with key details
   - Dateline and introduction paragraph
   - Body paragraphs with supporting information and quotes
   - Boilerplate about the company
   - Contact information for media inquiries

6. Video Script Template
   - Introduction with a hook
   - Brief overview of the video's purpose
   - Main points or steps, each with a clear transition
   - Conclusion with a summary and call-to-action
   - Outro with branding and contact information
"""

SYSTEM_MESSAGE={"role": "system", "content": SYSTEM_PROMPT}

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append(SYSTEM_MESSAGE)

for message in st.session_state.messages:
    if message["role"] != "system":
        avatar=avatars[message["role"]]
        with st.chat_message(message["role"],avatar=avatar):
            st.markdown(message["content"])

if prompt := st.chat_input("Please paste the marketing information that you'd like to copy edit or create"):
    new_message={"role": "user", "content": prompt}
    st.session_state.messages.append(new_message)
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant", avatar=avatars["assistant"]):
        message_placeholder = st.empty()
        full_response = ""
        for response in anthropic.Anthropic().messages.create(
            model="claude-3-opus-20240229",
            max_tokens=1024,
            messages=[{"role": m["role"], "content": m["content"]}
                      for m in st.session_state.messages], stream=True):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})