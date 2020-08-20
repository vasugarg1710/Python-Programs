import re
str = """St. Teresa School
Shakti Khand-II,
Indirapuram Ghaziabad -201010
(U.P) - INDIA

Mobile : + 91- 8826320085, 8826000216

Email Id: stteresaschool_indirapuram@gmail.com"""

patt = re.compile(r"\w+@\S+")
matches = patt.findall(str)
for match in matches:
    print(match)