def search_min(mas, n_row, n):
    n_min = n_row
    tmp_min = 0
    i = n_min
    while tmp_min == 0:
        if mas[i] != 0:
            tmp_min = mas[i]
            n_min = i
        i += 1

    for i in range(i, n):
        if abs(mas[i]) < abs(tmp_min) and mas[i] != 0:
            tmp_min = mas[i]
            n_min = i
    return n_min

def step_metod(n_min, n_row, a, m, n):
    for i in range(n_row, m + 1):
        if i != n_min:
            koef = a[n_row][i] / a[n_row][n_min]
            for j in range(n_row, m + n):
                a[j][i] -= koef * a[j][n_min]

def status(mas, n_row, m):
    l = 0
    for i in range(n_row, m + 1):
        if mas[n_row][i] != 0:
            l += 1
    return l

def change_col(a, n_row, n_col, n_min, n, m):
    for i in range(n_row, n + m):
        a[i][n_col], a[i][n_min] = a[i][n_min], a[i][n_col]

def main():
    n, m = map(int, input().split())
    a = [[0] * (m + 1) for _ in range(m + n)]

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            a[i][j] = row[j]
        a[i][m] = -row[m]

    for i in range(n, m + n):
        for j in range(m + 1):
            if i - n == j:
                a[i][j] = 1
            else:
                a[i][j] = 0

    n_min = 0
    flag = 0
    n_row = 0
    n_col = 0
    k = 0

    while n_row < n and n_col < m:
        flag = status(a, n_row, m)
        if flag == 2:
            n_min = search_min(a[n_row], n_row, m)
        if flag == 1 and a[n_row][m] == 0:
            if n_col != n_min:
                change_col(a, n_row, n_col, n_min, n, m)
            n_row += 1
            n_col += 1
        elif flag == 2 and a[n_row][m] != 0 and n_row < n and a[n_row][m] % a[n_row][n_min] != 0:
            k = -1
            n_row = m + 1
        elif flag == 0:
            n_row += 1
        else:
            n_min = search_min(a[n_row], n_row, m)
            if n_min == m:
                k = -1
                n_row = m + 1
            step_metod(n_min, n_row, a, m, n)

    if m < n:
        tmp_flag = 0
        for i in range(n_row, n):
            if a[i][m] != 0:
                tmp_flag = 1
                break
        if tmp_flag == 1:
            k = -1

    if k == -1:
        print("NO")
    else:
        k = m - n_col
        print(k)
        for i in range(n, m + n):
            print(a[i][m], end="")
            for j in range(m - k, m):
                print("", a[i][j], end="")
            print()

if __name__ == "__main__":
    main()