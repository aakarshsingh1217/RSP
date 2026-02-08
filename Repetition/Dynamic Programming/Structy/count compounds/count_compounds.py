def count_compounds(compound: str, elements: list[str]):
    def dp(idx: int):
        if idx in memo:
            return memo[idx]
        if idx == len(compound):
            return 1
        
        num_ways = 0
        
        for element in elements:
            if compound.startswith(element.lower(), idx):
                num_ways += dp(idx + len(element))

        memo[idx] = num_ways

        return memo[idx]

    memo = {}
    
    return dp(0)