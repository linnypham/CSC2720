def remove_dup(input):
    unique = set()
    output = []
    for i in input:
        if i not in unique:
            unique.add(i)
            output.append(i)
    return output
input = [ 1, 2, 3, 4, 4, 6, 6, 6 ]
print(remove_dup(input))
