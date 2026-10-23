subjects = ["The student", "The professor", "The principal"]
verbs = ["attends", "teaches", "visits"]
objects = ["the class", "the laboratory", "the library"]

for s in subjects:
    for v in verbs:
        for o in objects:
            print(s, v, o)