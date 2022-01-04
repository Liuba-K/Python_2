import re

RE_GET_PARSER = re.compile(r'(?P<remote_addr>(\d+\.\d+\.\d+\.\d+)).*\[(?P<request_datetime>(.*))\] \"(?P<request_type>(\w+)) '
                           r'(?P<requested_resourse>(/\w+/\w+)).*\" (?P<response_code>(\d+)) (?P<response_size>(\d+))')

with open("pars_logs.txt", "w", encoding="utf-8") as p:
    with open("nginx_logs.txt", "r", encoding="utf-8") as f:
        for line in f:
            print(*map(lambda x: x.groupdict().values(), RE_GET_PARSER.finditer(line)), file=p)


#url = '54.173.226.7 - - [17/May/2015:15:05:00 +0000] "GET /downloads/product_2 HTTP/1.1" 404 336 "-" "Debian APT-HTTP/1.3 (1.0.1ubuntu2)'

#remote_addr= (\d+\.\d+\.\d+\.\d+)# есть повтор
#request_datetime= (?<=[&[])(.*)(?=&*])
#request_type=(?<=[&\"])(.*)(?=&* /)
#requested_resourse= (/\b\w{9}/\w+\b)
#response_code or size = \s\d{3}
#check = re.compile(r'^(\b.+\b).*\[(.+)].*\"([A-Z]+) +(/.+?)\s.*?\" (\d+) (\d+) .*$|^$')


