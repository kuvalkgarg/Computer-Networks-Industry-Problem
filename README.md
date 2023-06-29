#  Web Server Monitoring, Port Scanning and Fingerprinting Suite

## Description
This project consists of various network tools implemented in Python. It includes features such as fingerprinting using sockets, port scanning, and web server monitoring. These tools can be used to gather information about systems on a network, check the status of ports, and monitor changes on a specific web server.

## Languages and Frameworks/Libraries
The project is implemented in **Python**. The following libraries are utilized:

**socket:** Used for socket programming to establish network connections and perform fingerprinting.
**hashlib:** Used for generating hashes of web server content.
**urllib:** Used for sending HTTP requests and retrieving web server content.

## Installation and Execution
Clone the repository to your local machine.
Ensure you have Python installed (version 3.0 or above).
Install the required dependencies by running the following command:
```
pip install hashlib
```
Open a terminal or command prompt and navigate to the project directory.
Run the Python script by executing the following command:
```
python network_tools.py
```
## Setup
Fingerprinting using Sockets:
Modify the **target_host** and **target_port** variables in the source code to specify the host and port you want to fingerprint.
Run the script and observe the output, which will display the information of the system and services running on the open ports.

Port Scanner:
When prompted, enter the host you would like to scan for open ports.
The script will scan a range of ports and display whether each port is open or closed.
Additionally, you can enter a specific port number to scan individually.

Web Server Monitoring:
Modify the **url** variable in the source code to specify the website you want to monitor.
Run the script, and it will periodically check the website's content hash for changes.
If any changes are detected, it will notify you and provide the updated content hash.

## Conclusion
This project provides a set of network tools implemented in Python. By utilizing socket programming, port scanning, and web server monitoring, it offers functionalities to gather system information, check port statuses, and monitor web server content changes. Feel free to explore and customize the tools according to your specific needs.
