#from requests import get, utils
#file_logs = utils.get_unicode_from_response(get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs"))

with open("nginx_logs.txt", "r", encoding="utf-8") as file_logs:
    for line in file_logs:
        remote_addr_line = file_logs.readline(14).replace(" -", "").replace(" ", "")
        file_logs.read(32)
        line.seek()
        request_type_line = file_logs.read(7).replace(' ] ', '').replace('"', '').replace(']', '').replace('0', '').replace(' ', '')
        requested_resource = file_logs.read(21).replace('H', '').replace(' ', '').replace('T', '')
#        line += remote_addr_line, request_type_line, requested_resource
        print(remote_addr_line, request_type_line, requested_resource)

#open(r"https://gbcdn.mrgcdn.ru/uploads/asset/2729331/attachment/e84f9ad49c706008fba3b58e2a1e5b09.txt", "r", encoding="utf-8")


