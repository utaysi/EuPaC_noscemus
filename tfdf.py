import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load your CSV file
# df = pd.read_csv("your_file.csv")

# Sample example data
data=pd.read_csv('/content/res_df.csv')
# Example DataFrame (replace this with your actual data)

df = pd.DataFrame(data)
latin_stopwords = {
    'et', 'in', 'de', 'non', 'cum', 'ad', 'per', 'ex', 'pro', 'ab',
    'si', 'aut', 'sed', 'ut', 'quam', 'nam', 'nec', 'quoque', 'quod',
    'enim', 'vel', 'ac', 'atque', 'ne', 'dum', 'nunc', 'tamen'
}

def get_top_keywords(df, label_col, n=10):
    # Filter titles where label_col is True
    titles = df[df[label_col]]["Full title"].dropna().values
    
    # Vectorize with TF-IDF
    vectorizer = TfidfVectorizer(stop_words=list(latin_stopwords))
    tfidf_matrix = vectorizer.fit_transform(titles)
    
    # Sum scores and extract keywords
    scores = np.asarray(tfidf_matrix.sum(axis=0)).flatten()
    features = vectorizer.get_feature_names_out()
    word_scores = sorted(zip(features, scores), key=lambda x: x[1], reverse=True)
    
    return word_scores[:n]

# Get top keywords
bio_keywords = get_top_keywords(df, "Biology", n=10)
med_keywords = get_top_keywords(df, "Medicine", n=10)

# Print results
print("🔬 Top Biology Keywords:")
for word, score in bio_keywords:
    print(f"{word}: {score:.4f}")

print("\n💊 Top Medicine Keywords:")
for word, score in med_keywords:
    print(f"{word}: {score:.4f}")
