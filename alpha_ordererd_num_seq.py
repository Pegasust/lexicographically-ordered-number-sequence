from numerization import *

def generate_num_seq(min_num, max_num, num_defs= None, base = 10):
    """
    min_num and max_num are both included
    """
    buffer_length = max_num - min_num + 1
    str_buffer = []
    for i in range(0, buffer_length):
        num_str = ""
        actual_num = min_num + i
        if num_defs is None:
            if base == 10:
                num_str = numerization(actual_num)
            elif base == 16:
                num_str = numerization_hexa(actual_num)
        else:
            num_str = _numerization_str(actual_num, num_defs, base)
        str_buffer.append((num_str, actual_num))
    # Sort the str_buffer lexicographically
    str_buffer.sort(key = lambda tup: tup[0])
    if buffer_length < 50:
        print(str_buffer)
    result = [num for (num_str, num) in str_buffer]
    return result

def geenrate_num_seq_hexa(min_num, max_num):
    return generate_num_seq(min_num, max_num, None, 16)

if __name__ == "__main__":
    print(generate_num_seq(1, 20))
