<p align="center">
  <img src="https://framerusercontent.com/assets/r0fB0LdlevK6WWlfVG4OTrxc.png" width="100">
</p>

<h1 align="center">(>flagcat<)</h1>

# ClipStudioPaintLayersExtractor

A Python library to extract and manipulate Clip Studio Paint (.clip) files.

## Installation

```bash
pip install clipstudio
```

## Usage

```python
from clipstudio import ClipStudio

# Load a .clip file
clip = ClipStudio.load("path/to/your/file.clip")

# Extract the thumbnail
thumbnail = clip.get_thumbnail()
thumbnail.save("thumbnail.png")

# Extract layers
layers = clip.get_layers()
print(layers)

clip.close()
```
