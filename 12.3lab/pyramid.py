import math

def volume(a, b, h):
    S1 = a**2 * math.sqrt(3) / 4
    S2 = b**2 * math.sqrt(3) / 4
    V = h * (S1 + S2 + math.sqrt(S1 * S2)) / 3
    return V

def area(a, b, h):
    S1 = a**2 * math.sqrt(3) / 4
    S2 = b**2 * math.sqrt(3) / 4

    r1 = a * math.sqrt(3) / 6
    r2 = b * math.sqrt(3) / 6

    l = math.sqrt(h**2 + (r1 - r2)**2)

    P1 = 3 * a
    P2 = 3 * b

    S = S1 + S2 + (P1 + P2) * l / 2
    return S