#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AITheneum - A playground for study of and practice with all matters related with LLM's and Langchain"
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""
import os
from langchain_openai import ChatOpenAI

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



