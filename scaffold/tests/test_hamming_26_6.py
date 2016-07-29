#!/usr/bin/env python
# encoding: utf-8

# Copyright (C) 2016 Chintalagiri Shashank
#
# This file is part of hamming-test.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Docstring for test_hamming_26_6
"""

import pytest
import hamming

byte_vectors = [0, 255, 3, 5, 10, 15, 33, 28, 19, 100, 122, 158, 198, 224]

@pytest.mark.parametrize('b1', byte_vectors)
@pytest.mark.parametrize('b2', byte_vectors)
@pytest.mark.parametrize('b3', byte_vectors)
def test_round_trip(b3, b2, b1):
    ibuf = hamming.buffer(3)
    ibuf[0] = b1
    ibuf[1] = b2
    ibuf[2] = b3
    hpack = hamming.pack_hamming26_6(ibuf.cast())
    ret = hamming.buffer(1)
    obuf = hamming.buffer(3)
    hpack = hamming.check_hamming26_6(hpack, ret.cast())
    assert ret[0] == 0
    ret = hamming.unpack_hamming26_6(hpack, obuf.cast())
    assert ret == 0
    for i in range(3):
        assert ibuf[i] == obuf[i]
