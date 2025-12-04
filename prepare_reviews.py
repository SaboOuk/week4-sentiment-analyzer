import pandas as pd
import random


def create_review_dataset():
    """
    Create sample product reviews for training.
    Real applications use thousands of reviews!
    """

    reviews = [
        # Positive reviews (sentiment = 1)
        {"text": "This product is amazing! Best purchase ever!", "sentiment": 1},
        {"text": "Excellent quality and fast shipping. Very happy!", "sentiment": 1},
        {"text": "Love it! Works perfectly and looks great.", "sentiment": 1},
        {"text": "Exceeded my expectations. Highly recommend!", "sentiment": 1},
        {"text": "Five stars! Fantastic product and great price.", "sentiment": 1},
        {"text": "So glad I bought this. Life changing!", "sentiment": 1},
        {"text": "Perfect! Exactly what I needed. Thank you!", "sentiment": 1},
        {"text": "Outstanding quality. Will buy again for sure.", "sentiment": 1},

        # Negative reviews (sentiment = 0)
        {"text": "Terrible product. Complete waste of money.", "sentiment": 0},
        {"text": "Broke after one day. Very disappointed.", "sentiment": 0},
        {"text": "Horrible quality. Returning immediately.", "sentiment": 0},
        {"text": "Does not work as advertised. Avoid!", "sentiment": 0},
        {"text": "Worst purchase ever. Total garbage.", "sentiment": 0},
        {"text": "Cheap and poorly made. Not worth it.", "sentiment": 0},
        {"text": "Completely useless. I want my money back.", "sentiment": 0},
        {"text": "Awful experience. Customer service was rude too.", "sentiment": 0},
        {"text": "Defective product. Very frustrating.", "sentiment": 0},
        {"text": "Don't buy this. You'll regret it.", "sentiment": 0},

        # Mixed/Neutral reviews (for complexity)
        {"text": "It's okay. Not great but not terrible either.", "sentiment": 1},
        {"text": "Product works but shipping took forever.", "sentiment": 0},
        {"text": "Good product but overpriced for what you get.", "sentiment": 1},
        {"text": "Has potential but needs improvement.", "sentiment": 0},
    ]

    # (Optional) shuffle so positives/negatives are mixed
    random.shuffle(reviews)

    df = pd.DataFrame(reviews)
    return df


if __name__ == "__main__":
    data = create_review_dataset()
    # Make sure the data folder exists
    import os
    os.makedirs("data", exist_ok=True)

    try:
        data.to_csv("data/training_reviews.csv", index=False)
        print(f"Created {len(data)} sample reviews")
    except OSError as e:
        print("Warning: failed to write 'data/training_reviews.csv':", e)
        # Try a fallback filename so the script can continue when the target
        # file is locked or otherwise unavailable (this helps progress during
        # development). If the fallback also fails, re-raise the exception.
        fallback = "data/training_reviews_fallback.csv"
        try:
            data.to_csv(fallback, index=False)
            print(f"Created fallback file: {fallback} ({len(data)} sample reviews)")
        except Exception as e2:
            print("Failed to write fallback file:", e2)
            raise
