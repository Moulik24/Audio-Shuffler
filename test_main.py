from unittest import TestCase

from main import get_all_sounds


class Test(TestCase):
    def test_get_all_sounds(self):
        all_sounds = get_all_sounds('test_sound_files')
        self.assertTrue(len(all_sounds) == 10)
