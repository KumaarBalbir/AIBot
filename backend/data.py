import pandas as pd
from Retrieval import RAG_LLM
data = pd.read_csv('/Users/shashank/python/RAG/Fish-Production-in-India.csv')
docs = list(data['data'])
print(type(docs))

ob = RAG_LLM()
data = data.astype(str)
ob.add_data(data)