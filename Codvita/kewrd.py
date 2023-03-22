a=["break", "case", "continue", "default", "defer", "else","for", 
    "func", "goto", "if", "map", "range", "return", "struct", "type", "var"]
grter=input()
if grter in a:
    print(grter,"is a keyword")
else:
    print(grter,"is not a keyword")