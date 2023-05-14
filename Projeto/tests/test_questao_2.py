from Projeto.Questao_2 import questao_2

# ** TESTE LETRA A ** 

# def test_letra_a_1(): # rever
#     teste= 'HMmmmhmhmh'
#     assert questao_2.regex_2_a(teste)

# def test_letra_a_2(): # rever 
#     teste= 'HMhmmm'
#     assert questao_2.regex_2_a(teste)

def test_letra_a_3():
    teste='MHhhmm'
    assert questao_2.regex_2_a(teste)

def test_letra_a_4():
    teste= 'MHhmmmhmh'
    assert questao_2.regex_2_a(teste)

# def test_letra_a_5(): # rever 
#     teste= 'HMhmmmhhhmmmmhhhhm'
#     assert questao_2.regex_2_a(teste)

def test_letra_a_6_Fail(): # teste para ser invalidado
    teste='HHmmhh'
    assert questao_2.regex_2_a(teste)

def test_letra_a_7_Fail(): # teste para ser invalidado
    teste= 'MMhmmm'
    assert questao_2.regex_2_a(teste)

def test_letra_a_8_Fail(): # teste para ser invalidado 
    teste= 'HMm'
    assert questao_2.regex_2_a(teste)

def test_letra_a_9_Fail(): # teste para ser invalidado
    teste= 'MH'
    assert questao_2.regex_2_a(teste)

def test_letra_a_10_Fail(): # teste para ser invalidado
    teste= 'HHm'
    assert questao_2.regex_2_a(teste)

# ** TESTE LETRA B ** 

def test_letra_b_1():
    teste= 'HMhhhhm'
    assert questao_2.regex_2_b(teste)

def test_letra_b_2():
    teste= 'MHmmmhhhhhmm'
    assert questao_2.regex_2_b(teste)

def test_letra_b_3():
    teste= 'HMmmm'
    assert questao_2.regex_2_b(teste)

def test_letra_b_4():
    teste= 'MHhhhhhmmmmmmmmm' # 9 m's
    assert questao_2.regex_2_b(teste)

def test_letra_b_5_Fail(): # teste para ser invalidado
    teste= 'HHhhhhm'
    assert questao_2.regex_2_b(teste)

def test_letra_b_6_Fail(): # teste para ser invalidado
    teste= 'MMmmm'
    assert questao_2.regex_2_b(teste)

def test_letra_b_7_Fail(): # teste para ser invalidado 
    teste= 'HMmmmm'
    assert questao_2.regex_2_b(teste)

def test_letra_b_8_Fail(): # teste para ser invalidado 
    teste= 'HMhmhmhmhmhmm'
    assert questao_2.regex_2_b(teste)


# ** TESTE LETRA C ** 

def test_letra_c_1():
    teste= 'MHmhhmhmmhmmhmh'
    assert questao_2.regex_2_c(teste)

def test_letra_c_2():
    teste= 'HMmhmmh'
    assert questao_2.regex_2_c(teste)

def test_letra_c_3():
    teste= 'MHmhhmhmhmhmhmhmhmhmhmhmhmhmhmhmhmhhhhhmmh'
    assert questao_2.regex_2_c(teste)

def test_letra_c_4_Fail():  # teste para ser invalidado
    teste= 'MMmhmhmhmhh'
    assert questao_2.regex_2_c(teste)

def test_letra_c_5_Fail():  # teste para ser invalidado
    teste= 'HHmhmhmhhhmhmmhhhh'
    assert questao_2.regex_2_c(teste)

def test_letra_c_6_Fail():  # teste para ser invalidado
    teste= 'MHmhmhmhmhmmhmm'
    assert questao_2.regex_2_c(teste)

def test_letra_c_7_Fail():  # teste para ser invalidado
    teste= 'HMhmmhmhmmhmh'
    assert questao_2.regex_2_c(teste)

def test_letra_c_8_Fail():  # teste para ser invalidado
    teste= 'MHhmhmhmhmhmm'
    assert questao_2.regex_2_c(teste)

# ** TESTE LETRA D ** 

def test_letra_d_1(): 
    teste= 'HHmhhmhmhmmmhmh'
    assert questao_2.regex_2_d(teste)

def test_letra_d_2():
    teste= 'MMhmhmhmmhmmhmhmhm'
    assert questao_2.regex_2_d(teste)

def test_letra_d_3():
    teste= 'HHmhhmmhmmhmhmhm'
    assert questao_2.regex_2_d(teste)

