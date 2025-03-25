---
title: Gripper Refined V1 Complete Print
date: January 23, 2025
author: David Zhang
position: CTO
avatar: DZ
tags: aa
images: assets/blog/images/gripper-refined-print-linear-actuator-axle.jpg, assets/blog/images/gripper-refined-print-m200.jpg
---

I modified the main linear mechanism by adding gears and a container for the linear actuator. Because I didn’t have the CAD file for the linear actuator, I found it quite difficult to model and properly make a container for it that would keep the linear actuator from moving at an angle. As you can see in this [video](https://youtu.be/E-dHsgfKOfo), it was a complete disappointment and a waste of PLA. The print was also very low quality as we were in a hurry (here is the [STEP file](https://drive.google.com/file/d/1SJOKX2HULdFf48tS1fz4IHvbFKGeJHQl/view?usp=sharing)). Additionally, I had not considered the electrical side of this problem. To test the entire gripper, I headed to Konstantin’s house. For the design to work, I expected the linear actuator to be able to stop at a certain point, but this is very difficult given that it only has two power wires without any signal or something that is able to detect the extension. Thus, when retracting the linear actuator to close the gripper, we found that the linear actuator actually crushes the print and completely broke the coupler while squashing the slider piece. Also, I noticed that the linear actuator axle couldnt retract fully (though it wasn’t a large difference if you see the image below), suggesting that it has probably skipped a few gears internally. When I left, the electrical engineer was able to fit the gear onto the M200 motor and was able to rotate the gripper as seen in [this video](https://youtu.be/4bq-KlKKDm0). We had a discussion and decided the best way to reduce the chances of breaking the gripper was to add a stiff spring that wouldn’t allow the linear actuator to skip gears for some time while there is current sensing to see if there is excess force applied. From this experience and the feedback given from the electrical engineer, there should be changes such as:
- Increased tolerance for the parts that are connected to the components such as the linear actuator housing or gear held by the M200
- Decreased tolerance for parts that are related to the axle 
- Remove the sliding component that attaches to the linear actuator housing and replace with something else 
- A spring mechanism
- A gripper that has a long axle 
- The use of the linear actuators' built-in stopping point helps prevent damage to components by avoiding crushing

