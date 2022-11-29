from optimized_hashmap import HashTable


if __name__ == "__main__":
    table = HashTable()
    table['a'] = 10
    print(table)
    table['b'] = 20
    print(table)
    table['c'] = 20
    print(table)
    table['d'] = 20
    print(table)
    table['e'] = 20
    print(table)
    table.delete('a')
    print(table)
    table.delete('b')
    print(table)
    table.delete('c')
    print(table)