---
title: Sealing the Float
date: March 20, 2025
author: David Zhang
position: CTO
avatar: DZ
tags: aa
images: assets/blog/images/Types-of-Seals.jpg
---
These days, I have been working on sealing and joining the gripper and the float. So far, the o-ring seal has been successful, which shouldn’t be surprising but is definitely surprising to me. For the float flange, I designed it so that there would be a flat surface (the acrylic) and it compresses the o-ring towards a resin printed groove. From what I read, the optimal compression should be a 25% compression, and allowing DeepSeek to do all the math (ID=88mm, OD=95mm, CS=3.5mm), the groove depth should be around 2.5 mm, and the groove width should be around 4 mm. However, due to the lack of experience, I made the groove depth more shallow at 2 mm with a max compression of 42.9%. This way we could always increase the pressure in case it doesn’t work but it doesn’t go above 42.9% to avoid damaging the o-ring further (in case a team member is assigned with assembling the float). 

Yesterday, I finished sealing the flange with epoxy and the nitrile rubber o-rings arrived, so Omar and I added the o-rings and compressed the o-ring with a few bolts (we didn’t have enough hex nuts, so we couldn’t fill the 12 holes, but rather did around 5 that were evenly spaced, but the final should probably have all 12 to distribute the pressure on the o-ring). Because Omar didn’t understand how the o-rings worked, they didn’t leave a gap in some areas of the face seal (and the 3mm acrylic kind of bends). This may cause the [o-ring to degrade](https://eriks.com/en/know-how-hub/blogs/o-ring-degradation-characteristics-causes-solutions/). After some DeepSeek calculations, the gap between the flanges should be around 0.5 mm to 1 mm. 

