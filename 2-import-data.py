import _setup
import json

client = _setup.connect_to_weaviate()

# Load data from the data.json file
data_file = open('data.json')
data = json.load(data_file)
# Closing file
data_file.close()

# Configure a batch process
client.batch.configure(
  batch_size=100, 
  dynamic=True,
  timeout_retries=3,
  callback=None,
)

# Batch import all Authors
for document in data['documents']:
    print("importing document: ", document["name"])

    properties = {
        "name": document["name"],
        "enName": document["enName"],
        "link": document["link"],
        "lang": document["lang"],
        "content": document["content"]
    }

    # client.batch.add_data_object(properties, "Document")
    client.data_object.create(properties, "Document")
