from docling.document_converter import DocumentConverter
import os
import requests
import json
from typing import Optional, Dict, Any
from config import *
from pathlib import Path


def html_to_markdown(path):
    """Fetch a Wayback Machine snapshot"""
    target = MARKDOWN_FOLDER + path.name + '.md'
    if os.path.isfile(target):
        return
    try:
        converter = DocumentConverter()
        result = converter.convert(path)
        open(target, 'w').write(result.document.export_to_markdown())
    except Exception as e:
        print(f"Error: {e}")
        return False

def run():
    # Test URLs
    for path in Path(HTML_FOLDER).rglob('*.html'):
        print(path)
        html_to_markdown(path)

# Example usage
if __name__ == "__main__":
    run()

