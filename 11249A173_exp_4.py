s="10"
state=0
for c in s:
    if state == 0 and c == "0":
        state = 1
    elif state == 0 and c == "1":
        state = 0
    elif state == 1 and c == "0":
        state = 1
    elif state == 1 and c == "1":
        state = 0
    else:
        state = -1
        break

print("Accepted" if state == 1 else "Rejected")