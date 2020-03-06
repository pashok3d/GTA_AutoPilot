# GTA_AutoPilot
Self-driving AI system for GTA:SA using OpenCV and CNN
# About
Gta_AutoPilot is a computer vision project representing AI system for an autonomous driving in [GTA:San Andreas](https://en.wikipedia.org/wiki/Grand_Theft_Auto:_San_Andreas). In the project, we read frames directly from the desktop using OpenCV, instead of working with the game's code. This approach enables to use the system basically on any other game. The system can be devided into 3 parts: collecting data, learning using CNN and exploiting.

![](Capture.gif)
# Collecting data
Collecting data consists in reading and processing frames using OpenCV. Parallely, we read keyboard keys, which correspond to the prediction classes. To provide derterminism in the system's predictions, we use simple driving function to enable constant car speed if possible.
# How to run 
> **Note: If you want to test already trained system on GTA:SA jump to “[Example](https://github.com/pashok3d/GTA_AutoPilot/blob/master/README.md#example)” section.**
### Prerequisite
* to-do
### Collecting data
* Run the game in windowed mode, 640x480 resolution, at the top left of your screen. 
* For best perfomance, use first person view, if possible.
* Run `scanner.py` 
* Press following keys to save frames with corresponding move: 'O' - sraight, 'K' - left, 'L' - right.
Interface keys: 'P' - pause data collection, 'Q' - quit.
### Learning
* Run `model.py`
### Exploiting
* Run the game in windowed mode, 640x480 resolution, at the top left of your screen. 
* For best perfomance, use first person view, if possible.
* Run `predictor.py`
  Interface keys: 'P' - pause autopilot, 'Q' - quit.
# Example
* Run GTA:SA in windowed mode, 640x480 resolution, at the top left of your screen. 
* For best perfomance:
  * Use first person view (Use 'V' key)
  * Type SLOWITDOWN to slow the time 
  * Type VROCKPOKEY to spawn the vechicle used while training
* Run `predictor.py`
  Interface keys: 'P' - pause autopilot, 'Q' - quit.

