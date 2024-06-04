import streamlit as st

st.title('Streamlit Course')

st.code('''def get_anthropic_response(text):
    import os
    import anthropic
    client=anthropic.Anthropic(
        api_key=os.environ.get("ANTHROPIC_API_KEY"))
    message = client.messages.create(
            model="claude-3-opus-20240229",
            # model='claude-3-haiku-20240307',
            max_tokens=4000,
            temperature=0.2,
            system=f"""
            the user input is a video transcript of a lecture.
            summarize the transcript.
            and then add a python code that demonstrate to concept of the lecture.
            """,
            messages=[
                {"role": "user", "content":text}
            ]
        )
    return message['messages'][0]['content']''')