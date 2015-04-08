from rat import *
from sys import argv
from os import _exit

MSG_LISTENING = "<server> Now listening for connections..."
ERR_PORT_EVEN = "Error: Sorry! This assignment specifies an " + \
    "input port must be an odd number!"
ERR_INPUT_ARGS = "Error: Address or port numbers invalid!"
ERR_INVALID_ARGS = "Syntax: fxa-server.py <local port #> " + \
    "<NetEmu IP address> <NetEmu port #>"

def main():
    '''The entry point of the program.'''

    # Parse command-line arguments
    if (len(argv) != 4):
        print(ERR_INVALID_ARGS)
        _exit(0)
    
    # Check arguments
    local_port = argv[1]
    netemu_ip = argv[2]
    netemu_port = argv[3]

    if not port_check(local_port) or \
    not port_check(netemu_port) or \
    not address_check(netemu_ip):
        print(ERR_INPUT_ARGS)
        _exit(0)

    if (int(local_port) % 2 != 1):
        print(ERR_PORT_EVEN)
        _exit(0)

    local_port = int(local_port)
    netemu_port = int(netemu_port)

    server_loop(local_port, netemu_ip, netemu_port)

def server_loop(local_port, netemu_ip, netemu_port):
    '''The main loop of the server.'''

    server_sock = RatSocket(debug_mode=True)
    server_sock.listen(("127.0.0.1", local_port))
    print(MSG_LISTENING)
    while True:
        # Loop here
        pass

def address_check(ip_addr):
    '''Checks if a given IP address is valid.'''

    try:
        octets = [int(x) for x in (ip_addr.split("."))]
        for octet in octets:
            if (octet < 0 and octet > 255):
                return False
    except Exception:
        return False

    return True

def port_check(port):
    '''Checks if a given port number is valid.'''

    try:
        port = int(port)

        # Assumed that ports 0 and 65535 are reserved
        if (port <= 0): return False
        if (port >= 65535): return False
    except Exception:
        return False

    return True

main()