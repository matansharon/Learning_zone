import streamlit as st
import PyPDF2
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
def read_pdf(file: st.file_uploader): # type: ignore
    pdf_reader=PyPDF2.PdfReader(file)
    pages=pdf_reader.pages
    text=[]
    for page in pages:
        text.append(page.extract_text())
    return text

def embedder(pages):
    client = OpenAI()
    results=[]
    for page in pages:
        response = client.embeddings.create(
            input=page,
            model="text-embedding-3-large"
        )

    results.append(response.data[0].embedding)
    return results


def sidebar():
    with st.sidebar:
        st.session_state.file=st.file_uploader("Upload a file",type=["pdf"])
        if st.session_state.file:
            pages_text=read_pdf(st.session_state.file)
            st.write("Text extracted from the pdf file")
            st.write(pages_text)
            st.write("End of text")
        else:
            st.write("Please upload a pdf file")
        

def main():
    sidebar()
    st.title("Nvidia Workshop")
    st.write("Welcome to the Nvidia Workshop")
    st.write("This is a simple Streamlit app")
    
    query=st.chat_input("Enter your query")
    show=st.button("Show")
    if show and st.session_state.file:
        pages=read_pdf(st.session_state.file)
        embedding=embedder(pages)
        st.write("Embedding of the text")
        st.write(embedding)
    if query:
        st.write("You entered: ",query)

if __name__ == "__main__":
    main()