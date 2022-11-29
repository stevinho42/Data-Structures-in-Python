MAX_SIZE = 5_000

class HashTable:
    def __init__(self, max_size=MAX_SIZE) -> None:
        self.data_list = [None] * max_size
        self.len = 0


    def get_valid_index(self, key: str) -> int:
        idx = hash(key) % MAX_SIZE

        while True:
            if self.data_list[idx] is None:
                return idx
            k, v = self.data_list[idx]
            if k == key:
                if v is not False:
                    return idx
            
            idx += 1
            if idx == len(self.data_list):
                idx = 0


    def __getitem__(self, key: str) -> str:
        idx = self.get_valid_index(key)
        if idx is not None:
            kv = self.data_list[idx]
            return kv[1]
        else:
            raise IndexError("Index not found")
    
    def __setitem__(self, key:str , value: str) -> None:
        idx = self.get_valid_index(key)
        if self.data_list[idx] is None:
            self.len += 1
        self.data_list[idx] = (key, value)

    def delete(self, key: str, value: str) -> None:
        idx = self.get_valid_index(key)
        self.data_list[idx] = False
        self.len -= 1

        
    def __iter__(self):
        return (x for x in self.data_list if x is not None or False)

    def __len__(self):
        return self.len

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)
