from django.shortcuts import render
from xml.dom import minidom 
from pymongo import MongoClient

import json
import os

# Variable
conn = None
# Create your views here.
def index(request):
    
    # connectionDB()

    # for collection in conn['aem-dialog'].properties.find({}):
    #     print (json.dump(collection), "\n")
    file_list = getFilesList()
    print (file_list)
    return render(request, 'dialog.html', {'file_list' : file_list})

def getFilesList():
    file_list = {}
    for root, dirs, files in os.walk("E:\Codecs\AEM Edit Dialog\AEM_edit-dialog", topdown = False):
        for name in files:
            if ".xml" in name:
                f = open(os.path.join(root, name), "r")
                if "cq:Component" in f.read():
                        file_list[root.split("\\")[-1]] = root
                f.close()

    return file_list

def connectionDB():
    global conn
    server = "localhost"
    port = 27017
    conn = MongoClient(server, port)
