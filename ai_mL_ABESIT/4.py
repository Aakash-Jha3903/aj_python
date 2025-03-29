#STEP-05 STEMMING/LEMMATIZER
# import day3
import nltk
from nltk.stem import PorterStemmer,WordNetLemmatizer 
nltk.download('wordnet')

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = ["running", "studies", "better"]
print("Stemming:", [stemmer.stem(word) for word in words])
print("Lemmatization:", [lemmatizer.lemmatize(word) for word in words])

#lemmatization is better as it keeps words meaningful

#CONVERT TEXT INTO NUMERICAL FEATURES 
#CONVERT TEXT INTO A WORD FREQUENCY MATRIX

# from sklearn.feature_extraction.text import CountVectorizer

# vectorizer = CountVectorizer(max_features=10) #keep top 10 words
# X_bow = vectorizer.fit_transform(news_data_cleaned)

# print(vectorizer.get_feature_names_out())   # Most frequent words