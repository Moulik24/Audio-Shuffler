import argparse
import os
import random

from pydub import AudioSegment
from pydub.exceptions import CouldntDecodeError


def get_all_file_paths(root_dir):
    if root_dir is None:
        root_dir = os.curdir

    all_paths = []
    for (_, _, files) in os.walk(root_dir):
        all_paths.extend(files)
    return all_paths


def shuffle_file_paths(all_paths):
    random.shuffle(all_paths)


def convert_files_to_audio_segments(shuffled_file_paths):
    shuffled_audio_segments = []
    error_file_paths = []
    for file_path in shuffled_file_paths:
        audio_segment = to_audio_segment(file_path)
        if audio_segment:
            shuffled_audio_segments.append(audio_segment)
        else:
            error_file_paths.append(file_path)

    return shuffled_audio_segments, error_file_paths


def to_audio_segment(file_path):
    try:
        audio_segment = AudioSegment.from_file(file_path)
        return audio_segment
    except FileNotFoundError:
        return None
    except CouldntDecodeError:
        return None
    except IndexError:
        return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio', help='root directory of the audio files')
    args = parser.parse_args()
    all_file_paths = get_all_file_paths(args.audio)
    shuffle_file_paths(all_file_paths)
    shuffled_audio, error_files = convert_files_to_audio_segments(all_file_paths)
    with open("log_error_files.txt", "w") as log:
        for error_file in error_files:
            log.write(error_file + '\n')
