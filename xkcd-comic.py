import urllib.request, json
with urllib.request.urlopen("https://xkcd.com/info.0.json") as url:
    data= json.load(url)
    print("Today's comic (%s): %s" % (data["num"],data["safe_title"]))
    print(data["img"]) 
