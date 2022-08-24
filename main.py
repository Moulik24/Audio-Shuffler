import os


def get_all_sounds(root_dir):
    all_sounds = []
    for (_, _, files) in os.walk(root_dir):
        all_sounds.extend(files)
    return all_sounds
