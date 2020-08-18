import requests
import pickle
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
r = requests.get(url)
content = r.text

# saving iris.data in a text file
with open("irisds.txt", "w") as f:
    f.write(content)

# creating a list of list
parsed = content.split()
# creating a pickle file
with open("myiris.pkl", "wb") as f:
    pickle.dump(parsed, f)

# reading from a pickle file
with open("myiris.pkl", "rb") as f:
    data = pickle.load(f)


print(data[0])

