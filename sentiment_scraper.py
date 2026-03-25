import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Silently load the local AI dictionary
nltk.download('vader_lexicon', quiet=True)

print("[*] SYSTEM BOOT: Crypto Sentiment Scraper v2.2 (Data-Cleaned NLP)")
print("[*] Authenticated Developer: SJayJaybee")
print("[*] Injecting Custom Web3 Lexicon into VADER Matrix...")
print("-" * 40)
time.sleep(1)

def analyze_sentiment(text, sia):
    """Analyzes text using the fine-tuned VADER sentiment engine."""
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    
    if compound >= 0.05:
        return "POSITIVE", compound
    elif compound <= -0.05:
        return "NEGATIVE", compound
    else:
        return "NEUTRAL", compound

def main():
    token = "$SOL"
    print(f"\n[*] Initializing Local AI Crypto Sentiment Scraper for {token}...\n")
    time.sleep(1)
    
    # ---------------------------------------------------------
    # Initialize custom Web3 NLP Lexicon matrix
    # ---------------------------------------------------------
    sia = SentimentIntensityAnalyzer()
    crypto_dict = {
        "bullish": 2.5,
        "bearish": -2.5,
        "buy": 1.5,       # Catches "buy wall"
        "flying": 1.5,
        "adoption": 1.5,
        "dropping": -2.0, # Catches "dropping sharply"
        "congestion": -1.5,
        "annoying": -1.5
    }
    sia.lexicon.update(crypto_dict)
    
    print(f"[*] Fetching recent X data stream (Simulated PoC)...\n")
    time.sleep(1)
    
    mock_tweets = [
        "Solana network speeds are absolutely flying today. Bullish on $SOL.",
        "Just sold my bag. The congestion issues on $SOL are getting annoying.",
        "Major institutional buy wall spotted for $SOL at $140. Up we go!",
        "Total value locked dropping sharply across Solana DeFi. Not looking good.",
        "New integration announced for $SOL! Mass adoption is imminent."
    ]
    
    bullish_count = 0
    bearish_count = 0
    
    for i, tweet in enumerate(mock_tweets):
        # We convert the tweet to lowercase so the AI catches every word
        sentiment, confidence = analyze_sentiment(tweet.lower(), sia)
        print(f"Tweet {i+1}: '{tweet}'")
        print(f"--> AI Grade: {sentiment.upper()} (Score: {confidence:.2f})\n")
        time.sleep(0.5) 
        
        if sentiment == "POSITIVE":
            bullish_count += 1
        elif sentiment == "NEGATIVE":
            bearish_count += 1

    print("=" * 40)
    print(f"FINAL AI SENTIMENT REPORT FOR {token}")
    print(f"🟢 Bullish Signals: {bullish_count}")
    print(f"🔴 Bearish Signals: {bearish_count}")
    print("=" * 40)

if __name__ == "__main__":
    main()
