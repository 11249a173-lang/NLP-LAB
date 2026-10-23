NP = ["mary","student"]
VP = ["eats","studies"]
print("oredicted sentences:\n")
for s in NP:
    for v in VP:
        for o in NP:
            print(s,v,o)