

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

def serve_basicapp():
    #run('python basicapp.py &')
    run('python basicapp.py')

def basicapp():
    env.warn_only = True
    #time.sleep(3)
    check1 = run('curl 127.0.0.1:5000')
    #print(check1)
    if "Flask" not in check1:
        print("Failed Checkpoint basicapp")
    else:
        print("You passed checkpoint basicapp!")

def uwsgi():
    check = run('curl 127.0.0.1:8370')
    if "Flask" not in check:
        print("Failed checkpoint uwsgi")
    else:
        print("You passed checkpoint uwsgi!")


def get_files():
    pass










