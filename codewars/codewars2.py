def tribonacci(sig, n):
    if n == 0: return []
    if n == 1: return [1]
    r = sig    
    t = sig[:]
    for i in range(n-3):
        r.append(sum(t))
        t = r[-3:]
        
    return r

def tribonacci(signature, n):
    res = signature[:n]
    for i in range(n - 3): res.append(sum(res[-3:]))
    return res

