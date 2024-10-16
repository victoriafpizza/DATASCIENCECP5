import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregar dados
df = pd.read_csv('diabetes.csv')

# Calcular a matriz de correlação
correlation_matrix = df.corr()

# Visualizar a matriz de correlação
plt.figure(figsize=(16, 12))  # Aumente o tamanho da figura
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', annot_kws={"size": 10})
plt.xticks(rotation=45, ha='right')  # Rotacione os rótulos do eixo X
plt.yticks(rotation=0)  # Rotacione os rótulos do eixo Y
plt.show()


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Selecione as variáveis com maior correlação
features = df[['BMI', 'Age', 'HighBP']]
target = df['Diabetes_012']

# Divida os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)

# Crie e treine o modelo
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Faça previsões
y_pred = rf.predict(X_test)

from sklearn.metrics
import confusion_matrix, classification_report

# Matriz de confusão
cm = confusion_matrix(y_test, y_pred)
print('Matriz de Confusão:\n', cm)

# Relatório de Classificação
print('Relatório de Classificação:\n', classification_report(y_test, y_pred))

