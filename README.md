# Audio-Shuffler
Given a directory with input audio files, create an output audio file that has the input audio files in shuffled order.

In shuffleAudio.sh, set the audioRootDir to the path of the root directory of the audio files that you want to shuffle.
Set the outputFilePath to the path of the new audio file that you want to create. These paths are respective to this current directory where the python script is.
The default for these values are testSoundFiles and output.wav respectively.

Finally, a pause can be set between successive audio files, where if you have sounds: [sound1, sound2, sound3], you can get [sound1,pause,sound2,pause,sound3].
In shuffleAudio.sh, this variable is called pauseDuration, and is the pause length in seconds. It can be set to 0 for no pauses.