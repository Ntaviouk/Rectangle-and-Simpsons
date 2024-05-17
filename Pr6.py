import math


def Func(x):
    return math.e ** x + math.cos(x)


def rectangle(A, B, N):
    M = 0
    S = 0
    H = (B - A) / N
    X = A - (H / 2)

    while M != N:
        X = X + H
        F = Func(X)
        S = S + F
        M = M + 1

    I = S * H
    print(I)


def Simpson(A, B, M, ε):
    K = M
    while True:
        H = (B - A) / (2 + M)
        N = 0
        T = A
        F = Func(T)
        I = F

        while True:
            T = T + H
            F = Func(T)
            I = I + H * F
            N += 1
            if M == N:
                break
            else:
                T = T + H
                F = Func(T)
                I = I + 2 * F

        T = B
        F = Func(T)
        I = H * (I + F) / 3

        if M == K:
            U = I
            M = M + M
        else:
            R = (I - U) / 16
            if abs(R) > ε:
                U = I
                M = M + M
            else:
                I = I + R
                print(I, R)
                break


if __name__ == "__main__":
    print("Метод Середніх Прямокутників")
    rectangle(0, 1, 5)
    print("\n\nМетод Сімпсона")
    Simpson(0, 1, 5, 0.5 * 10 ** -6)
