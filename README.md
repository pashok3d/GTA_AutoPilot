# GTA_AutoPilot
Self-driving AI system for GTA:SA using OpenCV and CNN
# About
Gta_AutoPilot is a computer vision project representing AI system for an autonomous driving in [GTA:San Andreas](https://en.wikipedia.org/wiki/Grand_Theft_Auto:_San_Andreas). In the project, we read frames directly from the desktop using OpenCV, instead of working with the game's code. This approach enables to use the system basically on any other game. The system can be devided into 3 parts: collecting data, learning using CNN and exploiting.
# Collecting data
Collecting data consists in reading and processing frames using OpenCV. Parallely, we read keyboard keys, which correspond to the prediction classes. To provide derterminism in the system's predictions, we use simple driving function to enable constant car speed if possible.
