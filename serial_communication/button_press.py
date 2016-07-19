import RPi.GPIO as GPIO
import time
import os
import subprocess
import shlex
import pygame
from pygame.locals import *
import sys

pygame.init()

#screen = pygame.display.set_mode((1080,760), pygame.FULLSCREEN)
screen = pygame.display.set_mode((1360,760), pygame.FULLSCREEN)
pygame.display.set_caption('Basic Pygame program')

# Fill background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))

font = pygame.font.Font("/home/pi/Swiss-911.ttf", 250) #single line font
font2 = pygame.font.Font("/home/pi/Swiss-911.ttf", 100) # temp/heart font
font3 = pygame.font.Font("/home/pi/Swiss-911.ttf", 75) # data font

butPin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    
    while True:
        input_state = GPIO.input(butPin)
        if input_state == False:

            background.fill((0, 0, 0))
        
            text = font.render("INSERT HAND", 1, (250, 250, 250))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            textpos.centery = background.get_rect().centery
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            time.sleep(2.0) 
        
            # Get temperature
            time.sleep(0.4)
            with open("/home/pi/BAYMAX/ScriptFiles/temperature.txt") as f:
                temperature = None
                for line in (line for line in f if line.rstrip('\n')):
                    temperature = line

            # Temperature Found
            temperature = temperature[:-2]
            print (temperature)
        
            background.fill((0, 0, 0))
        
            text = font.render("COLLECTING DATA", 1, (250, 250, 250))
            text2 = font3.render("DO NOT REMOVE HAND", 1, (250, 250, 250))
            #Do not remove hand
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            textpos.centery = background.get_rect().centery
            background.blit(text, textpos)
            background.blit(text2, (150, 500))
            screen.blit(background, (0, 0))
            pygame.display.flip()
            #time.sleep(15.0) 
       

        

            # Find Pulse
            os.system('./facesShellScript')

            #Remove Hand
            background.fill((0, 0, 0))
        
            text = font.render("REMOVE HAND", 1, (250, 250, 250))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            textpos.centery = background.get_rect().centery
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
            time.sleep(2.0) 

            pulse = "Processing"
            #Display vitals
            background.fill((0, 0, 0))
        
            text = font2.render("Temperature", 1, (250, 250, 250))
            text2 = font2.render("Heart Rate", 1, (250, 250, 250))
            text3 = font3.render(str(temperature + " F"), 1, (250, 250, 250)) # temp data
            text4 = font3.render(pulse, 1, (250, 250, 250))  # heart data
            #Heart Rate
            #processing
            textpos = text.get_rect()
            background.blit(text, (250,150))
            background.blit(text2, (800,150))
            background.blit(text3, (250,300))
            background.blit(text4, (800,300))
            screen.blit(background, (0, 0))
            pygame.display.flip()
            
            os.system('./facesShellScript2')
            with open("/home/pi/BAYMAX/Results/pulse.txt") as f:
                pulse = None
                for line in (line for line in f if line.rstrip('\n')):
                    pulse = line

            print (pulse)

            background.fill((0, 0, 0))
            
            text = font2.render("Temperature", 1, (250, 250, 250))
            text2 = font2.render("Heart Rate", 1, (250, 250, 250))
            text3 = font3.render(str(temperature + " F"), 1, (250, 250, 250)) # temp data
            text4 = font3.render(pulse, 1, (250, 250, 250))  # heart data
            #Heart Rate
            #processing
            textpos = text.get_rect()
            background.blit(text, (250,150))
            background.blit(text2, (800,150))
            background.blit(text3, (250,300))
            background.blit(text4, (800,300))
            screen.blit(background, (0, 0))
            pygame.display.flip()
            

            time.sleep(10.0)
            

            print("done")
        else:
            background.fill((0, 0, 0))
         
            text = font.render("BAYMAX CE", 1, (255, 255, 255))
            textpos = text.get_rect()
            textpos.centerx = background.get_rect().centerx
            textpos.centery = background.get_rect().centery
            background.blit(text, textpos)
            screen.blit(background, (0, 0))
            pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()

    
    print("not looping")
    
except KeyboardInterrupt:
    pygame.quit()
    sys.exit(0)
    
    
