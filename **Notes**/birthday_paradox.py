
# What is the birthday paradox?
## sharing common birthday is surprisingly likely
## if 20 people, 20/365 == 2/36 == 1/18 --> 5%
## if 20 people, actually close to 50%
## 60/365 --> at least two collisions!

# Similarly, collisions are surprisingly likely!
## making array bigger will help but not solve

import random
import hashlib

def our_hash_function(random_key):
    # turn random key into a string so we can encode()
    # put the bytes through sha256
    # get out the hash (hexdigest)
    # turn back into base-10 number
    return int(hashlib.sha256(f"{random_key}".encode()).hexdigest(), 16)

def how_many_before_collision(length_of_list):

    all_indices = set()
    collision = False

    indices_made = 0
    
    # see how far we get before we have a collision
    while not collision:
        # make a bunch of random keys
        random_key = random.random()
        # hash them, modulo them, and keep track of these indices
        hashed_key = our_hash_function(random_key)

        new_index = hashed_key % length_of_list

        if new_index in all_indices:
            # exit while loop if we already made this key == collision
            collision = True
        
        # otherwise track our new index
        all_indices.add(new_index)
        indices_made += 1

    print(f"Hashes before collision: {indices_made}, buckets: {length_of_list}, load factor: {indices_made/length_of_list * 100}")


how_many_before_collision(4096)