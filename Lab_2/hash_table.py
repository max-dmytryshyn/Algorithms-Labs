class HashTable:

    def __init__(self, length=8):
        self.array = [None for _ in range(length)]
        self.size = 0

    def hash(self, key):
        return hash(key) % len(self.array)

    def double_storage(self):
        new_hash_map = HashTable(len(self.array) * 2)
        for list in self.array:
            if list is None:
                continue
            for elem in list:
                new_hash_map.add(elem[0], elem[1])
        self.array = new_hash_map.array

    def add(self, key, value):
        index = self.hash(key)
        if self.array[index] is not None:
            for elem in self.array[index]:
                if elem[0] == key:
                    elem[1] = value
                    break
            else:
                self.array[index].append([key, value])

        else:
            self.array[index] = [[key, value]]

        self.size += 1
        load_factor = self.size / len(self.array)
        if load_factor > 2 / 3:
            self.double_storage()

    def get(self, key):
        index = self.hash(key)
        if self.array[self.hash(key)] is None:
            raise KeyError()

        else:
            for elem in self.array[index]:
                if elem[0] == key:
                    return elem[1]
            else:
                raise KeyError()

    def remove(self, key):
        index = self.hash(key)
        if self.array[index] is [None]:
            raise KeyError()

        else:
            for elem in self.array[index]:
                if elem[0] == key:
                    element_to_delete = elem
                    self.array[index].remove(elem)

                    if len(self.array[index]) == 0:
                        self.array[index] = None

                    return element_to_delete[1]
            else:
                raise KeyError()

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        return self.get(key)

