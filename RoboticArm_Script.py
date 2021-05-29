
#libraires
import RPi.GPIO as GPIO #import gpio library, set GPIO call as “GPIO”
import time # import timer library
import curses  # import curses (keyboard emulator)

#GPIO Set-up
GPIO.setmode(GPIO.BOARD) #set up gpio board
GPIO.setup(7,GPIO.OUT)  #set pin 7 as output
GPIO.setup(11,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(28,GPIO.OUT)

#curses setup
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(true)

#pulse set up
p = GPIO.PWM(i,50)  #pulse width modulation on pin i at 50hz
q = GPIO.PWM(7,50)
r = GPIO.PWM(11,50)

#code
try: 

p.start(7.5) # start pulse width modulation @ 7.5 pulse frequency

While True:
              char = screen.getch() 
                        if char == curses.KEY_END: #key end
                           break #end loop
                       
 elif char == curses.KEY_ENTER: #key enter
                                 if i = 18 {i = 122} # if gpio = 13, gpio = 15
                                time.sleep(1) # stop for 1 sec
                                if i = 22 (i = 27} #if gpio = 15, gpio = 13
                                 time.sleep(1) # stop for a second
                                  if i = 27 (i = 17} #if gpio = 15, gpio = 13
                                 time.sleep(1)
                                  if i = 17 (i = 18} #if gpio = 15, gpio = 13
                                 time.sleep(1)

             (this may cause problems as it may do all if the statements at once)
                   
 elif char == curses.KEY_LEFT: #key down
                           for j in range(1.5, 12.5, 1) #j range
                                q.ChangeDutyCycle(j) #change duty cycle up
                                 time.sleep(0.2) #sleep
                    
 elif char == curses.KEY_RIGHT: #key right
                                 
         for j in range(2.5, 12.5, 1) #j range
                                r.ChangeDutyCycle(j) #change duty cycle up
                                 time.sleep(0.2) #sleeps
                     
 elif char == curses.KEY_UP: # key up
                                for j in range(2.5, 12.5, 1) #j range
                                 p.ChangeDutyCycle(j) //change duty cycle up
                                 time.sleep(0.2) //sleep for .2 seconds
                   
 elif char == curses.KEY_DOWN: #key down
                                for j in range(12.5, 2.5, -1)  #j range
                                  p.ChangeDutyCycle(j) #change duty cycle down
                                  time.sleep(0.2) # sleep for .2 seconds



#end code
finally:

              p.stop(0) # stop pulse width modulation

             curses.nobreak(); 
             screen.keypad(0); 
             curses.echo()
             curses.endwin()
 
            GPIO.cleanup()
