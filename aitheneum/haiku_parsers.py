#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AITheneum - A playground for study of and practice with all matters related with LLM's and Langchain
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""

from typing import List
from langchain_core.output_parsers.transform import BaseTransformOutputParser

class HaikuOutputParser(BaseTransformOutputParser[str]):
    """OutputParser that parses LLMResult into a more pleasant Haiku representation."""

    @classmethod
    def is_lc_serializable(cls) -> bool:
        """Return whether this class is serializable."""
        return True

    @classmethod
    def get_lc_namespace(cls) -> List[str]:
        """Get the namespace of the langchain object."""
        return ["langchain", "schema", "output_parser"]

    @property
    def _type(self) -> str:
        """Return the output parser type for serialization."""
        return "default"

    def parse(self, text: str) -> str:
        """Returns the input text with no changes."""
        
        # Split the message into lines
        #lines = text.split('\n')
        # Join the lines with an empty line in between
        #pretty_haiku = "\n\n".join(lines)
        #return pretty_haiku
        
        lines = text.split('\n')
        styled_lines = [
            f"\033[93m{lines[0]}\033[0m",  # Yellow
            f"\033[1;97m{lines[1]}\033[0m",  # Bold White
            f"\033[95m{lines[2]}\033[0m"     # Purple
        ]
        pretty_haiku = "\n\n".join(styled_lines)
        return pretty_haiku
