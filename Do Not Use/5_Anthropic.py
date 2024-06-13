from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
import streamlit as st
anthropic = Anthropic()
anthropic.api_key=st.secrets['ANTHROPIC_API_KEY']
prompt = st.text_input('Ask your question', '?')
completion = anthropic.completions.create(
    model="claude-2.1",
    max_tokens_to_sample=1000,
    temperature=0,
    prompt=f"{HUMAN_PROMPT}{AI_PROMPT}",
)
st.write(completion.completion)
