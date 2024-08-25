# HeadpatVR
Device that brings tactile feelings of VR head pats using mechanical force applied by brushes 
> [!WARNING]
> This project is in the development phase. Please note that components of the project are subject to frequent changes

## Introduction
Feel VR head pats in real life!  
This device monitors hand contacts with a head in VRChat and reproduces cuddles on a head in real life using brushes controlled by servo motors
![device_preview](https://github.com/user-attachments/assets/33619470-76d3-4ab6-b97f-7be217b56698)

Inspired by a [similar project that uses vibrating motors](https://github.com/danielfvm/Patstrap)
Why another version?
I found vibrations on a head too unpleasant and decided to try to reproduce head pats in another way

### Project parts
**Server**  
This repository includes only the server application that should be launched on the PC along with VRChat. You can download the server source code and launch it by instructions in Setup->Server section. It doesn't have UI but provides useful logs to give you an understanding of what's going on

**Firmware**  
The source code can be found [here](https://github.com/Mercuso/headpat-vr-esp). it is written based on Arduino framework. You need PlatformIO IDE to compile and upload it to your esp8266 controller

**Hardware**  
- 2 servo motors
- ESP-WROOM-32 38pin board
- esp-32 expansion board
- fasteners
- basement for the motors
- basement for esp-32 expansion board
- power supply

**Plastic parts**  
The parts for mounting controller board and motors can be printed on FDM printer. The 3D models can be found [here]()

## Setup

### Components

#### Microcontroller
The printable parts for mounting controller are developed for ESP-WROOM-32 38pin expansion board. The key feature of the expansion board is 3 rows of pins where 2 of them are 5v and gnd pins, and the 3-rd one is the pin from the board. It allows to easily connect servo motors without any soldering
The firmware is also written for ESP-32 based boards
However, the range of compatible controllers should be wider. The mounting parts and harware for ESP-8266 based board may be added in future

#### Servo motors
It's just a motor with the ability to control its position. 
You can read more about its basics here: https://docs.arduino.cc/tutorials/generic/basic-servo-control/. 
In this project, the TowerPro SG90 motor is used. You can find its specs here: https://www.towerpro.com.tw/product/sg90-analog/. 
There are 2 motors needed - for the left and right side. 

#### Case and mountings
It's recommended to use BOBOVR M3 Pro headset strap since it has a rigid frame that allows to fix additional devices on it  
The ESP-WROOM-32 38pin expansion board can be mounted on the front part of it  
The motors can be mounted on the top part of the frame  
The 3D models of these parts for mounting controller and motors can be downloaded from there **TODO: add the link to printables**

#### Fasteners
- M2x5 screw (2 items), M2 nuts (2 items)  
- M3x10 DIN912 screw (5 intems), M3 nuts (5 items)  
- M3x20 DIN912 screw (2 intems), Heat-Set Inserts (2 items) or M3 nuts (2 items)  

It's recommended to have spare parts for the case if something is damaged or missing

### Electronics assembly
Since there are only 3 electronic components, the wiring is simple
![wiring](https://github.com/user-attachments/assets/2473b2b2-1a3f-42c4-86a9-93c490f48358)

You can use on-board BOBOVR battery or a regular power bank as a power supply by connecting it to the expansion board. Make sure that the board jumper is in the right position (in the 5V position)

### Building and uploading firmware
The documentation and source code of the firmware can be found [here](https://github.com/Mercuso/headpat-vr-esp)

### Server
The latets binary file can be downloaded from the [Releases](https://github.com/Mercuso/headpat-vr/releases) section
Alternatively, you can build it locally. Download repository, install python and execute the `build.bat` file. The executable file will be located in the `dist` folder

### Preparing VRChat avatar
Follow the instructions described in the Patstrap project documentation's VRChat section:  
https://github.com/danielfvm/Patstrap?tab=readme-ov-file#vrchat

### Case and mountings assembly
> [!WARNING]  
> The case and mounting system is still in development. The 3D models may change soon

The latest assembly instructions can be found here:
- [Controller board basement assembly](docs/MC_CASE_ASSEMBLY.md)
- [Motors mount assembly](docs/HEAD_MOUNT_ASSEMBLY.md)
