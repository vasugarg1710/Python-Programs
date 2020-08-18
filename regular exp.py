import re
str = "Our Address Group  +91 1234567890 Technology and Innovation Office (GTIO),Tata Sons. Bombay House, 24,Homi Mody Street 91 1234567893 ,400001 91 2312312412 Mumbai, India."

patt = re.compile(r'\b91 \d{10}')
matches = patt.findall(str)
for match in matches:
    print(match)