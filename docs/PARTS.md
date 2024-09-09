# Parts list

## Electronics


| Component       | Model name    | Quantity | Link                                                                                             | Comments                 |
| --------------- | ------------- | -------- | ------------------------------------------------------------------------------------------------ | ------------------------ |
| Servo motor     | TowerPro SG90 | 2        | [SG90 9g Servo Tower Pro Micro Servo](https://www.aliexpress.com/i/1005004508427060.html)        | Didn't buy it from there |
| Board           | ESP-WROOM-32  | 1        | [AliExpress ESP32 38PIN](https://www.aliexpress.com/item/1005005970816555.html)                  |                          |
| Expansion board |               | 1        | [AliExpress ESP32 Expansion board 38PINS](https://www.aliexpress.com/item/1005006176546785.html) |                          |
| Power supply    | BOBOVR B2     | 1        | [Official store BOBOVR B2 Battery Pack](https://www.bobovr.com/products/b2)                      |                          |


### Components breakdown

#### Servo motor
This type of servo motor is widely used for RC models and DIY Arduino-based projects  
I bought it from a local supplier and the price was even lower than on global online retail websites 

There are a lot of manufacturers that produce this type of servo motor.   
Recommended manufacturer - TowerPro  
The required characteristics are:  
Operating Angle: 120 - 180 degrees  
Power supply: 4.8 - 6 V  
Weight: 9g  
Control System: Analog  
Dimentions: can be found [here](https://www.towerpro.com.tw/product/sg90-analog/) in the product description  

The current consumption heavily depends on the load - it is high at the start of the moving cycle and when it meets an obstacle  
The official documentation doesn't say anything about the highest level of it, but the Arduino tutorial mentions that the current for this kind of motor can reach up to 800 mA  

#### Microcontroller board
Development kit built based on ESP-WROOM-32 module, provides a pepripherial that includes 38 pins for connecting external devices  
In theory, it can be used without expansion board and with less number of pins, but it will require a soldering to properly connect the servo motors  

#### Expansion board
Additional board which purpose is to expand the number of pins to easily connect servo motors without any soldering  

#### Battery
BOBOVR battery is chosen just because it is already included into the BOBOVR straps system, it outputs 5V 2A which is enough to supply 2 motors (up to 1600mA) and microcontroller board (don't know the exact number, but should be less than 400mA). It can be replaced with any other battery that has the same power

## Brushes
The easiest option I found is to buy the device that already has silicone brushes, take them off and print the adapter to attach them to the servo motor lever  
Link to the device: https://www.aliexpress.com/item/1005005692082758.html  
The brushes can be easily removed without damaging anything, so this device remains operational  
If you found the similiar silicone brushes that can be bought standalone - please let me know!  

## Printable parts
The following parts can be printed on FDM printer:

| Part codename         | Quantity |
| --------------------- | -------- |
| controller_base       | 1        |
| controller_base_hooks | 2        |
| servo_mount_clip      | 2        |
| servo_mount           | 2        |
| servo_lever_adapter   | 2        |

Recommended material - PLA  
These parts can be downloaded from here: https://www.printables.com/model/992952-headpatvr-printable-parts  
It's recommended to use files in STEP format if your slicer supports it. This format ensures the better precision  

## Fasteners

| Type                | Quantity |
| ------------------- | -------- |
| M3x10 DIN 912 screw | 6        |
| M3x20 DIN 912 screw | 2        |
| M2x8 DIN 7985 screw | 2        |
| M3 DIN 934 nut      | 8        |
| M2 DIN 934 nut      | 2        |


Screws and nuts are standard and widely used components, can be easily found in shops that sell building materials and fasteners
It's recommended to buy fasteners made of a stainless steel or with zinc plating
