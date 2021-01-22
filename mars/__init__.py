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

class object:
    def __init__(self, path):
        self.path = path

class mars:
    def __init__(self, key, value, object):
        self.path = object.path
        self.__value = value
        self.__default = value
        self.key = key
        try:
            open(self.path)
        except:
            self.__create()
        try:
            self.__fetch(True)
        except:
            pass

    def __create(self):
        with open(self.path, 'w') as f:
            json.dump({}, f)

    def __put(self, file_json=None, add=False, value=None, brute=False):
        with open(self.path, 'w') as f:
            if add:
                file_json.update({self.key: value})
            if brute:
                file_json = {self.key: value}
            json.dump(file_json, f)

    def __dump(self, value=None):
        try:
            file_json = json.load(open(self.path))
        except:
            self.__put(value=value,brute=True)
            return
        for x in file_json:
            if x == self.key:
                file_json[x] = value
                self.__put(file_json)
                return
        if not file_json:
            self.__put(file_json, True, value)

    def __fetch(self, brute=False):
        try:
            file_json = json.load(open(self.path))
        except:
            return
        for x in file_json:
            if x == self.key:
                if brute:
                    self.__value = file_json[x]
                    return
                if self.__value != file_json[x]:
                    return
                self.__value = file_json[x]
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