# Entrada
num = int(input("Entre com um número de até 3 dígitos: "))

# Validação de tipo e positivo
if num < 0:
    print("Erro: número deve ser inteiro e positivo.")
else:

    # Validação de faixa
    if num > 999:
        print("Erro: número fora do intervalo (000 a 999).")
    else:

        # Extrair dígitos
        d1 = num // 100
        d2 = (num % 100) // 10
        d3 = num % 10
        

        # Verificação de repedição 
        if d1 == d2 and d1 == d3:
            print("Erro: todos os dígitos iguais.")
        else:

            print("Número informado:", num)

            iteracao = 0

            while num != 495:

                # Extrair dígitos novamente
                d1 = num // 100
                d2 = (num % 100) // 10
                d3 = num % 10

                # Ordenação (decrescente) usando trocas
                if d1 < d2:
                    temp = d1
                    d1 = d2
                    d2 = temp

                if d1 < d3:
                    temp = d1
                    d1 = d3
                    d3 = temp

                if d2 < d3:
                    temp = d2
                    d2 = d3
                    d3 = temp

                # Número decrescente (NDD)
                ndd = d1*100 + d2*10 + d3

                # Número crescente (NDC)
                ndc = d3*100 + d2*10 + d1

                resultado = ndd - ndc

                iteracao = iteracao + 1

                print("Iteração", iteracao, ":", ndd, "-", ndc, "=", resultado)

                num = resultado

            print("Constante de Kaprekar reduzida (495) atingida em", iteracao, "iterações.")