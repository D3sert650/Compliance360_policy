
from openai import OpenAI
import streamlit as st

# import os

# if os.path.exists('images/AuditManagement.jpeg'):
#     print('File found.')
# else:
#     print('File not found.')


# Set page configuration
st.set_page_config(
    page_title="Compliance360+ Home",
    page_icon=":shield:",
    layout="wide",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #575757;
        padding: 20px;
    }
    .title {
        font-size: 3em;
        color: #575757;
        text-align: center;
        margin-bottom: 20px;
    }
    .subtitle {
        font-size: 1.5em;
        color: #D1F801;
        text-align: center;
        margin-bottom: 40px;
    }
    .feature {
        text-align: center;
        margin-bottom: 30px;
    }
    .feature img {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
    }
    .feature h3 {
        font-size: 1.2em;
        color: #D1F801;
        margin-top: 10px;
    }
    .feature p {
        font-size: 1em;
        color:#D1F801;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#col1, col2 = st.columns([1, 2])

# Main title
# with col1: 
#     st.image(image="images/Compliance360+.jpeg", width=100)

st.markdown('<div class="title">Welcome to Compliance360+</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Streamlining Your Compliance Journey with AI-Powered Precision</div>', unsafe_allow_html=True)


# with col2: 
#     # st.markdown('<div class="title align-items: center; justify-content: center">Welcome to Compliance360+</div>', unsafe_allow_html=True)
#     # st.markdown('<div class="subtitle">Streamlining Your Compliance Journey with AI Powered Precision</div>', unsafe_allow_html=True)
#     st.markdown(
#         """
#         <div style="display: flex; height: 100%; align-items: center; justify-content: center;">
#             <h1 style="color: #EAEAEA; font-size: 50px; text-align: center;">Welcome to Compliance360+</h1>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
#     st.markdown(
#         """
#         <div style=" align-items: center; justify-content: center;">
#          <h2 style="color: #FFFF99; font-size: 20px; text-align: center;">
#             <b>Streamlining Your Compliance Journey with AI-Powered Precision</b>
#         </h2>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )
# Features section
features = [
    {
        "image": "images/AuditManagement.jpeg",
        "title": "Automated Audit Management",
        "description": "Centralize your compliance status with real-time dashboards and automated evidence collection."
    },
    {
        "image": "images/RAM.png",
        "title": "Risk Assessment & Monitoring",
        "description": "Leverage dynamic risk registers and predictive alerts to stay ahead of potential compliance gaps."
    },
    {
        "image": "images/AIRG.png",
        "title": "AI Governance Module",
        "description": "Ensure AI-specific compliance with specialized dashboards, model oversight, and bias detection."
    },
]

# Display features
for feature in features:
    col1, col2, col3 = st.columns([1, 2, 1])
    print(feature['image'])
    st.image(feature['image'], caption=feature['title'], width=600, use_container_width=True)
    with col2:
        st.markdown(
            f"""
            <div class="feature">
                <h3>{feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
# <img src="{feature['image']}" alt="{feature['title']}">
# Call to Action
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://compliance3609.godaddysites.com/" target="_blank" style="background-color: #4B8BBE; color: white; padding: 15px 25px; text-decoration: none; border-radius: 5px; font-size: 1.2em;">Learn More</a>
    </div>
    """,
    unsafe_allow_html=True
)

# # Show title and description.
# st.title("💬 Compliance360+")
# st.write(
#     # "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
#     # "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     # "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
#     "Welcome to Compliance360+."
#     "We're an AI company for AI companies."

# )


# import streamlit as st

# policy_assistant = st.Page("Policy-Assistant.py", title= "Policy Assistant")
# risk_scout = st.Page("Risk_Scout.py", title="Risk Scout")
# compliance_strategist = st.Page("Compliance-Strategist.py", title="Compliance Strategist")


# # Define pages
# # pages = [
# #     #st.Page("Landing-Page.py", title="💬 Compliance360+", icon="📝"),
# #     st.Page("Policy-Assistant.py", title="Policy Assistant", icon="📝"),
# #     st.Page("Risk_Scout.py", title="Risk Scout", icon="🔍"),
# #     st.Page("Compliance-Strategist.py", title="Compliance Strategist", icon="📋"),
# # ]

# pg = st.navigation([policy_assistant,risk_scout, compliance_strategist ])
# st.set_page_config(page_title="Landing Page")
# # Set up navigation


# # Run the selected page
# pg.run()


# st.sidebar.title("Sidebar Title")
# option = st.sidebar.selectbox("Choose a number", [1, 2, 3, 4, 5])
# st.sidebar.write(f"You selected {option}")

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
#openai_api_key = st.text_input("OpenAI API Key", type="password")
# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

#     # Create an OpenAI client.
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
