#!/usr/bin/python3
"""
Module for the creation of a unique FileStorage instance for the application
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
