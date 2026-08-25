# scapad
> a custom macropad made by me with hackclubs hackpad guide (link in the credits below)

# What it does
this macropad has 3 buttons:

| Physical key | PCB Switch | XIAO PIN | ACTION |
|--------------|------------|----------|--------|
| 0            | SW1        | D10      | COPY (Ctrl+C) |
| 1            | SW2        | D9       | PASTE (Ctrl+P) |
| 2            | SW3        | D8       | UNDO (Ctrl+Z) |

# Schematic (wiring)
### The Schematic is simple you just connect one side of each switch to gnd and the other side to the XIAO PIN that it belongs to

<img width="988" height="527" alt="image" src="https://github.com/user-attachments/assets/06db5a02-214d-47f7-acf7-ee87bcca0335" />

# Pcb Preview 

<img width="552" height="510" alt="Screenshot 2026-08-24 191812" src="https://github.com/user-attachments/assets/60d891aa-4225-4b24-af61-711f7fa59eb2" />

# Hardware
Here is the list of the components needed

•Seeed Studio XIAO SAMD21

•Any MX-style mechanical switch *3

•Custom PCB

•Custom Case

•USB-C connection

# FIRMWARE
the firmware is writen in python by using the keyboard-optimized CircuitPython build for the XIAO SAMD21.
Recommended version:
CircuitPython 10.2.1 — XIAO SAMD21 Keyboard Optimized
DOWNLOAD:
### [HERE](https://circuitpython.org/board/seeeduino_xiao_kb/)

### INSTAL FIRMWARE
## 1st step
Intall CircuitPython
## 2nd step
Put the XIAO into bootloader mode by using its reset procedure, then copy the downloaded `.UF2` file to the bootloader drive.
After it restarts, a drive named `CIRCUITPY` should appear.
## 3rd step
Copy `code.py`
Copy:
```text
firmware/code.py
```
to the root of the `CIRCUITPY` drive:
```text
CIRCUITPY/
└── code.py
```
CircuitPython will automatically run the file.
## Code preview
<img width="354" height="446" alt="image" src="https://github.com/user-attachments/assets/dece1582-a135-4775-a9a3-cb625c287d23" />

# CASE (not required to work)
The case is purely for design and protection reasons
You can download my version of the case from here 
```text
CAD/scapadv2.step
```
or
```text
CAD/scapadv2.f3d
```
## Case preview
<img width="607" height="374" alt="image" src="https://github.com/user-attachments/assets/d2382e5d-2d8b-471e-a4c8-f78757d8ce5d" />

# IMPORTANT 
The project is specifically made for the XIAO SAMD21 and the PCB pin connections listed above.
Do not use the code.py if you are using a diffrent microcontroller or if you are using diffrent connection the code will need changes

# CREDITS
-[hackclub hackpad guide](https://hackpad.hackclub.com/guide) - helped with the case and pcb design

-[Open AI](https://chatgpt.com) - helped with the firmware





