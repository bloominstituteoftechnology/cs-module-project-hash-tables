import hashlib
import random​

def hash_function(key):
    """
    Returns the low 32 bits of the md5 hash of the key.
    """
    # You don't need to understand this
    return int(hashlib.md5(str(key).encode()).hexdigest()[-8:],16)&0xffffffff​

def how_many_before_collision(buckets, loops=1):
    for i in range(loops):
        tries = 0
        tried = set()

        while True:
            random_key = random.random()
            index = hash_function(random_key) % buckets​

            if index not in tried:
                tried.add(index)
                tries += 1
            else:
                break​

        print(f"{buckets} buckets, {tries} before hash collision. ({tries / buckets * 100:.1f}% full)")​

how_many_before_collision(65536, 10)