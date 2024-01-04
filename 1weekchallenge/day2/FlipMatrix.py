def flippingMatrix(matrix):
    total = 0
    # n is the nxn dimension of the wanted submatrix (second given input)
    for i in range(n):
        for j in range(n):

            total += max(matrix[i][j], matrix[i][-j-1],
                         matrix[-i-1][j], matrix[-i-1][-j-1])
    print(total)
    return(total)


if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)
