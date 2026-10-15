from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
def main():
    df = pd.read_csv(Path(__file__).with_name("churn.csv"))
    X = df.drop(columns=["customer_id","churned"]); y = df["churned"]
    numeric = ["tenure_months","monthly_charge","support_contacts"]
    categorical = ["contract_type"]
    prep = ColumnTransformer([
        ("num", Pipeline([("impute",SimpleImputer(strategy="median")),("scale",StandardScaler())]), numeric),
        ("cat", Pipeline([("impute",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]), categorical)
    ])
    model = Pipeline([("prep",prep),("classifier",LogisticRegression(max_iter=1000))])
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    model.fit(X_train,y_train); pred=model.predict(X_test); prob=model.predict_proba(X_test)[:,1]
    print(classification_report(y_test,pred,zero_division=0))
    print("Confusion matrix:\n",confusion_matrix(y_test,pred))
    print("ROC-AUC:", round(roc_auc_score(y_test,prob),3))
if __name__ == "__main__": main()
