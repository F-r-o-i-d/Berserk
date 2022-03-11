def request_parser(text):
    body = ""
    path = ""
    headers = {}
    whiteSuite = 0
    text = text.decode()
    for x in text.split("\r\n"):
        if(len(x)<1):
            body = x
        else:
            try:
                headers[x.split(":")[0]] = x.split(":")[1]
            except:
                path = x.split(" ")[1]
    return path, headers