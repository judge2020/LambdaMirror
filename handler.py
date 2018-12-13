import os
import subprocess
import shutil

token = os.environ["github_token"]
source = os.environ["source_repo"]
target = os.environ["target_repo"]

source = "https://" + token + "@github.com/" + source
target = "https://" + token + "@github.com/" + target

folder = "mirror"


def hello(event, context):
    os.chdir("/tmp")
    print(subprocess.getoutput("git --version"))
    if os.path.exists(folder):
        os.chdir(folder)
        print()
        a = subprocess.getoutput('git fetch -p origin')
        b = subprocess.getoutput('git push --mirror')
        return ("Cached run: \n---\n" + str(a) + "\n---\n" + str(b)).replace(token, '')
    os.mkdir(folder)
    a = subprocess.getoutput('git clone --mirror ' + source + " " + folder)
    os.chdir(folder)
    b = subprocess.getoutput('git remote set-url --push origin ' + target)
    c = subprocess.getoutput('git push --mirror')
    return ("Non-Cached run: " + str(a) + "\n---\n" + str(b) + "\n---\n" + str(c)).replace(token, '')
