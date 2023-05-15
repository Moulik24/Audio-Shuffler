# Audio-Shuffler
Given a directory with input audio files, create one merged output audio file that has the input audio files in shuffled order.
The inspiration of this project is the game of Karuta: https://en.wikipedia.org/wiki/Karuta, where cards are read
in a random order. This script generates a long recording of random order cards given individual recordings of each of them.
As demoed in the test_sound_files directory, you can create recordings of normal playing cards, such as "Ace of Hearts" 
to play the following version of Karuta: https://www.reddit.com/r/boardgames/comments/etpnyx/karuta_competitive_memory_with_standard_playing/

The script can also be used for just creating a shuffled playlist of sound files. It might take a pretty long time, but
you can run the script on your home directory for example, and if there are some audio files in the depths of your file system, 
the script will shuffle them and present you with a shuffled-merged recording of them.

## Setup
You can clone the entire project or just download the main.py script and shuffleAudio.sh, but will also need Pydub. 
You can find their installation instructions here: https://github.com/jiaaro/pydub#:~:text=eye%20on%20both.-,Installation,-Installing%20pydub%20is

I also followed https://www.youtube.com/watch?v=d2Y0lGrRoMI&t=604s&ab_channel=NilegProduction for windows installation.

## Run the script + more features
The shuffleAudio.sh file is meant to make running the script easy.

In shuffleAudio.sh, set the audioRootDir to the path of the root directory of the audio files that you want to shuffle.
The subdirectories can also have non audio files within them, they just won't show up in the final shuffled audio file.
The default is to the testSoundFiles directory.

Set the outputFilePath to the path of the new audio file that you want to create. The path should end with a file extension 
that is known to be an audio file, such as .wav or .mp3, and the default is output.wav.


A pause can be set between successive audio files, where if you have sounds: [sound1, sound2, sound3], you can get [sound1,pause,sound2,pause,sound3].
In shuffleAudio.sh, this variable is called pauseDuration, and is the pause length in seconds. It can be set to 0 for no pauses.

Some additional functionality includes the output of log_error_files.txt and log_success_files.txt.
There may some files that are not recognized as decodable audio files by Pydub and which may not be shuffled.
The path to these types of files will be put in log_error_files.txt. Those that are successfully recognized as audio files and are shuffled
will show up in log_success_files.txt.
The corresponding audio files in log_success_files.txt will be shuffled and merged into an output file,
so you can check this file before playing the output recording to make sure that all desired files will be present in the recording.
