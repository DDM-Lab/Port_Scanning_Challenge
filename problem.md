# PORT Scanning

- Namespace: picoctf/research
- ID: port-scanning
- Type: custom
- Category: General
- Points: 1
- Templatable: no
- Max Users: 1

## Description
Identify and connect to 4 open ports on the target system.
Each successful connection will reveal part of the encrypted flag.

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
## Attributes

- author: DDM Lab
- organization: picoCTF
- event: S-25 ddmlab reseach study
