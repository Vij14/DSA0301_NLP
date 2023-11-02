def isEndingWithAB(input_string):
    S0 = 0  
    S1 = 1  
    current_state = S0
    for char in input_string:
        if current_state == S0:
            if char == 'a':
                current_state = S1
        elif current_state == S1:
            if char == 'b':
                current_state = S0
    return current_state == S1

test_strings = ["ab", "aab", "abab", "ba", "abc"]
for string in test_strings:
    if isEndingWithAB(string):
        print(f"'{string}' ends with 'ab'.")
    else:
        print(f"'{string}' does not end with 'ab'.")
