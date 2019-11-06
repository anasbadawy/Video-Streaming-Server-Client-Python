import socket
import cv2
import pickle
import numpy as np
import struct  # new
import datetime

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('127.0.0.1', 8889))
serv.listen(5)
print("Ready to serve . . .")

def startConnection(serv):

	conn, addr = serv.accept() 
	data = b""
	payload_size = struct.calcsize(">L")
	print("payload_size: {}".format(payload_size))
	while True:
		while len(data) < payload_size:
			data += conn.recv(4096)
			if len(data)==0:
				startConnection(serv)
		#print("Done Recv: {}".format(len(data)))
		packed_msg_size = data[:payload_size]
		data = data[payload_size:]
		msg_size = struct.unpack(">L", packed_msg_size)[0]
		print("msg_size: {}".format(msg_size))
		recivDate = datetime.datetime.now()

		while len(data) < msg_size:
			container = conn.recv(4096)
			if len(container)==0:
				startConnection(serv)
			data += container

		frame_data = data[:msg_size]
		data = data[msg_size:] 

		frame = pickle.loads(frame_data, fix_imports=True, encoding="bytes")
		print("delay: {}".format(recivDate-frame['time']))
		frame = cv2.imdecode(frame['frame'], cv2.IMREAD_COLOR)		

		cv2.imshow('Streaming Video', frame)

		cv2.waitKey(1)

	print("Close the client socket")
		
	conn.close()

startConnection(serv)