#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AITheneum - A playground for study of and practice with all matters related with LLM's and Langchain
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""
import os
from pathlib import Path
import chromadb
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain

embeddings = OpenAIEmbeddings()


try:
        llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
        print(e)
        exit(1)


def load_pdf(path: Path):
 
    loader = PyPDFLoader(str(path))
    pages = loader.load_and_split()

    # save to disk
    vectordb = Chroma.from_documents(pages, embeddings, persist_directory="./chroma_db")
    return vectordb

def ask_about_forth(query:str):
    # load from disk
    vectordb = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

        <context>
        {context}
        </context>

        Question: {input}""")

    retriever = vectordb.as_retriever()
    
    document_chain = create_stuff_documents_chain(llm, prompt)
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    response = retrieval_chain.invoke({"input": query})
    return(response["answer"])

    #DOES NOT WORK
    #chain = retriever | prompt | llm
    #response = chain.invoke({"input": query})
    #return(response["answer"])
    