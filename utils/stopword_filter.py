from nltk.corpus import stopwords

#stopwords that will be remove
stop_words = set(["mightn't", 
're', 'wasn', 'wouldn', 'be', 'has', 'that', 'does', 'shouldn', 'do', "you've",'off', 'for',
 "didn't", 'm', 'ain', 'haven', "weren't", 'are', "she's", "wasn't", 'its', "haven't", "wouldn't", 
 'don', 'weren', 's', "you'd", "don't", 'doesn', "hadn't", 'is', 'was', "that'll", "should've", 'a', 
 'then', 'the', 'mustn', 'i', 'nor', 'as', "it's", "needn't", 'd', 'am', 'have',  'hasn', 'o', "aren't",
 "you'll", "couldn't", "you're", "mustn't", 'didn', "doesn't", 'll', 'an', 'hadn', 'whom', 'y', "hasn't", 
 'itself', 'couldn', 'needn', "shan't", 'isn', 'been', 'such', 'shan', "shouldn't", 'aren', 'being', 'were', 
 'did', 'ma', 't', 'having', 'mightn', 've', "isn't", "won't"])


#removing stopwords and
def stopword_filter(words):
    filtered_text = []
    for w in words:
        if w not in stop_words:
            filtered_text.append(w)
    return filtered_text
