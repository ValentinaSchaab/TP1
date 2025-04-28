def rom_a_dec(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if len(romano) == 0:
        return 0

    if len(romano) == 1:
        return valores[romano[0]]

    if valores[romano[0]] < valores[romano[1]]:
        return valores[romano[1]] - valores[romano[0]] + rom_a_dec(romano[2:])
    else:
        return valores[romano[0]] + rom_a_dec(romano[1:])

print(rom_a_dec('III'))      # 3
print(rom_a_dec('IV'))       # 4
print(rom_a_dec('IX'))       # 9
print(rom_a_dec('XX'))       # 20
print(rom_a_dec('MDX'))  # 1994
