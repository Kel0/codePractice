class Node:
    def __init__(self):
        self._offset = 0
        self._offset_size = 2
        self._init_list = []

    def __resize(self):
        if len(self._init_list) >= self._offset_size:
            _val = len(self._init_list)
            if len(self._init_list) + 1 // 2 % 2 == 0:
                _val = len(self._init_list) + 1

            elif len(self._init_list) - 1 // 2 % 2 == 0:
                _val = len(self._init_list) - 1

            self._offset_size = _val * 2

        elif len(self._init_list) < self._offset_size // 2:
            self._offset_size //= 2
            self.__resize()

        if self._offset_size < 2:
            self._offset_size = 2

    def append(self, item):
        self._init_list.append(item)
        self.__resize()

    @property
    def list(self):
        return self._init_list

    def insert(self, key, value):
        self._init_list = self._init_list[:key] + [value] + self._init_list[key:]
        self.__resize()

    def remove(self, value):
        self._init_list = [e for e in self._init_list if e != value]
        self.__resize()
        return self._init_list

    def __iadd__(self, other):
        self._init_list += other
        self.__resize()
        return self

    def __sizeof__(self):
        return self._offset_size

    def __len__(self):
        return len(self._init_list)

    def __getitem__(self, index):
        return self._init_list[index]

    def __setitem__(self, key, value):
        self._init_list[key] = value
        self.__resize()

    def __delitem__(self, key):
        self._init_list = (
            (self._init_list[:key]) if key != 0 else [] + self._init_list[key + 1 :]
        )
        self.__resize()

    def __str__(self):
        return str(self._init_list)


class MutableArray:
    def __init__(self):
        self._node = Node()

    def append(self, item):
        self._node.append(item)

    def at(self, index):
        return self._node[index]

    def push(self, item):
        self._node.append(item)

    def size(self):
        return len(self._node)

    def capacity(self):
        return self._node.__sizeof__()

    def is_empty(self):
        return not bool(self.size())

    def insert(self, index, item):
        self._node.insert(index, item)

    def prepend(self, item):
        self._node[0] = item

    def pop(self):
        val = self._node[len(self._node) - 1]
        del self._node[len(self._node) - 1]
        return val

    def delete(self, index):
        del self._node[index]

    def remove(self, value):
        self._node.remove(value)

    def find(self, item):
        for idx, i in enumerate(self._node.list):
            if not i == item:
                continue
            return idx
        return -1

    def __iadd__(self, other):
        self._node += other
        return self

    def __getitem__(self, index):
        return self._node[index]

    def __str__(self):
        return self._node.__str__()
