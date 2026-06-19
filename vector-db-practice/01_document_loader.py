from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("notes.pdf")

documents = loader.load()

print(documents)
print(documents[0].page_content)
print(documents[0].metadata)