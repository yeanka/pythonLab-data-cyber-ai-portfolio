from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
ROOT=Path(__file__).resolve().parents[2]
DATA=ROOT/"data-science"/"03-customer-churn"/"churn.csv"
def main():
    df=pd.read_csv(DATA); X=df.drop(columns=["customer_id","churned"]); y=df.churned
    num=["tenure_months","monthly_charge","support_contacts"]; cat=["contract_type"]
    prep=ColumnTransformer([("num",Pipeline([("impute",SimpleImputer(strategy="median")),("scale",StandardScaler())]),num),
                            ("cat",Pipeline([("impute",SimpleImputer(strategy="most_frequent")),("onehot",OneHotEncoder(handle_unknown="ignore"))]),cat)])
    model=Pipeline([("prep",prep),("clf",LogisticRegression(max_iter=1000))])
    Xtr,Xte,ytr,yte=train_test_split(X,y,test_size=.25,random_state=42,stratify=y)
    model.fit(Xtr,ytr); pred=model.predict(Xte); prob=model.predict_proba(Xte)[:,1]
    print(classification_report(yte,pred,zero_division=0)); print("Confusion matrix:\n",confusion_matrix(yte,pred))
    print("ROC-AUC:",round(roc_auc_score(yte,prob),3))
    names=model.named_steps["prep"].get_feature_names_out()
    coefs=model.named_steps["clf"].coef_[0]
    ranking=sorted(zip(names,coefs),key=lambda x:abs(x[1]),reverse=True)
    print("\nLargest absolute logistic coefficients (not causal explanations):")
    for name,coef in ranking[:10]: print(f"{name}: {coef:.3f}")
if __name__=="__main__": main()
