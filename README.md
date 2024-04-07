# rfc3442-dhcp-option-121
Classless DHCP Route Option 121 Calculator

# Introduction
This Python Generator Script is based on this [GitHub Gist](https://gist.github.com/TheTechromancer/bf389d6bdabc7fd8355af6caa122fa5f) from [@TheTechromancer] (https://github.com/TheTechromancer).

The Default Gateway is added BEFORE all other entries, according to [this](https://www.medo64.com/2018/01/configuring-classless-static-route-option/) other RFC3442 Generator.

# Purpose
The purpose of DHCP Option 121 or Classless DHCP Static Routing is to push the Static Routes definition from the DHCP Server to the DHCP Client.

In this way, all DHCP Clients automatically receive the Static Routes Table from the DHCP Server, thus avoiding the need to manually define (and maintain) Static Routes on each and every single one of your Devices.

# Technical Explanation
A great technical explanation on how the DHCP Option 121 (according to RFC3442) is generated can be found on the [OPNSense Forum](https://forum.opnsense.org/index.php?topic=1972.0).

**Important** Only **ONE** single entry of DHCP Option 121 must be entered into PFSense/OPNSense/etc DHCP Server.
Therefore make sure you add **ALL** the required networks/gateways in the array at the start of `generator.py` before you generate your entry.

# Usage
Clone the Repository:
```
git clone https://github.com/luckylinux/rfc3442-dhcp-option-121.git
cd https://github.com/luckylinux/rfc3442-dhcp-option-121
```

Edit `routes.py` using your preferred text editor and enter **all** the required routes.

For instance using `nano`:
```
nano routers.py
```

Now run the Generator:
```
# Make the File executable - Normally it should already be executable
chmod +x generator.py

# Run the Generator
./generator.py
```

# Setup in your Router
## OPNSense
![image](https://github.com/luckylinux/rfc3442-dhcp-option-121/assets/7126291/4aaa5dbc-076f-466f-b427-e8a0d644350f)

## PFSense
(Feel free to submit a PR)

## Ubiquiti
(Feel free to submit a PR)

## Mikrotik
(Feel free to submit a PR)

# References and Existing Tools
Several RFC3442 DHCP Option 121 Calculators / Generators can be found online.

A quick search on Google Points to some of them, which I list below.
Note that, except the code from , NONE of this was tested by me !

- Javascript
  - https://www.medo64.com/2018/01/configuring-classless-static-route-option/
  - https://github.com/FrayedString/rfc3442
- PERL
   - https://github.com/oldengremlin/route-4-dhcp
- Python
   - https://gist.github.com/TheTechromancer/bf389d6bdabc7fd8355af6caa122fa5f
   - https://github.com/beckit/DHCP_121_macOS
