#
# checkflix.py
# Find which movies in icheckmovies.com lists are on Netflix
# For copyright see LICENSE.md
# Author: Soren Rasmussen github: scrasmussen
#
from urllib.request import urlopen
from bs4 import BeautifulSoup
from tabulate import tabulate

# List name
#  |-get a list from iCheckMovies
#  |-check a movie against allflicks.net


def initListList():
    print("Create listList.txt")
    listList=[]
    # from 1 to 8
    for i in range(1,9):
        ICHECKURL="https://www.icheckmovies.com/lists/?page="+str(i)+"&tags=user:icheckmovies"
        req = urlopen(ICHECKURL);
        soup = BeautifulSoup(req,"lxml")
        titleList = soup.findAll(class_="title")
        for title in titleList[:-1]:
            listList.append(title["href"])

    f = open("listList.txt", 'w')
    for name in listList:
        f.write("%s\n"%name[7:-1])
    f.close()

def readListList():
    listList = []
    f = open("listList.txt")
    listList = f.read().splitlines()
    f.close()
    return listList

def chooseList(listList):
    print("Here are the lists:")
    for i, name in enumerate(listList):
        print(i, name.replace('+',' ').title())
    return int(input("\nWhich playlist would you like to check? "))

def getTitleList(listName):
    ICHECKURL="https://www.icheckmovies.com/lists/"+listName
    req = urlopen(ICHECKURL);
    soup = BeautifulSoup(req,"lxml")
    titles = soup.findAll(class_="optionIcon optionIMDB external")
    titleList = []
    for title in titles:
        name=title["title"]
        titleList.append(name[6:-12])
    return titleList

def printTitleList(listName):
    for count, item in enumerate(listName, 1):
        if (len(item) > 40):
            item = item[0:36] + '...'
        print(item.ljust(40), end=''),
        if (count % 2 == 0):
            print()


print("Start")

# Read name of movie lists from file or generate file from website
readList=1
if readList:
    listList = readListList()
else:
    initListList()

# Choose list
i = chooseList(listList)
# i=59

print('-----------------------------')
print(listList[i])
print('-----------------------------')
titleList = getTitleList(listList[i])

printTitleList(titleList)

# movie = "Jaws"
# SEARCH FOR A SPECIFIC MOVIE
# SEARCHURL="http://www.netflixreleases.com/search/?keyword="+movie
# req = urlopen(SEARCHURL);
# soup = BeautifulSoup(req,"lxml")
# titles = soup.findAll(class_="listitem")
# titleList = []
# for title in titles:
#     movie += ' ('
#     if movie in title.text:
#         print("==",title.text)



# print("Fin")