def test_letra_d_4():
    teste= 'MMhmhmhmhmhmhmmhmmh'
    assert questao_2.regex_2_d(teste)

def test_letra_d_5():
    teste= 'HHhmmmmh'
    assert questao_2.regex_2_d(teste)

def test_letra_d_6_Fail(): # teste para ser invalidado
    teste= 'HMhmmmmh'
    assert questao_2.regex_2_d(teste)

def test_letra_d_7_Fail(): # teste para ser invalidado
    teste= 'MHmhhmmhmmhmhmhm'
    assert questao_2.regex_2_d(teste)

def test_letra_d_8_Fail(): # teste para ser invalidado
    teste= 'HHmmhhhhmh'
    assert questao_2.regex_2_d(teste)

def test_letra_d_9_Fail(): # teste para ser invalidado
    teste= 'MMmhhmhmhmhhh'
    assert questao_2.regex_2_d(teste)

def test_letra_d_10_Fail(): # teste para ser invalidado
    teste= 'MMmhhmh'
    assert questao_2.regex_2_d(teste)

# ** TESTE LETRA E ** 

def test_letra_e_1():
    teste= 'HHhmhmhmhmhmhm'
    assert questao_2.regex_2_e(teste)

def test_letra_e_2():
    teste='MMhm'
    assert questao_2.regex_2_e(teste)

def test_letra_e_3():
    teste= 'MMmhmhmhmhmhmh'
    assert questao_2.regex_2_e(teste)

def test_letra_e_4_Fail(): # teste para ser invalidado
    teste= 'HMhm'
    assert questao_2.regex_2_e(teste)

def test_letra_e_5_Fail(): # teste para ser invalidado
    teste= 'MHhmhmhmhmh'
    assert questao_2.regex_2_e(teste)
 
def test_letra_e_6_Fail(): # teste para ser invalidado
    teste= 'HHmmmhmhmh'
    assert questao_2.regex_2_e(teste)

def test_letra_e_7_Fail(): # teste para ser invalidado
    teste= 'MMhhhmhmhhmhh'
    assert questao_2.regex_2_e(teste)

def test_letra_e_8_Fail(): # teste para ser invalidado
    teste= 'HHmm'
    assert questao_2.regex_2_e(teste)

# ** TESTE LETRA F ** 

def test_letra_f_1():
    teste= 'HHhmmmmhmhmmhmmh'
    assert questao_2.regex_2_f(teste)

def test_letra_f_2():
    teste= 'MMmmmhmhmh'
    assert questao_2.regex_2_f(teste)

def test_letra_f_3():
    teste= 'HHmh'
    assert questao_2.regex_2_f(teste)

def test_letra_f_4():
    teste= 'MMh'
    assert questao_2.regex_2_f(teste)

def test_letra_f_5_Fail(): # teste para ser invalidado
    teste= 'MHhmmmmhmm'
    assert questao_2.regex_2_f(teste)

def test_letra_f_6_Fail(): # teste para ser invalidado
    teste= 'HMmh'
    assert questao_2.regex_2_f(teste)

def test_letra_f_7_Fail(): # teste para ser invalidado 
    teste= 'MMhhmmhh'
    assert questao_2.regex_2_f(teste)

def test_letra_f_8_Fail(): # teste para ser invalidado 
    teste= 'HHhh'
    assert questao_2.regex_2_f(teste)

# ** TESTE LETRA G ** 

def test_letra_g_1(): 
    x_teste= 2
    y_teste=3
    teste= 'hmhmhmmhmmhmmhmm'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)

def test_letra_g_2(): 
    x_teste= 4
    y_teste=5
    teste= 'mmmhhhhm'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)

def test_letra_g_3(): 
    x_teste= 5
    y_teste=7
    teste= 'mhhmhhhmhmmm'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)

def test_letra_g_4_Fail(): # teste para ser invalidado
    x_teste= 5
    y_teste=3
    teste= 'hmhmhmmhmmhmmhmm'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)

def test_letra_g_5_Fail(): # teste para ser invalidado
    x_teste= 2
    y_teste=3
    teste= 'mmmhhmmhhh'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)

def test_letra_g_6_Fail(): # teste para ser invalidado
    x_teste= 7
    y_teste=1
    teste= 'mhhh'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)

def test_letra_g_7_Fail(): # teste para ser invalidado
    x_teste= 10
    y_teste=11
    teste= 'hhh'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)

def test_letra_g_8(): 
    x_teste= 10
    y_teste=11
    teste= 'hmhhhhhmmmmmh'
    assert questao_2.regex_2_g(x_teste,y_teste,teste)


