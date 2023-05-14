import re


def valida_nome(n: str) -> bool:
  """
    Validação de nome, nome do meio(opcional) e sobrenome,
    onde ambos se iniciam com letra maiúscula, 
    tendo apenas um espaço entre eles, não aceitando caracteres especiais ou números.

    Args:
       Cadeia de string
    Return:
        Valor booleano, validando se a cadeia do parâmetro 
        faz parte da linguagem estabelecida.
    """

  m = re.search(r'[A-Z][a-z]+(([ ][A-Z][a-z]+)?)[ ][A-Z][a-z]+', n)
  if m == None:
    return False
  elif m.group() == n:
    return True
  else:
    return False


def valida_email(cadeia: str) -> bool:
  """
    Validação de email, em que deve ter somente um @, com pelo menos 
    1 alfanumérico antes, e somente string minúsculas após. Deve terminar 
    com a sub cadeia '.br' ou '.com.br'.
        
    Arguments: 
      Cadeia de string.
    Return: 
      Valor booleano, validando se a cadeia do parâmetro faz parte 
      da linguagem estabelecida. 
    """

  padrao_regex = r"^[a-zA-Z0-9]+@[a-z]+(.com.br|.br)$"
  validacao = re.search(padrao_regex, cadeia)
  return validacao


def valida_senha(senha: str) -> bool:
  """
        Validação de senha, em que podem ter símbolos minúsculos, maiúsculos e dígitos.
    Deve conter pelo menos um símbolo maiúsculo e um dígito. O comprimento deve ser igual a 8.

    Args:
        Cadeia de string
    Return:
        Valor booleano, afirmando se a cadeia informada faz parte da linguagem.

    """

  padrao_regex = r"^(?=.*[A-Z])(?=.*[0-9])[A-Za-z0-9]{8}$"
  valido = re.search(padrao_regex, senha)
  return bool(valido)


def valida_cpf(cadeia: str) -> bool:
  """
    Validação de cpf onde as sentenças devem ter o formato xxx.xxx.xxx-xx, 
    e x deve pertencer ao alfabeto N={0,1,2,...,9}.

    Args: 
      Cadeia de string.
    Return: 
      Valor booleano, verificando se a cadeia passada no parâmetro da função respeita o padrao predeterminado.
    """
  cpf_regex = re.compile(r'^((\d){3}\.){2}(\d){3}\-(\d){2}$', flags=re.M)
  match = cpf_regex.search(cadeia)
  return match


def valida_telefone(n: str) -> bool:
  """
    Validação de telefone tendo os seguintes padrões: 
    (xx) 9xxxx-xxxx
    (xx) 9xxxxxxxx
    xx 9xxxxxxxx
    Sendo x uma string de número inteiro

    Args:
        Cadeia de string
    Return:
        Valor booleano, validando se a cadeia do parâmetro faz parte da linguagem                   estabelecida
    """

  m = re.search(
    r'((\([0-9]{2}\)[ ])(([9][0-9]{4}\-[0-9]{4})|([9][0-9]{8})))|([0-9][0-9][ ][9][0-9]{8})',
    n)
  if m == None:
    return False
  elif m.group() == n:
    return True
  else:
    return False


def valida_data_horario(cadeia: str) -> bool:
  """
    Validação de data e hora, em que as sentenças devem ter o formato dd/mm/aaaa hh:mm:ss, onde d, m, a, h, m, s ∈ N.

    Arguments: 
      Cadeia de strings.
    Return: 
      Valor booleano, validando se a cadeia colocada no parâmentro faz parte do regex
      estabelecido.
  """

  padrao_regex = r"^[0-9]{2}/[0-9]{2}/[0-9]{4} [0-9]{2}:[0-9]{2}:[0-9]{2}"
  validacao = re.search(padrao_regex, cadeia)
  return validacao


def valida_numReal(numero):
  """
        Validação de número real (com ou sem sinal). Podem começar com os símbolos
        "+" ou "-" ou "ε". Em seguida devem ter, pelo menos, um número natural. Em 
        seguida, devem ter, exatamente, um símbolo separador ".". Em seguida, devem
        finalizar com, pelo menos, um número natural.

        Exceção:
            Devem ser aceitos números sem a parte fracionária.

        Args:
            Número Real
        Return: 
            Valor booleano, afirmando se a o número real informado satisfaz os requisitos da 
            linguagem.
    """

  padrao_regex = r"^[+-]?[0-9]+(\.[0-9]+)?$"
  valido = re.search(padrao_regex, numero)
  return bool(valido)
