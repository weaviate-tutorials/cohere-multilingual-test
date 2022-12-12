import _setup

def semantic_serch(query):
    client = _setup.connect_to_weaviate()

    nearText = {
        "concepts": [query],
        "distance": 0.7,
    }

    properties = [
        # "name", "content", "enName", "link", "lang",
        "name", "enName", "content",
        "_additional {certainty distance}"
    ]

    result = (
        client.query
        .get("Document", properties)
        .with_near_text(nearText)
        .with_limit(5)
        .do()
    )

    return result['data']['Get']['Document']
  