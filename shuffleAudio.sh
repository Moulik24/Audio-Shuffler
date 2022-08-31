#!/bin/bash
audioRootDir=test_sound_files
outputFilePath=output.wav
pauseDuration=2
python main.py --audio $audioRootDir --output $outputFilePath --pause $pauseDuration