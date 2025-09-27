def finding_length(iterable):
    length = 0
    for i in iterable:
        length += 1

    print(f'The length of {iterable} is = {length}')

names_list = ['Shailaja', 'Deeksha', 'Hashmath', 'Atharva']

for name in names_list:
    finding_length(name)
