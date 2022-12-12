import sys
import _query_base
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Get the user query from the command line
user_query = str(sys.argv[1])

# Pass the user query to Weaviate
query_result = _query_base.semantic_serch(user_query)

# Print out the result
pp.pprint(query_result)
