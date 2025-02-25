#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2024, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations # isort:skip

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Module under test
import bokeh.colors.color as bcc # isort:skip

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------


class Test_Color:

    def test_clamp(self) -> None:
        assert bcc.Color.clamp(10) == 10
        assert bcc.Color.clamp(10, 20) == 10
        assert bcc.Color.clamp(10, 5) == 5
        assert bcc.Color.clamp(-10) == 0

    def test_darken(self) -> None:
        c = bcc.HSL(10, 0.2, 0.2, 0.2)
        c2 = c.darken(0.1)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.h == 10
        assert c2.s == 0.2
        assert c2.l == 0.1

        c2 = c.darken(0.3)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.h == 10
        assert c2.s == 0.2
        assert c2.l == 0

    def test_darken_rgb(self) -> None:
        c = bcc.RGB(123, 12, 234, 0.2)
        c2 = c.darken(0.1)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.r == 97
        assert c2.g == 10
        assert c2.b == 185

        c2 = c.darken(1.2)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.r == 0
        assert c2.g == 0
        assert c2.b == 0

    def test_lighten(self) -> None:
        c = bcc.HSL(10, 0.2, 0.2, 0.2)
        c2 = c.lighten(0.2)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.h == 10
        assert c2.s == 0.2
        assert c2.l == 0.4

        c2 = c.lighten(1.2)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.h == 10
        assert c2.s == 0.2
        assert c2.l == 1.0

    def test_lighten_rgb(self) -> None:
        c = bcc.RGB(123, 12, 234, 0.2)
        c2 = c.lighten(0.1)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.r == 148
        assert c2.g == 52
        assert c2.b == 245

        c2 = c.lighten(1.2)
        assert c2 is not c
        assert c2.a == 0.2
        assert c2.r == 255
        assert c2.g == 255
        assert c2.b == 255

class Test_HSL:
    def test_init(self) -> None:
        c = bcc.HSL(10, 0.2, 0.3)
        assert c
        assert c.a == 1.0
        assert c.h == 10
        assert c.s == 0.2
        assert c.l == 0.3
        c = bcc.HSL(10, 0.2, 0.3, 0.3)
        assert c
        assert c.a == 0.3
        assert c.h == 10
        assert c.s == 0.2
        assert c.l == 0.3

    def test_repr(self) -> None:
        c = bcc.HSL(10, 0.2, 0.3)
        assert repr(c) == c.to_css()
        c = bcc.HSL(10, 0.2, 0.3, 0.3)
        assert repr(c) == c.to_css()

    def test_copy(self) -> None:
        c = bcc.HSL(10, 0.2, 0.3)
        c2 = c.copy()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.h == c.h
        assert c2.s == c.s
        assert c2.l == c.l

    def test_from_hsl(self) -> None:
        c = bcc.HSL(10, 0.2, 0.3)
        c2 = bcc.HSL.from_hsl(c)
        assert c2 is not c
        assert c2.a == c.a
        assert c2.h == c.h
        assert c2.s == c.s
        assert c2.l == c.l

        c = bcc.HSL(10, 0.2, 0.3, 0.1)
        c2 = bcc.HSL.from_hsl(c)
        assert c2 is not c
        assert c2.a == c.a
        assert c2.h == c.h
        assert c2.s == c.s
        assert c2.l == c.l

    def test_from_rgb(self) -> None:
        c = bcc.RGB(255, 100, 0)
        c2 = bcc.HSL.from_rgb(c)
        assert c2 is not c
        assert c2.a == 1
        assert c2.h == 24
        assert c2.s == 1.0
        assert c2.l == 0.5

        c = bcc.RGB(255, 100, 0, 0.1)
        c2 = bcc.HSL.from_rgb(c)
        assert c2 is not c
        assert c2.a == 0.1
        assert c2.h == 24
        assert c2.s == 1.0
        assert c2.l == 0.5

    def test_to_css(self) -> None:
        c = bcc.HSL(10, 0.2, 0.3)
        assert c.to_css() == "hsl(10, 20.0%, 30.0%)"
        c = bcc.HSL(10, 0.2, 0.3, 0.3)
        assert c.to_css() == "hsla(10, 20.0%, 30.0%, 0.3)"

    def test_to_hsl(self) -> None:
        c = bcc.HSL(10, 0.2, 0.3)
        c2 = c.to_hsl()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.h == c.h
        assert c2.s == c.s
        assert c2.l == c.l

        c = bcc.HSL(10, 0.2, 0.3, 0.1)
        c2 = c.to_hsl()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.h == c.h
        assert c2.s == c.s
        assert c2.l == c.l

    def test_to_rgb(self) -> None:
        c = bcc.HSL(10, 0.2, 0.3)
        c2 = c.to_rgb()
        assert c2 is not c
        assert c2.a == 1.0
        assert c2.r == 92
        assert c2.g == 66
        assert c2.b == 61

        c = bcc.HSL(10, 0.2, 0.3, 0.1)
        c2 = c.to_rgb()
        assert c2 is not c
        assert c.a == 0.1
        assert c2.r == 92
        assert c2.g == 66
        assert c2.b == 61

