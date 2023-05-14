import re
from itertools import product


def regex_2_a(cadeia:str)-> bool: 
  """
    Validação de uma família seguindo o seguinte padrão: 
    ◦ H representa um homem;
    ◦ M representa uma mulher;
    ◦ h representa um filho do sexo masculino (natural ou adotado);
    ◦ m representa uma filha do sexo feminimo (natural ou adotado);
    ◦ A posição relativa de uma letra em relação às demais indica a idade relativa daquele
    membro da família em relação aos demais (os mais novos estão sempre à direita).

    Sendo os casais heterossexuais mais velhos que os filhos e com pelo menos duas filhas mulheres,
    ou pelo menos um filho homem, ou ainda pelo menos dois filhos homens e uma filha
    mulher
    Arguments:
        Cadeia de string
    Return:
        Valor booleano, validando se a cadeia do parâmetro 
        faz parte da linguagem estabelecida.
    """
  regex_A = re.compile(r'^(HM|MH)(mm+|h+|hhm+)(h|m)*$')
  match = regex_A.search(cadeia)
  return bool(match)

def regex_2_b(cadeia:str)-> bool:
  """
    Validação de uma família seguindo o seguinte padrão: ◦ H representa um homem;
    ◦ M representa uma mulher;
    ◦ h representa um filho do sexo masculino (natural ou adotado);
    ◦ m representa uma filha do sexo feminimo (natural ou adotado);
    ◦ A posição relativa de uma letra em relação às demais indica a idade relativa daquele
    membro da família em relação aos demais (os mais novos estão sempre à direita).

    Sendo os casais heterossexuais mais velhos que os filhos e com uma quantidade ímpar de filhas
    mulheres.

    Arguments:
        Cadeia de string
    Return:
        Valor booleano, validando se a cadeia do parâmetro 
        faz parte da linguagem estabelecida.
    """
  m = re.search(r'([M][H]|[H][M])h*mh*(h*mh*mh*)*', cadeia)
  if m == None:
    return False
  elif m.group() == cadeia:
    return True
  else:
    return False


def regex_2_c(cadeia: str) -> bool:
  """
    Casais heterossexuais mais velhos que os filhos, com a filha mais velha mulher e o filho
    mais novo homem.

    Arguments: 
        Cadeia de string
    Return: 
        valor booleano, validando se a cadeia faz parte do regex
        estabelcido.
    """
  padrao_regex = r'^(HM|MH)m(h|m)*h$'
  validacao = re.search(padrao_regex, cadeia)
  return validacao


def regex_2_d(cadeia):
  """
    Casais homossexuais mais velhos que os filhos, com pelo menos seis filhos, em que os
    dois primeiros filhos formam um casal e os últimos também

    Args:
        Cadeia de String
    Return: 
        Valor booleano, afirmando se a cadeia informada faz parte da linguagem.
    """

  padrao_regex = r"^(HH|MM)(hm|mh)(m|h){2}(m|h)*(hm|mh)$"
  valido = re.search(padrao_regex, cadeia)
  return bool(valido)


def regex_2_e(cadeia:str)-> bool:
  """
    Validação de uma família seguindo o seguinte padrão: 
    ◦ H representa um homem;
    ◦ M representa uma mulher;
    ◦ h representa um filho do sexo masculino (natural ou adotado);
    ◦ m representa uma filha do sexo feminimo (natural ou adotado);
    ◦ A posição relativa de uma letra em relação às demais indica a idade relativa daquele
    membro da família em relação aos demais (os mais novos estão sempre à direita).

    Casais homossexuais mais velhos que os filhos, em que o sexo dos filhos é alternado
    conforme a ordem de nascimento.

    Arguments:
        Cadeia de string
    Return:
        Valor booleano, validando se a cadeia do parâmetro 
        faz parte da linguagem estabelecida.
    """
  regex_E = re.compile(r'^(HH|MM)((hm)*h?|(mh)*m?)$')
  validacao_e = regex_E.search(cadeia)
  return bool(validacao_e)

def regex_2_f(cadeia:str)->bool:
  """
    Validação de uma família seguindo o seguinte padrão:
    ◦ H representa um homem;
    ◦ M representa uma mulher;
    ◦ h representa um filho do sexo masculino (natural ou adotado);
    ◦ m representa uma filha do sexo feminimo (natural ou adotado);
    ◦ A posição relativa de uma letra em relação às demais indica a idade relativa daquele
    membro da família em relação aos demais (os mais novos estão sempre à direita).

    Sendo os casais homossexuais mais velhos que os filhos, com qualquer quantidade de filhos
    homens e mulheres, mas que não tiveram dois filhos homens consecutivos.

    Args:
        Cadeia de string
    Return:
        Valor booleano, validando se a cadeia do parâmetro faz parte da linguagem estabelecida
    """
  m = re.search(r"^((MM|HH)((m|hm)([h|m])*)?)$|^(MMh|HHh)$", cadeia)
  if m == None:
    return False
  elif m.group() == cadeia:
     return True
  else:
        return False  



def regex_2_g(x: int, y: int, cadeia_filho: str) :
  """
    Arranjo de no mínimo x∈ℕ e no máximo y ∈ℕ , com x> 0 , y > 0 , e x≤ y , de
    adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos
    homens e mulheres, mas que os três filhos mais novos não foram homens.

    Arguments: 
        cadeia de strings
        x = int, que corresponde ao valor mínimo de adultos
        y = int, que corresponde ao valor máximo de adultos
    Return: 
        cadeias em que seguem a regra pré estabelecida, sendo feita os arranjos de adultos
        e com a verificação dos filhos.
    """
  adultos = ['H', 'M']
  arranjos = []

  if x <= y:
    padrao = fr"^(H|M){{{x},{y}}}(((h|m)*(m{{1,2}}|mh{{1,2}}))|h{{1,2}})?$"
    for i in range(x, y + 1):
      for i in product(adultos, repeat=i):
        arranjos = ''.join(i)
        arranjos += cadeia_filho
        verificacao = re.search(padrao, arranjos)
        print(f'{arranjos} -> Cadeia validada') if verificacao else print(
          f'{arranjos} -> Cadeia não validada.')
    return verificacao
  else:
    return False


# print(regex_2_g(2, 3, 'hmmmmhhh'))
