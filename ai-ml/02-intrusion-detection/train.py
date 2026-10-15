from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
def main():
    df=pd.read_csv(Path(__file__).with_name("traffic.csv"))
    X=df.drop(columns=["label_attack"]); y=df["label_attack"]
    numeric=["duration_seconds","packet_count","bytes_transferred","failed_connections"]
    prep=ColumnTransformer([("num",Pipeline([("impute",SimpleImputer(strategy="median")),("scale",StandardScaler())]),numeric),
                            ("cat",OneHotEncoder(handle_unknown="ignore"),["protocol"])])
    model=Pipeline([("prep",prep),("clf",RandomForestClassifier(n_estimators=150,random_state=42,class_weight="balanced"))])
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    model.fit(Xtr,ytr); pred=model.predict(Xte); prob=model.predict_proba(Xte)[:,1]
    print(classification_report(yte,pred,zero_division=0))
    print("Confusion matrix:\n",confusion_matrix(yte,pred))
    print("ROC-AUC:",round(roc_auc_score(yte,prob),3))
if __name__=="__main__": main()
