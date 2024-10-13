# SPDX-FileCopyrightText: 2024-present Sergiu Deitsch <sergiu.deitsch@gmail.com>
#
# SPDX-License-Identifier: Apache-2.0

from elpv_dataset.utils import load_dataset
import elpv_dataset
import os
import pytest


@pytest.mark.parametrize(
    'fname',
    [None, os.path.join(os.path.dirname(elpv_dataset.__file__), 'data', 'labels.csv')],
)
def test_load_dataset(fname):
    images, proba, types = load_dataset(fname)

    assert len(images) == 2624
    assert len(proba) == 2624
    assert len(types) == 2624
