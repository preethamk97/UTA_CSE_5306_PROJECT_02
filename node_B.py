"""
* DS CSE-5306-001 Project 2
* Author 1:
* 	Preetham Karanth Kota 
*	pxk6418@mavs.uta.edu
*	1002076418
"""
import os
import threading
import xmlrpc.client
from xmlrpc.server import SimpleXMLRPCServer

#A is 0,B is 1, C is 2
VECTOR_AT_NODE_B             = [0,0,0]
port_num = {"A": "9000", "B": "8000", "C": "7000"}

def send_message(message_to_be_sent,to_node):

	print("[*] {B}-->{",to_node.strip()," MSG:'",message_to_be_sent,"' Time Vector Before: ",VECTOR_AT_NODE_B)
	VECTOR_AT_NODE_B[1] += 1
	proxy_server = xmlrpc.client.ServerProxy(("http://localhost:"+port_num[to_node.strip()]))
	if (to_node.strip() == "A"):
		status = proxy_server.rpc_callback_at_nodeA(message_to_be_sent,"B" ,to_node,VECTOR_AT_NODE_B[1])

	elif (to_node.strip() == "C"):
		status = proxy_server.rpc_callback_at_nodeC(message_to_be_sent,"B" ,to_node,VECTOR_AT_NODE_B[1])

	print("[*] {B}-->{",to_node.strip()," MSG:'",message_to_be_sent,"' Time Vector After: ",VECTOR_AT_NODE_B,"\n")

def recv_message(message,from_node,time_at_node):

	print("[*] {",from_node.strip(),"} ---> {B} MSG: ",message,"BEFORE Vector Node A: ",VECTOR_AT_NODE_B)
	VECTOR_AT_NODE_B[1] += 1
	if(from_node == "A"):
		VECTOR_AT_NODE_B[0] = time_at_node
	
	elif(from_node == "C"):
		VECTOR_AT_NODE_B[2] = time_at_node
	
	print("[*] {",from_node.strip(),"} ---> {B} MSG: ",message,"AFTER Vector Node A: ",VECTOR_AT_NODE_B,"\n")

def rpc_callback_at_nodeB(message_to_be_sent = " ",from_node = " " ,to_node = " ", time_at_node = 0):

	if (from_node == "MASTER"):
		thread1 = threading.Thread(target = send_message, args = (message_to_be_sent,to_node,))
		thread1.start()

	else:
		thread1 = threading.Thread(target = recv_message, args = (message_to_be_sent,from_node,time_at_node,))
		thread1.start()

	return 1

if __name__ == "__main__":
	print("\n*** Process Node B started\n")
	print("[*] Process Listening at PORT 8000 ....\n")
	server = SimpleXMLRPCServer(('localhost', 8000))
	server.register_function(rpc_callback_at_nodeB, 'rpc_callback_at_nodeB')
	server.serve_forever()

