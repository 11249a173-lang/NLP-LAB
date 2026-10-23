import re
text = "Hello world! Natural language processing is fun."
space_tokens = text.split()
print("Space split:", space_tokens)
regex_tokens = re.findall(r"\b\w+\b", text)
print("Regex tokens:", regex_tokens)
