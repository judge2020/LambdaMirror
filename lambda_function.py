import os
import sys, urllib.request, tarfile, subprocess


def setupgit():
    os.chdir('/tmp')
    urllib.request.urlretrieve('https://raw.githubusercontent.com/judge2020/LambdaMirror/master/git-2.4.3.tar', 'git.tar')
    tar = tarfile.open("git.tar")
    tar.extractall()
    tar.close()
    # return [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(".")) for f in fn]
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
    os.mkdir('ClashBotV2')
    os.system('./git clone --bare https://github.com/xseano/ClashBotV2 ClashBotV2')
    os.chdir('ClashBotV2')
    os.system('./../git remote add mirrorto https://TOKEN@github.com/CorporateClash/ClashBotV2.git')
    os.system('./../git push -f --mirror mirroto')
    return os.listdir('.')
