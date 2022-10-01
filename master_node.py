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

port_num = { "A": "9000","B": "8000","C": "7000"}

def master_node_functions():

	choice =  int(input("\n[*] Enter 1 to RUN, 0 EXIT: "))
	if  (choice == 0):
		return
	
	send_proc = input("[*] Enter the Sending Node (A/B/C): ")
	recv_proc = input("[*] Enter the Recieveing Node (A/B/C): ")
	message = input("[*] Enter the Message: ")
	
	print("[*] [PORT NUM] Proc A:",port_num["A"]," Proc b:",port_num["B"]," Proc C:",port_num["C"],)
	proxy_server = xmlrpc.client.ServerProxy("http://localhost:"+port_num[send_proc.strip()])

	if (send_proc.strip() == "A"):
		status = proxy_server.rpc_callback_at_nodeA(message,"MASTER" ,recv_proc,0)

	if (send_proc.strip() == "B"):
		status = proxy_server.rpc_callback_at_nodeB(message,"MASTER" ,recv_proc,0)


	if (send_proc.strip() == "C"):
		status = proxy_server.rpc_callback_at_nodeC(message,"MASTER" ,recv_proc,0)
	
	print("[*] {",send_proc,"}-->{",recv_proc,"} MSG:'",message,"' ")
	master_node_functions()

if __name__ == "__main__":
	print("\n----- MASTER NODE ------\n")
	master_node_functions()

