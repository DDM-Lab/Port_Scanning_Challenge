# Port Scanning Challenge

This challenge simulates a real-world port scanning and connection exercise, where you need to identify open ports, connect to them, and retrieve encoded data fragments to reconstruct a hidden flag.

In this walkthrough you have two files:
1. This file `walkthrough.md`
2. The solver `solver.py`

## Overview

In this CTF challenge, you'll act as a penetration tester conducting port scanning on a target system. Your goal is to:
1. Scan for open ports
2. Connect to specific ports to retrieve encoded flag fragments
3. Combine and decode these fragments to reveal the final flag (a hidden image)

The challenge simulates common network reconnaissance techniques used in ethical hacking and security assessments.

## Step-by-Step Instructions

### 1. Scanning for Open Ports

1. Once the challenge starts, type the `scan` command to identify open ports:
   ```
   Enter command: scan
   ```
2. You'll see output similar to an Nmap scan, showing several open ports with associated services.
3. Make note of these ports - these are your potential targets.

### 2. Connecting to Ports

1. Connect to an open port using the `connect` command followed by the port number:
   ```
   Enter command: connect PORT_NUMBER
   ```
2. Upon successful connection, you'll receive an encoded fragment of the flag.
3. You need to connect to 4 different ports to collect all fragments.
4. Use the `status` command at any time to check your progress:
   ```
   Enter command: status
   ```

### 3. Collecting All Fragments

1. Continue connecting to different open ports until you've collected all 4 fragments.
2. Each successful connection will give you a base64-encoded fragment like:
   ```
   [+] Encoded part X of 4 found: iVBORw0KGgoAAAANSUhEUgAAAhYAA...
   ```
3. The challenge will output a file: `fragments.txt` with all the four fragments.

### 4. Decoding the Flag

1. Once you've collected all 4 parts, you'll need to edit the `solver.py` file:
   - Open `solver.py` in your favorite text editor
   - Replace `FIXME` with the full encoded message (all 4 fragments combined in correct order from the `fragments.txt`)
   - Fix the base64 decoding line (hint: what's wrong with the `decoded_once = base64.b64decode(FIXME)` line?)

2. Run the solver script:
   ```
   python solver.py
   ```

3. If successful, the script will decode the base64 data and save it as `decoded_image.png`
4. Open the image to reveal the final flag!

### 5. Submitting Your Result

1. Create a file named `ports_challenge.txt` and copy/paste the Qualtrics information into this file.
1. Upload `ports_challenge.txt` to Qualtrics to receive credit for completing the challenge.
2. Submit the flag to Qualtrics.


## Understanding the Solution

### Port Scanning

Port scanning is a technique used to identify open ports on a target system. In real-world scenarios:

- **Open ports** indicate running services that could potentially be exploited
- **Service identification** helps attackers determine what software is running on the target
- **Port selection** matters, as standard/well-known ports (like 80, 22, 443) often reveal more about a system than obscure ports

This challenge simulates a simplified version of `nmap`, a powerful port scanning tool used by security professionals.

### Base64 Encoding

The flag fragments you collect are encoded using Base64:

- **Base64** is an encoding scheme that converts binary data to ASCII text format
- It's commonly used to transmit binary data over text-based protocols
- It's not encryption - just a way to represent binary data using printable characters
- The `+`, `/` and `=` characters are common indicators of Base64-encoded data

In this challenge, the encoding is used to:
1. Split the original data (an image) into 4 parts
2. Convert each binary part into text that can be displayed in the terminal
3. Require you to reconstruct and decode the data to reveal the hidden image


## Learning Objectives

After completing this challenge, you should be able to:

1. **Understand port scanning** concepts and how to interpret scan results
2. **Recognize the importance** of service identification in security assessments
3. **Identify Base64-encoded** data and understand how to decode it
4. **Apply Python programming** skills to solve encoding/decoding problems
5. **Appreciate how binary data** (like images) can be transmitted as text

## Additional Resources

- [Base64 Encoding Explained](https://en.wikipedia.org/wiki/Base64)
- [Python Base64 Documentation](https://docs.python.org/3/library/base64.html)


## Troubleshooting

If you're having trouble with the solution:
- Double-check that you've correctly copied everything correctly from  `fragments.txt`
