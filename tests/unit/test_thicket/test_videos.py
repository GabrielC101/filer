from thicket import videos
from thicket.videos import VideoFile


def test_import():
    assert videos


def test_video_file():
    assert VideoFile.type == 'video'
