# imports
from bs4 import BeautifulSoup
import requests
import csv

# this function returns a soup page object
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj


def main():

    fobj = open('https-artikel.csv', 'w')      # open file
    csvw = csv.writer(fobj, delimiter = ';')      # create csv writer, set delimiter to ;

    ghd_ir_url = "https://www.heise.de/thema/https"   

    content = getPage(ghd_ir_url)
    content = content.findAll("div", { "class" : "imgwrap" })
        
    for t in content:
        txt = []
        txt.append(t.img["alt"])
        csvw.writerow(txt)
        #print(t.img["alt"])
        #print(txt)

    fobj.close()                                

# main program
if __name__ == '__main__':
    main()