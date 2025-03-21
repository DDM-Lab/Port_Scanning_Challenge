# Port Scanning Challenge

A cybersecurity educational challenge that simulates port scanning and connection in a CTF-style environment.

## Overview

This challenge teaches participants about port scanning and service enumeration in a controlled environment. Participants must find open ports on a simulated server, connect to them, and collect encoded flag fragments. The challenge is designed to be educational while maintaining the authentic feel of a CTF competition.

## Key Features

- Realistic nmap-style scan output
- Service-specific connection responses
- Encoded flag fragments distributed across ports
- Two experimental conditions (control/treatment)
- Progress milestones and CTF-style feedback

## Challenge Objective

Participants need to:
1. Scan for open ports on the target system
2. Connect to any 4 of the 8 discovered ports
3. Collect encoded flag fragments
4. Decode the flag (outside the challenge)

## Experimental Conditions

The challenge features two conditions that can be toggled with command-line arguments:

1. **Control Condition**: The eight ports include four lesser-known default ports (e.g., SMTP, DNS, POP3, IMAP) and four non-default (user-defined) ports.

2. **Treatment Condition**: The eight ports include four well-known default ports (e.g., HTTP, SSH, FTP, HTTPS) and four non-default (user-defined) ports.

All options are presented in random order during the scan.

## Flag System

- Each successful port connection reveals part of an encoded flag
- Participants need to connect to any 4 ports to collect all flag fragments
- The encoded flag is split into 4 equal parts
- Milestone messages appear after finding the first and last parts
- A hint about base64 decoding is provided upon completion

## Setup and Running

### Requirements
- Python 3.6+

### Running the Challenge

Basic usage:
```bash
python port_scanning_challenge.py
```

With options:
```bash

# Run in control condition 
python port_scanning_challenge.py 


# Run in treatment condition (well-known ports)
python port_scanning_challenge.py --treatment

# Run with debug information
python port_scanning_challenge.py --debug

# Run treatment with debug information
python port_scanning_challenge.py --treatment --debug
```

## Available Commands

During the challenge, participants can use the following commands:
- `scan` - Scan for open ports
- `connect <port>` - Connect to a specific port
- `status` - Display current progress
- `help` - Display help message
- `exit` - Exit the challenge

## Challenge Flow

1. The participant starts by running a scan to discover open ports
2. For each port they connect to, they receive a fragment of the encoded flag
3. After connecting to 4 ports, they have the full encoded flag
4. They receive a hint about decoding the base64-encoded flag
5. Challenge is completed after collecting all 4 fragments

## Error Messages

The challenge provides helpful feedback when:
- Attempting to connect to closed or unscanned ports
- Specifying invalid port numbers
- Using incorrect command syntax

## Scoring and Data Collection

At the end of the challenge, a summary is shown with:
- Ports connected
- Total unique ports connected
- Total ports attempted
- Number of flag fragments collected

This information can be used for research or educational assessment.

## Developer Notes

You can modify the challenge by:
- Changing the encoded flag in the `generate_flag_parts()` method
- Adjusting the ports in the control and treatment conditions
- Adding more service-specific responses for different port types