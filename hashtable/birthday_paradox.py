import random
import hashlib

# bcrypt
# hashlib

# birthday paradox
# 'collision' of birthdays is more likely than our intuition


# can we avoid collisions by using a really big array?

# sha256 always produces a unique output, but we mod its output, so we still get collisions
def our_hash(key, num_buckets):
    key_bytes = f'{key}'.encode()
    hashed_key = int(hashlib.sha256(key_bytes).hexdigest(), 16)
    return hashed_key % num_buckets

def how_many_before_collision(num_buckets):
    hashed_keys = set()
    tries = 0
    while True:
        # make a bunch of random keys
        key = random.random()
        # hash them, modulo them by the number of buckets aka size of the array
        hashed_key = our_hash(key, num_buckets)

        if hashed_key in hashed_keys:
            break

        else:
        # see how far we get before we have a collision
            hashed_keys.add(hashed_key)
            tries += 1

    print(f'collision! Tries: {tries} before collision, that is {tries/num_buckets * 100}%')

# 8, 16, 32
how_many_before_collision(10000)