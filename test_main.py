from unittest import TestCase

from main import get_all_sounds


class Test(TestCase):
    def test_get_all_sounds_from_test_directory(self):
        all_sounds = get_all_sounds('test_sound_files')
        self.assertTrue(len(all_sounds) == 10)

    def test_get_all_sounds_from_current_directory(self):
        try:
            all_sounds = get_all_sounds(".")
        except:
            assert False

    def test_get_all_sounds_no_directory_specified(self):
        try:
            all_sounds = get_all_sounds(None)
        except:
            assert False

