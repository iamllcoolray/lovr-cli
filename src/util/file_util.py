import os

def content(file_name: str) -> str:
    file_path = os.path.join(os.getcwd(), f"src/docs/{file_name}")
    
    with open(file_path, 'r') as src:
        source_file_content = src.read()
        return source_file_content