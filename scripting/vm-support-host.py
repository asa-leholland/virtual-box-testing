import os
import re
import subprocess
import shutil
import time
import datetime
import fnmatch

path_to_vbox_manage = "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
path_to_working_dir = 'C:\\Users\\asale\\Documents\\GitHub\\virtual-box-testing\\scripting'
path_to_requests_dir = 'C:\\Users\\asale\\Documents\\GitHub\\virtual-box-testing\\scripting\\restart_requests'
path_to_request_archives_dir = 'C:\\Users\\asale\\Documents\\GitHub\\virtual-box-testing\\scripting\\archived_requests'


def display_vbox_output():
    subprocess.call([path_to_vbox_manage, 'list', 'vms'])

def display_vbox_output_1():
    output = subprocess.getoutput("ls -l")
    print(output)


def display_vbox_output_2():
    subprocess.run(['ls', '-l'], capture_output=True, text=True).stdout

def get_list_of_running_vms():
    result = str(subprocess.check_output([path_to_vbox_manage, 'list', 'runningvms']))
    array_results = re.findall(r'"(.*?)"', result)
    return array_results

def get_list_of_all_vms():
    result = str(subprocess.check_output([path_to_vbox_manage, 'list', 'vms']))
    array_results = re.findall(r'"(.*?)"', result)
    return array_results

def start_a_vm(vm_name):
    subprocess.call([path_to_vbox_manage, 'startvm', vm_name])
    print(f'Virtual machine {vm_name} has been started.')

def shut_down_a_vm(vm_name):
    subprocess.call([path_to_vbox_manage, 'controlvm', vm_name, 'acpipowerbutton'])
    print(f'Virtual machine {vm_name} has been shut down.\n')

def process_request(filename):   
    if fnmatch.fnmatch(filename, path_to_requests_dir + '\\restart*'):
        print('Host has received request to restart a virtual machine.')
        f = open(filename, "r")
        requested_vm_name = f.readline()
        f.close()
        valid_vms = get_list_of_running_vms()
        if requested_vm_name in valid_vms:
            restart_vm(vm_name=requested_vm_name)
            archive_request(request_filename=filename)
        else:
            all_vms = get_list_of_all_vms()
            if requested_vm_name in all_vms:
                start_a_vm(requested_vm_name)
                archive_request(request_filename=filename)
            else:
                print(f'Requested machine {requested_vm_name} cannot be found.')
                delete_request(filename)

    else:
        print('Host has received a request that cannot be processed.')
        delete_request(filename)

    

def restart_vm(vm_name):
    path_to_vbox_manage = "C:\Program Files\Oracle\VirtualBox\VBoxManage.exe"
    subprocess.call([path_to_vbox_manage, 'controlvm', vm_name, 'reset'])
    print(f'Host has restarted virtual machine {vm_name}.')

def archive_request(request_filename):
    timestamp = re.sub("[^0-9]", "", str(datetime.datetime.now()))
    infile_name = os.path.join(path_to_requests_dir, request_filename)
    temp = request_filename.replace(path_to_requests_dir, '')
    outfile_name = os.path.join(path_to_request_archives_dir + temp + '_' + timestamp)
    shutil.move(infile_name, outfile_name)
    print('Request has been archived.\n')

def delete_request(request_filename):
    os.remove(request_filename)
    print('Request has been deleted.\n')

def clear_requests_folder():
    for filename in os.listdir(path_to_requests_dir):
        if filename != ".gitkeep":
            os.remove(os.path.join(path_to_requests_dir, filename))

def create_request_test(vm_name):
    print(f'Request created to restart {vm_name}.')
    new_file_path = os.path.join(path_to_requests_dir, 'restart_' + vm_name)
    f = open(new_file_path, 'a')
    f.write(vm_name)
    f.close()

def run_host():
    print('\nHost is looking for client requests.\n')
    for filename in os.listdir(path_to_requests_dir):
        if filename != ".gitkeep":
            f = os.path.join(path_to_requests_dir, filename)
            if os.path.isfile(f):
                process_request(filename=f)

def run_checker():
        
    clear_requests_folder()
    
    print('test1: test restarting a running machine')
    if "Ubuntu 2018" not in get_list_of_running_vms():
        start_a_vm("Ubuntu 2018")
    create_request_test(vm_name="Ubuntu 2018")
    run_host()

    print('test2: test restarting a machine that is not running')
    if "Ubuntu 2018" in get_list_of_running_vms():
        shut_down_a_vm("Ubuntu 2018")
    create_request_test(vm_name="Ubuntu 2018")
    run_host()

    print('test3: test restarting a machine that does not exist')
    create_request_test(vm_name="Ubuntu 2019")
    run_host()
        
    if "Ubuntu 2018" in get_list_of_running_vms():
        shut_down_a_vm("Ubuntu 2018")
                


if __name__ == '__main__':
    run_checker()
    
