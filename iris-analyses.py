import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Chargement
iris = pd.read_csv("iris_dataset.csv")

# On renomme les colonnes
iris.columns = ["id","sepal_length","sepal_width","petal_length","petal_width","species"]

# On supprime l'identifiant des iris
del iris["id"]

# On supprime les individus contenant au moins une valeur manquante
iris_dna = iris.dropna(axis=0, how='any')
print("iris : {} individus, iris_dna : {} individus".format(len(iris),len(iris_dna)))

iris_setosa = iris_dna[iris_dna["species"] == "setosa"]
iris_virginica = iris_dna[iris_dna["species"] == "virginica"]
iris_versicolor = iris_dna[iris_dna["species"] == "versicolor"]

# Affichage des diagrammes de dispersion
sns.pairplot(iris_dna,hue="species")

plt.show()



plt.plot(iris_dna["petal_width"],iris_dna["petal_length"],'o',alpha=0.5)
plt.xlabel("petal width")
plt.ylabel("petal_length")
plt.show()



import scipy.stats as st
import numpy as np

print("Questions 1 :")

# coefficients de corrélation linéaires de petal_width en fonction de petal_length 

petal_width_fonction_petal_length = st.pearsonr(iris_dna["petal_width"],iris_dna["petal_length"])[0]
print("coefficients de corrélation linéaires de petal_width en fonction de petal_length : ", petal_width_fonction_petal_length)


#coefficients de corrélation linéaires de sepal_width en fonction de petal_width
sepal_width_fonction_petal_width = st.pearsonr(iris_dna["sepal_width"],iris_dna["petal_width"])[0]
print("coefficients de corrélation linéaires de sepal_width en fonction de petal_width : ", sepal_width_fonction_petal_width)


print("Questions 2 :")
print("On observe une forte corrélation linéaire de petal_width en fonction de petal_length, sepal_width en fonction de petal_width ne semble au contraire pas corrélé.")




print("Questions 3 :")
import statsmodels.api as sm
# Y la variable petal_width, sur le dataframe iris_dna 

Y = iris_dna['petal_width']
# X est la variable petal_length sur le dataframe iris_dna 
X = iris_dna[['petal_length']]
X = X.copy() # On modifiera X, on en crée donc une copie
X['intercept'] = 1.
result = sm.OLS(Y, X).fit() # OLS = Ordinary Least Square (Moindres Carrés Ordinaire)
a,b = result.params['petal_length'],result.params['intercept']



plt.plot(iris_dna.petal_length,iris_dna.petal_width, "o")
plt.plot(np.arange(10),[a*x+b for x in np.arange(10)])
plt.xlabel("petal_length")
plt.ylabel("petal_width")
plt.show()
print("cas 1 : a =", a, "et b =", b)



# Y la variable sepal_width sur le dataframe iris_setosa

Y = iris_setosa['sepal_width']
#  X est la variable petal_width sur le dataframe iris_setosa
X = iris_setosa[['petal_width']]
X = X.copy() # On modifiera X, on en crée donc une copie
X['intercept'] = 1.
result = sm.OLS(Y, X).fit() # OLS = Ordinary Least Square (Moindres Carrés Ordinaire)
a,b = result.params['petal_width'],result.params['intercept']


plt.plot(iris_setosa.petal_width,iris_setosa.sepal_width, "o")
plt.plot(np.arange(4),[a*x+b for x in np.arange(4)])
plt.xlabel("petal_width")
plt.ylabel("sepal_width")
plt.show()
print("cas 2 : a =", a, "et b =", b)


# Y la variable sepal_width sur le dataframe iris_virginica

Y = iris_virginica['sepal_width']
#  X est la variable petal_width sur le dataframe iris_virginica
X = iris_virginica[['petal_width']]
X = X.copy() # On modifiera X, on en crée donc une copie
X['intercept'] = 1.
result = sm.OLS(Y, X).fit() # OLS = Ordinary Least Square (Moindres Carrés Ordinaire)
a,b = result.params['petal_width'],result.params['intercept']


plt.plot(iris_virginica.petal_width,iris_virginica.sepal_width, "o")
plt.plot(np.arange(5),[a*x+b for x in np.arange(5)])
plt.xlabel("petal_width")
plt.ylabel("sepal_width")
plt.show()
print("cas 3 : a =", a, "et b =", b)




# Y la variable sepal_width sur le dataframe iris_versicolor

Y = iris_versicolor['sepal_width']
#  X est la variable petal_width sur le dataframe iris_versicolor
X = iris_versicolor[['petal_width']]
X = X.copy() # On modifiera X, on en crée donc une copie
X['intercept'] = 1.
result = sm.OLS(Y, X).fit() # OLS = Ordinary Least Square (Moindres Carrés Ordinaire)
a,b = result.params['petal_width'],result.params['intercept']


plt.plot(iris_versicolor.petal_width,iris_versicolor.sepal_width, "o")
plt.plot(np.arange(5),[a*x+b for x in np.arange(5)])
plt.xlabel("petal_width")
plt.ylabel("sepal_width")
plt.show()
print("cas 4 : a =", a, "et b =", b)




print("Questions 4 :")

coeffs = {
    "cas 1" : {'a': 0.38599421003086454 , 'b': 0.5092683365299998},
    "cas 2" : {'a': 1.7875014940283402 , 'b': 1.4593274917352779},
    "cas 3" : {'a': 0.6992505959712972 , 'b': 1.0377429413261894},
    "cas 4" : {'a': 0.9735704312621847 , 'b': 0.809489372078844},
}
lignes_modifiees = []

for (i,individu) in iris.iterrows(): # pour chaque individu de iris,...
    if pd.isnull(individu["petal_width"]): #... on test si individu["petal_width"] est nul.
        a = coeffs["cas 1"]['a']
        b = coeffs["cas 1"]['b']
        X = individu["petal_length"]
        Y = a*X + b
        iris.loc[i,"petal_width"] = Y # on remplace la valeur manquante par Y
        lignes_modifiees.append(i)
        print("On a complété petal_width par {} a partir de petal_length={}".format(Y,X))
        
    if pd.isnull(individu["sepal_width"]):
        espece = individu["species"]
        X = individu["petal_width"]
        if espece == "setosa":
            a = coeffs["cas 2"]['a']
            b = coeffs["cas 2"]['b']
        
        elif espece == "virginica":
            a = coeffs["cas 3"]['a']
            b = coeffs["cas 3"]['b']    
        
        elif espece == "versicolor":
            a = coeffs["cas 4"]['a']
            b = coeffs["cas 4"]['b']
        Y = a*X + b
        iris.loc[i,"petal_width"] = Y # on remplace la valeur manquante par Y
        lignes_modifiees.append(i)
        print("On a complété sepal_width par {} a partir de l'espece:{} et de petal_width={}".format(Y,espece,X))


