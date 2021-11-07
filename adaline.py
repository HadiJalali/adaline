import random

# x1, x2, output
or_dataset = [(1, 1, 1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1)]

alpha = 0.1

print(f'{alpha} has been selected as learning rate value.')

w1 = round(random.random(), 2)
w2 = round(random.random(), 2)
bias = round(random.random(), 2)

print(f'{w1}, {w2} and {bias} has been selected for W1, W2 and Bias respectively.')

while True:
    lwg = []  # stores largest weight change
    for s in or_dataset:
        y = bias + s[0]*w1 + s[1]*w2
        new_bias = bias + alpha*(s[2] - y)
        new_w1 = w1 + alpha * s[0] * (s[2] - y)
        new_w2 = w2 + alpha * s[1] * (s[2] - y)
        lwg.append(max(abs(bias-new_bias), abs(w1-new_w1), abs(w2-new_w2)))
        print(f'Step ====  {or_dataset.index(s) + 1}  =====')
        print(f'bias = {new_bias}')
        print(f'w1 = {new_w1}')
        print(f'w2 = {new_w2}')
        #print(f'largest weight change is {lwg}')
        bias = new_bias
        w1 = new_w1
        w2 = new_w2
    if alpha > max(lwg):
        print("Algorithm converged successfully")
        print(f'bias = {bias}')
        print(f'w1 = {w1}')
        print(f'w2 = {w2}')
        break

# Test
for t in or_dataset:
    result = 1
    y = bias + t[0]*w1 + t[1]*w2
    if y >= 0:
        result = 1
    else:
        result = -1
    print(result == t[2])
