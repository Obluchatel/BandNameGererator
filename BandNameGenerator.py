import random
import csv
def names():
    with open('names.csv', 'rb') as f:
        reader = csv.reader(f)
        names = tuple(reader)
        names = str(random.choice(names))
        names = str(names).replace('[', '').replace(']', '').replace(' ', '')
        names = names.replace("'", "")
        return names


def adjective():
    with open('adjectives.csv', 'rb') as f:
        reader = csv.reader(f)
        adjective = tuple(reader)
        adjective = str(random.choice(adjective))
        adjective = str(adjective).replace('[', '').replace(']', '').replace(' ', '')
        adjective = adjective.replace("'", "")
        return adjective

def nouns():
    with open('nouns.csv', 'rb') as f:
        reader = csv.reader(f)
        nouns = tuple(reader)
        nouns = str(random.choice(nouns))
        nouns = str(nouns).replace('[', '').replace(']', '').replace(' ', '')
        nouns = nouns.replace("'", "")
        return nouns

def bandname (names, adjective, nouns):
    bandname = str("Your band name - " + names + " and " + adjective + " " + nouns + ".")
    print bandname

    
bandname(names(), adjective(), nouns())





