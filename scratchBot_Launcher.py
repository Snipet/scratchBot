import requests
import json
import time
import scratchCommands

global mostRecentVersion
global myVersion

def update():
    print("Downloading most recent version (" + mostRecentVersion + ")")
    getFile("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/scratchCommands.py", "scratchCommands.py")
    setVersion(mostRecentVersion)
    print("ScratchBot has been downloaded")

def getFile(URL, FILE):
    lines = getFileContents(URL)
    open(FILE, 'w').close()
    f = open(FILE, "a")
    for line in lines:
        f.write(line + "\n")
    f.close()

def getFileContents(URL):
    r = requests.get(URL)
    code = r.text
    code = code.split("\n")
    lines = []
    for line in code:
        lines.append(line.replace("\r", ""))
    return lines

def getVersion():
    f = open("version.json", "r")
    f = json.loads(f.read())
    return f["version"]
  
def setVersion(v):
    j = {
        "version": v,
        "username": "",
        "password": ""
    }
    
    f = open("version.json", "w")
    f.write(json.dumps(j))
    f.close()
    
def main():
    try:
        f = open("version.json")
        f.close()
    except:
        setVersion(0)
        
    mostRecentVersion = getFileContents("https://raw.githubusercontent.com/BonfireScratch/scratchBot/master/version.txt")
    myVersion = getVersion()
    if mostRecentVersion != myVerion:
        update()
        
    while True:
        scratchCommands.scratchCheck("BOT", "REG ACCOUNT", "PASSWORD")
        time.sleep(5)

main()
