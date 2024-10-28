#!/usr/bin/python3
Names = ['Cletus', 'Samuel', 'Precious', 'Daniel', 'Louisa']
Names2 = ['Selina', 'Simon', 'Gladys', 'Michael', 'Mohammed']
Names.append('Kate')
Names.remove('Louisa')
Names.pop()
Names.sort()
Names.reverse()
Names.extend(Names2)
print(Names)

Set = { 5, 3, 2, 8}
Set2= {2, 8, 10, 0}
Set.add(12)
Set.remove(5)
print(Set)
print(Set.union(Set2))
print(Set.intersection(Set2))
print(Set.difference(Set2))