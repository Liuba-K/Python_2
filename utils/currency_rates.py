from requests import get, utils

response = get('http://www.cbr.ru/scripts/XML_daily.asp')
encodings = utils.get_encoding_from_headers(response.headers)
content = response.content.decode(encoding=encodings)

def currency_rates(CharCode):
    for valute in content.split("<CharCode>"):
        if CharCode.upper() in valute:
            print(float(valute.replace("/", "").split("<Value>")[-2].replace(",", ".")))
        if "Date=" in valute:
            print(valute.split("Date=")[1].split()[0])

if __name__ == "main":
    print("Hi, I am main")

else:
    print("Hi")

