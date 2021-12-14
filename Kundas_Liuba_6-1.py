
with open("nginx_logs.txt", "r", encoding="utf-8") as f:
    file_logs = ((line.split()[0], line.split()[5].replace('"', ''), line.split()[6]) for line in f)
    for log in file_logs:
        print(log)
