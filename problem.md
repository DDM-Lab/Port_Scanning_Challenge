# Collect the fragments

- Namespace: picoctf/research
- ID: port-scan-treatment
- Type: custom
- Category: General
- Points: 1
- Templatable: yes
- MaxUsers: 1

## Description

Identify and connect to 4 open ports on the target system.
Each successful connection will reveal part of the flag.
The flag seems too long, though. Can you write a Python script that is able to
decode the flag and saves it with the appropriate extension?

**NOTE: Do not close the Qualtrics survey.**

## Details

Connect to the program with netcat:

`$ nc {{server}} {{port}}`

**NOTE: Do not forget to save the Qualtrics data along with the flag!**


## Hints

- If you concatenate all fragments, you will be able to identify their encoding format.
- How should you open the final file?
- Use the walkthrough provided in the Qualtrics survey

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
- event: picoCTF Experimental Problems 1
