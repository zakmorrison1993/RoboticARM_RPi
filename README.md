# RoboticARM_RPi-Python

This project uses a Raspberry Pi 3 Model B+	(2.5A)


Currently this doesn't work!

There are inconsistencies with code and schematics!!


Example of:

- Use of libraries

- Loop 'For' statements

- RPi knowledge

- Basic circuitry knowledge



Appendix A: First example build - Failed :






![image](https://user-images.githubusercontent.com/84570199/120076705-e12b2900-c09e-11eb-9656-dea38d5969b0.png)



Critism of Appendix A:

- This was my first (robotic) python script

- Structural integrity made from cardboard - not good

- Ampage too powerful for RP 3+ more suited for RP 4

- No hand, difficulty develop structure.

- Rushed project


As you can see the Arm has four Servo units controlling joints/wrist and hand. there is an H bridge that feeds a DC 3V motor that allows the Arm to move 360 degrees. This also has LM2596 which reduces the voltage for the motor. This is my first proper schematic and realise later a Voltage Divider may have been more efficient.

This all goes to an RPi 3B however, as mentioned before, the Amps are too high for that and according to documentation fits an RPi 4 better. However, it is possible to reduce the amp for different RPi devices. The diode connecting it to power is to reduce voltage to 5V for the RPi



APPEDNIX B: Second Hand Build - To be Completed :


