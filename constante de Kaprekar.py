# Entrada
num = int(input("Entre com um número de até 4 dígitos: "))

# Validação de tipo e positivo
if num < 0:
    print("Erro: número deve ser inteiro e positivo.")
else:

    # Validação de faixa
    if num > 9999:
        print("Erro: número fora do intervalo (0000 a 9999).")
    else:

        # Extrair dígitos
        d1 = num // 1000
        d2 = (num % 1000) // 100
        d3 = (num % 100) // 10
        d4 = num % 10

        # Validação de repetição (3 ou mais iguais)
        if (d1 == d2 and d1 == d3) or \
           (d1 == d2 and d1 == d4) or \
           (d1 == d3 and d1 == d4) or \
           (d2 == d3 and d2 == d4):

            print("Erro: número possui muitos dígitos repetidos.")

        else:

            print("Número informado:", num)

            iteracao = 0

            # Loop principal
            while num != 6174:

                # Extrair dígitos
                d1 = num // 1000
                d2 = (num % 1000) // 100
                d3 = (num % 100) // 10
                d4 = num % 10

                # Ordenação decrescente (manual)
                if d1 < d2:
                    temp = d1
                    d1 = d2
                    d2 = temp

                if d1 < d3:
                    temp = d1
                    d1 = d3
                    d3 = temp

                if d1 < d4:
                    temp = d1
                    d1 = d4
                    d4 = temp

                if d2 < d3:
                    temp = d2
                    d2 = d3
                    d3 = temp

                if d2 < d4:
                    temp = d2
                    d2 = d4
                    d4 = temp

                if d3 < d4:
                    temp = d3
                    d3 = d4
                    d4 = temp

                # Número decrescente (NDD)
                ndd = d1*1000 + d2*100 + d3*10 + d4

                # Número crescente (NDC)
                ndc = d4*1000 + d3*100 + d2*10 + d1

                # Subtração
                resultado = ndd - ndc

                iteracao = iteracao + 1

                print("Iteração", iteracao, ":", ndd, "-", ndc, "=", resultado)

                # Atualiza número
                num = resultado

            print("Constante de Kaprekar (6174) atingida em", iteracao, "iterações.")
