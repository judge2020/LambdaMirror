import os
import sys, urllib.request, tarfile, subprocess

#NOTE: SSH is not supported at this time, I don't want to go down that can of worms
# repo format: myOrgOrUser/repo
# eg "judge2020/LambdaMirror" will point to https://github.com/judge2020/LambdaMirror

token = os.environ["GH_TOKEN"]
source = os.environ["SOURCE_REPO"]
target = os.environ["TARGET_REPO"]

source = "https://" + token + "@github.com/" + source
target = "https://" + token + "@github.com/" + target


def setupgit():
    os.chdir('/tmp')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/judge2020/LambdaMirror/master/git-2.4.3.tar', 'git.tar')
    tar = tarfile.open("git.tar")
    tar.extractall()
    tar.close()
    GIT_TEMPLATE = os.path.join(os.getcwd(), 'usr/share/git-core/templates')
    GIT_EXEC = os.path.join(os.getcwd(), 'usr/libexec/git-core')
    GIT_LIB = os.path.join(os.getcwd(), 'usr/lib64')
    os.environ["GIT_TEMPLATE_DIR"] = GIT_TEMPLATE
    os.environ["GIT_EXEC_PATH"] = GIT_EXEC
    os.environ["LD_LIBRARY_PATH"] = GIT_LIB



def lambda_handler(event, context):
    setupgit()
    sys.path.append('/tmp/usr/bin')
    os.chdir('/tmp/usr/bin')
    os.mkdir('mirror')
    a = os.system('./git clone --mirror ' + source + " mirror")
    os.chdir('mirror')
    b = os.system('./../git remote set-url --push origin ' + target)
    c = os.system('./../git push --mirror')
    return str(a) + "|" + str(b) + "|" + str(c)
