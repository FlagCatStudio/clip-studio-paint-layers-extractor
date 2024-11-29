import os
from src.clipstudio import ClipStudio

def test_load_clip_file():
    clip = ClipStudio.load("tests/data/sample.clip")
    assert clip is not None

def test_get_layers():
    clip = ClipStudio.load("tests/data/sample.clip")
    layers = clip.get_layers()
    assert isinstance(layers, list)
    clip.close()

def test_save_thumbnail():
    clip = ClipStudio.load("tests/data/sample.clip")
    thumbnail = clip.get_thumbnail()
    thumbnail.save("tests/data/thumbnail.png")
    clip.close()

def test_cleanup():
    os.remove("extracted_clip.sqlite")
    os.remove("tests/data/thumbnail.png")