class Test_RGB:
    def test_init(self) -> None:
        c = bcc.RGB(10, 20, 30)
        assert c
        assert c.a == 1.0
        assert c.r == 10
        assert c.g == 20
        assert c.b == 30

        c = bcc.RGB(10, 20, 30, 0.3)
        assert c
        assert c.a == 0.3
        assert c.r == 10
        assert c.g == 20
        assert c.b == 30

    def test_repr(self) -> None:
        c = bcc.RGB(10, 20, 30)
        assert repr(c) == c.to_css()
        c = bcc.RGB(10, 20, 30, 0.3)
        assert repr(c) == c.to_css()

    def test_copy(self) -> None:
        c = bcc.RGB(10, 20, 30)
        c2 = c.copy()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.r == c.r
        assert c2.g == c.g
        assert c2.b == c.b

    def test_from_hex_string(self) -> None:
        # '#rrggbb'
        c = bcc.RGB.from_hex_string("#A3B20F")
        assert (c.r, c.g, c.b, c.a) == (163, 178, 15, 1.0)
        c = bcc.RGB.from_hex_string("#a3b20f")
        assert (c.r, c.g, c.b, c.a) == (163, 178, 15, 1.0)

        # '#rrggbbaa'
        c = bcc.RGB.from_hex_string("#A3B20FC0")
        assert (c.r, c.g, c.b, c.a) == (163, 178, 15, 192/255.0)
        c = bcc.RGB.from_hex_string("#a3b20fc0")
        assert (c.r, c.g, c.b, c.a) == (163, 178, 15, 192/255.0)

        # '#rgb'
        c = bcc.RGB.from_hex_string("#7A3")
        assert (c.r, c.g, c.b, c.a) == (119, 170, 51, 1.0)
        c = bcc.RGB.from_hex_string("#7a3")
        assert (c.r, c.g, c.b, c.a) == (119, 170, 51, 1.0)

        # '#rgba'
        c = bcc.RGB.from_hex_string("#7A3B")
        assert (c.r, c.g, c.b, c.a) == (119, 170, 51, 187/255.0)
        c = bcc.RGB.from_hex_string("#7a3b")
        assert (c.r, c.g, c.b, c.a) == (119, 170, 51, 187/255.0)

        # Invalid hex string
        with pytest.raises(ValueError):
            bcc.RGB.from_hex_string("#")
        with pytest.raises(ValueError):
            bcc.RGB.from_hex_string("#1")
        with pytest.raises(ValueError):
            bcc.RGB.from_hex_string("#12")
        with pytest.raises(ValueError):
            bcc.RGB.from_hex_string("#12345")
        with pytest.raises(ValueError):
            bcc.RGB.from_hex_string("#1234567")
        with pytest.raises(ValueError):
            bcc.RGB.from_hex_string("#123456789")
        with pytest.raises(ValueError):
            bcc.RGB.from_hex_string(" #abc")

    def test_from_hsl(self) -> None:
        c = bcc.HSL(10, 0.1, 0.2)
        c2 = bcc.RGB.from_hsl(c)
        assert c2 is not c
        assert c2.a == 1.0
        assert c2.r == 56
        assert c2.g == 48
        assert c2.b == 46

        c = bcc.HSL(10, 0.1, 0.2, 0.3)
        c2 = bcc.RGB.from_hsl(c)
        assert c2 is not c
        assert c2.a == 0.3
        assert c2.r == 56
        assert c2.g == 48
        assert c2.b == 46

    def test_from_rgb(self) -> None:
        c = bcc.RGB(10, 20, 30)
        c2 = bcc.RGB.from_rgb(c)
        assert c2 is not c
        assert c2.a == c.a
        assert c2.r == c.r
        assert c2.g == c.g
        assert c2.b == c.b

        c = bcc.RGB(10, 20, 30, 0.1)
        c2 = bcc.RGB.from_rgb(c)
        assert c2 is not c
        assert c2.a == c.a
        assert c2.r == c.r
        assert c2.g == c.g
        assert c2.b == c.b

    def test_to_css(self) -> None:
        c = bcc.RGB(10, 20, 30)
        assert c.to_css() == "rgb(10, 20, 30)"
        c = bcc.RGB(10, 20, 30, 0.3)
        assert c.to_css() == "rgba(10, 20, 30, 0.3)"

    def test_to_hex(self) -> None:
        c = bcc.RGB(10, 20, 30)
        assert c.to_hex(), f"#{c.r:02x}{c.g:02x}{c.b:02x}"
        assert bcc.RGB(10, 20, 30, 0.0).to_hex() == "#0a141e00"
        assert bcc.RGB(10, 20, 30, 0.5).to_hex() == "#0a141e80"
        assert bcc.RGB(10, 20, 30, 0.996).to_hex() == "#0a141efe"
        assert bcc.RGB(10, 20, 30, 1.0).to_hex() == "#0a141e"

    def test_to_hsl(self) -> None:
        c = bcc.RGB(255, 100, 0)
        c2 = c.to_hsl()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.h == 24
        assert c2.s == 1.0
        assert c2.l == 0.5

        c = bcc.RGB(255, 100, 0, 0.1)
        c2 = c.to_hsl()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.h == 24
        assert c2.s == 1.0
        assert c2.l == 0.5

    def test_to_rgb(self) -> None:
        c = bcc.RGB(10, 20, 30)
        c2 = c.to_rgb()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.r == c.r
        assert c2.g == c.g
        assert c2.b == c.b

        c = bcc.RGB(10, 20, 30, 0.1)
        c2 = c.to_rgb()
        assert c2 is not c
        assert c2.a == c.a
        assert c2.r == c.r
        assert c2.g == c.g
        assert c2.b == c.b

    def test_brightness(self) -> None:
        assert round(bcc.RGB(  0,   0,   0).brightness, 2) == 0.0
        assert round(bcc.RGB(127, 127, 127).brightness, 2) == 0.5
        assert round(bcc.RGB(128, 128, 128).brightness, 2) == 0.5
        assert round(bcc.RGB(255, 255, 255).brightness, 2) == 1.0

    def test_luminance(self) -> None:
        assert round(bcc.RGB(  0,   0,   0).luminance, 3) == 0.000
        assert round(bcc.RGB(190,   0, 190).luminance, 3) == 0.149
        assert round(bcc.RGB(130, 130,  90).luminance, 3) == 0.218
        assert round(bcc.RGB(255, 255, 255).luminance, 3) == 1.000

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
