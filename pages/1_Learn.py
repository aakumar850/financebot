import streamlit as st

st.set_page_config(
    page_title="Learn | Marketing Tips and Tricks",
    page_icon="portico_bug.svg",
)

(column1,column2)=st.columns([2,8])
column1.image("Portico-logo-color.svg", width=100)
column2.title("Key Marketing Concepts")

st.write("""
    \n **Target Audience** A target audience is the specific group of people most likely to be interested in your products or services. They are the people you want to reach with your marketing messages.
    \n **Example:** As a yoga studio owner offering yoga therapy, you may have a target audience of adults aged 35-55 who are interested in holistic health and stress relief.

   \n **Marketing Channels** Marketing channels are the various platforms and methods used to communicate with your target audience and promote your business. These can include digital channels like websites, social media, and email, as well as traditional channels like print ads, events, and referrals.
   \n **Example:** As a CAI entrepreneur, you may use a combination of channels, such as a website, Meta page, Instagram account, and local health fairs, to reach your target audience.

   \n **Content Marketing** Content marketing is a strategic approach focused on creating and distributing valuable, relevant, and consistent content to attract and retain a clearly defined audience and, ultimately, to drive profitable customer action.
   \n **Example:** As an Ayurvedic practioner, you could create blog posts about the benefits of ayurveda, share helpful tips on social media, and offer a free e-book on stress management to attract potential clients.

   \n **Search Engine Optimization (SEO)** SEO is the practice of optimizing your website and online content to improve your visibility and ranking in search engine results pages (SERPs). This helps drive more organic (non-paid) traffic to your website.
   \n **Example:** As a CAI entrepreneur using Portico Care will optimize your website by including relevant keywords in your page titles, headings, and content, as well as building high-quality backlinks from other reputable websites.

   \n **Conversion Rate** Conversion rate is the percentage of visitors to your website who take a desired action, such as filling out a contact form, subscribing to a newsletter, or making a purchase.
   \n **Example:** If 100 people visit your website and 10 of them sign up for a free consultation, the conversion rate would be 10%.
         
   \n **Branding** Branding is the process of creating a unique identity for your business that distinguishes it from competitors. It encompasses elements such as your logo, color palette, tone of voice, and overall customer experience.
   \n **Example:** As a CAI entrepreneur, you could create a cohesive brand identity by using a specific color scheme and logo across all your marketing materials, and by developing a warm, empathetic tone in their communications.

   \n **Email Marketing** Email marketing is the practice of sending targeted, personalized emails to a list of subscribers who have opted-in to receive communications from your business. It can be used to nurture leads, promote services, and build customer loyalty.
   \n **Example:** As a CAI entrepreneur, you could send a monthly newsletter featuring health tips, client success stories, and promotional offers for your services.

   \n **Social Media Advertising** Social media advertising involves creating and placing paid ads on social media platforms like Facebook, Instagram, and LinkedIn to reach a larger, targeted audience.
   \n **Example:** As a CAI entrepreneur, you could create a Meta ad campaign targeting people in your local area who have expressed interest in holistic health, meditation, or stress relief.

   \n **Analytics** Analytics refers to the process of collecting, analyzing, and reporting data related to your marketing efforts. It helps you measure the effectiveness of your campaigns and make data-driven decisions.
   \n **Example:** As a CAI entrepreneur using Portico Care, we will share Analytics to track website traffic, page views, and conversion rates. You could use this data to optimize your content and marketing strategies.

   \n **Customer Personas** Customer personas are fictional, generalized representations of your ideal customers. They help you understand your target audience's needs, preferences, and behaviors, enabling you to tailor your marketing efforts accordingly.
   \n **Example:** A CAI entrepreneur, you could create a persona representing a busy, health-conscious professional looking for natural ways to manage stress and improve well-being.

   \n **Content Calendar** A content calendar is a planning tool that helps you organize, schedule, and manage your content creation and distribution across various marketing channels.
   \n **Example:** As a CAI entrepreneur, you could use a content calendar to plan out a month's worth of blog posts, social media updates, and email newsletters, ensuring a consistent and balanced content mix.

   \n **A/B Testing** A/B testing, also known as split testing, is a method of comparing two versions of a marketing element (such as a webpage, email subject line, or ad) to determine which one performs better.
   \n **Example:** As a CAI entrepreneur, you could create two versions of a social media post, each with a different headline, and use A/B testing to see which one generates more sign-ups for a free consultation.

   \n **Customer Retention** Customer retention refers to the strategies and actions taken by a business to keep existing customers engaged and encourage them to continue using their products or services.
   \n **Example:** A CAI entrepreneur, you could implement a loyalty program that rewards clients for recurring appointments or referrals, helping to foster long-term relationships and reduce client churn.
    """)