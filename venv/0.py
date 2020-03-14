import pandas as pd

def dataFrameFilter(dataFrame, columnName, keywords, fromWhatColumn):
    objectiveIDs = []
    splitted = keywords.split(",")
    print("Выделенные ключевые слова: \n", splitted)

    for word in enumerate(dataFrame[columnName]):
        for i in splitted:
            if (word[1] == i):
                objectiveIDs.append(dataFrame.drop(columns=columnName).iloc[word[0]][fromWhatColumn])
    return objectiveIDs

def filterByKeywords(dataFrame, columnName, keywords):
    clustersmod = dataFrame.copy()
    objectiveIDs = []
    splitted = keywords.split(",")
    print("Найденные ключевые слова: \n", splitted)

    for word in enumerate(clustersmod[columnName]):
        for i in splitted:
           clustersmod.loc[clustersmod[columnName] != i]
    return clustersmod

data = pd.read_csv("Data.csv")
clust_heads = {"id_покупателя":data["IDПользователя"], "товар":data["Товар"], "бренд":data["Бренд"], "тег":data["Теги"], "сумма":data["Сумма"]}
clusters = pd.DataFrame(clust_heads)
print(clusters)

t = dataFrameFilter(clusters, "бренд", "oral-b,oral b,oralb", "id_покупателя")
print(t)
print("Число покупателей, удовлетворяющих критерию: ",len(t))

#t1 = filterByKeywords(clusters,"бренд","oral-b")
#print(t1)




#objectiveIDs = []
#for word in enumerate(clusters["бренд"]):
#    if (word[1] == "oral-b" or word[1] == "oralb" or word[1] == "oral b"):
#        objectiveIDs.append(clusters.drop(columns="бренд").iloc[word[0]]['id_покупателя'])
