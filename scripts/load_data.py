import sys
import os

# Append the root directory to the system path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(root_dir)

from langchain.document_loaders import WebBaseLoader
from vector_db import VectorDb
from open_ai import OpenAi

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide the path url")
        sys.exit(1)

    urls = sys.argv[1:]

    open_ai = OpenAi()
    vector_db = VectorDb()

    loader = WebBaseLoader(urls)
    content = loader.load()
    vector_db.load_page_to_db(content)

    print("Webpages loaded to the database successfully.")
