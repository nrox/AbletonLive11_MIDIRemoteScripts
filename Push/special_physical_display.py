# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\Push\special_physical_display.py
# Compiled at: 2022-11-29 09:57:03
# Size of source mod 2**32: 3675 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.base import flatten, group
from ableton.v2.control_surface.elements import PhysicalDisplayElement
DISPLAY_BLOCK_LENGTH = 18

class SpecialPhysicalDisplay(PhysicalDisplayElement):
    ascii_translations = {
      '\x00': 0,
      '\x01': 1,
      '\x02': 2,
      '\x03': 3,
      '\x04': 4,
      '\x05': 5,
      '\x06': 6,
      '\x07': 7,
      '¦': 8,
      '°': 9,
      'Ä': 10,
      'Ç': 11,
      'Ö': 12,
      'Ü': 13,
      'ß': 14,
      'à': 15,
      'ä': 16,
      'ç': 17,
      'è': 18,
      'é': 19,
      'ê': 20,
      'î': 21,
      'ñ': 22,
      'ö': 23,
      '÷': 24,
      'ø': 25,
      'ü': 26,
      '♭': 27,
      '\x1b': 27,
      '\x1c': 28,
      '\x1d': 29,
      '\x1e': 30,
      '\x1f': 31,
      ' ': 32,
      '!': 33,
      '"': 34,
      '#': 35,
      '♯': 35,
      '$': 36,
      '%': 37,
      '&': 38,
      "'": 39,
      '(': 40,
      ')': 41,
      '*': 42,
      '+': 43,
      ',': 44,
      '-': 45,
      '.': 46,
      '/': 47,
      '0': 48,
      '1': 49,
      '2': 50,
      '3': 51,
      '4': 52,
      '5': 53,
      '6': 54,
      '7': 55,
      '8': 56,
      '9': 57,
      ':': 58,
      ';': 59,
      '<': 60,
      '=': 61,
      '>': 62,
      '?': 63,
      '@': 64,
      'A': 65,
      'B': 66,
      'C': 67,
      'D': 68,
      'E': 69,
      'F': 70,
      'G': 71,
      'H': 72,
      'I': 73,
      'J': 74,
      'K': 75,
      'L': 76,
      'M': 77,
      'N': 78,
      'O': 79,
      'P': 80,
      'Q': 81,
      'R': 82,
      'S': 83,
      'T': 84,
      'U': 85,
      'V': 86,
      'W': 87,
      'X': 88,
      'Y': 89,
      'Z': 90,
      '[': 91,
      '\\': 92,
      ']': 93,
      '^': 94,
      '_': 95,
      '`': 96,
      'a': 97,
      'b': 98,
      'c': 99,
      'd': 100,
      'e': 101,
      'f': 102,
      'g': 103,
      'h': 104,
      'i': 105,
      'j': 106,
      'k': 107,
      'l': 108,
      'm': 109,
      'n': 110,
      'o': 111,
      'p': 112,
      'q': 113,
      'r': 114,
      's': 115,
      't': 116,
      'u': 117,
      'v': 118,
      'w': 119,
      'x': 120,
      'y': 121,
      'z': 122,
      '{': 123,
      '|': 124,
      '}': 125,
      '~': 126,
      '\x7f': 127}

    def set_num_segments(self, num_segments):
        super(SpecialPhysicalDisplay, self).set_num_segments(num_segments)
        for segment in self._logical_segments:
            segment.separator = ' '

    def _build_inner_message(self, message):
        message = super(SpecialPhysicalDisplay, self)._build_inner_message(message)
        return flatten([g[:-1] for g in group(message, DISPLAY_BLOCK_LENGTH)])