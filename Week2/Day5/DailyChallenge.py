# Using list comprehension

# receive a string of words
sequence = input('Provide a sequence of words where each word is seperated with a comma. (Example- apple,banana,orange): ')
# using list comprehension turn str to list
sequence_list = [word for word in sequence.split(',')]
# sort then list, then convert to str, then print
print(','.join(sorted(sequence_list)))


# Other way to produce this (i find it simpler to understand)
sequence = input('Provide a sequence of words where each word is seperated with a comma. (Example- apple,banana,orange): ')

sequence_list = sequence.split(',')
sequence_list.sort()

print(','.join(sequence_list))

