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
VECTOR_AT_NODE_A             = [0,0,0]
port_num = {"A": "9000", "B": "8000", "C": "7000"}

def send_message(message_to_be_sent,to_node):

	print("[*] {A}-->{",to_node.strip(),"} MSG:'",message_to_be_sent,"' Time Vector Before: ",VECTOR_AT_NODE_A)
	VECTOR_AT_NODE_A[0] += 1
	proxy_server = xmlrpc.client.ServerProxy(("http://localhost:"+port_num[to_node.strip()]))
	if (to_node.strip() == "B"):
		status = proxy_server.rpc_callback_at_nodeB(message_to_be_sent,"A" ,to_node,VECTOR_AT_NODE_A)

	elif (to_node.strip() == "C"):
		status = proxy_server.rpc_callback_at_nodeC(message_to_be_sent,"A" ,to_node,VECTOR_AT_NODE_A)

	print("[*] {A}-->{",to_node.strip(),"} MSG:'",message_to_be_sent,"' Time Vector After: ",VECTOR_AT_NODE_A,"\n")

def recv_message(message,from_node,time_at_node):

	print("[*] {",from_node.strip(),"} ---> {A} MSG: ",message,"BEFORE Vector Node A: ",VECTOR_AT_NODE_A)
	VECTOR_AT_NODE_A[0] += 1
	VECTOR_AT_NODE_A[1] = time_at_node[1]
	VECTOR_AT_NODE_A[2] = time_at_node[2]
	print("[*] {",from_node.strip(),"} ---> {A} MSG: ",message,"AFTER Vector Node A: ",VECTOR_AT_NODE_A,"\n")

def rpc_callback_at_nodeA(message_to_be_sent = " ",from_node = " " ,to_node = " ", time_at_node = None):

	if (from_node == "MASTER"):
		thread1 = threading.Thread(target = send_message, args = (message_to_be_sent,to_node,))
		thread1.start()

	else:
		thread1 = threading.Thread(target = recv_message, args = (message_to_be_sent,from_node,time_at_node,))
		thread1.start()

	return 1

if __name__ == "__main__":
	print("\n*** Process Node A started\n")
	print("[*] Process Listening at PORT 9000 ....\n")
	server = SimpleXMLRPCServer(('localhost', 9000))
	server.register_function(rpc_callback_at_nodeA, 'rpc_callback_at_nodeA')
	server.serve_forever()

