---
title: Frame Design
date: March 7, 2025
author: David Zhang
position: CTO
avatar: DZ
tags: aa
images: assets/blog/images/frame-design-ati.png, assets/blog/images/frame-design-revised.png, assets/blog/images/frame-design-alubend1.jpeg, assets/blog/images/frame-design-alubend2.jpeg
---
Although the CAD model of the frame design was completed a while ago, I wanted to talk about the design choices. Because we don’t have a lot of experience with the frame, I wanted to make it as structurally sound as possible. Despite the functionality, I ruled out Atisam’s unique design and opted for something that has been done before. I read through the technical documentation of many teams mainly from the explorers class and I found [Callibro’s](https://20693798.fs1.hubspotusercontent-na1.net/hubfs/20693798/EX29%20Cabrillo_Robotics_SeaHawk_Technical_Documentation_2024.pdf), [CityU’s](https://20693798.fs1.hubspotusercontent-na1.net/hubfs/20693798/City%20University%20of%20Hong%20Kong_CityU%20Underwater%20Robotics_technical%20documentation_2024.pdf), and [Blue Robotics’](https://bluerobotics.com/store/rov/bluerov2/) designs appealing due to their simplicity, which includes two planes made of aluminum or HDPE with HDPE side plates. The top plane is for the electronic capsule and motors, which were in a typical 6 or [8 motor configuration](https://discuss.bluerobotics.com/t/frame-configuration-advantages-disadvantages/7968). We chose 8 motors for 6 degrees of freedom, auto stabilisation, and the ability to pitch for the gripper and other tooling (especially as our gripper is extremely long and it would be impractical to tilt it). To save space, Ahmed wanted to build PCBs and a custom watertight box for electronics similar to many of the teams, but I also ruled this out because I was scared of waterproofing due to inexperience. Instead, we used the [watertight capsule](https://bluerobotics.com/store/watertight-enclosures/locking-series/wte-locking-tube-r1-vp/) by Blue Robotics and found a method of placing it in a way that reduces space by bending the aluminum as seen in the images below, which was provided by Shiva from a meeting with a PCL staff. 

For the bottom plate, we wanted to ensure structural stability but also decrease the mass similar to Callibro’s SeaHawk. I recalled from a [video](https://www.youtube.com/watch?v=GafRRl5XRPM) that Voronoi patterns were used in nature and they were rather strong. We used this [Voronoi generator](https://websvg.github.io/voronoi/) with specific coordinates from the json file to create a pattern to be used for our ROV. Additionally, we had a modular tooling board to fit different tools with bolts. 

Finally, I added as many bolt holes as possible to ensure modularity in case we needed something. 

