continua = str('s')

while continua=='s' or continua=='S':

    num = int(input('Informe um número de 0 a 999: '))
    n1 = num // 1 % 10
    n2 = num // 10 % 10
    n3 = num // 100 % 10

    if num > 999 and num < 0:
        print('Número inválido. ')

    else:
        print('O número {:.0f} por exenso é: '.format(num), end="")

        if n3 > 0:
            if n3 == 1:
                if n3 == 1 and n2 == 0 and n1 == 0:
                    print('Cem')
                else:
                    print('Cento e ', end="")

            elif n3 == 2:
                if n3 == 2 and n2 == 0 and n1 == 0:
                    print('Duzentos')
                else:
                    print('Duzentos e ', end="")

            elif n3 == 3:
                if n3 == 3 and n2 == 0 and n1 == 0:
                    print('Trezentos')
                else:
                    print('Trezentos e ', end="")

            elif n3 == 4:
                if n3 == 4 and n2 == 0 and n1 == 0:
                    print('Quatrocentos')
                else:
                    print('Quatrocentos e ', end="")

            elif n3 == 5:
                if n3 == 2 and n2 == 0 and n1 == 0:
                    print('Quinhentos')

                else:
                    print('Quinhentos e ', end="")

            elif n3 == 6:
                if n3 == 2 and n2 == 0 and n1 == 0:
                    print('Seicentos')
                else:
                    print('Seicentos e ', end="")

            elif n3 == 7:
                if n3 == 7 and n2 == 0 and n1 == 0:
                    print('Setecentos')
                else:
                    print('Setecentos e ', end="")

            elif n3 == 8:
                if n3 == 8 and n2 == 0 and n1 == 0:
                    print('Oitocentos', end="")
                else:
                    print('Oitocentos e ', end="")

            elif n3 == 9:
                if n3 == 9 and n2 == 0 and n1 == 0:
                    print('Novecentos')
                else:
                    print('Novecentos e ', end="")

        if n2 > 0:
            if n2 == 1:
                if n2 == 1 and n1 == 0:
                    print('Dez')

                elif n2 == 1 and n1 == 1:
                    print('Onze')

                elif n2 == 1 and n1 == 2:
                    print('Doze')

                elif n2 == 1 and n1 == 3:
                    print('Treze')

                elif n2 == 1 and n1 == 4:
                    print('Quatorze')

                elif n2 == 1 and n1 == 5:
                    print('Quinze')

                elif n2 == 1 and n1 == 6:
                    print('Dezesseis')

                elif n2 == 1 and n1 == 7:
                    print('Dezessete')

                elif n2 == 1 and n1 == 8:
                    print('Dezoito')

                elif n2 == 1 and n1 == 9:
                    print('Dezenove')

        if n2 == 2:
            if n2 == 2 and n1 == 0:
                print('Vinte')
            else:
                print('Vinte e ', end="")

        if n2 == 3:
            if n2 == 3 and n1 == 0:
                print('Trinta')
            else:
                print('Trinta e ', end="")

        if n2 == 4:
            if n2 == 4 and n1 == 0:
                print('Quarenta')
            else:
                print('Quarenta e ', end="")

        if n2 == 5:
            if n2 == 5 and n1 == 0:
                print('Cinquenta')
            else:
                print('Cinquenta e ', end="")

        if n2 == 6:
            if n2 == 6 and n1 == 0:
                print('Sessenta')
            else:
                print('Sessenta e ', end="")

        if n2 == 7:
            if n2 == 7 and n1 == 0:
                print('Setenta')
            else:
                print('Setenta e ', end="")

        if n2 == 8:
            if n2 == 8 and n1 == 0:
                print('Oitenta')
            else:
                print('Oitenta e ', end="")

        if n2 == 9:
            if n2 == 9 and n1 == 0:
                print('Noventa')
            else:
                print('Noventa e ', end="")

        if n1 >= 0:
            if n1 == 0:
                print('Zero')
                
            if n1 == 1:
                print('Um')

            elif n1 == 2:
                print('Dois')

            elif n1 == 3:
                print('Três')

            elif n1 == 4:
                print('Quatro')

            elif n1 == 5:
                print('Cinco')

            elif n1 == 6:
                print('Seis')

            elif n1 == 7:
                print('Sete')

            elif n1 == 8:
                print('Oito')

            elif n1 == 9:
                print('Nove')

    continua = input('Deseja continuar? (s/n) ')
    
 
