# network_port_scanner
This Python script is designed to perform TCP port scanning on a specified host or IP address. It utilizes 
the argparse library to accept command-line arguments and the nmap library for conducting the port 
scans. The script accepts two main arguments: the host IP address and a comma-separated list of ports 
to scan. It then iterates through the provided port list, attempting to identify the state (open, closed, 
filtered, etc.) of each specified port on the target host. The scan results are displayed, indicating the state 
of each scanned port. In case of an invalid argument or input error, the script gracefully handles 
exceptions and provides appropriate error messages. This script provides a basic foundation for 
conducting TCP port scans and can be further extended or integrated into larger network security or 
monitoring tools.

###CLI COMMAND FOR RUNNING THE CODE:
## python scanner.py -o <host_ip_address> -p <port_list>

##### *If not in root directory, use cd command to change the directory where the script is stored
