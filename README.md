# default-effect

TODO: write a README with python version, and other relevant information to run this

Thoughs:
- Instead of "Port 1 is not open or hasn't been scanned yet," we could specify, "Port 1 is closed or invalid. Use the 'scan' command to identify open ports."
- Should we say "part 1 of 4" so participants know the flag is divided into four parts
- Maybe show when a milestone is achieved (e.g., "You found all encoded parts!")
- We're not outputting if participants have tried multiple ports repeatedly and even if they attempted invalid ports. Maybe we don't need to add this, something to discuss

### Example output:

```
Challenge complete. Thanks for participating!
Ports connected: [80, 443, 65432, 8080]
Please copy the order of the ports
Total unique ports connected: 4
```