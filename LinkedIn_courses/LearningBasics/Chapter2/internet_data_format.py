# # working with internet data formats
# import urllib.request
# import json

# def main():
#     weburl = urllib.request.urlopen("http://www.google.com")
#     print("result code:", weburl.getcode())

#     data = weburl.read()
#     print(data)


# if __name__ == '__main__':
#     main()

# working with JSON data

# def printResults(data):
#     theJSON = json.loads(data)

#     if "title" in theJSON["metadata"]:
#         print(theJSON["metadata"]["title"])

#     count = theJSON["metadata"]["count"]
#     print(count, "events recorded")

#     for i in theJSON["features"]:
#         print(i["properties"]["place"])
#     print("------------------------\n")

#     for i in theJSON["features"]:
#         if i["properties"]["mag"] >= 4.0:
#             print(i["properties"]["place"])
#     print("------------------------\n")

#     print("\nEvents that ere felt:")
#     for i in theJSON["features"]:
#         feltReports = i["properties"]["felt"]
#         if feltReports != None:
#             if feltReports > 0:
#                 print(i["properties"]["felt"], feltReports, "times")


# def main():
#     urlData = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php"

#     weburl = urllib.request.urlopen(urlData)
#     print("result code:" + str(weburl.getcode()))
#     if (weburl.getcode() == 200):
#         data = weburl.read()
#         printResults(data)
#     else:
#         print("Received an error from the server, cannot print results",
#               weburl.getcode())


# if __name__ == '__main__':
#     main()

# working with HTML
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        pass

    def handle_starttag(self, tag, attrs):
        pass

    def handle_data(self, data):
        pass


def main():
    parser = MyHTMLParser()

    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read()
        parser.feed(contents)


if __name__ == '__main__':
    main()
