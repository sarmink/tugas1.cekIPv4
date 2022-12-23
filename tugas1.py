import socket

def is_valid_ipv4(ip):

    if ip == "0.0.0.0":
      return False
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

ip_address = input("Masukkan alamat IP : ")

if is_valid_ipv4(ip_address):
    print("IP valid")
else:
    print("IP tidak valid")
