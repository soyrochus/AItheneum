#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AITheneum - A playground for study of and practice with all matters related with LLM's and Langchain
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""

import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

#set the key from file "openai_key.txt" in the same directory as this file or set the environment variable OPENAI_API_KEY
load_dotenv("openai_api_key.env")
