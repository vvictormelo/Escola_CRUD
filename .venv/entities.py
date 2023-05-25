class TipoCurso:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao


class Titulo:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao


class Instituicao:
    def __init__(self, id, sigla, descricao):
        self.id = id
        self.sigla = sigla
        self.descricao = descricao


class TipoDisciplina:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao


class Professor:
    def __init__(self, id, nome, sexo, estado_civil, nascimento, telefone):
        self.id = id
        self.nome = nome
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.nascimento = nascimento
        self.telefone = telefone
