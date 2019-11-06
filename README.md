# Video Streaming Server-Client Network 
Streaming TCP client/server network using Python's socket and opencv with measuring delay.

# Network Running 
After Cloning network's files.

Run streamingServer.py. You will be prompted for a host and port for the server. Incase you want to run the client on the same computer or local network as the server, use localhost as "127.0.0.1". If you are going to run the client on a different network, use the computer's local IP address. The port can be any 16 bit number (lower than 65535), but the port must be forwarded on your router if the client will be on a different network.

Run streamingClient.py. If the server is running on the same computer, use localhost as the host. If the server is running on a different computer, but the same local network, use the local IP address of the computer that the server is running on. If the server is running on a different network, use the external IP address of the network.

# Network Usage
The client should successfully connect to the server. When the server receives a message from client and the streaming starts, you will see the frames in server side using opencv's "imshow" function. the delay time for sending frames from client to server side will be printed as well.
