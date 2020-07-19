# given a list of records, able to quickly report everyone in a particular category

records = [
    ("Corey", "iOS"),
    ("Tyler", "DS"),
    ("Anika", "DS"),
    ("Jenna", "Web"),
    ("Leighton", "Web"),
    ("Nico", "Web"),
    ("Carl", "Web"),
    ("Michael", "iOS")
]

def build_index(records):
    index = {}
    
    #loop over records
    # key is track
    # value is list of names
    
    for record in records:
        name, track = record
    
        if track not in index:
            index[track] = []
        index[track].append(name)
    return index

index = build_index(records)

for track in index:
    print(track)
        
print(index["Web"])

# how to handle updated records?
# update the index directly, as each record or batch of records
# loop over records every once in a while, and handle deduplication


