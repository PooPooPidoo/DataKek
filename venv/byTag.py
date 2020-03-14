import pandas as pd
from matplotlib import pyplot as plt

objectiveIDs = []
data = pd.read_csv("Data.csv")
clust_heads = {"тег":data["Теги"].dropna(), "id_покупателя":data["IDПользователя"]}
clusters = pd.DataFrame(clust_heads).dropna(0,"any")
print(clusters)
clusters.to_csv("out.csv")
for i in enumerate(clusters["тег"]):
    words = i[1].split("; ")
    for word in words:
        if (word == "электрическая" or word == "электрическая зубная щетка" or word == "электрической" or word == "oral-b" or word == "oralb" or word == "oral b"):
            objectiveIDs.append(clusters.drop(columns="тег").iloc[i[0]]['id_покупателя'])
print(objectiveIDs)

average = len(objectiveIDs)
print (average)

#print (data)
#print (klusters)
#print (data["Цена"])
#for i in data.