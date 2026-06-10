from sentence_transformers import (
    SentenceTransformer
)
from sentence_transformers.util import cos_sim

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

text1 = "Car"

text2 = "Automobile"

embedding1 = model.encode(text1)

embedding2 = model.encode(text2)

similarity = cos_sim(
    embedding1,
    embedding2
)

print(similarity)