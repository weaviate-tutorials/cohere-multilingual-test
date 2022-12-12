import weaviate

def connect_to_weaviate():
    return weaviate.Client(
        url="https://your-name-goes-here.semi.network",
        additional_headers={
            'X-Cohere-Api-Key': 'your-api-key-goes-here'
        }
    )
