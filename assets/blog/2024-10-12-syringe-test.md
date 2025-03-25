---
title: Syringe Force Test
date: October 12, 2024
author: David Zhang
position: CTO
avatar: DZ
tags: to be done later
images:
---

Last year, our float didn’t work mainly because our stepper motor couldn’t provide enough force to pull the syringes (which also required quite a bit of force to pull). Thus, it was important that we calculated if the stepper motor had enough torque. I did this by first testing how much force is required to pull a syringe as seen in this video. The max force was probably 6 kg (which is a lot). Thus, my dad suggested that I cut the syringe’s head, which reduced the max force to 2.5 kg, so three syringes takes around 75 newtons. I haven’t really taken proper physics classes yet, so I headed to ChatGPT to see if my stepper motor was capable of applying this much force. 

From the [spec sheet](https://www.aliexpress.com/item/1005006104443954.html), it had 0.34 N*m of holding torque, and it calculated that the force able to be produced would be 80 N, which is above 75 N. Thus, it would probably be able to deliver enough force, and if not, we can use planetary gears to increase the torque. 
