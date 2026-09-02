import sys

def int_div(a, b):
    res = abs(a) // abs(b)
    if (a < 0) ^ (b < 0):
        res = -res
    return res

def solve(N, M, A, B):
    Q = [[1 if i == j else 0 for j in range(M)] for i in range(M)]
    
    for i in range(min(N, M)):
        while True:
            row_zero = all(A[i][j] == 0 for j in range(i+1, M))
            col_zero = all(A[k][i] == 0 for k in range(i+1, N))
            if row_zero and col_zero:
                if A[i][i] == 0:
                    found = False
                    for r in range(i, N):
                        for c in range(i, M):
                            if A[r][c] != 0:
                                A[i], A[r] = A[r], A[i]
                                B[i], B[r] = B[r], B[i]
                                for k in range(N):
                                    A[k][i], A[k][c] = A[k][c], A[k][i]
                                for k in range(M):
                                    Q[k][i], Q[k][c] = Q[k][c], Q[k][i]
                                found = True
                                break
                        if found: break
                    if not found:
                        break
                else:
                    break
            
            if A[i][i] == 0:
                found = False
                for r in range(i, N):
                    for c in range(i, M):
                        if A[r][c] != 0:
                            A[i], A[r] = A[r], A[i]
                            B[i], B[r] = B[r], B[i]
                            for k in range(N):
                                A[k][i], A[k][c] = A[k][c], A[k][i]
                            for k in range(M):
                                Q[k][i], Q[k][c] = Q[k][c], Q[k][i]
                            found = True
                            break
                    if found: break
            
            changed = False
            for j in range(i+1, M):
                if A[i][j] != 0:
                    q = int_div(A[i][j], A[i][i])
                    for k in range(N):
                        A[k][j] -= q * A[k][i]
                    for k in range(M):
                        Q[k][j] -= q * Q[k][i]
                    if A[i][j] != 0:
                        for k in range(N):
                            A[k][i], A[k][j] = A[k][j], A[k][i]
                        for k in range(M):
                            Q[k][i], Q[k][j] = Q[k][j], Q[k][i]
                    changed = True
                    break
            
            if changed: continue
            
            for k in range(i+1, N):
                if A[k][i] != 0:
                    q = int_div(A[k][i], A[i][i])
                    for c in range(M):
                        A[k][c] -= q * A[i][c]
                    B[k] -= q * B[i]
                    if A[k][i] != 0:
                        A[i], A[k] = A[k], A[i]
                        B[i], B[k] = B[k], B[i]
                    changed = True
                    break
            
            if changed: continue

    free_vars = []
    Y_fixed = [0] * M
    for i in range(N):
        if i < M:
            aii = A[i][i]
        else:
            aii = 0
            
        if aii == 0:
            if B[i] != 0:
                return "NO SOLUTIONS"
        else:
            if B[i] % aii != 0:
                return "NO SOLUTIONS"
            Y_fixed[i] = B[i] // aii

    for j in range(M):
        if j >= N or A[j][j] == 0:
            free_vars.append(j)
            
    K = len(free_vars)
    res = [str(K)]
    for r in range(M):
        line = []
        for v in free_vars:
            line.append(str(Q[r][v]))
        const_term = sum(Q[r][c] * Y_fixed[c] for c in range(M) if c not in free_vars)
        line.append(str(const_term))
        res.append(" ".join(line))
        
    return "\n".join(res)

def main():
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
        B.append(-int(input_data[idx]))
        idx += 1
        
    result = solve(N, M, A, B)
    print(result)

if __name__ == '__main__':
    main()
