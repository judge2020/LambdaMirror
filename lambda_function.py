import os
import sys, urllib.request, tarfile, random

#NOTE: SSH is not supported at this time, I don't want to go down that can of worms
# repo format: myOrgOrUser/repo
# eg "judge2020/LambdaMirror" will point to https://github.com/judge2020/LambdaMirror

token = os.environ["GH_TOKEN"]
source = os.environ["SOURCE_REPO"]
target = os.environ["TARGET_REPO"]

source = "https://" + token + "@github.com/" + source
target = "https://" + token + "@github.com/" + target


def setupgit():
    tar = tarfile.open("git.tar")
    tar.extractall(path="/tmp")
    tar.close()
    os.chdir('/tmp')
    GIT_TEMPLATE = os.path.join(os.getcwd(), 'usr/share/git-core/templates')
    GIT_EXEC = os.path.join(os.getcwd(), 'usr/libexec/git-core')
    GIT_LIB = os.path.join(os.getcwd(), 'usr/lib64')
    os.environ["GIT_TEMPLATE_DIR"] = GIT_TEMPLATE
    os.environ["GIT_EXEC_PATH"] = GIT_EXEC
    os.environ["LD_LIBRARY_PATH"] = GIT_LIB



def lambda_handler(event, context):
    folder = "mirror"
    if not os.path.exists('/tmp/usr/bin/git'):
        os.chdir('/var/task')
        setupgit()
    os.chdir('/tmp/usr/bin')
    if os.path.exists(folder):
        os.chdir(folder)
        a = os.system('./../git fetch -p origin')
        b = os.system('./../git push --mirror')
        return "Cached run: " + str(b) + "|" + str(b)
    os.mkdir(folder)
    a = os.system('./git clone --mirror ' + source + " " + folder)
    os.chdir(folder)
    b = os.system('./../git remote set-url --push origin ' + target)
    c = os.system('./../git push --mirror')
    return "Non-Cached run: " + str(a) + "|" + str(b) + "|" + str(c)
