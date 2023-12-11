import nltk
from utils import tokenizer 
from utils import lemmatizer
from utils import tense 
from utils import search
from utils import stopword_filter

def animation_view(text):
	tokenized = tokenizer.tokenize(text)
	stopFilterdWords = tokenized["words"]
	filtered_text = lemmatizer.lemmatize(stopFilterdWords, tokenized["tagged"])
	words = tense.tensing(filtered_text, tokenized["tense"])
	response = search.search(words)
	return response
	


res = animation_view("Hi King How Are You")
print(res)