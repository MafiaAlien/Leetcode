

def _fact(n: int):
    if n <= 1:
        return 1 
    else:
        return n * _fact(n-1)

def combination(selected: int, total: int)-> int:
    assert selected > 0 and total > 0, "the number must be positive"
    numerator = _fact(total)
    denominator = _fact(selected) * _fact(total - selected)
    return  numerator / denominator

def permutation(selected: int, total: int)-> int:
    assert selected > 0 and total > 0, "the numbers must be positive"
    numerator = _fact(total)
    denominator = _fact(selected)
    return numerator / denominator

if __name__ == "__main__":
    # print(combination(selected=15, total=49))
    print(permutation(3, 27) * permutation(1, 22) * permutation(11, 45))