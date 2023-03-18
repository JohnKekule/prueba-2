#Cretate an function of sumatory of riemann

def riemann_sum(f, a, b, n):
    h = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + i * h)
    return s * h