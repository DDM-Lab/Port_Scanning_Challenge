# Port Scan

- Namespace: picoctf/examples
- ID: port-scan
- Type: custom
- Category: General
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Description

This service can provide you with a random number, but can it do anything else?

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`


## Hints

- Can you point the program to a function that does something useful for you?

## Solution Overview

Enter 'win' as the input to the program

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

Examining source code to identify functionality

## Tags

- python

## Attributes

- author: DDM Lab
- organization: picoCTF
- event: DDM LAB Research