points = [(2,1),(1,2)]

def f(w):
    return sum([(w * x - y)**2 for x,y in points])
    
def df(w):
    return sum([2 * (w * x - y) * x for x,y in points])

# Gradient Descent
w = 0 
eta =  0.01
for t in range(100):
    value = f(w)
    
    gradient = df(w)
    w = w - eta * gradient
    print(f'iteration: {t},w : {w},F(w): {value}')
