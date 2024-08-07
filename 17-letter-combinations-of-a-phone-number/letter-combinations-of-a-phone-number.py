class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return ''

        digit_mapping={
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z'],
        }
        
        combinations=[]
        for character in digit_mapping[digits[0]]:
            combinations.append(character)
        for num in digits[1:]:
            new_combinations=[]
            for word in combinations:
                for character in digit_mapping[num]:
                    new_combinations.append(word+character)
            combinations=new_combinations
        return combinations