from flask import render_template, request
from app import app  # Import the app instance from __init__.py

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    if request.method == 'POST':
        text = request.form['text'].lower()
        
        # Simple sentiment analysis based on keywords
        if any(word in text for word in ['happy', 'good', 'excellent', 'great', 'love', 'wonderful']):
            sentiment = "POSITIVE"
        elif any(word in text for word in ['sad', 'bad', 'terrible', 'awful', 'hate', 'worst']):
            sentiment = "NEGATIVE"
        elif any(word in text for word in ['ok', 'okay', 'fine', 'average', 'neutral']):
            sentiment = "NEUTRAL"
        elif len(text.split()) > 3:  # If text has more than 3 words and contains mixed sentiments
            # Check if text contains both positive and negative words
            has_positive = any(word in text for word in ['good', 'nice', 'like'])
            has_negative = any(word in text for word in ['but', 'however', 'though', 'bad'])
            if has_positive and has_negative:
                sentiment = "MIXED"
            else:
                sentiment = "NEUTRAL"  # Default if no clear sentiment is detected
        else:
            sentiment = "NEUTRAL"  # Default for short or unclear text
    
    return render_template('index.html', sentiment=sentiment)