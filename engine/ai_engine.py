from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_best_match(old_element, candidates):

    def to_text(el):
        return f"{el['id']} {el['class']} {el['text']} {el['tag']}"

    old_text = to_text(old_element)

    texts = [old_text] + [to_text(c) for c in candidates]

    vectorizer = TfidfVectorizer().fit_transform(texts)
    vectors = vectorizer.toarray()

    scores = cosine_similarity([vectors[0]], vectors[1:])[0]

    best_index = scores.argmax()
    best_score = scores[best_index]

    return candidates[best_index], best_score