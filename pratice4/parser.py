import urllib.request

from bs4 import BeautifulSoup

def main():
##
#
    f = open('parser.txt', 'w')
    page = urllib.request.urlopen("https://in.mail.yahoo.com/").read()
#class beautifulsoup
    html = BeautifulSoup(page, "html.parser")

    f.write(str(html.title.string))
#
#the entire texts of webpage.
    f.write(str(html.get_text()))
# d
# d
# d
# body
# html
# [document]
    for link in html.find_all(True):
# ' for '
        #link name
        f.write(str(link.name))
        #header
        f.write(str(html.find_all('script')))
        f.write(str(html.prettify()))
        f.write(str(html.find_all(["li", "ul"])))

if __name__== "__main__":
    main()

