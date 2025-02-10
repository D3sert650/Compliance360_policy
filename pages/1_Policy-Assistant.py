import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Policy Assistant",
    page_icon="📝",
)

st.title("Policy Assistant")
st.write(
    "Your AI-Powered Compliance Copilot—Simplifying Regulations, Automating Risk Management, and Keeping Your Business Audit-Ready 24/7.")

st.write('''✨ Key Benefits:

✅ Instant Regulatory Insights – Get AI-driven interpretations of global compliance laws.

✅ Automated Compliance Monitoring – Stay ahead of audits and policy changes.

✅ Smart Risk Assessment – Identify and mitigate compliance risks proactively.

✅ Effortless Documentation – Generate reports and policy summaries in seconds.

🔎 Stay compliant. Stay secure. Stay ahead. With Policy Assistant, compliance is no longer a headache, it’s an automated advantage.''')

# Create a session state variable to store the chat messages. This ensures that the
# messages persist across reruns.


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the existing chat messages via `st.chat_message`.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Create a chat input field to allow the user to enter a message. This will display
    # automatically at the bottom of the page.
if prompt := st.chat_input("How can the Policy Assistant help you with your compliance needs?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

        # Stream the response to the chat using `st.write_stream`, then store it in
        # session state.
    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
