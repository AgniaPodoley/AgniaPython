squares = []
mynumbers = list (range(0,10))
for v in mynumbers:
   square = v**2
   squares.append(square)

print(sum(squares))

squares5 = [value**5 for value in range(1,6)]
print(squares5[1:3])

