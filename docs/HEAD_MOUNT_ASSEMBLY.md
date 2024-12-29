# Head mount assembly

## Tools
For this assembly, you need the following tools:  
- Screwdriver  

## Parts
Check the complete parts list with detailed description and where to find them in the [PARTS documentation](PARTS.md)  

For this step, you need the following plastic parts:
- servo_mount (x2)
- servo_mount_clip (x2)
- servo_lever_adapter (x2)

Fasteners:
- M2x8 screws (x2)
- M2X20 screws (x2)
- M2 nuts (x2)

Electronics:
- Micro Servo sg90 servo motor kit (x2)
- ESP-WROOM-32 38pin board
- esp-32 expansion board

Other:
- silicone brush (x2)
- torsion spring (x2)

## Assembly

### Clip preparation
Prepare the torsion spring for inserting it into the servo mount clip  
Bend the torsion spring legs and cut off the tips to the size as it is shown on the picture below
> [!WARNING]
> Be careful while cutting off the tips. They can fly away in unpredictable directions and damage your eyes  

Insert M2 nut into the servo mount clip  
Use screw to simplify this process. The nut hole is stiff, do not afraid to use force to insert it

Insert the spring into the servo mount clip  

Align servo mount holes with servo mount clip hole as shown on the picture, the torsion spring leg should come into the servo mount groove

Join parts with M2X20 screw. Make sure that screw came out into the servo mount hole from the opposite side. Be careful at this moment - if holes are not aligned, the screw can break the bracket  
Do not overtighten the screw. The parts should move freely

Repeat the same steps with another servo mount system

### Clip mounting
put the plastic clip to the upper part of the headset strap system

insert the screw from the bottom  
Tighten the screw  
> [!WARNING]
> Be careful, don't damage the headset lenses!

![servo-mount-step-1-2](https://github.com/user-attachments/assets/9143aaf4-5f21-4ac7-93cd-9a43287ea648)
![servo-mount-step-1-3](https://github.com/user-attachments/assets/d51cf17d-2677-46df-8542-f41b150570b8)


Do the same on the opposite side

### Servo motors preparation
This step assumes that the firmware is already uploaded on the ESP-32 board  
Before fixing servo motors in servo mounts, the motors should be calibrated and then the levers should be fixed in correct position  

connect motors to the extension board as shown on the picture. The corresponding line of pins is closer to the side where the motor should be placed  
Then connect power supply to the board or reload it if it is already connected. The motors shafts should move to the default position once board connected to WiFi network

Put the lever adapter to the lever
![servo-mount-step-1-10](https://github.com/user-attachments/assets/2ade0d75-eb10-4c16-8df8-7f4d59f38bf8)

Put the lever to the motor shaft in postion as shown on the picture
The picture shows the lever position for the left side (right side if you look to a headset from front)

You can test the lever movement usiing web UI testing tool. Make sure that the lever left and right extreme positions are simmetric

Adjust the lever position if needed

Fix the lever on the motor shaft using the small screw from the motor kit


### Fixing the servo motors in the servo mounts
Insert the motor to the motor mount as it is shown on the picture  
Pay attention to the motor shaft, it should be on the side that is opposite to the supports  

Use the screws to fix it. The screws should be included into the motor kit  

Put on the silicone brush

Repeat same steps for the opposite side

### Final result
