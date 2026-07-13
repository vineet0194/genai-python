import tiktoken

# means i want to create an encoder for gpt-4o
enc = tiktoken.encoding_for_model("gpt-4o")

text = "Hey There! My name is Vineet"
tokens = enc.encode(text)

# Tokens: [25216, 3274, 0, 3673, 1308, 382, 69023, 292]
print("Tokens:", tokens)

tokens = [25216, 3274, 0, 3673, 1308, 382, 69023, 292]
decoded = enc.decode(tokens)

print("Decoded:", decoded)