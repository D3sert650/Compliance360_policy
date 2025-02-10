import streamlit as st

st.set_page_config(
    page_title="Compliance Strategist",
    page_icon="📝",
)

st.title("Compliance Strategist")
st.write("""


Compliance Officer 🏛️⚖️

“Your AI-Driven Compliance Commander—Enforce Policies, Ensure Security, and Stay Audit-Ready.”

🔍 Take Control of Compliance with Intelligent Automation

✅ Real-Time Regulatory Alerts – Stay ahead of changing laws and mandates.

✅ Automated Policy Enforcement – Ensure governance with AI-driven rule execution.

✅ AI-Powered Risk Reports – Identify gaps before they become violations.

✅ Seamless Integration – Works with internal compliance workflows and documentation.

🔒 Govern with confidence, mitigate compliance risks, and uphold industry standards. With Compliance Officer, managing regulations is no longer reactive—it’s proactive and automated! 🚀


""")

st.image("images/CS.png")



# # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

#     # Create a session state variable to store the chat messages. This ensures that the
#     # messages persist across reruns.
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display the existing chat messages via `st.chat_message`.
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Create a chat input field to allow the user to enter a message. This will display
#     # automatically at the bottom of the page.
#     if prompt := st.chat_input("What is up?"):

#         # Store and display the current prompt.
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )

#         # Stream the response to the chat using `st.write_stream`, then store it in 
#         # session state.
#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})
