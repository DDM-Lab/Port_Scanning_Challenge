# File Download

- Namespace: picoctf/research
- ID: file-download-ecc
- Type: custom
- Category: General Skills
- Points: 1
- Templatable: no
- MaxUsers: 0

## Description

Identify and connect to 4 open ports on the target system.
Each successful connection will reveal part of the encrypted flag. 

## Details
Connect to the program with netcat:

$ nc {{server}} {{port}}


## Hints

- You can use the walkthrough

## Solution Overview

Just XOR the two provided chipher text, then XOR with the known plain text to get the flag.

## Challenge Options

```yaml
cpus: 0.5
memory: 128m
pidslimit: 20
ulimits:
  - nofile=128:128
diskquota: 64m
init: true
```

## Learning Objective

Identify different kinds of encoding.

## Attributes

- author: DDM LAB
- organization: picoCTF
- event: DDM LAB Research Study