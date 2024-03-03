


def func_cadastro_reserva():
   
    while True:
        print(f"\033[1;33m{' CADASTRAR RESERVA ':=^138}\033[m")
        nome = str(input('Informe o nome completo do cliente: ')).strip()
        cpf = str(input('Informe o CPF do cliente (apenas números): ')).strip()
        pessoas = str(input('Informe a quantidade de pessoas para a mesma reserva: ')).strip()
        quarto = str(input('Informe o tipo de quarto (S → Standar, D → Deluxe, P → Premium): ')).strip().upper()
        dias = str(input('Informe a quantidade de dias a reservar: ')).strip()
      
        if nome.count(' ') > 0 and nome.replace(' ', '').isalpha():
           
            if cpf.isnumeric() and len(cpf) == 11:
               
                if pessoas.isnumeric():
                  
                    if dias.isnumeric():
                       
                        if len(quarto) == 1 and quarto in 'SDP':
                            preco = 0
                           
                            if quarto == 'S':
                                preco = 100
                            elif quarto == 'D':
                                preco = 200
                            elif quarto == 'P':
                                preco = 300
                            valor = preco * int(pessoas) * int(dias)
                            status = 'r'
                            if valor > 0:
                                break
        print(f"\033[1;33m{'':=^138}\033[m")
        print('\033[31mPor favor, informe os dados corretamente!\033[m')
    print(f"\033[1;33m{'':=^138}\033[m")
    
    info = nome + ',' + cpf + ',' + pessoas + ',' + quarto + ',' + dias + ',' + str(valor) + ',' + status + ' \n'
   
    banco = open('banco_de_dados.txt', 'a')
    banco.write(info)
    banco.close()
    print('\033[32mCadastro realizado com sucesso!\033[m')



def func_entrada_cliente():
    
    while True:
        print(f"\033[1;33m{' CHECK IN ':=^138}\033[m")
        busca = str(input('Informe o CPF do cliente (somente números): ')).strip()
        if busca.isnumeric() and len(busca) == 11:
            break
        print('\033[31mCPF informado é inválido! Por favor, tente novamente.\033[m')
    
    banco = open('banco_de_dados.txt', 'r')
    dados = banco.readlines()
    banco.close()
   
    lista_dados = []
    texto_dados = ''
    codigo = '0'
   
    for d in dados:
        nome, cpf, pessoas, quarto, dias, valor, status = d.split(',')
        if cpf == busca and status == 'r \n':
            lista_dados.append(d.split(','))
    
    if len(lista_dados) > 1:
        print(f"\033[1;33m{'':-^138}\033[m")
        print('Foram encontradas as seguintes reservas para o CPF informado:')
        for i, ld in enumerate(lista_dados):
            print(f'[{i}] Nome: {ld[0]}; Número de pessoas: {ld[2]};'
                  f'Modelo de quarto: {ld[3]}; Número de dias: {ld[4]}; Valor a pagar: R${int(ld[5]):.2f}')
        print(f"\033[1;33m{'':-^138}\033[m")
      
        while True:
            codigo = str(input('Informe o código da reserva a ser efetuada: ')).strip()
            if codigo.isnumeric():
                if 0 <= int(codigo) < len(lista_dados):
                    break
            print('\033[31mPor favor, digite um código válido!\033[m')
   
    if len(lista_dados) >= 1:
        texto_reserva = texto_reserva_atualizado = ''
        
        for i in range(7):
            texto_reserva += lista_dados[int(codigo)][i]
            if i != 6:
                texto_reserva += ','
       
        for i in range(6):
            texto_reserva_atualizado += lista_dados[int(codigo)][i]
            texto_reserva_atualizado += ',' if i != 5 else ',a \n'
        
        pos = dados.index(texto_reserva)
        dados.remove(texto_reserva)
        dados.insert(pos, texto_reserva_atualizado)
        
        for d in dados:
            texto_dados += d
       
        banco = open('banco_de_dados.txt', 'w')
        banco.write(texto_dados)
        banco.close()
        print('\033[32mCheck in realizado com sucesso!\033[m')
    else:
        print('\033[31mNão foram encontradas reservas para o CPF informado.\033[m')



