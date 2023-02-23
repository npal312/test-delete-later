import requests
import json
import my_brand

def getData(id, repo):
    print("I did it: " + id, repo)
    
    pass


def getID():
    id = input("Provide the GitHub ID: ")
    if id == "":
        print("Invalid input: Cannot have GitHub ID be empty")
        exit()

    if len(id.split(" ")) > 1:
        print("Invalid input: Cannot have multiple words in a GitHub ID")
        exit()
    getRepoList(id)


def getRepoList(id):
    url = "https://api.github.com/users/" + id + "/repos"
    r = requests.get(url)
    print(r.text)
    repo = input("Provide the GitHub Repository you want to see the number of commits from: ")
    if repo == "":
        print("Invalid input: Cannot have GitHub Repository name be empty")
        exit()

    getData(id, repo)
    
getID()