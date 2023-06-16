# Cli Application 
This application wraps around the nmap port scanner using asyncio.
2 files are passed to the input of the python script:
1. List of 10 random IP addresses
2. List of 10 arbitrary ports
- It runs an nmap scan (with default configuration which scans the top 1000 most used ports on an IP address)
- Parses the output of nmap -a (determines which ports are open, which are closed)
- Outputs the result to the console in json format
