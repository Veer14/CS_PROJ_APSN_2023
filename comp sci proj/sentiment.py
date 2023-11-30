import nltk 
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_analysis(text):
    x = "temp"
    sent = SentimentIntensityAnalyzer()
    sent_score = sent.polarity_scores(text)["compound"]
    if sent_score >= 0.05:
        x = "p"
    elif sent_score <= -0.16:
        x = "n"
    else:
        x = "r"
    return x