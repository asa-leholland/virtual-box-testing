# main.py
# Author: Asa LeHolland

import virtualbox

vbox = virtualbox.VirtualBox()

def list_available_machines():
    return [m.name for m in vbox.machines]


def launch_machine(machine_name):
    session = virtualbox.Session()
    machine = vbox.find_machine(machine_name)
    progress = machine.launch_vm_process(session, "gui", [])
    progress.wait_for_completion()


def query_session_state_description(session):
    session_state = session.state

    session_state_descriptions = {
        'SessionState(0)': 'null',
        'SessionState(1)': 'unlocked',
        'SessionState(2)': 'locked',
        'SessionState(3)': 'spawning',
        'SessionState(4)': 'unlocking'
    }

    if str(session_state) in session_state_descriptions:
        return session_state_descriptions[session_state]
    else:
        return str(session_state)

def query_machine_state_description(machine):
    machine_state = machine.state

    machine_state_descriptions = {
        'MachineState(0)': 'null',
        'MachineState(1)': 'powered off',
        'MachineState(2)': 'saved',
        'MachineState(3)': 'teleported',
        'MachineState(4)': 'live snapshotting',
        'MachineState(5)': 'starting',
        'MachineState(6)': 'stopping',
        'MachineState(7)': 'saving',
        'MachineState(8)': 'restoring',
        'MachineState(9)': 'teleporting paused VM',
        'MachineState(10)': 'teleporting in',
        'MachineState(11)': 'deleting snapshot online',
        'MachineState(12)': 'deleting snapshot paused',
        'MachineState(13)': 'online snapshotting',
        'MachineState(14)': 'restoring snapshot',
        'MachineState(15)': 'deleting snapshot',
        'MachineState(16)': 'setting up',
        'MachineState(17)': 'snapshotting',
        'MachineState(18)': 'first online',
        'MachineState(19)': 'last online',
        'MachineState(20)': 'first transient',
        'MachineState(21)': 'last transient'
    }

    if str(machine_state) in machine_state_descriptions:
        return machine_state_descriptions[machine_state]
    else:
        return str(machine_state)

def get_screen_resolution_details(session):
    details = {
        'height': session.console.display.get_screen_resolution()[0],
        'width': session.console.display.get_screen_resolution()[1],
        'bits_per_pixel': session.console.display.get_screen_resolution()[2],
        'x_origin': session.console.display.get_screen_resolution()[3],
        'y_origin': session.console.display.get_screen_resolution()[4],
        'guest_monitor_status': session.console.display.get_screen_resolution()[5]
        }
    return details

