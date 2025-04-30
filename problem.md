# Port Scan

- Namespace: picoctf/research
- ID: port-scan
- Type: custom
- Category: General
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Description

Identify and connect to 4 open ports on the target system.
Each successful connection will reveal part of the encrypted flag.

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`


## Hints

- You can use the walkthrough provided in the Qualtrics survey

## Solution Overview

The provided text is PNG, which has been converted to base64 format

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

Identify various kinds of encoding.

## Tags

- python

## Attributes

- author: DDM Lab
- organization: picoCTF
- event: DDM LAB Research
