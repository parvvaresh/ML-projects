from model.pre_process import pre_process
import joblib

def app(text: str) -> None:
    text = pre_process(text)
    
    vectorizer = joblib.load('./model/tfidf_vectorizer.pkl')
    
    new_tfidf_matrix = vectorizer.transform(text)  
    vector = new_tfidf_matrix.toarray()
    
    model = joblib.load('./model/model.pkl')
    print(model.predict(vector))


test_text = "this is a test ..."
app(test_text)