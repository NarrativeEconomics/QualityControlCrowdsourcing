documents = (
"The sky is blue",
"The sun is bright",
)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print(tfidf_matrix.shape)

from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix))

