from unittest import TestCase

from pydub import AudioSegment

from main import get_all_file_paths, convert_files_to_audio_segments, merge_audio_segments


class Test(TestCase):
    def test_get_all_file_paths_from_test_directory(self):
        all_sounds = get_all_file_paths('test_sound_files')
        self.assertTrue(all_sounds == ['test_sound_files\\Clubs\\3_C.m4a', 'test_sound_files\\Clubs\\7_C.m4a', 'test_sound_files\\Clubs\\K_C.m4a', 'test_sound_files\\Diamonds\\5_D.m4a', 'test_sound_files\\Hearts\\5_H.m4a', 'test_sound_files\\Hearts\\6_H.m4a', 'test_sound_files\\Hearts\\A_H.m4a', 'test_sound_files\\Hearts\\J_H.m4a', 'test_sound_files\\NonAudioFiles\\non_audio_file.txt', 'test_sound_files\\NonAudioFiles\\non_audio_file_no_ext', 'test_sound_files\\Spades\\5_S.m4a', 'test_sound_files\\Spades\\8_S.m4a'])

    def test_get_all_file_paths_from_current_directory(self):
        try:
            all_file_paths = get_all_file_paths(".")
        except:
            assert False

    def test_get_all_file_paths_no_directory_specified(self):
        try:
            all_file_paths = get_all_file_paths(None)
        except:
            assert False

    def test_convert_files_to_audio_segments_happy_path(self):
        all_audio_files = ["test_sound_files/Clubs/3_C.m4a", "test_sound_files/Spades/5_S.m4a", "test_sound_files/Hearts/5_H.m4a"]
        shuffled_audio, success_files, error_files = convert_files_to_audio_segments(all_audio_files)
        self.assertTrue(len(shuffled_audio) == 3)
        self.assertTrue(success_files == all_audio_files)
        self.assertTrue(error_files == [])

    def test_convert_files_to_audio_segments_non_existent_but_valid_sound_file(self):
        non_existent_sound_files = ["file_that_does_not_exist.wav"]
        shuffled_audio, success_files, error_files = convert_files_to_audio_segments(non_existent_sound_files)
        self.assertTrue(len(shuffled_audio) == 0)
        self.assertTrue(success_files == [])
        self.assertTrue(error_files == non_existent_sound_files)

    def test_convert_files_to_audio_segments_non_existent_and_not_valid_sound_file(self):
        non_existent_non_sound_files = ["file_that_does_not_exist.txt"]
        shuffled_audio, success_files, error_files = convert_files_to_audio_segments(non_existent_non_sound_files)
        self.assertTrue(len(shuffled_audio) == 0)
        self.assertTrue(success_files == [])
        self.assertTrue(error_files == non_existent_non_sound_files)

    def test_convert_files_to_audio_segments_non_existent_files(self):
        non_audio_files = ["test_sound_files/NonAudioFiles/non_audio_file.txt", "test_sound_files/NonAudioFiles/non_audio_file_no_ext"]
        shuffled_audio, success_files, error_files = convert_files_to_audio_segments(non_audio_files)
        self.assertTrue(len(shuffled_audio) == 0)
        self.assertTrue(success_files == [])
        self.assertTrue(error_files == non_audio_files)

    def test_convert_files_to_audio_segments_mixed_path(self):
        some_audio_files = ["test_sound_files/Clubs/3_C.m4a", "test_sound_files/NonAudioFiles/non_audio_file.txt"]
        shuffled_audio, success_files, error_files = convert_files_to_audio_segments(some_audio_files)
        self.assertTrue(len(shuffled_audio) == 1)
        self.assertTrue(success_files == ["test_sound_files/Clubs/3_C.m4a"])
        self.assertTrue(error_files == ["test_sound_files/NonAudioFiles/non_audio_file.txt"])

    def test_merge_audio_segments(self):
        audio_segments = [AudioSegment.from_file("test_sound_files/Spades/5_S.m4a"), AudioSegment.from_file("test_sound_files/Clubs/3_C.m4a")]
        merged_audio = merge_audio_segments(audio_segments)
        merged_audio_duration_actual = len(merged_audio)
        merged_audio_duration_expected = len(audio_segments[0]) + len(audio_segments[1])
        self.assertEqual(merged_audio_duration_expected, merged_audio_duration_actual)