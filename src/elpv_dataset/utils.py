# SPDX-FileCopyrightText: 2018, 2024 Sergiu Deitsch <sergiu.deitsch@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0

from PIL import Image
import numpy as np
import os


def load_dataset(fname=None):
    if fname is None:
        fname = os.path.join(os.path.dirname(__file__), 'data', 'labels.csv')

    data = np.genfromtxt(
        fname, dtype=['|S19', '<f8', '|S4'], names=['path', 'probability', 'type']
    )
    image_fnames = np.char.decode(data['path'])
    probs = data['probability']
    types = np.char.decode(data['type'])

    def load_cell_image(fname):
        with Image.open(fname) as image:
            return np.asarray(image)

    dir = os.path.dirname(fname)

    images = np.array([load_cell_image(os.path.join(dir, fn)) for fn in image_fnames])

    return images, probs, types
