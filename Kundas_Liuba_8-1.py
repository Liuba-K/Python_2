import re

def email_parse(email_address):

    RE_NAME = re.compile(r"(?:\w+[^@])(?:\w+)", re.IGNORECASE)
    US_D = {"username": RE_NAME.findall(email_address)[0], "domain": RE_NAME.findall(email_address)[1]}

    if not len(RE_NAME.findall(email_address)[1].split(".")) == 2:
        raise ValueError(f"wrong email: {email_address}")
    return US_D

print(email_parse("someon6@geekBrains.ru"))