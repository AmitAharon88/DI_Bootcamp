#1

matrix = [
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM ', 
    '$a ',
    '#t%',
    '^r!',
    ]

num_col = len(matrix[0])
print(num_col)
decoded_matrix = []

for num in range(num_col) :
    decoded_str = ''
    for row in matrix :
        letter = row[num]
        if letter.isalpha() :
            decoded_str += letter
        else :
            if decoded_str :
                decoded_str += ''
    decoded_matrix.append(decoded_str)
decoded_message = ' '.join(decoded_matrix)

print(decoded_message)