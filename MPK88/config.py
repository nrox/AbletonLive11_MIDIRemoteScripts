# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\MPK88\config.py
# Compiled at: 2022-11-29 09:57:03
# Size of source mod 2**32: 5222 bytes
from __future__ import absolute_import, print_function, unicode_literals
from .consts import *
TRANSPORT_CONTROLS = {
  'STOP': GENERIC_STOP,
  'PLAY': GENERIC_PLAY,
  'REC': GENERIC_REC,
  'LOOP': GENERIC_LOOP,
  'RWD': GENERIC_RWD,
  'FFWD': GENERIC_FFWD,
  'NORELEASE': 0}
DEVICE_CONTROLS = (
 (
  GENERIC_ENC1, 0),
 (
  GENERIC_ENC2, 0),
 (
  GENERIC_ENC3, 0),
 (
  GENERIC_ENC4, 0),
 (
  GENERIC_ENC5, 0),
 (
  GENERIC_ENC6, 0),
 (
  GENERIC_ENC7, 0),
 (
  GENERIC_ENC8, 0))
VOLUME_CONTROLS = (
 (
  GENERIC_SLI1, 0),
 (
  GENERIC_SLI2, 0),
 (
  GENERIC_SLI3, 0),
 (
  GENERIC_SLI4, 0),
 (
  GENERIC_SLI5, 0),
 (
  GENERIC_SLI6, 0),
 (
  GENERIC_SLI7, 0),
 (
  GENERIC_SLI8, 0))
TRACKARM_CONTROLS = (
 GENERIC_BUT1,
 GENERIC_BUT2,
 GENERIC_BUT3,
 GENERIC_BUT4,
 GENERIC_BUT5,
 GENERIC_BUT6,
 GENERIC_BUT7,
 GENERIC_BUT8)
BANK_CONTROLS = {
  'TOGGLELOCK': GENERIC_BUT9,
  'BANKDIAL': -1,
  'NEXTBANK': GENERIC_PAD5,
  'PREVBANK': GENERIC_PAD1,
  'BANK1': -1,
  'BANK2': -1,
  'BANK3': -1,
  'BANK4': -1,
  'BANK5': -1,
  'BANK6': -1,
  'BANK7': -1,
  'BANK8': -1}
PAD_TRANSLATION = ((0, 0, 81, 1), (1, 0, 83, 1), (2, 0, 84, 1), (3, 0, 86, 1), (0, 1, 74, 1),
                   (1, 1, 76, 1), (2, 1, 77, 1), (3, 1, 79, 1), (0, 2, 67, 1), (1, 2, 69, 1),
                   (2, 2, 71, 1), (3, 2, 72, 1), (0, 3, 60, 1), (1, 3, 62, 1), (2, 3, 64, 1),
                   (3, 3, 65, 1))
CONTROLLER_DESCRIPTION = {
  'INPUTPORT': 'Akai MPK88',
  'OUTPUTPORT': 'Akai MPK88',
  'CHANNEL': 0,
  'PAD_TRANSLATION': PAD_TRANSLATION}
MIXER_OPTIONS = {
  'NUMSENDS': 2,
  'SEND1': (-1, -1, -1, -1, -1, -1, -1, -1),
  'SEND2': (-1, -1, -1, -1, -1, -1, -1, -1),
  'MASTERVOLUME': -1}