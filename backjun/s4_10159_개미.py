w, h = map(int, input().split())
y, x = map(int, input().split())
t = int(input())

x, y = x+t, y+t

max_x = h*2
max_y = w*2

x %= max_x
y %= max_y

if x > h :
    x=max_x-x
if y > w :
    y=max_y-y

print(y, x)