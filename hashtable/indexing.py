

records = [
    ("Tara", "Web"),
    ("Kyle", "Web"),
    ("Adrian", "Web"),
    ("Janessa", "Web"),
    ("Mike", "Web"),
    ("Cai", "DS"),
    ("Chris", "DS"),
    ("Craig", "iOS")
]

# how could we show in O(1) time everyone in a particular track?

# build an index, or indexing on an attribute

# index on the track: make the track the key, have as value a list, append the names to the list

def build_index(records):
    idx = {}
    for name, track in records:
        if track in idx:
            idx[track].append(name)

        else:
            idx[track] = [name]

    return idx

# index the data on an attribute: rooms in a house, pools

indexed_records = build_index(records)

print(indexed_records['DS'])
print(indexed_records['Web'])
print(indexed_records['iOS'])