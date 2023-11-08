import socket

#Target/host
target = input("Enter the target host (e.g., example.com): ")

#Port range/Specific ports
ports_input = input("Enter a port range (e.g., 1-1024) / Specific ports (e.g., 80,443): ")

#Determine Input
ports_to_scan = []
try:
    #Port range
    if "-" in ports_input:
        start_port, end_port = map(int, ports_input.split("-"))
        ports_to_scan = list(range(start_port, end_port + 1))
    else:
        #Specific ports
        ports_to_scan = list(map(int, ports_input.split(",")))
except ValueError:
    print("Choose a valid option as shown in the example. Thank you!")
    exit(1)

#Flags mapping
flags_mapping = {
    "SYN": socket.SOCK_STREAM,
    "FIN": socket.SOCK_STREAM,
    "NULL": socket.SOCK_STREAM,
    "XMAS": socket.SOCK_STREAM,
    "ACK": socket.SOCK_STREAM,
}

#Display flags
print("Available scanning flags:")
for flag in flags_mapping:
    print(f"- {flag}")

#Input flags
selected_flags = input("Enter the flags you want to use separated by spaces (e.g., SYN NULL ACK): ").split()

#For Open ports
open_ports = []

#Port scanning
for port in ports_to_scan:
    for flag_name in selected_flags:
        sock_type = flags_mapping.get(flag_name.upper())
        if sock_type is not None:
            try:
                #Create Socket
                sock = socket.socket(socket.AF_INET, sock_type)
                sock.settimeout(2)

                #Connect to target and port
                result = sock.connect_ex((target, port))

                #if connection successful
                if result == 0:
                    print(f"Port {port} is open ({flag_name} scan)")
                    open_ports.append(port)
                sock.close()
            except Exception as e:
                pass

#Identify and print ports that did not respond (only for specific ports, not the entire range)
if "-" not in ports_input:
    non_responding_ports = [port for port in ports_to_scan if port not in open_ports]
    print(f"Ports list that did not respond: {non_responding_ports}")
