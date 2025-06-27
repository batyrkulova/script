# import requests
# proxies = {
#     "http": "https://api.ipify.org?format=json"
# }
# response = requests.get("https://ipinfo.io/json", proxies=proxies)
# print(response)


import requests

try:
    response = requests.get('https://www.example.com', stream=True)
    # Access the raw socket connection and get the peer's address
    server_ip = response.raw._connection.sock.getpeername()[0]
    print(f"The server's IP address is: {server_ip}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
finally:
    if 'response' in locals() and response:
        response.close() # Ensure the connection is closed∑