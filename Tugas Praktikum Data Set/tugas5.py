A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}

#Program A symmetric difference B
print('A komplemen B = ', A ^ B)
#Program B symmetric difference A
print('B komplemen A = ', B ^ A)
#Program A symmetric difference C
print('A komplemen C = ', A.symmetric_difference(C))
#Program B symmetric difference C
print('B komplemen C = ', B.symmetric_difference(C))