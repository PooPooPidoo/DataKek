import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

objectiveIDs = []
data = pd.read_csv("Data.csv")
clust_heads = {"brand":data["Бренд"].dropna(), "id_покупателя":data["IDПользователя"]}
clusters = pd.DataFrame(clust_heads).dropna(0,"any")
print(clusters)
clusters.to_csv("byBrands.csv")
for word in enumerate(clusters["brand"]):
        if (word == "oral-b" or word == "oralb" or word == "oral b"):
            objectiveIDs.append(i[0])
            #objectiveIDs.append(clusters.drop(columns="brand").iloc[i[0]]['id_покупателя'])
print(objectiveIDs)

average = len(objectiveIDs)
print (average)