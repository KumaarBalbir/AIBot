import requests
from Retrieval import RAG_LLM

API_URL = "https://api-inference.huggingface.co/models/gpt2-large"
headers = {"Authorization": "Bearer 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"}


def Query(input_text):

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    ob = RAG_LLM()
    out = ob.query(input_text)['documents'][0]
    context = ""
    for i, txt in enumerate(out):
        context = context+"\n"+f'{i}.)  ' + txt

    input_query = "Give Answers based on the Data Given Below as Context...\n" + \
        "Context:  \n"+context + "\n\n" + input_text

    output = ""
    output = query({
        # "inputs": input_text
        "inputs": input_query
    })
    # print(output)
    return output

# Example call
# Query("What are Top Fish Exporters in Andhra Pradesh and Mumbai?")
