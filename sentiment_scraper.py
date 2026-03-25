import time
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Silently load the local AI dictionary
nltk.download('vader_lexicon', quiet=True)

print("[*] SYSTEM BOOT: Crypto Sentiment Scraper v2.4 (Data-Cleaned NLP)")
print("[*] Authenticated Developer: SJAYJAYBEE")
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
    token = "$ETH"
    print(f"\n[*] Initializing Local AI Crypto Sentiment Scraper for {token}...\n")
    time.sleep(1)
    
    # ---------------------------------------------------------
    # Initialize custom Web3 NLP Lexicon matrix
    # ---------------------------------------------------------
    sia = SentimentIntensityAnalyzer()
    crypto_dict = {
        "bullish": 2.5,
        "bearish": -2.5,
        "pump": 1.5,      # Catches "pump will be legendary"
        "gem": 1.5,       # Catches "absolute gem"
        "accumulation": 1.5,
        "dumping": -2.0,  # Catches "dumping soon"
        "rekt": -2.0,     # Catches "got completely rekt"
        "gas": -1.5       # Negative context for high fees
    }
    sia.lexicon.update(crypto_dict)
    
    print(f"[*] Fetching recent X data stream (Simulated PoC)...\n")
    time.sleep(1)
    
    # Updated dataset to reflect Ethereum ecosystem sentiment
    mock_tweets = [
        "ETH gas fees are finally dropping. Mass adoption incoming. Bullish on $ETH.",
        "Whale alert: Massive sell wall spotted for $ETH. Looks like we are dumping soon.",
        "Just bought the dip! $ETH is an absolute gem at these levels.",
        "Got completely rekt by the slippage on that last trade. Ethereum layer 1 is still too slow.",
        "Institutional money is quietly in accumulation mode for $ETH. The next pump will be legendary."
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
