# Muse_BrainReader
This is a project in which I attempted to have a Muse Brain Scanner Communicate with my computer to become a working video game controller.



Has many issues, but the was able to have the headset communicate with my computer and send a somewhat interperable EEG signal. I atttempted making three working games: Flappy Bird, Pong, and Tower Stacker (there are some other games that I could not get done). I used joke names in a futile attempt to be funny.



Flappy Bird and Tower Stacker both utilize the delta signal deviations from blinging to act as a signal input to allow the player to control the game. Pong on the other hand uses the beta signal, and was supposed to allow the player to move the left paddle when focusing on it. Flappy Bird and Tower Stack are finnicky, but are able to be played; however, they may need to be sloweddown as the signal processing is not always the most responsive. Pong, on the other hand, is not playable as I intended, as it becomes rather difficult to controller the paddle to move in the direction the player wants it to go. More experimentation with weights need to be done to make it more effective.



At the end of the day, this is a high school project that demonstrated the best of my coding and problem solving abilities at the time, and if you would like to use parts of the code within your own project, feel free.



Some of this code was not my original work, and credit should be given to PyLSL and MuseLSL (https://github.com/alexandrebarachant/muse-lsl) for making an interpretation of the EEG signal that I could use within the game, as well as Petal Metrics (https://petal.tech/) for being a tool that could allow the headset to communicate with my computer.
