# FlagScanner
FlagScanner is a versatile Python-based port scanning utility designed for exploring target hosts using an array of TCP flags, which includes SYN, FIN, NULL, XMAS, and ACK. With a command line interface, this tool is an indispensable asset for network administrators, security enthusiasts, and anyone interested in the intricacies of port scanning and network analysis.

Here's a more refined description for each scan technique:

**SYN Scan:**
The SYN scan, often referred to as a half-open scan, sends a TCP SYN packet to the target port. When an open port is encountered, the target host responds with a SYN-ACK packet. This technique is known for its stealthiness and its ability to reveal open ports without completing the full three-way handshake.

**FIN Scan:**
The FIN scan dispatches a TCP FIN packet to the target port. If the port is open, it typically responds with an RST (reset) packet. It's a useful method for determining whether a port is closed without establishing a full connection.

**NULL Scan:**
The NULL scan sends a TCP packet with all flags set to 0 to the target port. When dealing with an open port, it often remains unresponsive. This scan is valuable for identifying ports that may not have active services running.

**XMAS Scan:**
The XMAS scan transmits a TCP packet with the FIN, URG, and PSH flags set to the target port. If the port is open, it may respond in a distinct manner, revealing its state. This method is ideal for distinguishing between open and closed ports.

**ACK Scan:**
The ACK scan sends a TCP ACK packet to the target port. It is commonly used to detect the presence of a firewall or identify filtered ports. If the port is open, it might respond with a RST packet.

**Here is an image illustrating how FlagScanner looks and how to use it:**
![image](https://github.com/glassesman1/FlagScanner/assets/73016511/48297688-087a-4af6-9c42-43cee21d2937)

- Enter the target domain name or host IP address.
- Specify the ports you want to scan. You can enter individual ports like 80 and 443 (80,443), or define a range of ports like 1-1000.
- Enter the scanning flags you wish to use, separated by spaces (e.g., SYN NULL ACK).
- In case some ports do not respond, the tool will display a message indicating the "Ports that did not respond: []."
