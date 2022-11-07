# UTA_CSE_5306_002_PROJECT

## Authors:
Preetham Karanth Kota</br>
pxk6418@mavs.uta.edu</br>
1002076418</br>

## System Requirements:
_***Linux OS:***</br>
Developed and tested the software on Ubunut 22.04 LTS. Any linux distribution should do just fine with
Python 3.10_

## Contents of the PROJECT:
Implementing a vector clock for distributed system.Created two threads for each process, one for sending messages to other nodes and one for listening to its communication port. Communication among nodes is done using RPC. Once the process sends a message, it prints its vector clock before and after sending a message. Similarly, once a process receives a message, it prints its vector clock before and after receiving the message. The number of processes (machines) is fixed (equal to or larger than 3) and processes will not fail, join, or leave the distributed system.

**How to Use:**</br>
1. Open any Linux terminal and run the command "python3 master_node.py" to get the Master node running </br>
2. Open any Linux terminal and run the command "python3 node_A.py" to get the node A running </br>
3. Open any Linux terminal and run the command "python3 node_B.py" to get the node B running </br>
4. Open any Linux terminal and run the command "python3 node_C.py" to get the node C running </br>
5. Enter 1 to continue at Master node terminal. Enter the Sending node,recieving node and type the message to be sent when promted on the terminal </br>
6. Once done you can check the respective nodes about their vector clock printed before and after the said event happens along with the message </br>
