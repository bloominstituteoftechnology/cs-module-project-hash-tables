import time

def sort_hash(value):
  total = 0
  for char in value:
    total += ord(char)
  return total

def text_alignment(longest, value):
  add_spaces = len(longest) - len(value)
  add_spaces += 2
  value += (" " * add_spaces)
  return value

def create_histogram(input_file: str):
  ignore = '":;,.-+=/\|[]{}()*^&'
  histogram_dict = {}
  with open(input_file) as f:
    words = f.read()
  words_list = words.split()
  longest = words_list[0]
  for word in words_list:
    if len(word) > len(longest):
      longest = word
    for char in word:
      if char in ignore:
        word = word.replace(char, "")
    if histogram_dict.__contains__(word):
      histogram_dict[word] += "#"
    else:
      histogram_dict.setdefault(word.lower(), "#")
  sorted_items = list(histogram_dict.items())
  sorted_items.sort(key = lambda x: (-sort_hash(x[1]), x[0]))
  for (x, y) in sorted_items:
    print(f"{text_alignment(longest, x)} {y}")

start_time = time.time()
create_histogram("./applications/histo/robin.txt")
end_time = time.time()
print(f"\n\nMy solutiontook: {end_time - start_time}\n\n")
    
            
          


