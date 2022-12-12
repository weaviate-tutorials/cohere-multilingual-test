# cohere-multilingual-test

## Prerequisites

To make use of this project you need 2 things:

1. Get a [Cohere API key](https://dashboard.cohere.ai/api-keys).
2. Create an `instance of Weaviate`
    * it is easiest to create a free instance with [Weaviate Cloud Service](https://console.semi.technology/), without authentication
    * or you can set up an instance with [Docker](https://weaviate.io/developers/weaviate/current/installation/index.html)

## Setup

To set up the project:
1. Update `_setup.py`
    * `url` - set to your Weaviate address
    * `X-Cohere-Api-Key` – set to your API key
2. Add Schema:
    ```bash
    1-add-schema.py
    ```
3. Import data
    ```bash
    2-import-data.py
    ```

## Query

Once you set up the project, you can run queries with the `query.py`. Like this:

```bash
python query.py "musical instruments"
```
