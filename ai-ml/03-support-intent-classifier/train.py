from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
def main():
    df=pd.read_csv(Path(__file__).with_name("tickets.csv"))
    Xtr,Xte,ytr,yte=train_test_split(df.ticket_text,df.intent,test_size=.25,random_state=42,stratify=df.intent)
    model=Pipeline([("tfidf",TfidfVectorizer(ngram_range=(1,2),stop_words="english")),
                    ("clf",LogisticRegression(max_iter=1500))])
    model.fit(Xtr,ytr)
    print(classification_report(yte,model.predict(Xte),zero_division=0))
    for text in ["I forgot my password","wifi is not connecting","my monitor is broken"]:
        print(text,"->",model.predict([text])[0])
if __name__=="__main__": main()
