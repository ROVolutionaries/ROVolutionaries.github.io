---
title: Float Design
date: March 7, 2025
author: David Zhang
position: Head of Mechanical Engineering
avatar: DZ
tags: aa
images:
---

The float design has been one of my main projects in MateROV since last year. Last year, we were very lost as we had no prior experience or help from others. We had no idea how a buoyancy engine worked, and articles such as the [wikipedia article](https://en.wikipedia.org/wiki/Buoyancy_engine) used methods that seemed impractical. After reading the preview mission task that required the measurement of depth, our team came up with gyro, laser pointers, and sonar. Thankfully, we found a [guide from instructables](https://www.instructables.com/Underwater-Glider/) and decided to use syringes to modify the buoyancy. Our float consisted mainly of scrap pieces lying around, such as syringes, stepper motors that were scavenged from defunct 3D printers, and a long bolt. Additionally, we were able to 3D print parts in the TKS design room and our mentor bought us 3.5 inch PVC. The design had an electronics compartment and a buoyancy engine compartment (my friend advised me to separate the electronics from the buoyancy engine even though we didn’t know proper methods of waterproofing, so the two compartments would inevitably be stuck together with epoxy). Because the float PVC was not transparent, it was impossible to tell whether the inside was waterproofed, and we had to sometimes go by luck (for example pouring in epoxy to waterproof the syringes). The syringes were extremely difficult to pull and lubricants such as WD40 somehow made it less smooth. Thus, we had to scrap our first float because the syringes were attached to the float. Additionally, because we were using a long bolt, it was extremely difficult to couple the bolt head to the stepper motor. We messed up the coupler a few times and hours before the regional competition, we had to EpoPutty the stepper motor directly to the bolt, where it's stuck to this day (a lot of things were done extremely last minute. For example, the electric engineer literally soldered the fuse in parallel at 3am before the regional competition). Finally, we noticed that the stepper motor had absolutely no torque at all (e.g if you gently tapped the stepper motor it would’ve stopped) and even if we minimized the errors there would be no way for the float to work. Also, this year we found out that the pressure sensor we bought from Amazon didn’t work. 

This year, I used a similar mechanism but [addressed all the issues](https://youtu.be/9TrLYAlDmAg):
 - The entire float is able to be taken out like an electronics tray in a capsule while having proper O-ring face seals
 - To decrease loss in efficiency, I used structural beams made of stainless steel to align the syringes with the stepper motor
 - Used bolts from the stepper motor instead of holding it with a 3D print 
 - Bought a [stepper motor](https://www.aliexpress.com/item/1005006104443954.html) that has relatively high torque, [lead screw set](https://www.aliexpress.com/item/1005002085320555.html) that was of high quality, and a fairly transparent [PVC pipe](https://www.aliexpress.com/item/1005005890935183.html) 
 - Expanded the hole of the syringe to decrease the force (because I am using tubing, I needed the outer circle of the syringe to make a connection. Thus, I expanded the size of the entrance by removing the middle part of the syringe. The [method used](https://www.youtube.com/watch?v=ORL7fASZpUw) was inspired by a tale I heard about a person using needles to drill holes into postage stamps to make it easier to rip. I did the same using a hammer, a nail, and pliers to yoink the part out)
 - Created a more accurate way of holding the syringe heads with 3D prints instead of drilling into the it by hand 
 - Used tubing rather than directly epoxy the float, which will probably allow for syringe removal if necessary 
 - Added a tonne of space for the electronics at the top 
 - Using a universal coupler for slight alignment issues (we haven’t tested this yet)

Although it may not be the final version, here is the [STEP file](https://drive.google.com/file/d/1AnbART2U5zjeA3a6lvJc0xrgnfLWK7QG/view?usp=sharing). 

Right now, I’m waiting for the manufacturing team to finish the prints and for the o-rings to arrive. I’m very excited to turn the theoretical CAD files into reality! In the future, I would like to use a compact and more reliable mechanism to push and pull syringes as shown in [this video](https://www.youtube.com/watch?v=KLEH8RJsYgI) by the Lego Experiment Channel. I may also experiment with other methods shown in [another video](https://www.youtube.com/watch?v=ZdhM0SjlS9o). 