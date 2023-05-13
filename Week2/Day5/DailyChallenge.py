sequence = input('Provide a sequence of words where each word is seperated with a comma. (Example- apple,banana,orange): ')

sequence_list = sequence.split(',')
sequence_list.sort()

print(','.join(sequence_list))
