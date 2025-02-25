# default-effect

# Port Scanner Challenge

This program simulates a port scanning challenge where users can scan for open ports, connect to them to reveal encoded parts, and ultimately analyze the complete encoded text to find a flag.

## Prerequisites

- Python 3.6 or higher
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
```
git clone https://github.com/saketh7502/default-effect.git
cd default-effect
```


## Running the Program

### Option 1: Running Directly

To run the program directly:
```
python port_scanner_challenge.py
```


### Option 2: Using Docker

1. Build the Docker image:
```
docker build -t default-effect .
```

2. Run the Docker container:
```
docker run -it default-effect
```

## How to Play

1. Use the `scan` command to scan for open ports.
2. Use the `connect <port>` command to connect to an open port and reveal an encoded part.
3. Once all parts are revealed, the program will prompt you to analyze the complete encoded text.
4. Use the `exit` command to quit the program


## Notes

- This is a simulated challenge and does not perform actual port scanning or network operations.
- The encoded text and port statuses are predetermined


## Control and treatment conditions:


Control Condition: The eight ports include four default ports and four non-default (user-defined) ports. The default ports are lesser-known defaults (e.g., not HTTP, SSH, or other widely recognized ports).
Treatment Condition: The eight ports also include four default ports and four non-default (user-defined) ports. However, in this condition, the default ports are well-known (e.g., HTTP, SSH, FTP).

All options should always be presented in a random order.

### Example output:

```
Challenge complete. Thanks for participating!
Ports connected: [80, 443, 65432, 8080]
Please copy the order of the ports
Total unique ports connected: 4
```


## Carolina's Feedback

- Instead of "Port 1 is not open or hasn't been scanned yet," we could specify, "Port 1 is closed or invalid. Use the 'scan' command to identify open ports."
- We don't have all of the ports (we should have 8)
- The output says I didn't try to connect to any invalid port, but I did.
- How are the control and treatment implemented? 
- Should we give more context at the beginning of the challenge? 