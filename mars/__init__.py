# Mars | Save and load variables magically
# Copyright (C) 2021 ItsTheGuy
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

import json
import plistlib

types = ["json", "plist"]

class object:
    def __init__(self, path, typeN=types):
        self.path = path
        self.type = types[typeN]

class mars:
    def __init__(self, key, value, object):
        self.path = object.path
        self.__value = value
        self.__default = value
        self.key = key
        self.type = object.type
        try:
            open(self.path)
        except:
            self.__create()
        try:
            self.__fetch(True)
        except:
            pass

    def __get_method(self):
        if self.type == "json":
            return json
        elif self.type == "plist":
            return plistlib

    def __open_param(self, read=False):
        if self.type == "json":
            if read:
                return "r"
            else:
                return "w"
        elif self.type == "plist":
            if read:
                return "rb"
            else:
                return "wb"

    def __create(self):
        with open(self.path, self.__open_param()) as f:
            self.__get_method().dump({}, f)

    def __put(self, file_struct=None, add=False, value=None, brute=False):
        with open(self.path, self.__open_param()) as f:
            if add:
                file_struct.update({self.key: value})
            if brute:
                file_struct = {self.key: value}
            self.__get_method().dump(file_struct, f)

    def __dump(self, value=None):
        try:
            with open(self.path, mode=self.__open_param(True)) as f:
                file_struct = self.__get_method().load(f)
        except:
            self.__put(value=value,brute=True)
            return
        for x in file_struct:
            if x == self.key:
                file_struct[x] = value
                self.__put(file_struct)
                return
        self.__put(file_struct, True, value)

    def __fetch(self, brute=False):
        try:
            with open(self.path, mode=self.__open_param(True)) as f:
                file_struct = self.__get_method().load(f)
        except:
            return
        for x in file_struct:
            if x == self.key:
                if brute:
                    self.__value = file_struct[x]
                    return
                if self.__value != file_struct[x]:
                    return
                self.__value = file_struct[x]
                return

    def set(self, value):
        try:
            self.__dump(value)
        except:
            return
        self.__value = value
        pass

    def get(self):
        try:
            self.__fetch()
        except:
            return self.__default
        return self.__value