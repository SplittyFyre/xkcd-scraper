import json
import os, sys
import urllib.request as ul

def pullcomic(jsonurl):

    jsondat = ul.urlopen(jsonurl)
    js = json.loads(jsondat.read().decode())

    targetfile = "xkcd" + str(js.get("num")) + "_" + js.get("title").replace(' ', '_') + ".png"

    print("xkcd #", js.get("num"))
    print(js.get("title"))
    print(js.get("alt"))
    print()

    ul.urlretrieve(js.get("img"), os.getcwd() + '/' + targetfile)



if len(sys.argv) > 1:
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        if str.isdigit(arg):
            if arg == "404":
                print("Error 404, file not found")
                print("- Love, Gen. Spaz")
            elif arg == "1608":
                print("xkcd #1608 is a hoverboard game")
                print("play it at  https://xkcd.com/1608/")
            else:
                url = "https://xkcd.com/" + arg + "/info.0.json"
                pullcomic(url)
        else:
            print("'{0}' is not an integer".format(arg))

        i += 1

else:
    pullcomic("https://xkcd.com/info.0.json")

