from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
def main():
    df=pd.read_csv(Path(__file__).with_name("messages.csv"))
    X_train,X_test,y_train,y_test=train_test_split(df["text"],df["label"],test_size=.3,random_state=42,stratify=df["label"])
    model=Pipeline([("tfidf",TfidfVectorizer(ngram_range=(1,2))),("clf",LogisticRegression(max_iter=1000))])
    model.fit(X_train,y_train); pred=model.predict(X_test)
    print(classification_report(y_test,pred,zero_division=0))
    print("Confusion matrix (label order follows sklearn):\n",confusion_matrix(y_test,pred))
    sample="urgent claim your free reward now"
    print(f"Sample prediction for {sample!r}: {model.predict([sample])[0]}")
if __name__=="__main__": main()
