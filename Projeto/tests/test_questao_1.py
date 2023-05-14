from Projeto.Questao_1 import questao_1

# # ** TESTE NOME **  

def test_valida_nome_1():
    teste= 'Ada Lovelaci'
    assert questao_1.valida_nome(teste)

def test_valida_nome_2(): 
    teste= 'Alan Turing'
    assert questao_1.valida_nome(teste)

def test_valida_nome_3(): 
    teste= 'Stephen Cole Kleene'
    assert questao_1.valida_nome(teste)

def test_valida_nome_4_Fail(): # teste para ser invalidado
    teste= '1Alan'
    assert questao_1.valida_nome(teste)

def test_valida_nome_5_Fail(): # teste para ser invalidado
    teste= 'Alan'
    assert questao_1.valida_nome(teste)

def test_valida_nome_6_Fail(): # teste para ser invalidado
    teste= 'A1lan'
    assert questao_1.valida_nome(teste)

def test_valida_nome_7_Fail(): # teste para ser invalidado
    teste= 'A1an Turing'
    assert questao_1.valida_nome(teste)

def test_valida_nome_8_Fail(): # teste para ser invalidado
    teste= 'Alan turing'
    assert questao_1.valida_nome(teste)

# # ** TESTE EMAIL ** 

def test_valida_email_1():
    teste='a@a.br'
    assert questao_1.valida_email(teste)

def test_valida_email_2():
    teste='divulga@ufpa.br'
    assert questao_1.valida_email(teste)

def test_valida_email_3(): 
    teste= 'a@a.com.br'
    assert questao_1.valida_email(teste)

def teste_valida_email_4_Fail(): # teste para ser invalidado
    teste= '@'
    assert questao_1.valida_email(teste)

def teste_valida_email_5_Fail(): # teste para ser invalidado
    teste= 'a@.br'
    assert questao_1.valida_email(teste) 

def teste_valida_email_6_Fail(): # teste para ser invalidado
    teste= '@a.br'
    assert questao_1.valida_email(teste)

def teste_valida_email_7_Fail(): # teste para ser invalidado
    teste= 'T@teste.br'
    assert questao_1.valida_email(teste)

def teste_valida_email_8_Fail(): # teste para ser invalidado
    teste= 'a@A.com.br'
    assert questao_1.valida_email(teste)

# # ** TESTE SENHA ** 

def teste_valida_senha_1(): 
    teste= '518R2r5e'
    assert questao_1.valida_senha(teste)

def teste_valida_senha_2():
    teste= 'F123456A'
    assert questao_1.valida_senha(teste)

def teste_valida_senha_3():
    teste= '1234567T'
    assert questao_1.valida_senha(teste)

def teste_valida_senha_4():
    teste= 'ropsSoq0'
    assert questao_1.valida_senha(teste)

def teste_valida_senha_5_Fail(): # teste para ser invalidado
    teste= 'F1234567A'
    assert questao_1.valida_senha(teste)

def teste_valida_senha_6_Fail(): # teste para ser invalidado
    teste= 'abcdefgH'
    assert questao_1.valida_senha(teste)

def teste_valida_senha_7_Fail(): # teste para ser invalidado
    teste= '1234567HI'
    assert questao_1.valida_senha(teste)

# # ** TESTE CPF** 

def teste_valida_cpf_1():
    teste= '123.456.789-09'
    assert questao_1.valida_cpf(teste)

def teste_valida_cpf_2():
    teste= '000.000.000-00'
    assert questao_1.valida_cpf(teste)

def teste_valida_cpf_3_Fail(): # teste para ser invalidado
    teste= '123.456.789-0'
    assert questao_1.valida_cpf(teste)

def teste_valida_cpf_4_Fail(): # teste para ser invalidado
    teste= '111.111.11-11'
    assert questao_1.valida_cpf(teste)

# # ** TESTE TELEFONE ** 

def teste_valida_telefone_1():
    teste= '(91) 99999-9999'
    assert questao_1.valida_telefone(teste)

def teste_valida_telefone_2():
    teste= '(91) 999999999'
    assert questao_1.valida_telefone(teste)

def teste_valida_telefone_3():
    teste= '91 999999999'
    assert questao_1.valida_telefone(teste)

def teste_valida_telefone_4_Fail(): # teste para ser invalidado
    teste= '(91) 59999-9999'
    assert questao_1.valida_telefone(teste)

def teste_valida_telefone_5_Fail(): # teste para ser invalidado
    teste= '99 99999-9999'
    assert questao_1.valida_telefone(teste)

def teste_valida_telefone_6_Fail(): # teste para ser invalidado
    teste= '(94)95555-5555'
    assert questao_1.valida_telefone(teste)

# ** TESTE DATA_HORARIO **

def teste_valida_data_hora_1():
    teste= '31/08/2019 20:14:55'
    assert questao_1.valida_data_horario(teste)

def teste_valida_data_hora_2():
    teste= '99/99/9999 23:59:59'
    assert questao_1.valida_data_horario(teste)

def teste_valida_data_hora_3_Fail(): # teste para ser invalidado
    teste= '99/99/9999 3:9:9'
    assert questao_1.valida_data_horario(teste)

def teste_valida_data_hora_4_Fail(): # teste para ser invalidado
    teste= '9/9/99 99:99:99'
    assert questao_1.valida_data_horario(teste)

def teste_valida_data_hora_5_Fail(): # teste para ser invalidado
    teste= '99/99/999903:09:09'
    assert questao_1.valida_data_horario(teste)

def teste_valida_data_hora_6_Fail(): # teste para ser invalidado
    teste= 'a9/99/9999 03:09:09'
    assert questao_1.valida_data_horario(teste)

def teste_valida_data_hora_7_Fail(): # teste para ser invalidado
    teste= 'a9/99/9999 0a:09:09'
    assert questao_1.valida_data_horario(teste)

# ** TESTE NUMERO_REAL ** 

def teste_valida_num_real_1():
    teste= '-25.467'
    assert questao_1.valida_numReal(teste)

def teste_valida_num_real_2():
    teste= '1'
    assert questao_1.valida_numReal(teste)

def teste_valida_num_real_3():
    teste= '-1'
    assert questao_1.valida_numReal(teste)

def teste_valida_num_real_4():
    teste= '+1'
    assert questao_1.valida_numReal(teste)

def teste_valida_num_real_5():
    teste= '64.2'
    assert questao_1.valida_numReal(teste)

def teste_valida_num_real_6_Fail(): # teste para ser invalidado
    teste= '1.'
    assert questao_1.valida_numReal(teste)

def teste_valida_num_real_7_Fail(): # teste para ser invalidado
    teste= '.2'
    assert questao_1.valida_numReal(teste)

def teste_valida_num_real_8_Fail(): # teste para ser invalidado
    teste= '+64,2'
    assert questao_1.valida_numReal(teste)