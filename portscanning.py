import socket
from concurrent.futures import ThreadPoolExecutor
import re


# Validate IP Address
def is_valid_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    return re.match(pattern, ip) is not None


# Scan a single port
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        if result == 0:
            return port
    except Exception:
        pass
    return None


# Banner Grabbing
def grab_banner(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((target, port))
        banner = sock.recv(1024).decode().strip()
        sock.close()
        return banner
    except Exception:
        return "No banner detected"


# Scan Ports Using Multi-threading
def scan_ports(target, ports):
    print(f"Scanning {target} for open ports...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(target, p), ports)
    open_ports = [port for port in results if port is not None]
    return open_ports


if __name__ == "__main__":
    try:
        # Get target IP
        target = input("Enter the target IP address: ")
        if not is_valid_ip(target):
            print("Invalid IP address format. Please try again.")
            exit()

        # Get port range
        port_range = input("Enter the port range (e.g., 1-1024): ").split("-")
        try:
            start_port, end_port = int(port_range[0]), int(port_range[1])
            if start_port < 1 or end_port > 65535 or start_port > end_port:
                raise ValueError
        except ValueError:
            print("Invalid port range. Please enter a valid range (e.g., 1-1024).")
            exit()

        ports = range(start_port, end_port + 1)

        # Scan ports
        open_ports = scan_ports(target, ports)

        # Display results
        if open_ports:
            print(f"\nOpen ports on {target}:")
            for port in open_ports:
                banner = grab_banner(target, port)
                print(f"Port {port}: OPEN | Banner: {banner}")
        else:
            print("No open ports found.")
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
