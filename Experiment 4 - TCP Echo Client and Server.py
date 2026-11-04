#echo server
import socket
def echo_server():
try:
# Create TCP socket (IPv4 + TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow address reuse (prevents &quot;Address already in use&quot; error)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to localhost and port
server_socket.bind((&#39;127.0.0.1&#39;, 65432))

# Listen for incoming connections
server_socket.listen(5)
print(&quot;Server listening on port 65432...&quot;)

while True:
# Accept client connection
connection, client_address = server_socket.accept()
print(f&quot;Connected by {client_address}&quot;)

while True:
# Receive data

data = connection.recv(1024)
if not data:
break

message = data.decode()
print(f&quot;Received: {message}&quot;)

# Send back same data (Echo)
connection.sendall(data)

connection.close()
print(&quot;Client disconnected\n&quot;)

except KeyboardInterrupt:
print(&quot;\nServer stopped manually.&quot;)
except Exception as e:
print(&quot;Error:&quot;, e)
finally:
server_socket.close()
if __name__ == &#39;__main__&#39;:
echo_server()

#Python Code:
#b,Echo Client:
import socket

def echo_client():
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((&#39;localhost&#39;, 65432))

while True:
# Send data to the server
message = input(&quot;Enter a message: &quot;)
client_socket.sendall(message.encode())
# Receive the echo response from the server
data = client_socket.recv(1024)
print(f&quot;Echoed from server: {data.decode()}&quot;)
if message.lower() == &#39;exit&#39;:
break

client_socket.close()

if __name__ == &#39;__main__&#39;:

echo_client()
