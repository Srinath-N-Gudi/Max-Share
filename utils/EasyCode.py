def getPath(path):
    if path == "":
        raise Exception("The part are empty")
    path = str(path)
    path = path.split("\'")[1]
    return path
