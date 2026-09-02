import sys

def int_div(a, b):
    # Целочисленное деление с усечением к нулю
    res = abs(a) // abs(b)
    if (a < 0) ^ (b < 0):
        res = -res
    return res

def solve(N, M, A, B_vec):
    # Формируем расширенную матрицу B
    # B имеет N + M строк и M + 1 столбцов
    B = []
    for i in range(N):
        row = A[i] + [B_vec[i]]
        B.append(row)
    for i in range(M):
        row = [1 if i == j else 0 for j in range(M)] + [0]
        B.append(row)
        
    R = 0
    for i in range(min(N, M)):
        # Проверяем, есть ли ненулевой элемент в подматрице B[i...N-1][i...M-1]
        found = False
        for r in range(i, N):
            for c in range(i, M):
                if B[r][c] != 0:
                    found = True
                    # Меняем местами строки r и i
                    B[i], B[r] = B[r], B[i]
                    break
            if found: break
            
        if not found:
            break
            
        R += 1
        
        while True:
            # Ищем столбец j от i до M-1 с наименьшим по модулю ненулевым элементом в строке i
            min_val = None
            min_col = -1
            for j in range(i, M):
                if B[i][j] != 0:
                    if min_val is None or abs(B[i][j]) < min_val:
                        min_val = abs(B[i][j])
                        min_col = j
                        
            # Меняем местами столбцы min_col и i
            for r in range(N + M):
                B[r][i], B[r][min_col] = B[r][min_col], B[r][i]
                
            pivot = B[i][i]
            
            # Зануляем остальные столбцы ПЕРЕМЕННЫХ в строке i
            for j in range(i+1, M):
                if B[i][j] != 0:
                    q = int_div(B[i][j], pivot)
                    for r in range(N + M):
                        B[r][j] -= q * B[r][i]
                        
            # Проверяем, занулились ли все столбцы переменных от i+1 до M-1
            if all(B[i][j] == 0 for j in range(i+1, M)):
                break
                
        # Теперь pivot содержит НОД коэффициентов текущей строки
        pivot = B[i][i]
        
        # Проверяем делимость свободного члена (последнего столбца) на НОД
        if B[i][M] % pivot != 0:
            return "NO SOLUTIONS"
            
        # Зануляем значение в столбце свободного члена для текущей строки
        q = B[i][M] // pivot
        for r in range(N + M):
            B[r][M] -= q * B[r][i]

    # Проверяем, остались ли ненулевые элементы в столбце свободных членов для нулевых строк уравнений
    for i in range(R, N):
        if B[i][M] != 0:
            return "NO SOLUTIONS"

    # Вычисляем количество свободных переменных и формируем ответ
    K = M - R
    res = [str(K)]
    for r in range(M):
        line = []
        for v in range(R, M):
            line.append(str(B[N + r][v]))
        line.append(str(B[N + r][M]))
        res.append(" ".join(line))
        
    return "\n".join(res)

def main():
    # Считываем весь ввод
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    M = int(input_data[1])
    
    A = []
    B = []
    
    idx = 2
    for i in range(N):
        row = []
        for j in range(M):
            row.append(int(input_data[idx]))
            idx += 1
        A.append(row)
        B.append(int(input_data[idx]))
        idx += 1
        
    result = solve(N, M, A, B)
    print(result)

if __name__ == '__main__':
    main()
