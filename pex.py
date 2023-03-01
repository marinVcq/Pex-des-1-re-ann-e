# -------------------------------------------------------------------------------------

# EXERCICE
# A partir de cette variable zen_of_python eccrivez un script permettant de calculer:
# - le nombre d'occurences de "better" dans les chaines de caractere de la liste.
# - Le nombre d'occurence du caractere espace
# - La chaine de caracte la plus grande
# - La taille moyenne des éléments de la liste

# -------------------------------------------------------------------------------------

import os 

zen_of_python = [
    "The Zen of Python, by Tim Peters",
    "",
    "Beautiful ids better than Ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Althouh practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!"
]

# Cette fonction prend en parametre:
# `list` -> une liste de chaine de caracteres
# `word` -> le mot recherché dans les chaines de caracteres
# Une Boucle For parcours chaques chaine de caractere de la liste.
# Si une ou plusieurs occurence du mot apparait dans une chaine, la variable count est incrémentée du nombre d'occurences via la fonction count().
# Une fois tous les élements de la liste parcourue, la fonction affiche la variable count (nombre total d'occurences du mot)

def find_occurences(word, list):
    count = 0
    for string in list:
        count += string.count(word)
    if word == " ":
        print(f'Le nombre d\'occurence du caractere espace et de {count}\n')
    else:
        print(f'Le nombre d\'occurence du mot {word} et de {count}\n')

# Cette fonction prend en parametre:
# `list` -> une liste de chaine de caracteres
# Cette fonction affiche la chaine de caractere en utilisant la méthode max() (methode de flemmard)

def find_longest1(list):
    print (f'(Methode 1) La chaine de caractere la plus longue est "{max(list, key = len)}"\n')
    
# -- Autre methode -- Une boucle for parcours chaque chaine de caracteres, la variable count stock
# le nombre de caractere, si une chaine est plus longue que la variable count, count prend alors sa valeur et ainsi de suite
# Enfin la fonction affiche la chaine la plus longue

def find_longest2(list):
    count = 0
    longest = ""
    for string in list:
        if len(string) > count:
            count = len(string)
            longest = string
    print (f'(Methode 2) La chaine de caractere la plus longue est "{longest}"\n')

# Cette fonction prend en parametre:
# `list` -> une liste de chaine de caracteres
# Cette fonction affiche la taille moyenne des elements de la chaine

def find_average_size(list):
    total = 0
    average_size = 0
    nb_items = len(list)
    
    for string in list:
        total += len(string)

    average_size = total/nb_items
    
    print (f'La taille moyenne des elements de la liste est de {average_size} arrondi a {round(average_size)}  \n')
    
    
# Question 1 - Mot recherché -> "better" | Liste utilisée -> zen_of_python
find_occurences("better", zen_of_python)

# Question 2 - Nombre d'occurence du caractère " " (espace)
find_occurences(" ", zen_of_python)

# Question 3 - La chaine de caractère la plus grande
find_longest1(zen_of_python)
find_longest2(zen_of_python)

# Question 4 - La taille moyenne des chaines de caractere de la liste
find_average_size(zen_of_python)


    