import socket
# import nmap


def scan_port(ip, port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.001)

    # Attempt to connect to the port
    result = sock.connect_ex((ip, port))
    sock.close()  # Close the socket

    # Check if the port is open
    if result == 0:
        return True
    else:
        return False


# Define the target IP address and port range to scan
ip = '192.168.0.37'
port_range = range(1, 60000)

ports = []

# Loop through the port range and scan each port
for port in port_range:
    if scan_port(ip, port):
        print(f"Port {port} is open")
        ports.append(port)


print(ports)
