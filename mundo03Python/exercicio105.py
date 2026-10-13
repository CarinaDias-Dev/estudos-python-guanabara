def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas de alunos (aceita várias)
    :Param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r

resp = notas(5.5, 9.5, 2, 6.5, 7.8, sit=True)
print(resp)
