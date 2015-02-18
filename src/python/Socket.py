from socket import socket

class SprocketSocket(object):
	'''
	this is just a basic class to handle socket connections
	'''
	def __init__(self, sock=None):
		if sock is None:
			self.socket = socket(socket.AF_INET,socket.SOCK_STREAM)
		else:
			self.socket = sock

	def Connect(self,host,port):
		self.socket.connect((host,port))

	def Send(self,msg):
		totalSent = 0
		while totalSent < MSGLEN