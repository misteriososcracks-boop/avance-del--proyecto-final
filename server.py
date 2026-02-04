import json
import socket
import threading
import subprocess
import psutil
import sys

HOST = "0.0.0.0"
PORT = 5050

if len(sys.argv) > 1:
    PORT = int(sys.argv[1])


def send_json(conn, obj):
    conn.sendall((json.dumps(obj) + "\n").encode())

def recv_line(conn):
    data = b""
    while True:
        c = conn.recv(1)
        if c == b"\n":
            return data.decode()
        data += c

def handle(conn):
    while True:
        msg = recv_line(conn)
        if not msg:
            break
        req = json.loads(msg)
        cmd = req.get("cmd")

        if cmd == "PING":
            send_json(conn, {"ok": True, "msg": "pong"})

        elif cmd == "LIST":
            procs = []
            for p in psutil.process_iter(["pid", "name"]):
                procs.append(p.info)
            send_json(conn, {"ok": True, "data": procs[:10]})

        elif cmd == "START":
            p = subprocess.Popen(req["command"], shell=True)
            send_json(conn, {"ok": True, "pid": p.pid})

        elif cmd == "STOP":
            psutil.Process(req["pid"]).terminate()
            send_json(conn, {"ok": True})

        elif cmd == "INFO":
            send_json(conn, {
                "cpu": psutil.cpu_percent(),
                "ram": psutil.virtual_memory().percent
            })

def main():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen()
    print("Servidor escuchando en puerto 5050")

    while True:
        c, _ = s.accept()
        threading.Thread(target=handle, args=(c,)).start()

main()

