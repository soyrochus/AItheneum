#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AITheneum - A playground for study of and practice with all matters related with LLM's and Langchain
@copyright: Copyright © 2024 Iwan van der Kleijn
@license: MIT
"""

class Logger:
    def __init__(self, name):
        self.name = name
        self.log_methods = []

    def __or__(self, other):
        if isinstance(other, Logger):
            combined_logger = Logger(f"{self.name}|{other.name}")
            combined_logger.log_methods = self.log_methods + other.log_methods
            return combined_logger
        else:
            raise ValueError("Can only combine Logger instances")

    def add_log_method(self, method):
        self.log_methods.append(method)

    def log(self, message):
        for method in self.log_methods:
            method(self.name, message)

# Define two logging functions
def console_logger(name, message):
    print(f"[{name} - Console] {message}")

def file_logger(name, message):
    with open(f"{name}.log", "a") as f:
        f.write(f"[{name} - File] {message}\n")

def pipe_example():
    # Create two Logger instances and add different log methods
    console = Logger("ConsoleLogger")
    console.add_log_method(console_logger)

    file = Logger("FileLogger")
    file.add_log_method(file_logger)

    # Combine loggers using the | operator
    combined_logger = console | file

    # Use the combined logger
    combined_logger.log("This is a test message.")
