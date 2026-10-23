import re
email="vyshnavi@gmail.com"
print("Valid" if re.match(r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$",email)
else "Invalid")