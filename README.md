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

## Project parts
### Server
This repository includes only the server application that should be launched on the PC along with VRChat. The server communicates with VRChat application using OSC protocol (you can find more details about VRChat OSC [here](https://docs.vrchat.com/docs/osc-overview)) It doesn't have UI but provides useful logs to give you an understanding of what's going on

### Firmware  
The source code is available [here](https://github.com/Mercuso/headpat-vr-esp)  
The code is written based on Arduino framework

### Hardware
- 2 servo motors
- ESP-WROOM-32 38pin board
- esp-32 expansion board
- fasteners
- silicone brushes
- mount system for the motors
- mount system for esp-32 expansion board
- power supply

The detailed list of parts with description can be found [here](docs/PARTS.md)

## Setup

### Firmware
The documentation and source code of the firmware can be found [here](https://github.com/Mercuso/headpat-vr-esp)
You need PlatformIO IDE to compile and upload it to your esp32-based board  

### Hardware
Since there are only 3 electronic components, the wiring is simple
![wiring](https://github.com/user-attachments/assets/2473b2b2-1a3f-42c4-86a9-93c490f48358)

You can use a regular power bank as a power supply by connecting it to the expansion board. Make sure that the board jumper is in the right position (in the 5V position)  
This is the minimal device setup to do basic tests  

The motors with brushes and the board should be mounted on the VR headset with the help of additional printable plastic parts    
The latest assembly instructions can be found here:  
- [Controller board basement assembly](docs/MC_CASE_ASSEMBLY.md)
- [Motors mount assembly](docs/HEAD_MOUNT_ASSEMBLY.md)


### Server
The latets binary file can be downloaded from the [Releases](https://github.com/Mercuso/headpat-vr/releases) section
Alternatively, you can build it locally. Download repository, install python and execute the `build.bat` file. The executable file will be located in the `dist` folder

### Preparing VRChat avatar
Follow the instructions described in the Patstrap project documentation's VRChat section:  
https://github.com/danielfvm/Patstrap?tab=readme-ov-file#vrchat

### Settings in VRChat
[Enable OSC support in VRChat](https://docs.vrchat.com/docs/osc-overview#enabling-it)
