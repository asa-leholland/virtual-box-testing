Saving another optiong found here: 
https://forums.virtualbox.org/viewtopic.php?f=6&t=50752

You could also "roll your own" remote-start utility. Here's how I would do it:

A constantly-running VBscript on the host monitors a shared folder on the host for a file of a certain format (certain name and/or extension). The file being looked for would be a text file, containing the name of the VM that needs to be launched and any desired password data. When the host VBscript finds the correct file in the shared folder, it opens the file, authenticates the password, reads the VM name, and launches the VM using Vboxmanage. Then it deletes the text file in the shared folder.

On each guest is another VBscript, run by the user when the VM is needed, that makes the correct text file containing the desired VM name and the password, and puts the text file in the host shared folder for the host VBscript to read.

Some fancy stuff could be done with this, such as having the host script check the status of the VM before starting it, to see if if is already started, and feeding back to the remote user's script another text file which the remote script waits for, telling the remote script when the VM is running. The remote script could then launch the Remote Desktop session automatically. With such feedback, users would only need one shortcut, no need for one program to start the VM and another to start the RDP session.

Of course VBscript is all Windows host/guest related, but Mac/Linux should have something similar.



Remote VirtualBox notes:
https://www.virtualbox.org/manual/ch07.html

<img src="https://docs.google.com/drawings/d/e/2PACX-1vQevc5XdrN6K5ADm2ybDjXvxPyoJ-_8ntQC5951pA12Htlbadk793UIfQNXWslp_rcQO5m3BGe4xBxC/pub?w=960&amp;h=720">
