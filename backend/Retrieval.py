import chromadb
# from transformers import pipeline, set_seed
# from chromadb.utils import embedding_functions
# from openai import OpenAI


class RAG_LLM:
    def __init__(self):
        self.chroma_client = chromadb.HttpClient(
            host='34.93.228.164', port=6969)
        self.collection = self.chroma_client.get_or_create_collection(
            name="impeda")

    def delete(self):
        self.chroma_client.delete_collection(name="impeda")

    def get_embedding(self, text, model="text-embedding-ada-002"):
        return self.client.embeddings.create(input=[text], model=model).data[0].embedding

    def add_data(self, data):
        # Convert DataFrame to a list of dictionaries
        data_dict_list = data.to_dict(orient='records')

        # Check if 'data' column exists in the DataFrame
        if 'data' in data.columns:
            documents = list(data['data'])
        else:
            documents = data_dict_list

        ids = [str(self.collection.count() + x)
               for x in range(len(data_dict_list))]
        self.collection.add(
            documents=documents,
            metadatas=[{"Tools": "Tools_data"}] * len(data_dict_list),
            ids=ids
        )

    def query(self, data):
        results = self.collection.query(
            query_texts=[data],
            n_results=5
        )
        return results


# Example usage


# ob = RAG_LLM()
# inp = 'AndhraPradesh Fish Exporters list'
# data = ob.query(inp)['documents'][0]
# # ob.delete()
# print(type(data))
# print(data)
# for i in data:
#     print(i)
#     print()


# # generator = pipeline('text-generation', model='gpt2-large')
# inp = '''Here is a Query. Rewrite the query in three sentences.

#         Summarize high severity tickets from the customer UltimateCustomer

#         Example :

#         Query:
#         Prioritize my P0 issues and add them to the current sprint

#         output:
#         1.) My Issue
#         2.)Prioritize P0 issues
#         3.)Add to the current sprint
#         '''

# import requests

# API_URL = "https://api-inference.huggingface.co/models/gpt2-large"
# headers = {"Authorization": "Bearer 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"}

# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()

# output = query({
# 	"inputs": inp,
# })

# print(output)
# generator(inp, max_length=100, num_return_sequences=1)
