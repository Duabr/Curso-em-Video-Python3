# Lê 9 números e então os mostra no formato de uma matriz.
from time import sleep
nums=[[], [], []]
print('Digite 9 números para colocá-los em uma matriz;')
for c in range(9):
    nums[c//3].append(int(input(f'Digite o número que ficará na posição [{c//3}][{c%3}]: ')))

print('\033[1mOrganizando números...\033[m')
sleep(2)
print(f'''[{nums[0][0]:^3}][{nums[0][1]:^3}][{nums[0][2]:^3}]
[{nums[1][0]:^3}][{nums[1][1]:^3}][{nums[1][2]:^3}]
[{nums[2][0]:^3}][{nums[2][1]:^3}][{nums[2][2]:^3}]''')