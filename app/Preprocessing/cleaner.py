import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
lemmatizer = WordNetLemmatizer()

# Define the cleaner class
class cleaner:
    def __init__(self, text):
        self.text = text
        pass

    def Punctuation_shpichel_cleaning(self, text):
        # Implement text cleaning logic here
        cleaned_text = re.sub(r'[^\w\s]', '', text)
        return cleaned_text

    def Cleaning_unnecessary_characters(self, text):
        # Remove unnecessary_characters
        text_clean = re.sub(r'\s+', ' ', text)
        text_clean = text_clean.strip()
        return text_clean

    def stop_words(self, text):
        # Remove stop words
        stop_words = set(stopwords.words('english'))
        tokens = text.split()
        tokens_clean = [word for word in tokens if word not in stop_words]
        return ' '.join(tokens_clean)

    def lower_case(self, text):
        # Convert to lower case
        return text.lower()

    def lemmatization(self, text):
        # Lemmatization
        tokens = text.split()
        lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(lemmatized_tokens)

text = "   Hello!!! This is a SIMPLE, messy   text with numbers 12345, a URL https://example.com and some stop words like THE, AND, IN. Let's see if it works :)"
a= cleaner(text)
test = a.Punctuation_shpichel_cleaning(a.text)
test = a.Cleaning_unnecessary_characters(test)
test = a.stop_words(test)
test = a.lower_case(test)
test = a.lemmatization(test)
print(test)
