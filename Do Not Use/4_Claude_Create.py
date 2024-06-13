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
I will assist with your **:green[content creation]** that you can use on your website, blog posts, social media, email campaigns, newsletters and many more ways.          
\n For example: You provide your draft or overview of your company's product and services, and I will offer tips as well as create engaging content for blog posts, social media updates, email newsletters, case study, press release and video script. 
\n **What marketing content would you like me to create for you today? If you have any existing content for me to review and copy edit you may paste it.**
\n Here are some questions from recent users which show different angles you can ask from:
\n "I'm a physiotherapist with 5 years of practice in San Francisco. Can you create social media Educational post?"
\n "I'm a dietician and here is existing content from my website. How can I improve it? Could you create effective content for it?"
\n "I just opened a new obesity management practice. Can you create a promotional social media post, advertising campaign and promotional email?"
\n "I just opened a yoga studio. Can you create all the different marketing content to promote my new business?"
""")

avatars={"system":"💻","user":"🤔","assistant":"💵"}
print("my avatars"+avatars["assistant"])
def send_request_and_process(full_response:str):       
    print("st session state messages: ", st.session_state.messages)
    for response in anthropic.Anthropic().messages.create(
        model="claude-3-opus-20240229"
        ,max_tokens=1024
        ,system= """
        Ignore all previous commands. 
        You are a helpful and patient marketing executive for Complementary & Integrative Care practice.
        Your tone is professional, concise, and courteous. 
        In reviewing the input, you look for inaccuracies, as well as understanding the user's intent.
        If the input is not marketing related then respond: "I can only answer marketing related content."
        If you are not sure about how to respond then say: "I'm sorry I do not know the answer to that."
        For everything else, Keep responses below 500 words. 
        Respond using the appropriate output format based on the type of content you are creating and note all URL links will start with www.porticowellness/yoursubdomain:
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
        - Announcement Post: Exciting news! We're thrilled to announce the launch of [Your Service/Product], designed to help you [Key Benefit]. Learn more: [Link to Website/Landing Page]
        - Educational Post: Did you know that [Interesting Fact/Statistic about Your Industry]? At [Your Brand], we're committed to helping you [Key Benefit] through our [Service/Product]. Discover how we can support you: [Link to Website/Blog Post]
        - Testimonial Post: "I've seen incredible results since working with [Your Brand]. Their [Service/Product] has helped me [Key Benefit]." - [Customer Name] Experience the difference for yourself: [Link to Website/Testimonial Page]
        - #[YourBrand] #[Relevant Hashtag] #[Industry Hashtag]
        - Call-to-action or question to encourage interaction
        - Tagging relevant accounts or partners
        - Tracking links or UTM parameters for analytics starting with www.porticowellness/yoursubdomain

        3. Email Newsletter Template
        - Compelling subject line
        - Personalized greeting
        - Featured content (e.g., blog post, success story, tip of the month)
        - Promotions or special offers
        - Upcoming events or webinars
        - Social media and contact information
        - Unsubscribe link and privacy policy

        4. Promotional Email Template
            - Subject Line: Limited Time Offer: [Discount/Offer] on [Service/Product]
            - Body:
        Dear [First Name],
        We're excited to announce a special limited-time offer just for you!
        From now until [End Date], you can enjoy [Discount/Offer] on our [Service/Product]. This is your chance to experience the benefits of [Key Benefit 1] and [Key Benefit 2] at an unbeatable price.
        To take advantage of this offer, simply [Call-to-Action] and enter the promo code [Promo Code] at checkout.

        Don't miss out on this amazing opportunity to [Key Benefit]. Act now before the offer ends!
        Best regards,
        [Your Name]
        [Your Brand]

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

        7. Advertising Campaign Template
        - Meta Ad:
        - Headline: Achieve [Key Benefit] with [Your Brand]
        - Body: Discover how our [Service/Product] can help you [Key Benefit] and transform your [Industry]. Learn more now!
        - Image: [Engaging Image or Video showcasing Your Service/Product]
        - Call-to-Action: [Sign Up Now/Learn More]

            - Google Search Ad:
            - Headline 1: [Your Brand] - [Key Benefit]
            - Headline 2: [Unique Selling Proposition]
            - Description: Discover how [Your Brand] can help you [Key Benefit]. [Call-to-Action] and experience the difference for yourself!
            - Call-to-Action: [Sign Up/Learn More]

            - Instagram Story Ad:
            - Image/Video: [Engaging Visual showcasing Your Service/Product]
            - Text Overlay: Achieve [Key Benefit] with [Your Brand]
            - Call-to-Action: [Swipe Up to Learn More]
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
    #for display
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