def func_saida_cliente():
   
    while True:
        print(f"\033[1;33m{' CHECK OUT ':=^138}\033[m")
        busca = str(input('Informe o CPF do cliente (somente números): ')).strip()
        if busca.isnumeric() and len(busca) == 11:
            break
        print('\033[31mCPF informado é inválido! Por favor, tente novamente.\033[m')
   
    banco = open('banco_de_dados.txt', 'r')
    dados = banco.readlines()
    banco.close()
    
    lista_dados = []
    texto_dados = ''
    codigo = '0'
   
    for d in dados:
        nome, cpf, pessoas, quarto, dias, valor, status = d.split(',')
        if cpf == busca and status == 'a \n':
            lista_dados.append(d.split(','))
    
    if len(lista_dados) > 1:
        print(f"\033[1;33m{'':-^138}\033[m")
        print('Foram encontradas as seguintes reservas ativas para o CPF informado:')
        for i, ld in enumerate(lista_dados):
            print(f'[{i}] Nome: {ld[0]}; Número de pessoas: {ld[2]};'
                  f'Modelo de quarto: {ld[3]}; Número de dias: {ld[4]}; Valor a pagar: R${int(ld[5]):.2f}')
        print(f"\033[1;33m{'':-^138}\033[m")
        
        while True:
            codigo = str(input('Informe o código da reserva a ser efetuada: ')).strip()
            if codigo.isnumeric():
                if 0 <= int(codigo) < len(lista_dados):
                    break
            print('\033[31mPor favor, digite um código válido!\033[m')
    
    if len(lista_dados) >= 1:
        texto_reserva = texto_reserva_atualizado = ''
       
        for i in range(7):
            texto_reserva += lista_dados[int(codigo)][i]
            if i != 6:
                texto_reserva += ','
       
        for i in range(6):
            texto_reserva_atualizado += lista_dados[int(codigo)][i]
            texto_reserva_atualizado += ',' if i != 5 else ',f \n'
        
        pos = dados.index(texto_reserva)
        dados.remove(texto_reserva)
        dados.insert(pos, texto_reserva_atualizado)
        
        for d in dados:
            texto_dados += d
        
        banco = open('banco_de_dados.txt', 'w')
        banco.write(texto_dados)
        banco.close()
        print('\033[32mCheck out realizado com sucesso!\033[m')
    else:
        print('\033[31mNão foram encontradas reservas ativas para o CPF informado.\033[m')



