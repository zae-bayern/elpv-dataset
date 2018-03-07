# A Benchmark for Visual Identification of Defective Solar Cells in Electroluminescence Imagery

This repository provides a dataset of solar cell images extracted from
high-resolution electroluminescence images of photovoltaic modules.

![An overview of images in the dataset. The darker the red is, the higher is the
likelihood of a defect in the solar cell overlayed by the corresponding color.](./doc/images/overview.jpg){width=100%}

## The Dataset

The dataset contains 2,426 samples of 300x300 pixels 8-bit grayscale images of
functional and defective solar cells with varying degree of degradations
extracted from 44 different solar modules. The defects in the annotated images
are either of intrinsic or extrinsic type and are known to reduce the power
efficiency of solar modules.

All images are normalized with respect to the size and perspective.
Additionally, any distortion induced by the lens used to capture the images was
eliminated prior to image segmentation.

## Annotations

Every image is annotated with a defect probability (a floating point value
between 0 and 1) and the type of the solar module (either mono- or
polycrystalline) the solar cell image was originally extracted from.

The individual images are stored in the `images` directory and the corresponding
annotations in `labels.csv`.

## Usage

In Python, use `utils/elpv_reader` in this repository to load the images and the
corresponding annotations as follows:

```python
from elpv_reader import load_dataset
images, proba, types = load_dataset()
```

The code requires NumPy and Pillow to work correctly.

## License

<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

For commercial use, please contact us for further information.
