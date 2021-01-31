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

from . import file

types = ["json", "plist"]

class object:
    def __init__(self, path, typeN=types):
        self.path = path
        self.type = types[typeN]

class mars:
    def __init__(self, key, value, object):
        self.__value = value
        self.__default = value
        self.key = key
        self.file = file.handler(object.type, object.path)
        try:
            open(object.path)
        except:
            self.__create()
        try:
            self.__fetch(True)
        except:
            pass

    def __create(self):
        self.file.dump({})

    def __put(self, file_struct=None, add=False, value=None, brute=False):
        if add:
            file_struct.update({self.key: value})
        if brute:
            file_struct = {self.key: value}
        self.file.dump(file_struct)

    def __dump(self, value=None):
        try:
            file_struct = self.file.load()
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
            file_struct = self.file.load()
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