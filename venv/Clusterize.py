import pandas as pd

data = pd.read_csv("Data.csv")
clust_heads = []
clusters = pd.DataFrame(clust_heads)
print(clusters)

for i in enumerate(data["Теги"]):
    words = str(i[1]).split("; ")
    for word in words:
        for header in clust_heads:
            print(header)
            if (header != word):
                clust_heads.append(word)
            elif (clust_heads == []):
                clust_heads.append(word)
                print("!")
print(clust_heads)

def kek():
    for i in enumerate(data["Теги"]):
        words = str(i[1]).split("; ")
        for word in words:
            for header in clust_heads:
                if (header == word):
                    clusters[header].append(data.iloc[i[0]]['IDПокупателя'])
                elif (header != word):
                    clust_heads.append(header)
                    clusters[header].append(data.iloc[i[0]]['IDПокупателя'])