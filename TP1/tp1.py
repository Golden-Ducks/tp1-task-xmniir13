with open("task1.txt", "r") as f:
    text = f.read()

print("Original text:\n", text)

text = text.lower()

symbols = ['@', '#', '$', '&', '*', '^', '~', '`', '|', '<', '>', '/', '\\']
for symbol in symbols:
    text = text.replace(symbol, '')

punctuation = ['!', '.', ',', '?', ':', ';', '"', "'", '(', ')', '[', ']', '{', '}', '-', '–', '_']
for p in punctuation:
    text = text.replace(p, '')

clean = ''
for char in text:
    if not char.isdigit():
        clean += char
text = clean                        
text = ' '.join(text.split())

print("\nCleaned text:\n", text)

###########
# Remove % when NOT preceded by a number 
#   Remove % when between a number and letters
###