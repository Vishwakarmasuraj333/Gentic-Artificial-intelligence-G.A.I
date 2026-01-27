# Generate AND/NOT function using McCulloch-Pitts neural net.

num_ip = int(input("Enter the number of inputs : "))

w1 = 1
w2 = 1

print("For the", num_ip, "inputs calculate the net input using yin = x1w1 + x2w2")

x1 = []
x2 = []

for j in range(num_ip):
    ele1 = int(input("x1 = "))
    ele2 = int(input("x2 = "))
    x1.append(ele1)
    x2.append(ele2)

print("x1 =", x1)
print("x2 =", x2)

n = []
m = []

for i in range(num_ip):
    n.append(x1[i] * w1)
    m.append(x2[i] * w2)

Yin = []
for i in range(num_ip):
    Yin.append(n[i] + m[i])

print("Yin (AND) =", Yin)

Yin = []
for i in range(num_ip):
    Yin.append(n[i] - m[i])

print("Yin (NOT) =", Yin)

Y = []
for i in range(num_ip):
    if Yin[i] >= 1:
        Y.append(1)
    else:
        Y.append(0)

print("Output Y =", Y)
