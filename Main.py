from Configuration import Configuration
import MoveFiles
from pyquery import PyQuery as pq
import requests
import wget
import shutil
from pathlib import Path

def find_first_slash(link_url):
    first_index = link_url.rfind("/")
    if first_index == -1:
        return -1
    return first_index

def find_second_slash(link_url):
    first_index = link_url.rfind("/")
    if first_index == -1:
        return -1
    second_index = link_url.rfind("/",0,first_index)
    return second_index
def clearExistingFilesAndFolders():
    directory = Path.cwd()
    for item in directory.iterdir():
        if item.is_file() and not item.name.endswith("py"):
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)


def getPageUrl(grade):
    return Configuration.base_url+grade

def getDoc(page):
    response = requests.get(page)
    response.encoding = Configuration.encode
    doc = pq(response.text)
    return doc

def downloadFiles(doc):
    pdf_list = doc(Configuration.tag)
    for link in pdf_list:
        link_url = link.attrib["href"]

        link_type = "pdf"
        if (link_url.endswith("mp3")):
            link_type = "mp3"

        link_name = link_url[find_first_slash(link_url)+1:]
        if (link_type == "mp3"):
            link_name = link_url[find_second_slash(link_url)+1:].replace("/","_")

        print("start download {} ---> url:{} name:{}".format(link_type,link_url,link_name))
        
        download_url = ""
        if(link_type == "mp3"):
            download_url = link_url
        elif(link_type == "pdf"):
            download_url = Configuration.host+link_url

        if download_url != "":
            filename = wget.download(download_url)
            shutil.move(filename,link_name)
           

def main():
    clearExistingFilesAndFolders()
    for grade in Configuration.grades:
        page = getPageUrl(grade)
        doc = getDoc(page)
        downloadFiles(doc)
        MoveFiles.move(grade)

if __name__ == "__main__":
    main()
