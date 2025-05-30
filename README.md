# DDoSerX

DDoSerX is a high-performance network traffic tool designed to send large volumes of UDP packets to a specified target. It supports IP spoofing to simulate distributed traffic sources and is optimized for environments such as OVH servers. This tool can be used for network stress testing and performance evaluation under heavy load conditions.

## Features

- High throughput UDP packet sender  
- Supports IP spoofing for traffic source diversification  
- Configurable target IP, port, packet size, and duration  
- Optimized for large-scale traffic generation  
- Simple command-line interface  

## Requirements

- Linux-based system (recommended)  
- Root privileges to enable raw socket operations and IP spoofing  
- Python 3.x (or relevant runtime depending on your script)  

## Installation

Clone this repository:

```bash
git clone https://github.com/stenlykaelan/ddoserx.git
cd ddoserx
python3 ddoserx.py
