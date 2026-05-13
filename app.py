import streamlit as st


st.title("Bottino carino")

with st.chat_message("assistant"):
    st.write("Hello human")

###########
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})