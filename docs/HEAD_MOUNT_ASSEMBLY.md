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

### Torsion spring preparation
This is the hardest part of the assembly. The torsion spring legs should be bent by 90 degrees angle as it is shown on the picture

![spring_dimensions](https://github.com/user-attachments/assets/f475abd2-5e5a-442e-8abd-ef8c4ab4f65a)

### Clip preparation

Insert M2 nut into the servo mount clip  
Use screw to simplify this process. The nut hole is stiff, do not afraid to use force to insert it

![servo_mount_clip_insert_m2_nut](https://github.com/user-attachments/assets/1f66ed0a-fc24-4836-a30b-e63923445708)

Insert the spring into the servo mount clip  
If the spring leg sticks over the side of the clip, cut it off  
> [!WARNING]
> Be careful while cutting off the spring tip. The piece can fly away in unpredictable directions and damage your eyes

![insert_torsion_spring_into_servo_mount_clip](https://github.com/user-attachments/assets/f78bd6d7-50f5-4dd2-9744-0685a4aa84fd)
![spring_insertion_result](https://github.com/user-attachments/assets/d3db099e-5fbb-41ed-95bf-a614342acbe7)

Align servo mount holes with servo mount clip hole as shown on the picture, the torsion spring leg should come into the servo mount groove
Cut off the part of the spring leg that sticks outside
> [!WARNING]
> Be careful while cutting off the spring tip. The piece can fly away in unpredictable directions and damage your eyes

![join_servo_mount_parts](https://github.com/user-attachments/assets/4f65fec5-5f62-4234-a5be-ca7b982ba9a1)

Join parts with M2X20 screw. Make sure that screw came out into the servo mount hole from the opposite side. Be careful at this moment - if holes are not aligned, the screw can break the bracket  
Do not overtighten the screw. The parts should move freely

![fix_servo_mount_parts](https://github.com/user-attachments/assets/dd5187e2-640b-4e42-80e9-b4a36666335c)

Repeat the same steps with another servo mount system

### Clip mounting
put the plastic clip to the upper part of the headset strap system

![clip_mount_s1](https://github.com/user-attachments/assets/1ae62a53-0527-4f06-a204-dc9ebe0c5c53)

insert the screw from the bottom  
Tighten the screw  
> [!WARNING]
> Be careful, don't damage the headset lenses!

![clip_mount_s2](https://github.com/user-attachments/assets/41b5acbe-54fb-4376-871d-402a4e173e7b)

Do the same on the opposite side

### Servo motors preparation
This step assumes that the firmware is already uploaded on the ESP-32 board  
Before fixing servo motors in servo mounts, the motors should be calibrated and then the levers should be fixed in correct position  

connect motors to the extension board as shown on the picture. The corresponding line of pins is closer to the side where the motor should be placed  
Then connect power supply to the board or reload it if it is already connected. The motors shafts should move to the default position once board connected to WiFi network

![connect_motors](https://github.com/user-attachments/assets/8329b4f5-1fb6-4b7a-9598-a5676660c201)

Put the lever adapter to the lever

![servo-mount-step-1-10](https://github.com/user-attachments/assets/2ade0d75-eb10-4c16-8df8-7f4d59f38bf8)

Put the lever to the motor shaft in postion as shown on the picture
The picture shows the lever position for the left side (right side if you look to a headset from front)

![lever_position](https://github.com/user-attachments/assets/d25366bb-54a8-46d6-a342-b4c56e8bdc52)

You can test the lever movement usiing web UI testing tool. Make sure that the lever left and right extreme positions are simmetric

Adjust the lever position if needed

Fix the lever on the motor shaft using the small screw from the motor kit

![fix_lever](https://github.com/user-attachments/assets/8b49d809-bfc5-44dc-818c-e0b755313c3a)

### Fixing the servo motors in the servo mounts
Insert the motor to the motor mount as it is shown on the picture  
Pay attention to the motor shaft, it should be on the side that is opposite to the supports  

![insert_motor](https://github.com/user-attachments/assets/e4d13483-400a-4a10-a3c3-ab0cf3f04375)

Use the screws to fix it. The screws should be included into the motor kit 

![fix_motor](https://github.com/user-attachments/assets/3f636ad9-7ab1-453e-bace-ef1880fb41d8)

Put on the silicone brush

![put_on_brush](https://github.com/user-attachments/assets/83e4d8c4-f8d3-428c-957f-8c610845ea83)

Repeat same steps for the opposite side

### Final result
![final_result_up](https://github.com/user-attachments/assets/5a97388b-4c72-4012-9e18-35af111299e0)
![final_result_profile](https://github.com/user-attachments/assets/d0c5ea6c-4eef-4e2c-9f93-af289d4918ae)
![final_result_front](https://github.com/user-attachments/assets/bdb409ea-2412-40c6-8525-c2140daa98bb)
