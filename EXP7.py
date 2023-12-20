import re

with open("samples.txt", 'r') as f:
    data = f.read()
    
    # name_pattern=r'(M(r|s|rs)\.\s[A-Z]\w+)'
    name_pattern=r'(M(r|s|rs)\.\s[A-Za-z]+)'
    names = re.findall(name_pattern,data)
    for name in names:
        print(name[0])

    email_pattern = r'([a-zA-Z0-9.]+@(gmail|yahoo)\.(com|co.in))'
    emails = re.findall(email_pattern, data)
    for email in emails:
        print(email[0])

    number_pattern = r'(\d{8}|\d+[*-]\d+[*-]\d+)'
    numbers = re.findall(number_pattern, data)
    for num in numbers:
        print(num)

    website_pattern = r'((https|http|www)+[a-z:/.]+[.](\w+)[.a-z]+)'
    websites = re.findall(website_pattern, data)
    for web in websites:
        print(web)

