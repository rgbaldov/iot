# Activity 14: NS-3 Installation Guide for RPi OS

**Prepared by:**  

[Renann G. Baldovino, PhD](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/faculty-profile/renann-baldovino/)  
**[Department of Manufacturing Engineering and Management, De La Salle University (DLSU)](https://www.dlsu.edu.ph/colleges/gcoe/academic-departments/manufacturing-engineering-management/)**

## 1. System Requirements

| Resource | Minimum | Recommended |
|-----------|----------|-------------|
| OS | Raspberry Pi OS (64-bit) | Raspberry Pi OS Bookworm 64-bit |
| RAM | 2 GB | 4 GB or more |
| Storage | 2–3 GB free | 5 GB+ |
| Compiler | `g++`, `python3`, `cmake` |
| Dependencies | `build-essential`, `git`, `mercurial`, `python3-dev`, `qtbase5-dev`, `libgtk-3-dev` |

---
## 2. Update System
```bash
sudo apt update && sudo apt upgrade -y
```
## 3. Install Required Packages
```bash
sudo apt install -y git build-essential cmake g++ python3 python3-dev \
                   qtbase5-dev libgtk-3-dev libxml2 libxml2-dev
```
## 4. Clone and Build NS-3
```bash
# Clone NS-3 repository
git clone https://gitlab.com/nsnam/ns-3-dev.git ns-3
cd ns-3
```
# Configure and build
```bash
./ns3 configure --enable-examples --enable-tests
./ns3 build
```
## 5. Test Installation
```bash
./ns3 run hello-simulator
```
