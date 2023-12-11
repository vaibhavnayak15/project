import nltk
from nltk.stem import WordNetLemmatizer


def lemmatize(words, tagged):
        # applying lemmatizing nlp process to words
        lr = WordNetLemmatizer()
        filtered_text = []
        for w,p in zip(words,tagged):
            if p[1]=='VBG' or p[1]=='VBD' or p[1]=='VBZ' or p[1]=='VBN' or p[1]=='NN':
                filtered_text.append(lr.lemmatize(w,pos='v'))
            elif p[1]=='JJ' or p[1]=='JJR' or p[1]=='JJS'or p[1]=='RBR' or p[1]=='RBS':
                filtered_text.append(lr.lemmatize(w,pos='a'))

            else:
                filtered_text.append(lr.lemmatize(w))
        return filtered_text