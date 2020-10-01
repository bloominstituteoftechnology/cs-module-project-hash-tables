# Your code here
myfile = 'applications/histo/robin.txt'
def word_freq_graph(filepath):
    graph = 'Words                  Frequency (Once per #)\n'
    with open(myfile) as f:
        s = f.read()
    filters = ['"', ':', ',', '.', '-', '+', '=', '/', '\\', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', ';','\r','\n','\t','\t','\r','\n']

    for i in filters:
        s = s.replace(i, '')
    s = s.lower().split(' ')
    count = {}
    for i in s:
        if i not in count:
            count[i] = 0
        count[i] += 1
    if '' in count:
        del count['']
    sa = sorted(sorted(count.items(),key=lambda z: z[0]),key=lambda z: z[1], reverse=True)
    for i in sa:
        freq = f'{i[1]}|' + ('#' * i[1])
        word = i[0] + ((20 - len(i[0]) - len(str(i[1]))) * ' ')
        graph += f'{word}\t{freq}\n'

    print(graph)
word_freq_graph(myfile)