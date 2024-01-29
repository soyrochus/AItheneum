#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AITheneum - A playground for study of and practice with all matters related with LLM's and Langchain
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from aitheneum.haiku_parsers import HaikuOutputParser

output_parser = StrOutputParser()
haiku_parser = HaikuOutputParser()

try:
        llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception as e:
        print(e)
        exit(1)

def haiku():
    """
    Write an haiku about the challenges of using Langchain
    """
    message = llm.invoke("Write an haiku about the challenges of using Langchain")
    print(message.content)


def haiku_spanish():
    """
    Write an haiku about the challenges of using Langchain (in Spanish)
    """

    prompt_es = ChatPromptTemplate.from_messages([
        ("system", "You are a relentless translator from any language to Spanish"),
        ("user", "{input}")
        ])
    #chain = prompt_es | llm | output_parser
    chain = prompt_es | llm | haiku_parser 
    
    message = chain.invoke({"input": "write an haiku about the pleasure of using Python"})
    print(message)

