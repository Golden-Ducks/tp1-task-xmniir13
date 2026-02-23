import nltk
import re
import spacy

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#--
text = "Hi Tarik\nHow are you?"
text = text.lower()
text = re.sub(r'[^\w\s]', '', text)
print(text)

print(re.findall(r"\s", text))

text = "I do not like python!"
tokens = text.split()
print(tokens)

text = "I do not like python!"
tokens = word_tokenize(text)
print(tokens)

#-------
nlp = spacy.load("en_core_web_sm")
text = "say something !"
doc = nlp(text)
tokens = [token.text for token in doc]
print(tokens)  

#---- 
text = "This is a sample sentence, showing off the stop words filtration."
tokens = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if w.lower() not in stop_words]
print("Original tokens:", tokens)
print("After removing stopwords:", filtered_tokens)

#--- 
text = "save your life and learn n8n."
doc = nlp(text)
filtered_tokens = [token.text for token in doc if not token.is_stop]
print("Original text:", text)
print("After removing stopwords:", filtered_tokens)