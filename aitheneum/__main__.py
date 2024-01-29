#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AITheneum - A playground for study of and practice with all matters related with LLM's and Langchain
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""


from pathlib import Path

from aitheneum.rag_example import ask_about_forth


if __name__ == "__main__":
    from aitheneum.openai_basic import haiku, haiku_spanish 
    from aitheneum.pipe_example import pipe_example
    from aitheneum.rag_example import load_pdf
    
    #haiku_spanish()
    
    #pipe_example()
    
    #vectordb = load_pdf(Path("testdata/Forth_Primer.pdf"))
    #query = "What is DO...LOOP in Forth?"
    #results = vectordb.similarity_search(query)
    #print(results)
    
    query = "What is DO...LOOP in Forth?"
    result = ask_about_forth(query)
    print(result)