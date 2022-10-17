'''
aplikace vam pomze vybrat co si dat na jidlo
'''

print('Co na jidlo ?')
odpoved = input('sladke nebo slane? \n'
                '1 - slane\n'
                '2 - sladke\n')

if int(odpoved) == 2:
    print('nabidla bych palacinky, tady je vhodný recept: https://www.recepty.cz/recept/hrnkove-palacinky-161618 :/')

if int(odpoved) == 1:
    odpoved2 = input('s masem nebo bez?\n'
                     '1 - s\n'
                     '2 - bez\n')

    if int(odpoved2) == 2:
        print('muzete si udelat testovinovy salat nebo jakykoliv jiny.')

    if int(odpoved2) == 1:
        odpoved3 = input('na panvicce nebo v hrnci?\n'
                         '1 - v hrnci\n'
                         '2- na panvicce\n')
        if int(odpoved3) == 1:
            print('muzete si udelat veprovy gulas s knedlikem.')

        if int(odpoved3) == 2:
            print('muzete si udelat cinske nudle s masem a mandlemi '))







