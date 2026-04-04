
with open("Task2.txt", "r") as f:
    text = f.read()

print("Original text:\n", text)

contractions = {
    "i'm": "i am",
    "it's": "it is",
    "don't": "do not",
    "can't": "cannot",
    "won't": "will not",
    "didn't": "did not",
    "doesn't": "does not",
    "wouldn't": "would not",
    "couldn't": "could not",
    "shouldn't": "should not",
    "isn't": "is not",
    "aren't": "are not",
    "wasn't": "was not",
    "weren't": "were not",
    "haven't": "have not",
    "hasn't": "has not",
    "hadn't": "had not",
    "i've": "i have",
    "we've": "we have",
    "they've": "they have",
    "i'll": "i will",
    "he'll": "he will",
    "she'll": "she will",
    "we'll": "we will",
    "they'll": "they will",
    "i'd": "i would",
    "he'd": "he would",
    "she'd": "she would",
    "that's": "that is",
    "there's": "there is",
    "what's": "what is",
    "let's": "let us",
    "who's": "who is",
    "you're": "you are",
    "they're": "they are",
    "we're": "we are",
    "you've": "you have",
    "you'll": "you will",
    "you'd": "you would",
}

text = text.lower()

for contraction, expanded in contractions.items():
    text = text.replace(contraction, expanded)

numbers = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three',
    '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
    '8': 'eight', '9': 'nine'
}
result = ''
for char in text:
    if char.isdigit():
        result += numbers[char]
    else:
        result += char
text = result

punctuation = ['!', '.', ',', '?', ':', ';', '"', "'", '(', ')', '[', ']', '{', '}', '-', '–', '_']
for p in punctuation:
    text = text.replace(p, '')

text = ' '.join(text.split())

print("\nNormalized text:\n", text)