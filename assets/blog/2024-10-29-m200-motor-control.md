---
title: M200 BLDC Motor Precise Control with FOC Prototype
date: October 29, 2024
author: Konstantin Logashenko
position: Electrical Engineer
avatar: KL
tags: later
images:
---

The specifications of the grabber arm necessitate 360-degree rotation of the grabber. Since the mechanism will be exposed to the water, the only feasible motor to achieve this rotation is the BlueRobotics M200, which is a brushless DC motor (BLDC). Most BLDC drive algorithms are optimized to run the motor at high RPM (more than 100 RPM minimum is typical). The Field-Oriented Control algorithm on the other hand allows much better control at low speeds, and is used widely in robotics with BLDC motors as powerful rotary actuators. The caveat is, however, that FOC algorithms generally need a position sensor to provide feedback on the motor’s angle. After researching implementations of such algorithms, I found the SimpleFOC library, which provides an open-loop (no sensor) implementation. This library is perfect for our application, since it can be used with low-cost common hardware. However, the disadvantage of open-loop control is lower torque. To verify the suitability of this implementation I built a prototype, which simply rotated the motor at low speeds continuously. I used a low power motor driver IC, which in the final design will be replaced by one with higher power output. The torque was not high as predicted, however the motion was very smooth. Torque will be higher in the final design due to higher current, and a gear reduction will be used on the grabber for both higher torque and finer rotation control.

This is a [video](https://www.youtube.com/watch?v=9GNqzMJjRaw).

