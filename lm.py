import torch 
import torch.nn.functional as F
import json
with open('notebooks/itos.json', 'r') as file:
    itos = json.load(file)
itos = {int(k): v for k, v in itos.items()}
weights=torch.load('notebooks/weights.pt')
def generate_next_character():
    out = []
    ix = 0
    while True:
        xenc = F.one_hot(torch.tensor([ix]), num_classes=27).float()
        logits = xenc @ weights # predict log-counts
        counts = logits.exp() # counts, equivalent to N
        p = counts / counts.sum(1, keepdims=True) # probabilities for next character
        ix = torch.multinomial(p, num_samples=1, replacement=True).item()
        out.append(itos[ix])
        if ix == 0:
            break
    ft=''.join(out)
    return ft[:-1]