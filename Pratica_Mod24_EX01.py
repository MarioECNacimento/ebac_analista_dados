#!/usr/bin/env python
# coding: utf-8

# ### 1) Cite 5 diferenças entre o Random Forest e o AdaBoost

# 1 - O algoritmo AdaBoost trabalha com stump (árvores com 1 nó e 2 níveis), n RF as àrvores nao tem limite de crescimento;    
# 2 - Os stumps não fazem uma classificação muito precisa, já as RF fazem uma classificação mais apurada;  
# 3 - No AdaBoost alguns stumps têm valores de votação maiores que outros, já na RF todas as árvores tem o mesmo peso de votação;  
# 4 - Ordem de crescimento dos stumps depende do desempenho do stump anterior, nas RF não existe ordem no crescimento das àrvores;  
# 5 - AdaBoost são mais sensiveis ao overfitting quando comparado as RF;

# ### 2) Acesse o link Scikit-learn– adaboost , leia a explicação (traduza se for preciso) e crie um jupyter notebook contendo o exemplo do AdaBoost.

# In[1]:


from sklearn.model_selection import cross_val_score
from sklearn.datasets import load_iris
from sklearn.ensemble import AdaBoostClassifier

X, y = load_iris(return_X_y=True)
clf = AdaBoostClassifier(n_estimators=100, algorithm="SAMME",)
scores = cross_val_score(clf, X, y, cv=5)
scores.mean()


# ### 3) Cite 5 Hyperparametros importantes no AdaBoost.

# n_estimator (número de estimadores);  
# learning_rate (taxa de aprendizado);  
# algorithm (algoritmo que o AdaBoost irá rodar);  
# random_state (seleção de randomização do conjunto de treinamento do algoritmo AdaBoost);  

# ### 4) (Opcional) Utilize o GridSearch para encontrar os melhores hyperparametros para o conjunto de dados do exemplo (load_iris)
# 

# In[3]:


from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import AdaBoostClassifier

X, y = load_iris(return_X_y=True)


model = AdaBoostClassifier()

grid = dict()
grid['n_estimators'] = [10, 50, 100, 500]
grid['learning_rate'] = [0.0001, 0.001, 0.01, 0.1, 1.0]

grid_search = GridSearchCV(estimator=model, param_grid=grid, n_jobs=-1, cv=5, scoring='accuracy')

grid_result = grid_search.fit(X, y)

print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))

means = grid_result.cv_results_['mean_test_score']
stds = grid_result.cv_results_['std_test_score']
params = grid_result.cv_results_['params']
for mean, stdev, param in zip(means, stds, params):
    print("%f (%f) with: %r" % (mean, stdev, param))


# In[ ]:




