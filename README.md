# youtuber-detector
Proposed a system that detects a face from a video or image using a webcam and after identifying the face of a particular YouTuber it will start playing user video on the user’s detected face frame with an accuracy of 95% for face detection also tested on 100+ images of YouTubers and 20 short videos.<br/>
Technologies: Speech Recognition, OpenCV, LBPH algorithm
The Phases

Speech Recognition
Data Gathering and Face Detection
Train the Recognizer
Face Recognition

Voice command to open camera
Libraries :
Speech Recognition: For performing speech and recognition.
Pyttsx3: Text to Speech (TTS) library for python 2 & 3, supports multiple
engine including sapi5,espeak etc.

Face detection
Face detection using Haar cascades is a machine learning based approach where a cascade function is trained with a set of input data.
 OpenCV already contains many pre-trained classifiers for face, eyes, smiles, etc.. Today we will be using the face classifier. 
Cascade Classifier : used to detect objects in a video stream. 
LBPH algorithm (Local Binary Patterns Histogram)
Local Binary Patterns Histogram (LBPH) is a facial recognition algorithm that was first proposed in 1996.
 It has 4 parameters: - radius , Neighbors, Grid X, Grid Y






![image](https://user-images.githubusercontent.com/66154551/156501411-888bc3b7-c499-4e9a-ba08-603150b73cf5.png)
Stream video on detected image
Once the youtubers face is detected, we will play one of his/her’s videos on his/her’s face by manipulating individual frames of the video.
Also we will adjust the video size to fit into the frame by resizing it if it goes out of the frame.




