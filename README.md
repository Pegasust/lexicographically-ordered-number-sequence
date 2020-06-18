# lexicographically-ordered-number-sequence

### Trivia night in Terraria
So we had a trivia night in Terraria, and we came across an esoteric number sequence: 
[8, 18, 11, 15, 5, 4, 14, 9, 19, 1, 7, 17, 6, 16, 10, ?, ?, ?, ?, ?].
Ofcourse, as much of a lover of mathematics and computer science as I am, I tried to decipher this number sequence, but we lost.
The host even hinted "think of the numbers as word". The first thing I thought was let 'a' be 0 or 1, the number would form a 
string to be completed because this number sequence doesn't have room for more (... symbol at the end).

But nope, how wrong was I.

Turns out, the sequence is actually poorly defined, given such number sequence, one could either provide at least two solution, depending on the range of the sequence:
 - 13, 3, 12, 20, 2 (1 to 20)
 
 - 13, 3, 12, 2, 0 (0 to 19)
 
The other trivia group got it right, and boy was I impressed and devoid of all the thought of them being Google-Andys.

### Implementation spec
Anyways, here is my implementation of generating such sequence in any integer base, positive or negative (or both), as long as there exists correct string definitions in the format of, for example, in hexadecimal:

def_base = 0x10
defs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "A_", "B_", "C_", "D_", "E_", "F_", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen","A-teen", "B-teen", "C-teen", "D-teen", "E-teen", "F-teen","twenty" , "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety","A-ty", "B-ty", "C-ty", "D-ty", "E-ty", "F-ty", "hundred", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion"]

If there exists such definitions for a number base, one can generate a sequence number given the range of choice in that base by calling from alpha_ordered_num_seq.py:

```{py}
# generate lexicographically oredered number sequence from -0x69 to 0x420 in base 16
generate_num_seq(-0x69, 0x420, defs, def_base) 
# equivalent to:
generate_num_seq_hexa(-0x69, 0x420)
```

### Room for optimizations:

 - One can certainly implement adding a string definition for negative at the end of the string definition and modify the code a bit to customize what is written for "negative".
 
 - Converting the _numerization function in numerization.py to iterative function may boost performance and memory usage.
 
 - Using a lookup table can be effective in generating numerization for large numbers, and thus boosts the time complexity of the program. (The time complexity of this program is so terrible I don't want any connection in the number theory field anymore).
