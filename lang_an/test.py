import json
import random

with open("words.json") as file:
    data = json.load(file)

    def next_word(word):
        nex = ""
        val = 0
        for e in list(data[word]["after"].keys()):
            if int(data[word]["after"][e]) > val and random.randint(0, 2) == 0:
                nex = e
                val = int(data[word]["after"][e])
        if nex == "":
            nex = random.choice(list(data[word]["after"].keys()))
        return nex


st = ("Justus")
wort = st.replace(" ", "").lower()
for t in range(1000):
    wort = next_word(wort)
    st += f" {wort} "
print(st)