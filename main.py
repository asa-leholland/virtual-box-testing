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
        'MachineState(1)': 'unlocked',
        'MachineState(2)': 'locked',
        'MachineState(3)': 'spawning',
        'MachineState(4)': 'unlocking',
        'MachineState(5)': 'running'
    }

    if str(machine_state) in machine_state_descriptions:
        return machine_state_descriptions[machine_state]
    else:
        return str(machine_state)

