from read_data import read_data
from pre_process import pre_process
from sklearn.model_selection import train_test_split
from tf_idf import tfidf_embedding, transform_new_text
from ml_models.parameters import  get_svm
from ml_models.save_best_parameter  import classification_parameter_finder
def train_save_model() -> None:
    
    X, y = read_data()
    print("read data from darabase ...")
    
    X["text"] = X["text"].apply(pre_process)
    print("pre - process text ...")   
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
    print("test and train split ...")
    
    X_train = tfidf_embedding(X_train ,"text")
    X_test = transform_new_text(X_test ,"text")
    print("vectorize text ...")
    

    
    
    model, parameter = get_svm()
    classification_parameter_finder(model, parameter, X_train, y_train, X_test, y_test)
    print("train and saved models ...")
    
train_save_model()