#!/usr/bin/python3
"""
this is __init__ dunder process for the models directory
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
