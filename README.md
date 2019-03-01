# Poetry-Printer

**IDEA:** Print out flash fiction on receipt paper so patrons have quick reading to-go. Extra cute!

**ITEMS NEEDED:** Thermal Printer, Raspberry Pi, code, button, database of poems.  

**PREP:** Set up CUPS on Pi, hook-up button, organize database. 

**STEPS:** Install Raspbian. Do: 

sudo apt-get update
sudo apt-get install libcups2-dev libcupsimage2-dev cups system-config-printer gcc
 
Wait a while for that all to process. Download these drivers, follow these instructions to get Star Micronics CUPS drivers. Set up printer in CUPS. Media size 72mmx30mm + fixed page length seems best for some reason. 20 characters per inch, 5.7 lines per inch. Job cancel after 10.

Find poems. Make them into plain-text files. Put them in a folder. These words make it go:

    #!/usr/bin/env python

    import os
    from time import sleep

    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN)
    GPIO.setup(24, GPIO.IN)

    os.system('sudo chown pi:pi /dev/usb/lp0')

    while True:

        if (GPIO.input(23) == False):    
        os.system('sh /home/pi/Desktop/PocketPoems/startup')        
        sleep(10);
        
    if (GPIO.input(24) == False):
     os.system('sh /home/pi/Desktop/PocketPoems/startup')
     sleep(10);
 

    #startup: a bash script for printing poems

    find ./ -type f -print0 | shuf -zn1 | xargs -0 cat | while read line 
    do
    echo $line > /dev/usb/lp0
    done
    sleep 1
    sudo echo -e  " \n\n\n\x1b\x64\x02" > /dev/usb/lp0
    COUNTER_FILE="counter.txt"
    count=`cat $COUNTER_FILE`
    ((count++))
    echo $count > $COUNTER_FILE
