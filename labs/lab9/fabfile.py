

from fabric.api import *
import time

env.host={'localhost'}

#env.user = 'root'

env.roledefs = {
    'check': ['localhost'],

}

def setup():
    sudo('apt install virtualenv git')
    run('mkdir /opt/basicapp/')

def virtualenv_setup():
    sudo('chown $USER:www-data /opt/basicapp/')
    run('cd /opt/basicapp')
    run('virtualenv venv')
    run('source venv/bin/activate')

def clone_files():
    run('git clone https://github.com/0xcf/decal/')
    run('mv decal/labs/lab9/* /opt/basicapp/')
    run('pip install -r requirements.txt')

def runlab9(): # does not work because it's a persistent process
    run('python lab9.py')

def install_uwsgi():
    sudo("apt install uwsgi uwsgi-plugin-python")

def uwsgi_configs():
    sudo("mv /opt/lab9/lab9.ini /etc/uwsgi/app-available/")
    sudo("ln -s /etc/uwsgi/app-available/lab9.ini /etc/uwsgi/app-enabled/lab9.ini")
    run("touch /opt/lab9/lab9.log")

def uwsgi_restart():
    sudo("systemctl start uwsgi")


def deploy():
    setup()
    virtualenv_setup()
    clone_files()
    #runlab9()
    install_uwsgi()
    uwsgi_configs()
    uwsgi_restart()



def basicapp():
    env.warn_only = True
    #time.sleep(3)
    check1 = run('curl 127.0.0.1:5000')
    #print(check1)
    if "Flask" not in check1:
        print("127.0.0.1:5000 is not up")
    else:
        print("127.0.0.1:5000 is up")
    if "basicapp.py" in run("ps a"):
        print("basicapp.py is in process")
    else:
        print("basicapp.py is not in processes")


def uwsgi():
    check = run('curl 127.0.0.1:8370')
    if "Flask" not in check:
        print("Server at 127.0.0.1:8370 does not contain the word Flask. Might be down")
    else:
        print("Server at 127.0.0.1:8370 is up")
    if "uwsgi" in run("ps -A | grep uwsgi"):
        print("uwsgi is running in processes")
    else:
        print("uwsgi is not running in processes")
    if "no app loaded" in sudo("tailj -n 15 /var/log/uwsgi/app/uwsgi.log"):
        print("The term 'no app loaded' appeared in uwsgi.log")


def nginx():
    check = run('curl 127.0.0.1:80')
    if "Flask" not in check:
        print("Failed checkpoint Nginx")
    else:
        print("You passed checkpoint Nginx!")
    if "nginx" in run("ps -A | grep nginx"):
        print("nginx is running in process")
    else:
        print("nginx is not running in proccesses")













