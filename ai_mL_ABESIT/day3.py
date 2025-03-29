from sklearn.datasets import fetch_20newsgroups

#news
news_data = fetch_20newsgroups(subset='all' ,categories= ['alt.atheism', 'sci.space'])

#print(news_data.data[0])
#print(news_data.data[1])

import re
import string
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
print(stop_words,"\n")




##
def clean_txt(text):
    text = text.lower()  # convert to lower case
    text = re.sub(r'\w*\d\w*', '', text)  # remove numbers
    text = re.sub(r'\b\w{1,2}\b', '', text)
    text = re.sub(r'\b\w{1,2}\b', '', text)
    #remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # remove stopwords
    text = ' '.join([word for word in text.split() if word not in stop_words and word.isalpha()])
    return text

# Apply cleaning 
news_data_cleaned  = [clean_txt(doc) for doc in news_data.data]
print(news_data_cleaned)