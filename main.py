import argparse
import os
import random


def get_all_sounds(root_dir):
    if root_dir is None:
        root_dir = os.curdir

    all_sounds = []
    for (_, _, files) in os.walk(root_dir):
        all_sounds.extend(files)
    return all_sounds


def shuffle_sounds(all_sounds):
    random.shuffle(all_sounds)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio', help='root directory of the audio files')
    args = parser.parse_args()
    all_sounds = get_all_sounds(args.audio)
    shuffle_sounds(all_sounds)
