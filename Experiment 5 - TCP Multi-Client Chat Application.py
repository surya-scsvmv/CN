#Chat Server
import socket
import threading
clients = []
def handle_client(client_socket, client_address):
print(f&quot;New connection from {client_address}&quot;)
while True:
try:
message = client_socket.recv(1024).decode()
if not message:
break
print(f&quot;Received from {client_address}: {message}&quot;)
# Broadcast message to all other clients
for client in clients:
if client != client_socket:
client.sendall(message.encode())
except Exception as e:
print(f&quot;Error with {client_address}: {e}&quot;)
break
# Remove disconnected client
if client_socket in clients:
clients.remove(client_socket)
client_socket.close()
print(f&quot;{client_address} disconnected&quot;)
def chat_server():
# Create TCP socket
server_socket = socket.socket(
socket.AF_INET,
socket.SOCK_STREAM
)
# Allow immediate reuse of the port
server_socket.setsockopt(
socket.SOL_SOCKET,
socket.SO_REUSEADDR,
1
)
# Bind server to localhost and port 55555
server_socket.bind((&#39;localhost&#39;, 55555))

# Listen for incoming connections
server_socket.listen(5)
print(&quot;Server listening on port 55555...&quot;)
while True:
# Accept a new client
client_socket, client_address = server_socket.accept()
# Add client to the client list
clients.append(client_socket)
# Create a separate thread for the client
thread = threading.Thread(
target=handle_client,
args=(client_socket, client_address)
)
# Allow thread to terminate when server stops
thread.daemon = True
# Start client thread
thread.start()
if __name__ == &#39;__main__&#39;:
chat_server()

#Chat Client
import socket
import threading
def receive_messages(client_socket):
while True:
try:
message = client_socket.recv(1024).decode()
if not message:
print(&quot;Disconnected from server.&quot;)
break
print(message)
except Exception as e:
print(f&quot;Error receiving message: {e}&quot;)
break
def chat_client():
# Create TCP socket
client_socket = socket.socket(
socket.AF_INET,
socket.SOCK_STREAM
)
try:
# Connect to the chat server
client_socket.connect((&#39;localhost&#39;, 55555))
print(&quot;Connected to chat server.&quot;)
except Exception as e:
print(f&quot;Unable to connect: {e}&quot;)
return
# Create a separate thread for receiving messages

receive_thread = threading.Thread(
target=receive_messages,
args=(client_socket,),
daemon=True
)
receive_thread.start()
# Send messages to server
while True:
try:
message = input()
if message.lower() == &quot;exit&quot;:
break
client_socket.sendall(message.encode())
except Exception as e:
print(f&quot;Error sending message: {e}&quot;)
break
# Close socket
client_socket.close()
if __name__ == &#39;__main__&#39;:
chat_client()