def func_alterar_reserva():
    
    while True:
        print(f"\033[1;33m{' ALTERAR RESERVA ':=^138}\033[m")
        busca = str(input('Informe o CPF do cliente (somente números): ')).strip()
        if busca.isnumeric() and len(busca) == 11:
            break
        print('\033[31mCPF informado é inválido! Por favor, tente novamente.\033[m')
    
    banco = open('banco_de_dados.txt', 'r')
    dados = banco.readlines()
    banco.close()
    
    lista_dados = []
    texto_dados = ''
    codigo = '0'
    
    for d in dados:
        nome, cpf, pessoas, quarto, dias, valor, status = d.split(',')
        if cpf == busca and status != 'f \n' and status != 'c \n':
            lista_dados.append(d.split(','))
    
    if len(lista_dados) == 1:
        print(f"\033[1;33m{' INFORMAÇÕES DA RESERVA ':-^138}\033[m")
        for i, ld in enumerate(lista_dados):
            print(f'[{i}] Nome: {ld[0]}. Número de pessoas: {ld[2]};'
                  f'Modelo de quarto: {ld[3]}; Número de dias: {ld[4]}; Valor a pagar: R${int(ld[5]):.2f}')
  
    elif len(lista_dados) > 1:
        print(f"\033[1;33m{' INFORMAÇÕES DA RESERVA ':-^138}\033[m")
        print('Foram encontradas as seguintes reservas para o CPF informado: ')
        for i, ld in enumerate(lista_dados):
            print(f'[{i}] Nome: {ld[0]}; Número de pessoas: {ld[2]};'
                  f'Modelo de quarto: {ld[3]}; Número de dias: {ld[4]}; Valor a pagar: R${int(ld[5]):.2f}')
        print(f"\033[1;33m{'':-^138}\033[m")
        
        while True:
            codigo = str(input('Informe o código da reserva a ser alterada: ')).strip()
            if codigo.isnumeric():
                if 0 <= int(codigo) < len(lista_dados):
                    break
            print('\033[31mPor favor, digite um código válido!\033[m')
    
    if len(lista_dados) >= 1:
        texto_reserva = ''
       
        for i in range(7):
            texto_reserva += lista_dados[int(codigo)][i]
            if i != 6:
                texto_reserva += ','
       
        while True:
            print(f"\033[1;33m{'':-^138}\033[m")
            pessoas = str(input('Informe a nova quantidade de pessoas para a mesma reserva: ')).strip()
            quarto = str(input('Informe o novo tipo de quarto (S → Standar, '
                               'D → Deluxe, P → Premium): ')).strip().upper()
            dias = str(input('Informe a nova quantidade de dias a reservar: ')).strip()
            status = str(input('Informe o novo status da reserva (R → Reservado, C → Cancelado, '
                               'A → Ativo, F → Finalizado): ')).strip().lower()
           
            if pessoas.isnumeric():
               
                if dias.isnumeric():
                    
                    if len(status) == 1 and status in 'rcaf':
                       
                        if len(quarto) == 1 and quarto in 'SDP':
                            preco = 0
                          
                            if quarto == 'S':
                                preco = 100
                            elif quarto == 'D':
                                preco = 200
                            elif quarto == 'P':
                                preco = 300
                            valor = preco * int(pessoas) * int(dias)
                            if valor > 0:
                                break
            print('\033[31mPor favor, informe os dados corretamente!\033[m')
        print(f"\033[1;33m{'':-^138}\033[m")
     
        while True:
            confirmar = str(input('Deseja realizar a alteração? (S → Sim, N → Não): ')).strip().upper()
            if confirmar in 'SN':
                break
            print('\033[31mPor favor, informe sua escolha apenas com S ou N.\033[m')
       
        if confirmar == 'S':
           
            texto_reserva_atualizado = lista_dados[int(codigo)][0] + ',' + lista_dados[int(codigo)][1] + ',' + pessoas \
                                       + ',' + quarto + ',' + dias + ',' + str(valor) + ',' + status + ' \n'
           
            pos = dados.index(texto_reserva)
            dados.remove(texto_reserva)
            dados.insert(pos, texto_reserva_atualizado)
            
            for d in dados:
                texto_dados += d
            # módulo do banco de dados, aberto na forma de substituição; todas as informações do banco são reescritas
            banco = open('banco_de_dados.txt', 'w')
            banco.write(texto_dados)
            banco.close()
            print('\033[32mAlteração realizada com sucesso!\033[m')
        else:
            print('\033[32mAlteração cancelada!\033[m')
    else:
        print('\033[31mNão foram encontradas reservas para o CPF informado.\033[m')
        print('\033[31mNão é possível alterar reservas finalizadas ou canceladas.\033[m')



