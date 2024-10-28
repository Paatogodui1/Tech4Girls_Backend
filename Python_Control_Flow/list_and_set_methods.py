#!/usr/bin/python3
Names = ['Cletus', 'Samuel', 'Precious', 'Daniel', 'Louisa']
Names2 = ['Selina', 'Simon', 'Gladys', 'Michael', 'Mohammed']
#Using Append()
Names.append('Kate')
#Using remove()
Names.remove('Louisa')
#Using pop()
Names.pop()
#Using sort()
Names.sort()
#Using reverse()
Names.reverse()
#Using extend(). Extending Names with Names2
Names.extend(Names2)
print(Names)

Set = { 5, 3, 2, 8}
Set2= {2, 8, 10, 0}
#Using add()
Set.add(12)
#Using remove()
Set.remove(5)
print(Set)
#Using union()
print(Set.union(Set2))
#Using intersection()
print(Set.intersection(Set2))
#Using difference()
print(Set.difference(Set2))