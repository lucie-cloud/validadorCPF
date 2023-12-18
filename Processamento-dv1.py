
def validadorCPF(cpf):
    # Variáveis
    soma = 0
    cont = 10
    dv = 0

    if(len(cpf) == 11):

        for i in range(0, 9):
            soma += int(cpf[i]) * cont
            cont -= 1

        resto = soma % 11

        if resto >= 2:
            dv = 11 - resto
        else:
            dv = 0

        if int(cpf[9]) == dv:

            # Reiniciaçozação das variáveis
            cont = 11
            soma = 0

            for i in range(0, 10):
                soma += int(cpf[i]) * cont
                cont -= 1

            resto = soma % 11

            if resto >= 2:
                dv = 11 - resto
            else:
                dv = 0

            if int(cpf[10]) == dv:
                return True
            else:
                return False
        else:
            return  False
    else:
        return  False

# Teste Validador de CPF
print('CPF válido!') if validadorCPF('54647142949') else print('CPF inválido!')
print('CPF válido!') if validadorCPF('54747142949') else print('CPF inválido!')
print('CPF Válido!') if validadorCPF('17824630706') else print ('CPF inválido!')
print('CPF válido!') if validadorCPF('17824630806') else print('CPF inválido!')