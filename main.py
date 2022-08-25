import argparse
import os
import random

from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError


def get_all_sounds(root_dir):
    if root_dir is None:
        root_dir = os.curdir

    all_sounds = []
    for (_, _, files) in os.walk(root_dir):
        all_sounds.extend(files)
    return all_sounds


def shuffle_sounds(all_sounds):
    random.shuffle(all_sounds)


def convert_files_to_audio_segments(shuffled_file_paths):
    shuffled_audio_segments = []
    for file_path in shuffled_file_paths:
        audio_segment = to_audio_segment(file_path)
        if audio_segment:
            shuffled_audio_segments.append(audio_segment)

    return shuffled_audio_segments


def to_audio_segment(file_path):
    try:
        audio_segment = AudioSegment.from_file(file_path)
        return audio_segment
    except FileNotFoundError:
        return None
    except CouldntDecodeError:
        return None
    # TODO: In error cases, add file name to a logger file that has a list of files that couldn't be processed


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio', help='root directory of the audio files')
    args = parser.parse_args()
    all_sounds = get_all_sounds(args.audio)
    shuffle_sounds(all_sounds)
