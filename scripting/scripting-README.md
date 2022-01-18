<!-- Saving another optiong found here: 
https://forums.virtualbox.org/viewtopic.php?f=6&t=50752

You could also "roll your own" remote-start utility. Here's how I would do it:

A constantly-running VBscript on the host monitors a shared folder on the host for a file of a certain format (certain name and/or extension). The file being looked for would be a text file, containing the name of the VM that needs to be launched and any desired password data. When the host VBscript finds the correct file in the shared folder, it opens the file, authenticates the password, reads the VM name, and launches the VM using Vboxmanage. Then it deletes the text file in the shared folder.

On each guest is another VBscript, run by the user when the VM is needed, that makes the correct text file containing the desired VM name and the password, and puts the text file in the host shared folder for the host VBscript to read.

Some fancy stuff could be done with this, such as having the host script check the status of the VM before starting it, to see if if is already started, and feeding back to the remote user's script another text file which the remote script waits for, telling the remote script when the VM is running. The remote script could then launch the Remote Desktop session automatically. With such feedback, users would only need one shortcut, no need for one program to start the VM and another to start the RDP session.

Of course VBscript is all Windows host/guest related, but Mac/Linux should have something similar.



Remote VirtualBox notes:
https://www.virtualbox.org/manual/ch07.html

<img src="https://docs.google.com/drawings/d/e/2PACX-1vQevc5XdrN6K5ADm2ybDjXvxPyoJ-_8ntQC5951pA12Htlbadk793UIfQNXWslp_rcQO5m3BGe4xBxC/pub?w=960&amp;h=720"> -->

# Remote Virtual Machine Management
These scripts 

# Instructions for Host:

1. On the Host machine, edit environmental variables to include the path to VirtualBox

2. Use the `host_paths_TEMPLATE.py` as a base to create your host paths. On your host machine, rename this file to be `host_paths.py`. Edit the paths of `host_paths.py` as follows:
    'path_to_vbox_manage' : This should be the path on the Host machine to the Host's copy of VBoxManage.exe 
    'path_to_working_dir' : This should be the path to the Host folder where this code will be run. 
    'path_to_requests_dir' : This path should lead to the `restart_requests` subfolder in this directory. This should be a sharable folder that the Host can distribute to the Client to allow for requests to be added.
    'path_to_request_archives_dir' : This path should lead to the `archived_requests` subfolder in this directory, and represents where records of successful requests will be saved.

3. Run `vm-support-host.py` to begin accepting requests.

# Instructions for Client:

1. Confirm that the host machine has been set up, and that you have shared access to the Host's directory where requests can be submitted.

2. To send a request, you will need to know the name of the virtual machine you want to restart.

3. 