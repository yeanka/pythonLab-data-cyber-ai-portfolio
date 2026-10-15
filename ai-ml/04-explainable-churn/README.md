# Explainable Customer Churn Baseline
Fits a logistic-regression pipeline and reports model metrics plus coefficients after preprocessing.
## Run
`python explain.py`
## Caution
Uses the synthetic churn dataset from `data-science/03-customer-churn/churn.csv`. Coefficients are associations in this generated dataset, not causal explanations. Explainability is not proof that a prediction is correct.
