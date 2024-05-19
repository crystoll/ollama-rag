import ollama

response = ollama.generate(model='phi3', 
                           prompt='explain quantum computing for a six-year old please.')
print(response['response'])


