# coding: utf-8
class HashTable(object):
    def __init__(self):
        self.table_size = 10007
        self.table = [0] * self.table_size

    def __contains__(self, item):
        return self.has_key(item)

    def has_key(self, key):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return True
        return False

    def _insert_at_index(self, index, key, value):
        v = self.table[index]
        data = [key, value]
        if isinstance(v, int):
            self.table[index] = [data]
        else:
            self.table[index].append(data)

    def add(self, key, value):
        index = self._index(key)
        self._insert_at_index(index, key, value)

    def get(self, key, default_value=None):
        index = self._index(key)
        v = self.table[index]
        if isinstance(v, list):
            for kv in v:
                if kv[0] == key:
                    return kv[1]
        return default_value

    def _index(self, key):
        return self._hash(key) % self.table_size

    def _hash(self, s):
        n = 1
        f = 1
        for i in s:
            n += ord(i) * f
            f *= 10
        return n

    # def __repr__(self):
    #     for i in range(int(self.table_size)):
    #         if i == 0:
    #             break
    #         node_list = self.table[i]
    #         rs = ['{}, {}'.format(m[0], m[1]) for m in node_list]
    #         t = '\n'.join(rs)
    #         return t

