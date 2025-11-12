import socket
import select
import sys



if len(sys.argv) != 6:
    print("")
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])
Command = sys.argv[3]
Dictionary = sys.argv[4]
Key = sys.argv[5]

socket_client = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
socket_client.connect((HOST, PORT))

message_for_server = f"{Command} {Dictionary} {Key}\n"
message_for_server_bit = message_for_server.encode("utf-8")
socket_client.sendall(message_for_server_bit)

answer_server = b''
while True: 
    data = socket_client.recv(1024)
    if data: 
        answer_server += data
    else:
        break

answer_server_str = answer_server.decode("utf-8").strip()
print(answer_server_str)
socket_client.close()
    








