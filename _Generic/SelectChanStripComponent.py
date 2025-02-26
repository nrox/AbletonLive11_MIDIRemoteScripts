# decompyle3 version 3.9.0
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: ..\..\..\output\Live\win_64_static\Release\python-bundle\MIDI Remote Scripts\_Generic\SelectChanStripComponent.py
# Compiled at: 2022-11-29 09:57:03
# Size of source mod 2**32: 1077 bytes
from __future__ import absolute_import, print_function, unicode_literals
from builtins import range
import _Framework.ChannelStripComponent as ChannelStripComponent

class SelectChanStripComponent(ChannelStripComponent):

    def __init__(self):
        ChannelStripComponent.__init__(self)

    def _arm_value(self, value):
        if self.is_enabled():
            track_was_armed = False
            if self._track != None:
                if self._track.can_be_armed:
                    track_was_armed = self._track.arm
            ChannelStripComponent._arm_value(self, value)
            if not self._track != None and self._track.can_be_armed or self._track.arm:
                if not track_was_armed:
                    if self._track.view.select_instrument():
                        self.song().view.selected_track = self._track