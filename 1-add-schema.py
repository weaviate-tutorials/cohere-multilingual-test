import _setup
import json

client = _setup.connect_to_weaviate()

class_obj = {
    "class": "Document",
    "description": "A class called document",
    "vectorizer": "text2vec-cohere",
    "moduleConfig": {
        "text2vec-cohere": {
            "model": "multilingual-22-12",
            "truncate": "NONE"
        }
    },
    "properties": [
    {
        "name": "content",
        "dataType": [ "text" ],
        "description": "Article body",
        "moduleConfig": {
            "text2vec-cohere": {
                "skip": False,
                "vectorizePropertyName": False
            }
        }
    },
    {
        "name": "name",
        "dataType": [ "string" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    {
        "name": "enName",
        "dataType": [ "string" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    {
        "name": "link",
        "dataType": [ "string" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    {
        "name": "lang",
        "dataType": [ "string" ],
        "moduleConfig": { "text2vec-cohere": { "skip": True } }
    },
    ]
}

# add the schema
client.schema.create_class(class_obj)

# get the schema
schema = client.schema.get()

# print the schema
print(json.dumps(schema, indent=4))