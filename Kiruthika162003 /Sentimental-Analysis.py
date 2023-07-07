import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download necessary NLTK resources
nltk.download('vader_lexicon')

# Create an instance of the sentiment intensity analyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis on a given text
def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment

# Example usage
text = "I really enjoyed the movie. It was fantastic!"
sentiment = analyze_sentiment(text)
print(sentiment)
