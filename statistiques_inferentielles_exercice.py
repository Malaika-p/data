homme = 399284
femme = 381883
total = homme + femme  # on calcul le nombre total de naissances
print('Naissances taille de l\'échantillon : ', total)

p_estim_h = homme/total # on calcul la proportion des naissances hommes
p_estim_f = femme/total # on calcul la proportion des naissances femmes
print('Proportion des naissances hommes : ', p_estim_h)
print('Proportion des naissances femmes : ', p_estim_f)

import statsmodels.api as sm

import statsmodels.stats.api as smsp

p_value = smsp.binom_test(homme,total, prop=0.5, alternative='larger') # on calcul la P-valeur de H0=0.5 vs H1>0.5
print('Hypothèse d’équiprobabilité des naissances femmes-hommes P-valeur : ', p_value)

h_cent = p_estim_h*100 # on calcul le nombre de naissances hommes pour un échantillon de taille n = 100
print('Naissances hommes échantillon de taille n = 100 : ', int(h_cent))

f_cent = p_estim_f*100 # on calcul le nombre de naissances femmes pour un échantillon de taille n = 100
print('Naissances femmes échantillon de taille n = 100 : ', int(f_cent))


p_value100 = smsp.binom_test(h_cent,100, prop=0.5, alternative='larger') # on calcul la P-valeur de H0=0.5 vs H1>0.5 pour un un échantillon de taille n = 100
print('Hypothèse d’équiprobabilité des naissances femmes-hommes échantillon de taille n = 100 P-valeur : ', p_value100)


h_mille = p_estim_h*1000 # on calcul le nombre de naissances hommes pour un échantillon de taille n = 1000
print('Naissances hommes échantillon de taille n = 1000 : ', int(h_mille))

f_mille = p_estim_f*1000 # on calcul le nombre de naissances femmes pour un échantillon de taille n = 1000
print('Naissances femmes échantillon de taille n = 1000 : ', int(f_mille))


p_value1000 = smsp.binom_test(h_mille,1000, prop=0.5, alternative='larger') # on calcul la P-valeur de H0=0.5 vs H1>0.5 pour un un échantillon de taille n = 1000
print('Hypothèse d’équiprobabilité des naissances femmes-hommes échantillon de taille n = 1000 P-valeur : ', p_value1000)

h_dmille = p_estim_h*10000 # on calcul le nombre de naissances hommes pour un échantillon de taille n = 10 000
print('Naissances hommes échantillon de taille n = 10 000 : ', int(h_dmille))


f_dmille = p_estim_f*10000 # on calcul le nombre de naissances femmes pour un échantillon de taille n = 10 000
print('Naissances femmes échantillon de taille n = 10 000 : ', int(f_dmille))

p_value10000 = smsp.binom_test(h_dmille,10000, prop=0.5, alternative='larger') # on calcul la P-valeur de H0=0.5 vs H1>0.5 pour un un échantillon de taille n = 10 000
print('Hypothèse d’équiprobabilité des naissances femmes-hommes échantillon de taille n = 10 000 P-valeur : ', p_value10000)