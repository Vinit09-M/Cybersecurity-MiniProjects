
---

## 🐍 port_scanner.py
```python
import socket
import concurrent.futures

def scan_port(host, port):
    """Try connecting to a port. Return True if open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)  # half-second timeout
            if s.connect_ex((host, port)) == 0:
                return port
    except:
        return None
    return None

def parse_ports(port_input, default_ports):
    """Parse user input for ports: default / range / list."""
    if not port_input.strip():
        return default_ports
    if "-" in port_input:
        start, end = port_input.split("-")
        return list(range(int(start), int(end) + 1))
    if "," in port_input:
        return [int(p.strip()) for p in port_input.split(",")]
    return [int(port_input)]

def main():
    default_ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 3389]

    host = input("Enter target (IP or domain): ").strip()
    ports_input = input(f"Ports to scan {default_ports}: ")

    ports = parse_ports(ports_input, default_ports)

    print(f"\nScanning {host} ...")
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(lambda p: scan_port(host, p), ports)
        for result in results:
            if result:
                print(f"[OPEN] {result}")
                open_ports.append(result)

    print(f"Scan complete. {len(open_ports)} port(s) open: {open_ports}")

if __name__ == "__main__":
    main()
