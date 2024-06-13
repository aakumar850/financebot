import streamlit as st

st.set_page_config(
    page_title="Plan | Campaigns",
    page_icon="Portico care logo.png",
)

(column1,column2)=st.columns([2,8])
column1.image("Portico care logo.png", width=100)
column2.title("Plan Your Campaigns")
st.write("""
\n Here are a few things to consider when planning your **:green[marketing campaign]** strategy:
\n **Social Media Cadence & Strategy:**
\n 1. Posting Frequency:
\n - Meta: 3-4 times per week.  - Instagram: 1-2 times per day.  - Twitter: 1-3 times per day.   - LinkedIn: 2-3 times per week
\n 2. Content Mix:
\n - Educational posts: 30%.    - Promotional posts: 20%.     - Engagement posts (polls, questions, etc.): 20%.    - Inspirational posts: 20%.  - Behind-the-scenes/personal posts: 10%
\n 3. Best Practices:
\n    - Use high-quality visuals (images, videos, infographics)
\n    - Engage with your audience by responding to comments and messages
\n    - Leverage relevant hashtags to increase reach
\n    - Monitor and analyze performance to optimize future content
\n **Email Marketing Cadence & Strategy:**
\n 1. Email Frequency:
\n    - Newsletter: 1-2 times per month.  - Promotional emails: 1-2 times per month.  - Automated welcome series: 3-5 emails over 2 weeks. - Abandoned cart/browsing follow-up: 2-3 emails over 1 week
\n 2. Content Strategy:
\n - Provide value through educational content, tips, and resources
\n - Highlight customer success stories and testimonials
\n - Announce new products, services, or promotions
\n - Segment your list based on interests, behaviors, or demographics
\n 3. Best Practices:
\n - Craft compelling subject lines to increase open rates
\n - Personalize emails with the recipient's name and relevant content
\n - Optimize for mobile devices (responsive design, concise copy)
\n - Include clear calls-to-action (CTAs) to drive engagement and conversions
\n **Advertising Campaign Cadence & Strategy:**
\n 1. Advertising Channels:
\n - Facebook & Instagram Ads.  - Google Search & Display Ads.  - LinkedIn Sponsored Content
\n 2. Campaign Structure:
\n - Top-of-funnel (awareness): Promote educational content, blog posts, or videos
\n - Middle-of-funnel (consideration): Showcase product/service benefits, case studies, or webinars
\n - Bottom-of-funnel (conversion): Offer free trials, demos, or limited-time promotions
\n 3. Budget Allocation:
\n - Allocate budget based on your target audience and their platform preferences
\n - Start with a small daily budget and adjust based on performance
\n - Consider increasing budget for high-performing campaigns or key promotions
""")