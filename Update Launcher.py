import tkinter as tk
from tkinter import filedialog
import os, ast, urllib.request

def URL(url):
    return url.replace(" ", "%20")

def Open_File(File,Write,Text):
    if Write:
        f = open(File,'w')
        f.write(Text)
    else:
        f = open(File)
        text = f.readlines()
        f.close()
        return (text)
    f.close()

def Get_Web_Info(Address, decode=True):
    url = Address
    response = urllib.request.urlopen(url)
    data = response.read()      # a `bytes` object
    if not decode:
        return data
    text = data.decode('utf-8') # a `str`; this step can't be used if data is binary
    return (text)


database = input("Enter URL for database... (No slash on the end) ")

JSONlist = ast.literal_eval(Get_Web_Info(database + "/Files.txt"))
VersionList = ast.literal_eval(Get_Web_Info(database + "/Versions.txt"))
ChangeLogs = ast.literal_eval(Get_Web_Info(database + "/ChangeLogs.txt"))

newVersion = input("Enter a name for the new version... ")
print("Starting file chooser...")
print("Choose a directory and all of it's contents will be uploaded.")
print("Remember: The directory itself won't be uploaded, just it's contents.")
print("Don't forget: Make sure you put the files on the database.")

root = tk.Tk()

root.withdraw()
root.update()
folder = filedialog.askdirectory(title="Choose a directory and all of it's contents will be uploaded.")


fileList = []
files = []
filesScanned = 0
printDelay = 0
Home = os.path.expanduser('~')



print("Generating JSON...")
for i in os.walk(folder):
    for c in i:
        currentPath = i[0].split("/")
        splitFolder = folder.split("/")
        while len(splitFolder) > 0:
            if currentPath[0] == splitFolder[0]:
                del currentPath[0]
                del splitFolder[0]
        currentPath = "/".join(currentPath)
        if (currentPath != ""):
            fileList.append(["Dir", currentPath])
                
        for item in i[2]:
            if item[0] != ".":
                files.append(currentPath + item)
                fileList.append(["File", currentPath + "/" + item])
                filesScanned = filesScanned + 1
                printDelay = printDelay + 1
        if printDelay >= 50:
            print(filesScanned + " files scanned.")
            printDelay = 0
        break



print("Choose an html file for the changelog...")

root = tk.Tk()

root.withdraw()
root.update()
ChangeLogs[newVersion] = (open(filedialog.askopenfilename(title="Choose an html file for the changelog...", filetypes = [("html files","*.html")])).read()).split(" \n")

   

print("Nearly done...")
print("Choose a location for the 3 files...")
print("Choose a location for 'Files.txt', 'Versions.txt' and 'ChangeLogs.txt'...")
root = tk.Tk()
root.attributes("-topmost", True)
root.withdraw()
root.update()
save = filedialog.askdirectory(title="Choose a location for 'Files.txt', 'Versions.txt' and 'ChangeLogs.txt'...")

JSONlist = fileList
VersionList.append(newVersion)


Open_File(save + "/Files.txt",True,str(JSONlist))
Open_File(save + "/Versions.txt",True,str(VersionList))
Open_File(save + "/ChangeLogs.txt",True,str(ChangeLogs))

print("Done!")
print("'Files.txt', 'Versions.txt' and 'ChangeLogs.txt' saved to " + save)

