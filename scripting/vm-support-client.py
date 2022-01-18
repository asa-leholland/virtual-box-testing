import os
from client_paths import client_paths

path_to_requests_dir = client_paths['path_to_requests_dir']

def request_restart():
    vm_name = input('Provide name of virtual machine to restart: ')
    print(f'Creating request to restart {vm_name}.')
    new_file_path = os.path.join(path_to_requests_dir, 'restart_' + vm_name)
    f = open(new_file_path, 'a')
    f.write(vm_name)
    f.close()

if __name__ == '__main__':
    request_restart()
    
