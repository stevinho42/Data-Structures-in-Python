
class HashTable:
    def __init__(self, max_size=1) -> None:
        self.max_size = max_size
        self.data_list = [None] * max_size
        self.len = 0
        self.len_with_tombstones = 0


    def get_valid_index(self, key: str) -> int:
        idx = hash(key) % self.max_size

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
            self.len_with_tombstones += 1
        self.data_list[idx] = (key, value)
        self.dynamic_resizing()
        
    def delete(self, key: str) -> None:
        idx = self.get_valid_index(key)
        self.data_list[idx] = False
        self.len -= 1
        self.dynamic_resizing()

    
    def dynamic_resizing(self):
        
        if self.len_with_tombstones == self.max_size:
            self.max_size *= 2
        elif self.len < self.max_size /2 and self.len_with_tombstones > self.max_size:
            self.max_size /= 2
        else:
            return
        print("the current size of the hashmap is {} before dynamic resizing".format(self.len))
        kv = self.__iter__()
        self.data_list =[None] * self.max_size
        self.len = 0
        for key, value in kv:
            self.__setitem__(key, value)
            self.len += 1
        self.len_with_tombstones  = self.len
        print("the current size of the hashmap is {}  after dynamic resizing".format(self.len))
        
        
    def __iter__(self):
        return (x for x in self.data_list if x is not None or False)

    def __len__(self):
        return self.lena

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(str(kv[1]))), '  ') for kv in self if kv is not False]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)
