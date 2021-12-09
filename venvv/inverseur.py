from projet import solution


example_matrix = [[-1, -1, 1, 1, 1, -1, -1],
                  [-1, 1, 1, 1, 1, 1, -1],
                  [1, 1, 1, 0, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [1, 1, 1, 1, 1, 1, 1],
                  [-1, 1, 1, 1, 1, 1, -1],
                  [-1, -1, 1, 1, 1, -1, -1]]


def produceInverse(M):
    Mprime = []
    for i in M:
        MprimeX = []
        for j in i:
            if j == -1:
                MprimeX.append(-1)
            elif j == 0:
                MprimeX.append(1)
            else:
                MprimeX.append(0)
        Mprime.append(MprimeX)
    return Mprime


if __name__ == "__main__":
    Mstart = example_matrix
    Mprime = produceInverse(example_matrix)
    print(solution(Mstart, Mprime))