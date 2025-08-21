import socket
import requests

def domain_to_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        return None

def ip_lookup(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Failed to fetch details"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    user_input = input("Enter domain or IP: ").strip()
    
    # if it's a domain, get IP
    if not user_input.replace(".", "").isdigit():
        ip = domain_to_ip(user_input)
        if ip:
            print(f"Domain: {user_input} → IP: {ip}")
        else:
            print("Invalid domain")
            exit()
    else:
        ip = user_input

    details = ip_lookup(ip)
    print("\nIP Details:")
    for k, v in details.items():
        print(f"{k}: {v}")
