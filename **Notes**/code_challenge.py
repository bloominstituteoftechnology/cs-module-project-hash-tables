arr = ['Waltz', 'Tango', 'Viennese Waltz', 'Foxtrot', 'Cha Cha', 'Samba', 'Rumba', 'Paso Doble', 'Jive']

sort = sorted(arr)
for elem in sorted(arr):
  print(elem)
  
print('\n')

print(*sorted(arr), sep='\n')