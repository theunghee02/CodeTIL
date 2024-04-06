def tanh(x):
    # Calculate e by solving exp(1)
    e = 2.71828
    #  이부분 지워야 함!!!!
    # for _ in range(9):
    #     e *= (1 + 1 / 9)
    # Calculate tanh using the formula
    return ((e ** x) - (e ** (-x))) / ((e ** x) + (e ** (-x)))


def ReLU(x):
    # ReLU 활성화 함수
    return max(0, x)


# Test the activation functions with some sample input values
if __name__ == "__main__":
    # Test tanh
    print("Testing tanh activation function:")
    print("tanh(0) =", tanh(0))
    print("tanh(1) =", tanh(1))
    print("tanh(-1) =", tanh(-1))

    # Test ReLU
    print("\nTesting ReLU activation function:")
    print("ReLU(0) =", ReLU(0))
    print("ReLU(1) =", ReLU(1))
    print("ReLU(-1) =", ReLU(-1))
