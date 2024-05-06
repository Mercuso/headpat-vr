# HeadpatVR
Device that brings tactile feelings of VR head pats using mechanical force applied by brushes 
> [!WARNING]
> This project is in the development phase. Please note that components of the project are subject to frequent changes

## Introduction
Feel VR head pats in real life!  
This device monitors hand contacts with a head in VRChat and reproduces cuddles on a head in real life using brushes controlled by servo motors
![patbandvr](https://github.com/Mercuso/headpat-vr/assets/18481258/d4069ea7-765f-457f-817b-56fe676c67cd)

Inspired by a similar device that uses vibrating motors
Why another version?
I found vibrations on a head too unpleasant and decided to try to reproduce head pats in another way

### Project parts
**Server**  
This repository includes only the server application that should be launched on the PC along with VRChat. You can download the server source code and launch it by instructions in Setup->Server section. It doesn't have UI but provides useful logs to give you understanding of what's going on

**Firmware**  
The source code can be found [here](https://github.com/Mercuso/headpat-vr-esp). it is written based on Arduino framework. You need PlatformIO IDE to compile and upload it to your esp8266 controller

**Hardware**  
- 2 servo motors
- NodeMCU V3 board (or any other board with similar characteristics)
- wires
- fasteners
- the enclosure for ESP board and mountings for the headband
- power supply

## Setup

### Components

#### Microcontroller
By this moment, only NodeMCU v3 microcontroller was tested. However, the range of controllers that satisfy the requirements should be wider. It must be ESP8266 board that can handle power load from 2 servo motors

#### Servo motors
It's just a motor with the ability to control its position
You can read more about its basics here: https://docs.arduino.cc/tutorials/generic/basic-servo-control/
In this project, the SG90 motor is used. There are 2 motors needed - for the left and right side
Example from Aliexpress: https://www.aliexpress.com/item/1005005912678947.html?spm=a2g0o.detail.1000023.1.4e0bb941ZYbLUj

#### Wires
In theory, motors can be connected to the microcontroller pins directly, with their connectors. However, the wires are too short to place the microcontroller in a convenient position. Also, one of the motors can't be connected directly through the 3-pin connector because the board doesn't have enough pins with the required relative position to connect 2 motors at once. That's why, additional wires are needed. The *male-to-female dupont jumper wires* can be used to resolve this issue without soldering  
*servo extension cables* can be used to extend the servo motor wires

#### Case and mountings
To keep the microcontroller from damage, it must be secured in a plastic case that can be printed on an FDM printer. Also, few more parts are needed to mount the motors on the head. The 3D models of these parts can be downloaded from there **TODO: add the link to printables**

#### Fasteners
- M2x8 screw (4 items)
- M3x40 DIN912 screw (2 items)
- M3x8 DIN912 screws (8 items)

It's recommended to have spare parts for the case if something is damaged or missing

### Electronics assembly
Since there are only 3 electronic components, the wiring is simple
![schematics](https://github.com/Mercuso/headpat-vr/assets/18481258/794e9367-17cf-476d-b6db-dd63ba80cd55)

But since all 3 wires are joined in the connector, it's impossible to do proper wiring for the right motor just with its own wires without splitting them. It can be achieved with the help of the male-to-female dupont jumper wires - just connect them to the motor connector and then connect them according to the scheme to the corresponding board pins
If the microcontroller board is located far from the motors, few servo extension cables can be used - they use the standard male-female connectors, same as on motors

You can use a regular power bank for power supply by connecting the board to it via its micro USB port
The result should look like this:
![wiring](https://github.com/Mercuso/headpat-vr/assets/18481258/f810ad13-eb61-49cc-8d3f-76c8c9f1e18d)

### Building and uploading firmware
The documentation and source code of the firmware can be found [here](https://github.com/Mercuso/headpat-vr-esp)

### Server
Unfortunately, I haven't found how to build the executable file from the Python scripts at the moment. It will be done in the future. The only option for now - install the project dependencies manually and launch it from the Windows terminal  

First, make sure you have Python installed in your operating system. If not, you can find installation instructions here: https://www.python.org/downloads/windows/  
Download or clone this repository, navigate to its folder, right-click here, and select "Open in Windows terminal"  
From the terminal, execute the following command:
```powershell
Set-ExecutionPolicy -Scope Process
```
It will allow the execution of Python scripts  
Then, create the virtual environment folder for installing the project dependencies locally:
```powershell
python  -m venv .\.venv 
```
and activate it:
```powershell
.venv\Scripts\activate
```
Next step - install project dependencies:
```powershell
pip install -r requirements.txt
```
Now everything is ready for launching the server  
From the same terminal execute the following command:
```powershell
python server.py
```

After that, whenever you need to launch the server, you need to open a terminal from the same folder, execute the virtual environment activation command, and execute the script:
```powershell
Set-ExecutionPolicy -Scope Process
.venv\Scripts\activate
python server.py
```

### Preparing VRChat avatar
Follow the instructions described in the Patstrap project documentation's VRChat section:  
https://github.com/danielfvm/Patstrap?tab=readme-ov-file#vrchat

### Case and mountings assembly
> [!WARNING]  
> The case and mounting system is in active development. The 3D models will change soon

The latest assembly instructions can be found here:
- [NodeMCU case assembly](docs/MC_CASE_ASSEMBLY.md)
- [Head mount assembly](docs/HEAD_MOUNT_ASSEMBLY.md)
