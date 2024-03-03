import argparse
import nmap
def argument_parser():
    parser = argparse.ArgumentParser(description = "TCP port scanner. accept a hostname/IP address and list of ports to scan. Attempts to identify the service running on a port.")
    parser.add_argument("-o", "--host", nargs = "?", help = "Host IP address")
    parser.add_argument("-p", "--port", nargs = "?", help = "comma-separation port list, such as '25,80,8000'")

    var_args = vars(parser.parse_args())
    return var_args
def nmap_scan(host_id, port_num):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(host_id, port_num)
    state = nm_scan[host_id]['tcp'][int(port_num)]['state']
    result = ("[*] {host} {tcp/port} {state}".format(host = host_id, port = port_num, state = state))
    return result
if __name__ == "__main__":
    try:
        user_args = argument_parser()
        host = user_args["host"]
        ports = user_args["ports"].split(",")
        for port in ports:
            print(nmap_scan(host, port))
    except AttributeError:
        print("Error, please provide the command_line_argument before running")