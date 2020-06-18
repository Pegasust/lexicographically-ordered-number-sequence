def _numerization(num, strlst, hardcoded_str, base = 10):
    # Well, just subdivide _numerization into parse single digit, 2 digits, 3 digits
    # and expo-digit and the program may probably be a lot shorter
    BASE = base
    twice_base = 2*BASE
    sqr_base = BASE * BASE
    cube_base = sqr_base * BASE # cubase DAW anyone? I'm more of an FL. # Thousands.
    if num < 0:
        strlst.append("negative")
        _numerization(-num, strlst, hardcoded_str, base)
        return
    if num <= twice_base: # 20
        strlst.append(hardcoded_str[num])
        return
    if num < sqr_base: # 100
        next_num = num-(twice_base)
        next_div_b = (next_num) // BASE
        # Index for the left digit (the "ty"s)
        index = twice_base + (next_div_b)
        # Append tys first (left) so that it follows: 44 -> forty four
        strlst.append(hardcoded_str[index])
        # Get the right number name for the right digit(s?)
        right_digit = next_num - (next_div_b * BASE)
        if right_digit != 0:
            # Append it (now on the right)
            _numerization(right_digit, strlst, hardcoded_str, base)
        return
    # Minus 2 because the first BASE numbers are "hardcoded" with the tys, for example, twenty, ninety,
    # A-ty, F-ty, but not G-ty, or "ten"-ty. This yields the exact position of "hundred"
    hundred_str_pos = (3 * BASE) - 2
    if num < cube_base: # 1000
        hundredth = num // sqr_base
        # 444 -> "four" hundred
        strlst.append(hardcoded_str[hundredth])
        strlst.append(hardcoded_str[hundred_str_pos])
        # 444 -> /four hundred/ "forty four"
        right_digits = num - (hundredth * sqr_base)
        _numerization(right_digits, strlst, hardcoded_str, base)
        return
    # 1000, 10000
    # DON'T DO ONE THOUSAND THOUSAND, DO ONE MILLION
    # DON'T DO ONE THOUSAND MILLION, DO ONE BILLION
    max_supported_expo_thousands = len(hardcoded_str) - (hundred_str_pos + 1)
    max_expo = cube_base ** max_supported_expo_thousands
    assert num//max_expo < cube_base
    expo = max_expo
    expo_thou = max_supported_expo_thousands
    while expo_thou > 0:
        expoth = num // expo
        if expoth != 0:
            # Skip 0 entries, this is basically searching for the highest
            # expo-thousandth.
            
            # 69 420 -> "sixty nine" thousand four hundred twenty
            _numerization(expoth, strlst, hardcoded_str, base)
            # Add the corresponding "expoth" word like "thousand" in the above case
            strlst.append(hardcoded_str[hundred_str_pos + expo_thou])
            # /sisxty nine thousand/ four hundred twenty
            right_digits = num - (expoth * expo)
            num = right_digits
        expo //= cube_base
        expo_thou -= 1
    # Do the rest right most 3-digit numbers
    _numerization(num,strlst, hardcoded_str, base)

def _numerization_str(num, hardcoded_str, base = 10):
    strlst = []
    _numerization(num, strlst, hardcoded_str, base)
    return " ".join(strlst)

def numerization(num):    
    hardcoded_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", # len = 10 (one-digit)
                    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", #len = 20 (teens)
                    "twenty" , "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", # len = 28 (tys)
                    "hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"] # the "expo-thousands"
    strlst = []
    _numerization(num, strlst, hardcoded_str, 10)
    return " ".join(strlst)

def numerization_hexa(num):
    hardcoded_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "A_", "B_", "C_", "D_", "E_", "F_",
                    "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen",
                     "A-teen", "B-teen", "C-teen", "D-teen", "E-teen", "F-teen",
                    "twenty" , "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
                     "A-ty", "B-ty", "C-ty", "D-ty", "E-ty", "F-ty", 
                    "hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"] # the "expo-thousands"
    strlst = []
    _numerization(num, strlst, hardcoded_str, 16)
    return " ".join(strlst)

if __name__ == "__main__":
    test_cases = [69420, 69420313, 113, 10, 13, 69, 42, 420, 313, 636, 363, 0, -0, 1, -42690]
    for test in test_cases:
        print(test, numerization(test))

    hexa_test_cases = [0xa, 0x1a, 0xe, 0xee, 0xde,0xdeadbeef, -0x5ae15bae]
    for hex_t in hexa_test_cases:
        print(hex(hex_t), numerization_hexa(hex_t))
