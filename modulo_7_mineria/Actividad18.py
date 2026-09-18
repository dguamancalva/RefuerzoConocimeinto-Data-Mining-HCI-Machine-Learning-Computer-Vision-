import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# 1. Dataset de transacciones
dataset = [
    ['Pan', 'Leche', 'Mantequilla'],
    ['Pan', 'Leche'],
    ['Pan', 'Pañales', 'Cerveza'],
    ['Leche', 'Mantequilla'],
    ['Pan', 'Leche', 'Mantequilla', 'Cerveza'],
    ['Pañales', 'Cerveza']
]

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
print(te_ary)
df = pd.DataFrame(te_ary, columns= te.columns_)
print(df)

frequent_itemsets = apriori(df, min_support= 0.3, use_colnames=True)

rules = association_rules(frequent_itemsets, metric = "confidence", min_threshold= 0.6)

reglas_valiosas= rules[rules['lift'] > 1.0]

print(reglas_valiosas[['antecedents', 'consequents', 'support', 'confidence', 'lift']])