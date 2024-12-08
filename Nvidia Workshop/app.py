import streamlit as st
import PyPDF2


def read_pdf(file: st.file_uploader): # type: ignore
    pdf_reader=PyPDF2.PdfReader(file)
    pages=pdf_reader.pages
    text=''
    for page in pages:
        text+=page.extract_text()
    return text


def sidebar():
    with st.sidebar:
        file=st.file_uploader("Upload a file",type=["pdf"])
        if file:
            text=read_pdf(file)
            st.write("Text extracted from the pdf file")
            st.write(text)
            st.write("End of text")
        else:
            st.write("Please upload a pdf file")
        

def main():
    sidebar()
    st.title("Nvidia Workshop")
    st.write("Welcome to the Nvidia Workshop")
    st.write("This is a simple Streamlit app")
    
    query=st.chat_input("Enter your query")
    if query:
        st.write("You entered: ",query)

if __name__ == "__main__":
    main()