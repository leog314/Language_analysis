import string
import json


def to_num():
    with open("words.json") as f:
        data = json.load(f)
        for word in data.keys():
            data[word]["num"] = list(data.keys()).index(word)

    with open("words.json", "w") as fu:
        fu.write(json.dumps(data, indent=4))
    return True


class txt:
    def __init__(self, text):
        self.txt = text
        self.wl = None
        self.iwl = None

    def analysis(self):
        wl = self.txt.replace("\n", " ").split(" ")
        n_str = ""
        n_wl = []
        for word in wl:
            for letter in word:
                if letter not in string.ascii_letters and letter not in string.digits:
                    pass
                else:
                    n_str += letter
            if not n_str == '':
                n_wl.append(n_str)
            else:
                pass
            n_str = ""
        self.wl = n_wl
        return n_wl

    def app_json(self):
        self.analysis()
        bef = ""
        c = 1
        c1 = 1
        c2 = 1
        ind = 0

        with open("words.json", "r") as f:
            data = json.load(f)
            for w in self.wl:
                if ind != len(self.wl)-1:
                    aft = self.wl[ind + 1]
                else:
                    aft = "."
                if w in data.keys():
                    c = int(data[w]["count"])
                    c += 1
                    if "after" in data[w].keys():
                        if aft in data[w]["after"].keys():
                            c2 = int(data[w]["after"][aft])
                            c2 += 1
                            data[w]["after"][aft] = c2
                        else:
                            data[w]["after"][aft] = c2
                        dic3 = data[w]["after"]

                    else:
                        dic3 = {aft: c2}

                    if "before" in data[w].keys():
                        if bef in data[w]["before"].keys():
                            c1 = int(data[w]["before"][bef])
                            c1 += 1
                            data[w]["before"][bef] = c1
                        else:
                            data[w]["before"][bef] = c1
                        dic2 = data[w]["before"]

                    else:
                        dic2 = {bef: c1}
                else:
                    dic2 = {bef: c1}
                    dic3 = {aft: c2}

                dic = {"count": c,
                       "before": dic2,
                       "after": dic3}
                data[w] = dic
                bef = w
                c = 1
                c1 = 1
                c2 = 1
                ind += 1

        with open("words.json", "w") as fu:
            fu.write(json.dumps(data, indent=4))

        return True

    def transl(self):
        self.analysis()
        to_num()
        n_str = ""
        with open("words.json") as f:
            data = json.load(f)
            for word in self.wl:
                n_str += f"{data[word]['num']} "
        self.iwl = n_str
        return self.iwl






