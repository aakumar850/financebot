from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import streamlit as st
anthropic = Anthropic()
anthropic.api_key=st.secrets['ANTHROPIC_API_KEY']
prompt = st.text_input('Ask your question', 'How to save money?')
completion = anthropic.completions.create(
    model="claude-2",
    max_tokens_to_sample=300,
   prompt=f"{HUMAN_PROMPT} {prompt} {AI_PROMPT}",
)
st.write(completion.completion)
