---
title: Control System Communication Protocols
date: March 2, 2025
author: Ahmed Shaikh
position: CEO
avatar: AS
tags: aa
images:
---

One of the primary requirements of our control system was communication between a Raspberry Pi and the Raspberry Pi Pico. The reason we decided to use a Raspberry Pi along with a separate microcontroller was that there were insufficient hardware PWM (Pulse Width Modulation) channels on the Raspberry Pi to control all the servos and thrusters on the ROV along with ADC (Analog to Digital Conversion) for the pH sensor. The Pico would offer a compact and efficient solution to the lack of hardware control and take some processing load off of the Raspberry Pi, which would already handle 4-5 camera inputs and control telemetry from the surface laptop.

Initially, I decided on the I2C protocol for communication between the Pi and the Pico as it had the highest data rate of the ones on the Pico. However, I noticed that the language I was programming the pico in, Micropython, did not support I2C slave mode. This was an issue because the I2C protocol requires a controller and a peripheral, and setting the Raspberry Pi as a peripheral device also proved challenging. Thus, I decided to rewrite my Pico code in C++ using the Raspberry Pi Pico SDK. Despite setting up slave mode on the Pico with an interrupt handler, I could not get this connection to work. I used the same processes as the various examples I saw online. 

Thus, I took an alternative approach and decided to use the UART communication protocol. I got this working much faster and resolved the data transfer issues quickly. 
