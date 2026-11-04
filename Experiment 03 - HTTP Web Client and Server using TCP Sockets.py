import socket
def download_web_page(hostname, port, path):
try:
# Create a socket object (IPv4 + TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((hostname, port))

# Prepare HTTP GET request
request = f&quot;GET {path} HTTP/1.1\r\nHost: {hostname}\r\nConnection: close\r\n\r\n&quot;

# Send request to server
client_socket.sendall(request.encode())

# Receive response from server
response = b&quot;&quot;
while True:
data = client_socket.recv(4096)
if not data:
break
response += data

# Close the connection
client_socket.close()

# Decode safely (avoid Unicode error)
return response.decode(errors=&quot;ignore&quot;)

except Exception as e:
return f&quot;Error occurred: {e}&quot;

# Example usage
hostname = &quot;example.com&quot; # Avoid https site with port 80
port = 80
path = &quot;/&quot;

response = download_web_page(hostname, port, path)
print(response)