def func_gerar_relatorios():
    
    while True:
        print(f"\033[1;33m{' GERAR RELATÓRIOS ':=^138}\033[m")
        print('[1] Relatório de todas as reservas R\n'
              '[2] Relatório de todas as reservas canceladas\n'
              '[3] Relatório de todas as reservas ativas\n'
              '[4] Relatório de todas as reservas finalizadas\n'
              '[5] Relatório do valor total recebido\n'
              '[6] Relatório de reserva por pessoa')
        print(f"\033[1;33m{'':=^138}\033[m")
        
        escolha = str(input('Informe o código do relatório desejado: ')).strip()
        if escolha.isnumeric():
            if 0 < int(escolha) <= 6:
                break
        print('\033[31mPor favor, digite um código válido!\033[m')
   
    banco = open('banco_de_dados.txt', 'r')
    dados = banco.readlines()
    banco.close()
   
    lista_dados = []
    soma = 0
    busca = ''
   
    if escolha == '6':
        while True:
            busca = str(input('Informe o CPF do cliente (somente números): ')).strip()
           
            if busca.isnumeric() and len(busca) == 11:
                break
            print('\033[31mCPF informado é inválido! Por favor, tente novamente.\033[m')
    
    for d in dados:
        nome, cpf, pessoas, quarto, dias, valor, status = d.split(',')
        if escolha == '1' and status == 'r \n':
            lista_dados.append(d.split(','))
        elif escolha == '2' and status == 'c \n':
            lista_dados.append(d.split(','))
        elif escolha == '3' and status == 'a \n':
            lista_dados.append(d.split(','))
        elif escolha == '4' and status == 'f \n':
            lista_dados.append(d.split(','))
        elif escolha == '5' and status == 'f \n':
            soma += int(valor)
        elif escolha == '6' and cpf == busca:
            lista_dados.append(d.split(','))
   
    if escolha in '12346' and len(lista_dados) > 0:
        print(f"{' NOME DO CLIENTE ':=^50}{' CPF ':=^21}{' PESSOAS ':=^15}{' QUARTO ':=^14}"
              f"{' DIAS ':=^12}{' VALOR ':=^14}{' STATUS ':=^12}")
        for ld in lista_dados:
            print(f'{ld[0]:.<50}', end='')
            print(f"{' ' + ld[1] + ' ':.^21}", end='')
            print(f"{' ' + ld[2] + ' ':.^15}", end='')
            if ld[3] == 'S':
                print(f"{'STANDAR':.^14}", end='')
            elif ld[3] == 'D':
                print(f"{'DELUXE':.^14}", end='')
            else:
                print(f"{'PREMIUM':.^14}", end='')
            print(f"{' ' + ld[4] + ' ':.^12}", end='')
            print(f"{' R$' + ld[5] + '.00 ':.^14}", end='')
            if ld[6] == 'r \n':
                print(f"{'RESERVADO':.^12}")
            elif ld[6] == 'c \n':
                print(f"{'CANCELADO':.^12}")
            elif ld[6] == 'a \n':
                print(f"{'ATIVO':.^12}")
            else:
                print(f"{'FINALIZADO':.^12}")
    
    elif escolha == '5':
        print(f'\033[32mRenda total: R${soma:.2f}\033[m')
    else:
        print('\033[31mNão foram encontrados dados para a opção desejada.\033[m')



while True:
    
    print(f"\033[1;33m{' MENU PRINCIPAL ':=^138}\033[m")
    print('[1] Cadastrar uma reserva\n'
          '[2] Check in\n'
          '[3] Check out\n'
          '[4] Alterar reserva\n'
          '[5] Gerar relatórios\n'
          '[6] Sair')
    print(f"\033[1;33m{'':=^138}\033[m")
    
    funcao = str(input('Executar a função: ')).strip()
   
    if funcao.isnumeric():
       
        if int(funcao) == 1:
            func_cadastro_reserva()
        elif int(funcao) == 2:
            func_entrada_cliente()
        elif int(funcao) == 3:
            func_saida_cliente()
        elif int(funcao) == 4:
            func_alterar_reserva()
        elif int(funcao) == 5:
            func_gerar_relatorios()
        elif int(funcao) == 6:
            print('\033[32mPrograma finalizado!\033[m')
            print(f"\033[1;33m{'':=^138}\033[m")
            break
        else:
            print('\033[31mERRO! Por favor, informe uma opção válida.\033[m')
    else:
        print('\033[31mERRO! Por favor, informe uma opção válida.\033[m')
