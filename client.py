import socket, json

s = socket.create_connection(("127.0.0.1", 5050))

def send(obj):
    s.sendall((json.dumps(obj)+"\n").encode())
    print(s.recv(4096).decode())

while True:
    print("\n1) PING\n2) LIST\n3) START\n4) STOP\n5) INFO\n6) EXIT")
    o = input("> ")

    if o=="1":
        send({"cmd":"PING"})
    elif o=="2":
        send({"cmd":"LIST"})
    elif o=="3":
        cmd = input("Comando: ")
        send({"cmd":"START","command":cmd})
    elif o=="4":
        pid = int(input("PID: "))
        send({"cmd":"STOP","pid":pid})
    elif o=="5":
        send({"cmd":"INFO"})
    elif o=="6":
        break

