array = [ [ 0 for i in xrange(5) ] for j in xrange(5) ]
n = 1
x, y = 0, 0
v = 1, 0
array[y][x] = n
while 1:
    x, y = x+v[0] , y+v[1]
    if x < 0 or x > 4 or y < 0 or y > 4 or array[y][x] != 0:
        x, y = x-v[0] , y-v[1]
        v = -v[1], v[0] # velocity vector +90 degree rotation
        x, y = x+v[0] , y+v[1]
    n+=1
    array[y][x] = n
    if n == 25:
        break
for y in xrange(5):
    for x in xrange(5):
        print "%2d"%array[y][x],
    print