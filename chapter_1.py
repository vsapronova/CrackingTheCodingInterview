


# 1.1

def uniq_char(str):
    dict = {}
    for char in str:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char]+=1
    if all(value == 1 for value in dict.values()):
        return "All unique"
    else:
        return "Not unique"

# 1.2

def is_permutation(str1, str2):
    dict = {}
    for char in str1:
        if char not in dict:
            dict[char] = 0
        dict[char] +=1
    for char in str2:
        if char in dict:
            dict[char]-=1
        dict[char]-=0
    if all(value == 0 for value in dict.values()):
        return "It's permutation"
    return "Not permutation"

def perm(str1, str2):
    array = []
    for char1 in str1:
        array.append(char1)
    for char2 in str2:
        if char2 in array:
            array.remove(char2)
        else:
            continue
    if array == []:
        return "It's perm"
    else:
        return "No, it's not a perm"

def is_perm(str1, str2):
    count_dict = {}
    if len(str1) == len(str2):
        for ch1 in str1:
            if ch1 not in count_dict:
                count_dict[ch1] = 1
            else:
                count_dict[ch1] += 1
        for ch2 in str2:
            if ch2 in count_dict:
                count_dict[ch2] -= 1
            else:
                return "Not a perm"
        if all(value == 0 for value in count_dict.values()):
            return "It's a perm"
    return "Not a perm"

def perm_is(str1, str2):
    new1 = sorted(str1)
    new2 = sorted(str2)
    for ch in range(len(new1)):
        if new1[ch] != new2[ch]:
            return "Not a perm"
        else:
            continue
    return "It's a perm"

# 1.3

def replace_spaces(str):
    chars = list(str)
    i = len(str) - 1
    j = i
    while chars[i] == ' ':
        i -= 1
    while i != j:
        if chars[i] == ' ':
            chars[j] = '0'
            chars[j-1] = '2'
            chars[j-2] = '%'
            j -= 2
        else:
            chars[j] = chars[i]
        i -= 1
        j -= 1
    return ''.join(chars)

# 1.4

def is_palindrome(str):
    str = str.replace(' ', '')
    str = str.lower()
    d = dict()
    for i in str:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    odd_char = 0
    for key, value in d.items():
        if value % 2 != 0 and odd_char == 0:
            odd_char += 1
        elif value % 2 != 0 and odd_char != 0:
            return False
    return True

# 1.5

def check_one_way(str1, str2):
    len_diff = abs(len(str1) - len(str2))
    if len_diff > 1:
        return False
    elif len_diff == 0:
        count_diff = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                count_diff += 1
                if count_diff > 1:
                    return False
        return True
    else:
        if len(str1) > len(str2):
            shorter, longer = str2, str1
        else:
            shorter, longer = str1, str2
        shift = 0
        for i in range(len(shorter)):
            if shorter[i] != longer[i + shift]:
                if shorter[i] != longer[i + 1]:
                    return False
                shift = 1
        return True

# 1.6

def str_comp(str1):
    compressed = []
    current_letter = str1[0]
    count = 1
    for letter in str1[1: ]:
        if current_letter == letter:
            count += 1
        else:
            compressed.append(current_letter + str(count))
            count = 1
            current_letter = letter
    compressed.append(current_letter + str(count))
    compressed_str = ''.join(compressed)
    if len(compressed_str) < len(str1):
        return compressed_str
    else:
        return str

# 1.7

def rotate_m(matrix):
    n = len(matrix)
    rotated = [None] * n
    for row in range(n):
        rotated[row] = [None] * n
    for row in range(n):
        for col in range(n):
            rotated[row][col] = matrix[n - col - 1][col]
    return rotated


def rotate_m_in_place(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False
    n = len(matrix)
    for layer in range(0, n//2):
        start = layer
        end = n - 1 - layer
        for i in range(start, end):
            x = i - start
            top = matrix[start][x + start]
            #left to top
            matrix[start][x + start] = matrix[end - x][start]
            #bottom to left
            matrix[end - x][start] = matrix[end][end - x]
            #right to bottom
            matrix[end][end - x] = matrix[x + start][end]
            #top to right
            matrix[x + start][end] = top
    return matrix

def rotate_matrix(matrix):
    if len(matrix) == 0 or len(matrix) != len(matrix[0]): return False
    size = len(matrix) - 1
    layers = size // 2
    for layer in range(layers):
        for i in range(layer, size - layer):
            top = matrix[layer][i]
            right = matrix[i][size - layer]
            bottom = matrix[size - layer][size - i]
            left = matrix[size - i][layer]

            matrix[layer][i] = left
            matrix[size - i][layer] = bottom
            matrix[size - layer][size - i] = right
            matrix[i][size - layer] = top
    return matrix



def transpose_matrix(matrix):
    # matrix.reverse()
    for row in range(len(matrix)):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    return matrix

# 1.8

def zero_matrix(matrix):
    zero_rows = []
    zero_cols = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                zero_rows.append(row)
                zero_cols.append(col)
    for row in zero_rows:
        for col in range(len(matrix[row])):
            matrix[row][col] = 0
    for col in zero_cols:
        for row in range(len(matrix)):
            matrix[row][col] = 0
    return matrix

# 1.9














# print(uniq_char("hello"))
# print(is_permutation("hello", "llohe"))
# print(perm("hello", "ollh"))
# print(replace_spaces("My dear friend    "))
# print(is_perm("aab", "abb"))
# print(perm_is("abbdc", "abbcd"))
# print(replace_spaces("Hello my friend good      "))
# print(is_palindrome("Race car"))
# print(is_palindrome("not race car"))
# print(check_one_way("abc", "abcb"))
# print(str_comp("abbccccaadd"))
# print(rotate_m([[1, 2, 1, 1],
#                 [2, 2, 2, 2,],
#                 [3, 3, 3, 3,],
#                 [4, 4, 4, 4]]))
print(rotate_matrix([[1, 2, 3, 4],
                    [5, 6, 7, 8,],
                    [9, 10, 11, 12,],
                    [13, 14, 15, 16]]))
# print(zero_matrix([[1, 2],
#                    [4, 0],
#                    [6, 7]]))
