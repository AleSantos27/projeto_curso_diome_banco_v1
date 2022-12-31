saldo = contador_deposito = contador_saque = soma_saque = soma_deposito = 0

while True:
                                        # BLOCO FUNÇÕES MENU
    menu = " "
    while menu not in "1230":
        menu = str(input('[1] - DEPOSITAR\n[2] - SACAR\n[3] - EXTRATO\n[0] - SAIR\nESCOLHA UMA OPERAÇÃO: ')).strip()
                                        # BLOCO FUNÇÕES DEPOSITO
    if menu == "1":
        saldo = soma_deposito
        valor_deposito = int(input('QUAL O VALOR DO DEPOSITO? '))
        if valor_deposito > 20:
            contador_deposito += 1
            soma_deposito += valor_deposito
            saldo += soma_deposito
        print('DEPOSITO EFETUADO COM SUCESSO!!!')
                                        #BLOCO FUNÇÕES SAQUE
    if menu == "2":
        valor_saque = int(input('QUAL O VALOR DO SAQUE? '))
        if valor_saque > saldo:
            print('SALDO INSUFICIENTE PARA ESSA OPERAÇÃO!\nFAÇA UM DEPOSITO PARA PROSSEGUIR COM A TRANSAÇÂO')
            continue
        if valor_saque > 500:
            print('SEU LIMITE PARA SAQUE É R$: 500,00 (QUINHENTOS REAIS)')
            continue
        if contador_saque >= 3:
            print('OPERAÇÂO NEGADA\nQUANTIDADE DE OPERAÇÔES FOI ATINGIDA\nAGUARDE 24 HORAS PARA TENTAR NOVAMENTE'
                  'OU RETIRE O CARTÃO E INSIRA NOVAMENTE PARA DEPOSITAR E/OU IMPRIMIR SEU EXTRATO')
            break
        else:
            soma_saque += valor_saque
            contador_saque += 1
            saldo += soma_deposito
            print('SAQUE EFETUADO COM SUCESSO!!!')
                                        #BLOCO FUNÇÕES EXTRATO
    if menu == "3":
        saldo_restante = soma_deposito - soma_saque
        print(f'TOTAL DE SAQUE: R$: {soma_saque}\nTOTAL DE DEPOSITO: R$ {soma_deposito}\nQUANTIDADE DE SAQUE R$: {contador_saque}'
              f'\nQUANTIDADE DE DEPOSITO R$: {contador_deposito}\nSALDO EM CONTA R$: {saldo_restante}')
                                        #BLOCO FUNÇÃO SAIDA
    if menu == "0":
        break
print('FOI UM PRAZER LHE ATENDER.\nVOLTE SEMPRE')
