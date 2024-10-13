
search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

def suggest_completions(search_history, partial_query):
    suggestions = [query for query in search_history if query.startswith(partial_query)]
    return suggestions

partial_query = input("Enter your partial search query: ")

suggestions = suggest_completions(search_history, partial_query)

if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
