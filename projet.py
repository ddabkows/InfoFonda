from pysat.solvers import Minisat22
# from pysat.solvers import Glucose4
from pysat.formula import CNF
from pysat.formula import IDPool


def getSize(M):
    """
    Function that outputs the number of 1's in a Solitaire board
    :param M: Matrix of matrices
    :return: The number of 1's on the board
    """
    size = 0
    for row in M:
        for column in row:
            if column == 1:
                size += 1
    return size


def generateBeginEndFormula(M, cnf, vpool, time):
    """
    Function that generates the clauses matching to the begin or the end matrix
    :param M: Matrix to be compared to
    :param cnf: The CNF formula
    :param vpool: The tool to pool the clauses
    :param time: The moment at which the formula is generated
    :return: The CNF formula
    """
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] == 1:
                cnf.append([vpool.id((i, j, time))])
            elif M[i][j] == 0:
                cnf.append([-vpool.id((i, j, time))])
    return cnf


def generateAllMoves(M):
    """
    Function that generates all possible moves
    :param M: A matrix from which everything is generated
    :return: All possible moves (not mandatory to be realisable at that moment)
    """
    possibleMoves = []
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j] != -1:
                # Verify if it is legal to make a horizontal move
                if j + 1 < len(M[i]) and M[i][j + 1] != -1:
                    if j + 2 < len(M[i]) and M[i][j + 2] != -1:
                        moveToAddA = []
                        moveToAddB = []
                        for k in range(j, j + 3):
                            moveToAddA.append((i, k))
                        for k in range(j + 2, j - 1, -1):
                            moveToAddB.append((i, k))
                        possibleMoves.append(moveToAddA)
                        possibleMoves.append(moveToAddB)
                # Verify if it is legal to make a vertical move
                if i + 1 < len(M) and M[i + 1][j] != -1:
                    if i + 2 < len(M) and M[i + 2][j] != -1:
                        moveToAddA = []
                        moveToAddB = []
                        for k in range(i, i + 3):
                            moveToAddA.append((k, j))
                        for k in range(i + 2, i - 1, -1):
                            moveToAddB.append((k, j))
                        possibleMoves.append(moveToAddA)
                        possibleMoves.append(moveToAddB)
    return possibleMoves


def generateFormulaBody(cnf, vpool, possibleMoves, Mstart, steps):
    """
    Function that generates all the intermediate matrices formula
    :param cnf: CNF formula to verify
    :param vpool: Maping tool
    :param possibleMoves: All the moves that are possible
    :param Mstart: Starting matrix used for the lengths
    :param steps: Number of steps to perform
    :return: The generated formula for the SAT solver
    """
    for t in range(1, steps + 1):
        d = []
        for i in range(len(possibleMoves)):
            d.append(vpool.id((i, t)))
        cnf.append(d)
        for i in range(len(possibleMoves)):
            # Formulas for i(see report)
            cnf.append([-vpool.id((i, t)), vpool.id((possibleMoves[i][0][0],
                                                     possibleMoves[i][0][1],
                                                     t - 1))])
            cnf.append([-vpool.id((i, t)), -vpool.id((possibleMoves[i][0][0],
                                                      possibleMoves[i][0][1],
                                                      t))])
            # Formulas for j (see report)
            cnf.append([-vpool.id((i, t)), vpool.id((possibleMoves[i][1][0],
                                                     possibleMoves[i][1][1],
                                                     t - 1))])
            cnf.append([-vpool.id((i, t)), -vpool.id((possibleMoves[i][1][0],
                                                      possibleMoves[i][1][1],
                                                      t))])
            # Formulas for k (see report)
            cnf.append([-vpool.id((i, t)), -vpool.id((possibleMoves[i][2][0],
                                                      possibleMoves[i][2][1],
                                                      t - 1))])
            cnf.append([-vpool.id((i, t)), vpool.id((possibleMoves[i][2][0],
                                                     possibleMoves[i][2][1],
                                                     t))])
            for row in range(len(Mstart)):
                for column in range(len(Mstart[row])):
                    if (row, column) not in possibleMoves[i]:
                        # Formulas for n != i, j, k
                        cnf.append([-vpool.id((i, t)), -vpool.id((row,
                                                                  column,
                                                                  t - 1)),
                                    vpool.id((row, column, t))])
                        cnf.append([-vpool.id((i, t)), vpool.id((row, column, t - 1)),
                                    -vpool.id((row, column, t))])
    return cnf


def solution(Mstart, Mprime):
    """
    Function that verifies if it is possible to go from a Solitaire board
    M to a board M'
    :param Mstart: The starting matrix
    :param Mprime: The ending matrix
    :return: Boolean (True if it is possible to go from M to M')
    """

    vpool = IDPool(start_from=1)
    cnf = CNF()

    steps = getSize(Mstart) - getSize(Mprime)
    if steps <= 0:
        return False

    possibleMoves = generateAllMoves(Mstart)

    cnf = generateBeginEndFormula(Mstart, cnf, vpool, 0)

    cnf = generateFormulaBody(cnf, vpool, possibleMoves, Mstart, steps)

    cnf = generateBeginEndFormula(Mprime, cnf, vpool, steps)

    s = Minisat22(use_timer=True)
    s.append_formula(cnf.clauses, no_return=False)
    result = s.solve()
    if result:
        return True
    else:
        return False


if __name__ == "__main__":
    p = [[1, 0, 0], [1, 0, 0], [0, 1, 0]]
    q = [[0, 0, 0], [0, 0, 0], [0, 0, 1]]
    solution(p, q)
