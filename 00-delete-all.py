import _setup
import json

client = _setup.connect_to_weaviate()

client.schema.delete_all()

schema = client.schema.get()
print(json.dumps(schema))