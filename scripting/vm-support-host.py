from asyncio import subprocess
from cgitb import text
from genericpath import exists
from multiprocessing.connection import wait
import os
from re import sub
import subprocess
import shutil
import time
import datetime
from os.path import exists
import fnmatch

# from credentials import credentials
# creds = credentials.require('path_to_vbox_manage': )

# os.system("start cmd")
path_to_vbox_manage = "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
path_to_working_dir = 'C:\\Users\\asale\\Documents\\GitHub\\virtual-box-testing\\scripting'
path_to_requests_dir = 'C:\\Users\\asale\\Documents\\GitHub\\virtual-box-testing\\scripting\\restart_requests'
path_to_request_archives_dir = 'C:\\Users\\asale\\Documents\\GitHub\\virtual-box-testing\\scripting\\archived_requests'

def display_output():
    # print(subprocess.check_output('dir c:\\'))
    os.system('dir c:\\')

def display_vbox_output():
    command_1 = ['VBoxmanage', 'list', 'vms']
    command_2 = ['dir', 'c:\\']

    

    # command_3 = ['dir', full_path]

    # pathToVirtualBox = 'from credentials import credentials'
    subprocess.call([path_to_vbox_manage, 'list', 'vms'])
    

def display_vbox_output_1():
    output = subprocess.getoutput("ls -l")
    print(output)


def display_vbox_output_2():
    subprocess.run(['ls', '-l'], capture_output=True, text=True).stdout

def get_list_of_running_vms():
    result = subprocess.check_output([path_to_vbox_manage, 'list', 'runningvms'])
    return result

def start_a_vm(vm_name):
    subprocess.call([path_to_vbox_manage, 'startvm', vm_name])
    print(f'Virtual machine {vm_name} has been started.')

def shut_down_a_vm(vm_name):
    subprocess.call([path_to_vbox_manage, 'controlvm', vm_name, 'acpipowerbutton'])
    print(f'Virtual machine {vm_name} has been shut down.')

def process_request(filename):
    
    if fnmatch.fnmatch(filename, 'restart*.txt'):
        print('Host has received request to restart a virtual machine')
        f = open(filename, "r")
        requested_vm_name = f.readline()

        print('IMPORTANT', get_list_of_running_vms())
        valid_vms = ['Ubuntu 2018']

        if requested_vm_name in valid_vms:
            restart_vm(vm_name=requested_vm_name)
            archive_request(request_filename=filename)

    else:
        print('Host has received a request that cannot be processed. Request will be deleted.')
        os.remove(filename)
        print('Request has been deleted.')

    

def restart_vm(vm_name):
    path_to_vbox_manage = "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
    subprocess.call([path_to_vbox_manage, 'controlvm', vm_name, 'reset'])
    print(f'Host has restarted virtual machine {vm_name}')

def archive_request(request_filename):
    timestamp = sub("[^0-9]", "", str(datetime.datetime.now()))
    shutil.move(os.path.join(path_to_requests_dir, request_filename), os.path.join(path_to_request_archives_dir, '_' + timestamp + request_filename))
    print('Request has been archived.')

def create_request_test(vm_name):
    print(f'Request created to restart {vm_name}')
    new_file_path = os.path.join(path_to_requests_dir, 'restart_' + vm_name)
    f = open(new_file_path, 'a')
    f.write(vm_name)
    f.close()

def run_checker():
    running = True
    print('Host is running, awaiting client requests')
    while running:
        start_a_vm("Ubuntu 2018")
        create_request_test(vm_name="Ubuntu 2018")
        create_request_test(vm_name="Ubuntu 2019")
        time.sleep(5)
        for filename in os.listdir(path_to_requests_dir):
            f = os.path.join(path_to_requests_dir, filename)
            if os.path.isfile(f):
                process_request(filename=f)
                time.sleep(5)
                running = False
        shut_down_a_vm("Ubuntu 2018")
                


if __name__ == '__main__':
    # display_output()
    # display_vbox_output()
    # display_vbox_output()
    # start_a_vm("Ubuntu 2018")
    # restart_vm("Ubuntu 2019")
    run_checker()
    time.sleep(5)
    
