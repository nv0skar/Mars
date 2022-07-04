# Mars | Save and load values magically
# Copyright (C) 2022 Oscar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from . import types
import json
import plistlib

class handler:
    def __init__(self, typeFile, path):
        self.type = typeFile
        self.path = path

    def dump(self, data):
        if self.type == types.json:
            with open(self.path, "w") as f:
                json.dump(data, f)
        elif self.type == types.plist:
            with open(self.path, "wb") as f:
                plistlib.dump(data, f)

    def load(self):
        if self.type == types.json:
            with open(self.path, "r") as f:
                return json.load(f)
        elif self.type == types.plist:
            with open(self.path, "rb") as f:
                return plistlib.load(f)
