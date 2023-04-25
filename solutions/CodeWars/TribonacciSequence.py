def tribonacci(signature, n):
    final_result = []
    if n > len(signature):
        result = signature
        for i in range(n - len(signature)):
            tamanho = len(result)
            n_num = sum(result[tamanho - 3:tamanho])
            result.append(n_num)
        final_result = result
    else:
        result_dir = []
        for i in range(n):
            result_dir.append(signature[i])
        final_result = result_dir
    return final_result
