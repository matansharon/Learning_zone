import os
import gradio as gr
from langchain.chains import RetrievalQA
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma


# Make sure OPENAI_API_KEY is set in your environment
# os.environ["OPENAI_API_KEY"] = "your-key-here"

# Load your vector store
# This assumes you already have a Chroma DB created at ./chroma_db
# If you haven't created it, you'd need something like:
# vectorstore = Chroma.from_documents(docs, embedding=OpenAIEmbeddings())
# vectorstore.persist()
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())

# Create a retrieval-based QA chain
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0), 
    chain_type="stuff",
    retriever=retriever
)

def answer_question(query: str) -> str:
    # This function runs the query through the RAG pipeline
    if not query.strip():
        return "Please enter a question."
    return qa_chain.invoke(query)

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## Retrieval-Augmented Generation App")
    question = gr.Textbox(label="Your question", placeholder="Ask a question...")
    answer = gr.Textbox(label="Answer")
    submit_btn = gr.Button("Get Answer")
    
    submit_btn.click(fn=answer_question, inputs=question, outputs=answer)

# If you just want to run locally:
demo.launch()

# To use LangServe, run:
# 1. Save this code as app.py
# 2. In a terminal: langserve app:demo
#   This should host the Gradio app and chain via LangServe.
