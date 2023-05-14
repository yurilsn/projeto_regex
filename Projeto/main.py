import Questao_1.questao_1 as q1
import Questao_2.questao_2 as q2

#Escolha de questão pelo usuário
escolher_questao = int(input('\nEscolha a questão que deseja para realizar o teste: \nDigite "1" para a primeira questão (Validação de campos) \nDigite "2" para a segunda questão (Arranjos familiares) \nDigite "3" para finalizar o teste \nEscolha a questão ou finalize o teste: '))
#Variável de alternativas da questão e das respectivas validações
alternativas = 'abcdefg'
validacoes = ['validação de Nome Completo', 'validação de Email', 'validação de Senha', 'validação de CPF', 'validação de Telefone', 'validação de Data e Hora', 'validação de Numeros reais']
casais = []

#laço para as questões e finalização do programa
while (escolher_questao != 3):
    #condição para ocorrer a questão 1
    if escolher_questao == 1:
        print('\nVocê escolheu a questão 1. \nAgora escolha a alternativa que deseja para testar:')
        #laço para a descrição das alternativas
        for c in range(0, 7):
            print(f'Digite "{alternativas[c]}" para escolher a {validacoes[c]}')
        escolher_alternativa = input('Escolha a alternativa: ')
        #laço para as escolhas de alternativas
        while (escolher_alternativa != "0"):
            print(f'\nVocê escolheu a alternativa "{escolher_alternativa}" para realizar o teste.\n')
            #cadeia = input('Insira a cadeia para ser testada: ')
            #condições para referir a escolha do usuário
            if escolher_alternativa == 'a':
                """
                Esta condição faz a validação do nome, nome do meio(opcional) e sobrenome, onde ambos se iniciam com letra maiúscula, 
                tendo apenas um espaço entre eles, não aceitando caracteres especiais ou números 
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                Validação de nome, nome do meio(opcional) e sobrenome, onde ambos se iniciam com letra maiúscula, 
                tendo apenas um espaço entre eles, não aceitando caracteres especiais ou números.

                ''')
                cadeia = input('Insira a cadeia para ser testada: ')
                print(f'\nA cadeia inserida tem valor booleano {q1.valida_nome(cadeia)}. \n')
            elif escolher_alternativa == 'b':
                """ 
                Esta condição faz a validação de email, em que deve ter somente um @, com pelo menos 
                1 alfanumérico antes, e somente string minúsculas após. Deve terminar 
                com a sub cadeia '.br' ou '.com.br'.
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                Validação de email, em que deve ter somente um @, com pelo menos 
                1 alfanumérico antes, e somente string minúsculas após. Deve terminar 
                com a sub cadeia '.br' ou '.com.br'.

                ''')
                cadeia = input('Insira a cadeia para ser testada: ')
                print(f'\nA cadeia inserida tem valor booleano {q1.valida_email(cadeia)}. \n')
            elif escolher_alternativa == 'c':
                """
                Esta condição valida a senha, em que podem ter símbolos minúsculos, maiúsculos e dígitos.
                Deve conter pelo menos um símbolo maiúsculo e um dígito. O comprimento deve ser igual a 8.
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                Validação de senha, em que podem ter símbolos minúsculos, maiúsculos e dígitos.
                Deve conter pelo menos um símbolo maiúsculo e um dígito. O comprimento deve ser igual a 8.

                ''')
                print(f'\nA cadeia inserida tem valor booleano {q1.valida_senha(cadeia)}. \n')           
            elif escolher_alternativa == 'd':
                """
                A condição faz a validação de cpf onde as sentenças devem ter o formato xxx.xxx.xxx-xx, 
                e x deve pertencer ao alfabeto N={0,1,2,...,9}.
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                Validação de cpf onde as sentenças devem ter o formato xxx.xxx.xxx-xx, 
                e x deve pertencer ao alfabeto N={0,1,2,...,9}.

                ''')
                cadeia = input('Insira a cadeia para ser testada: ')
                print(f'\nA cadeia inserida tem valor booleano {q1.valida_cpf(cadeia)}. \n')
            elif escolher_alternativa == 'e':
                """
                A condição faz a validação de telefone tendo os seguintes padrões: 
                (xx) 9xxxx-xxxx
                (xx) 9xxxxxxxx
                xx 9xxxxxxxx
                Sendo x uma string de número inteiro
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                Validação de telefone tendo os seguintes padrões: 
                (xx) 9xxxx-xxxx
                (xx) 9xxxxxxxx
                xx 9xxxxxxxx
                Sendo x uma string de número inteiro
                
                ''')
                cadeia = input('Insira a cadeia para ser testada: ')
                print(f'\nA cadeia inserida tem valor booleano {q1.valida_telefone(cadeia)}. \n')
            elif escolher_alternativa == 'f':
                """
                Esta condição faz a validação de data e hora, em que as sentenças devem ter o formato:
                dd/mm/aaaa hh:mm:ss, onde d, m, a, h, m, s ∈ N.
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                Validação de data e hora.
                Em que as sentenças devem ter o formato dd/mm/aaaa hh:mm:ss, onde d, m, a, h, m, s ∈ N.

                
                ''')
                cadeia = input('Insira a cadeia para ser testada: ')
                print(f'\nA cadeia inserida tem valor booleano {q1.valida_data_horario(cadeia)}. \n')
            elif escolher_alternativa == 'g':
                """
                A condição valida um número real (com ou sem sinal). Podendo começar com os símbolos
                "+" ou "-" ou "ε". Em seguida devem ter, pelo menos, um número natural. Em 
                seguida, devem ter, exatamente, um símbolo separador ".". Em seguida, devem
                finalizar com, pelo menos, um número natural.
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                Validação de número real (com ou sem sinal). Podem começar com os símbolos
                "+" ou "-" ou "ε". Em seguida devem ter, pelo menos, um número natural. Em 
                seguida, devem ter, exatamente, um símbolo separador ".". Em seguida, devem
                finalizar com, pelo menos, um número natural.
                
                ''')
                cadeia = input('Insira a cadeia para ser testada: ')
                print(f'\nA cadeia inserida tem valor booleano {q1.valida_numReal(cadeia)}. \n')
            #Escolher alternativa ou sair da questão
            escolher_alternativa = input('Digite a alternativa que deseja testar agora (Podendo ser a mesma testada anteriormente) ou digite "0" para sair da questão: ')

    #condição para a ocorrer a questão 2
    elif escolher_questao == 2:
        print('''\nVocê escolheu a questão 2. 

                    Esta questão apresenta a validação de uma família seguindo o seguinte padrão: 
                    ◦ H representa um homem;
                    ◦ M representa uma mulher;
                    ◦ h representa um filho do sexo masculino (natural ou adotado);
                    ◦ m representa uma filha do sexo feminimo (natural ou adotado);
                    ◦ A posição relativa de uma letra em relação às demais indica a idade relativa daquele
                    membro da família em relação aos demais (os mais novos estão sempre à direita).
                    Sendo os casais heterossexuais mais velhos que os filhos e com pelo menos duas filhas mulheres,
                    ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha
                    mulher
        
                Agora escolha a alternativa que deseja para testar:

            ''')
        #laço a descrição das alternativas
        for c in alternativas:
            print(f'Digite "{c}" para escolher a alternativa {c}) ')
        escolher_alternativa = input('Escolha a alternativa: ')
        #laço para as escolha de alternativas
        while (escolher_alternativa != "0"):
            print(f'\nVocê escolheu a alternativa "{escolher_alternativa}" para realizar o teste.\n')
            #condiçao para referir a escolha do usuário
            if escolher_alternativa in 'abcdef':
                if escolher_alternativa == 'a':
                    """
                    Condição para válidar casais heterossexuais mais velhos que os filhos e com pelo menos duas filhas mulheres,
                    ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher
                    """
                    print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                    Casais heterossexuais mais velhos que os filhos e com pelo menos duas filhas mulheres,
                    ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha mulher
                
                    ''')
                    cadeia = input('Insira a cadeia para ser testada: ')
                    print(f'\nA cadeia inserida tem valor booleano {q2.regex_2_a(cadeia)}. \n')
                elif escolher_alternativa == 'b':
                    """
                    Condição para válidar casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas
                    mulheres.
                    """
                    print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                    Casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas
                    mulheres.
                
                    ''')
                    cadeia = input('Insira a cadeia para ser testada: ')
                    print(f'\nA cadeia inserida tem valor booleano {q2.regex_2_b(cadeia)}. \n')
                elif escolher_alternativa == 'c':
                    """
                    Condição para válidar casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho
                    mais novo homem.
                    """
                    print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                    Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho
                    mais novo homem.
                
                    ''')
                    cadeia = input('Insira a cadeia para ser testada: ')
                    print(f'\nA cadeia inserida tem valor booleano {q2.regex_2_c(cadeia)}. \n')           
                elif escolher_alternativa == 'd':
                    """
                    Condição para válidar casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os
                    dois primeiros filhos formam um casal e os últimos também.
                    """
                    print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                    Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os
                    dois primeiros filhos formam um casal e os últimos também.
                
                    ''')
                    cadeia = input('Insira a cadeia para ser testada: ')
                    print(f'\nA cadeia inserida tem valor booleano {q2.regex_2_d(cadeia)}. \n')
                elif escolher_alternativa == 'e':
                    """
                    Condição para válidar casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado
                    conforme a ordem de nascimento.
                    """
                    print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                    Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado
                    conforme a ordem de nascimento.
                
                    ''')
                    print(f'\nA cadeia inserida tem valor booleano {q2.regex_2_e(cadeia)}. \n')
                elif escolher_alternativa == 'f':
                    """
                    Condição para válidar casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos
                    homens e mulheres, mas que não tiveram dois filhos homens consecutivos.
                    """
                    print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                    Casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos
                    homens e mulheres, mas que não tiveram dois filhos homens consecutivos.
                
                    ''')
                    cadeia = input('Insira a cadeia para ser testada: ')
                    print(f'\nA cadeia inserida tem valor booleano {q2.regex_2_f(cadeia)}. \n')
            elif escolher_alternativa == 'g':
                """
                Condição para realizar um arranjo de no mínimo x∈ℕ e no máximo y ∈ℕ , com x> 0 , y > 0 , e x≤ y , de
                adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos
                homens e mulheres, mas que os três filhos mais novos não foram homens.
                """
                print(f'''
                                    {'*'*15} REGRA PARA VALIDAÇÃO {'*'*15}
                
                    Arranjo de no mínimo x∈ℕ e no máximo y ∈ℕ , com x> 0 , y > 0 , e x≤ y , de
                    adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos
                    homens e mulheres, mas que os três filhos mais novos não foram homens.
                
                    ''')
                x= int(input("Insira a quantidade mínima para o arranjo de adultos: "))
                y= int(input("Insira a quantidade máxima para o arranjo de adultos: "))
                cadeia = input ('Insira a cadeia de filhos para ser testada: ')
                q2.regex_2_g(x,y,cadeia)
            #Escolher alternativa ou sair da questão
            escolher_alternativa = input('Digite a alternativa que deseja testar agora (Podendo ser a mesma testada anteriormente) ou digite "0" para sair da questão: ')
    else:
        print('\nVocê escolheu uma alternativa errada. Tente novamente. \n')
        escolher_questao = int(input('Escolha a questão que deseja para realizar o teste: \nDigite "1" para a primeira questão (Validação de campos) \nDigite "2" para a segunda questão \nDigite "3" para finalizar o teste \nEscolha a questão ou finalize o teste: '))
        continue
    #Escolher questão ou finalizar o porgrama
    escolher_questao = int(input('Escolha a questão que deseja para realizar o teste: \nDigite "1" para a primeira questão (Validação de campos) \nDigite "2" para a segunda questão \nDigite "3" para finalizar o teste \nEscolha a questão ou finalize o teste: '))
