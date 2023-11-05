from dotenv import load_dotenv
import streamlit as st
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
import pdfplumber


def main():
  load_dotenv()
  st.set_page_config(page_title="Domain Knowledge Base in PDF")
  st.header("Domain Knowledge Base in PDF💬")
  # upload file
  pdf = st.file_uploader("Upload a PDF file", type="pdf")

  # extract the context
  if pdf is not None:
    text = ""
    with pdfplumber.open(pdf) as pdf_reader:
      for page in pdf_reader.pages:
        text += page.extract_text()
    
    # split the text
    text_splitter = CharacterTextSplitter(
      separator="\n",
      chunk_size=1000,
      chunk_overlap=50,
      length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    # create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    user_question = st.text_input("Please feel free to ask me something:")
    if user_question:
      docs = knowledge_base.similarity_search(user_question)
      
      llm = OpenAI()
      chain = load_qa_chain(llm, chain_type="stuff")
      # cost tracker
      with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(cb)
          
      st.write(response)

if __name__ == '__main__':
    main()