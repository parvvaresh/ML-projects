from sklearn.feature_extraction.text import TfidfVectorizer
import joblib 

def tfidf_embedding(df, column_name):
    texts = [" ".join(tokens) for tokens in df[column_name]]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    joblib.dump(vectorizer, 'tfidf_vectorizer.pkl')
    return tfidf_matrix.toarray()




def transform_new_text(df, column_name):
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    new_texts = [" ".join(tokens) for tokens in df[column_name]]
    new_tfidf_matrix = vectorizer.transform(new_texts)
    return new_tfidf_matrix.toarray()



