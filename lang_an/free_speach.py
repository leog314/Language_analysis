import unicodedata
import string
import main
import torch
import torch.nn as nn

letters = string.ascii_letters + string.digits

def toascii(s):
    return "".join(
        char for char in unicodedata.normalize("NFD", s)
        if unicodedata.category(char) != "Mn"
        and char in letters
    )

def lines(file):
    with open(file, encoding="utf-8") as f:
        t = main.txt(f.read()).analysis()
    return [toascii(l) for l in t]

def charToIndex(char):
    return letters.find(char)

def charToTensor(char):
    ret = torch.zeros(1, len(letters))
    ret[0][charToIndex(char)] = 1
    return ret


def wordToTensor(word):
    ret = torch.zeros(len(word), 1, len(letters))
    for i, char in enumerate(word):
        ret[i][0][charToIndex(char)] = 1
    return ret


wl = lines("4276-0.txt")

class net(nn.Module):
    def __init__(self, inputs, hidden, outputs):
        super(net, self).__init__()
        self.hidden_size = hidden
        self.input_to_output = nn.Linear(inputs + hidden, outputs)
        self.input_to_hidden = nn.Linear(inputs + hidden, hidden)
        self.output_to_output = nn.Linear(hidden + outputs, outputs)
        self.dropout = nn.Dropout(0.1)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, input, hidden):
        combined = torch.cat((input, hidden), dim=1)
        hidden = self.input_to_hidden(combined)
        output = self.input_to_output(combined)
        out_combined = torch.cat((output, hidden), dim=1)
        output = self.output_to_output(out_combined)
        output = self.dropout(output)
        output = self.softmax(output)
        return output, hidden

