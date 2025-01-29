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

  
Thoughs:
- Instead of "Port 1 is not open or hasn't been scanned yet," we could specify, "Port 1 is closed or invalid. Use the 'scan' command to identify open ports."
- Should we say "part 1 of 4" so participants know the flag is divided into four parts
- Maybe show when a milestone is achieved (e.g., "You found all encoded parts!")
- We're not outputting if participants have tried multiple ports repeatedly and even if they attempted invalid ports. Maybe we don't need to add this, something to discuss
- Should we output the time that participants spent doing the problem?

## Control and treatment conditions:

Control Condition: All options are presented in a randomized order but consist solely of default port numbers, allowing researchers to observe decision-making in the absence of alternative choices.
Treatment Condition: All options are presented in a randomized order, with half being default port numbers and the other half non-default port numbers, enabling measurement of the preference for defaults. 

### Example output:

```
Challenge complete. Thanks for participating!
Ports connected: [80, 443, 65432, 8080]
Please copy the order of the ports
Total unique ports connected: 4
```
