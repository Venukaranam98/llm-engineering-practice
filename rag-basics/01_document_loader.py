from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("notes.pdf")

documents = loader.load()

print(documents)