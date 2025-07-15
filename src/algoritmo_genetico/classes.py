from typing import List, Tuple

class Disciplina:
    """
    Atributos:
        curso     (int): 0 para ADS e 1 para CC.
        nome      (str): o nome da disciplina.
        matricula (str): matrícula da disciplina.
    """
    
    def __init__(self, curso, nome, matricula):
        if curso == 0:
            self.curso = 'Análise e Desenvolvimento de Sistemas'
        elif curso == 1:
            self.curso = 'Ciência da Computação'
        else:
            raise ValueError("O valor esperado para curso é 0 (ADS) ou 1 (CC).")
        self.nome = nome
        self.matricula = matricula



class Turma:
    """
    Atributos
        curso     (int): 0 para ADS e 1 para CC.
        matricula (str): matrícula da turma.
        nome      (str): apelido/nome da turma; opcional.
    """
    def __init__(self, curso, matricula, nome=''):
        if curso == 0:
            self.curso = 'Análise e Desenvolvimento de Sistemas'
        elif curso == 1:
            self.curso = 'Ciência da Computação'
        else:
            raise ValueError("O valor esperado para curso é 0 (ADS) ou 1 (CC).")
        self.matricula = matricula
        self.nome = nome
        
        
        
class Horario:
    """
    Atributos
        h_inicio (str): hora de início do horário.
        h_fim    (str): hora de fim do horário.
    """
    def __init__(self, h_inicio, h_fim):
        self.h_inicio = h_inicio
        self.h_fim = h_fim
        
        
        
class Professor:
    """
    Atributos
        nome (str): Nome do(a) professor(a).
        horarios_disponibilidade (list[tuple[str, Horario]]): Lista de tuplas (dia, horário) representando os dias e horários disponíveis.
        preferencia_disciplina (list[Disciplina]): Lista de disciplinas que o(a) professor(a) prefere ministrar.
    """
    
    def __init__(self, nome):
        self.nome: str = nome
        self.horarios_disponibilidade = []
        self.preferencia_disciplina = []



class Aula:
    """
    Atributos
        id (int): id para quando houver aula da mesma disciplina e turma em dia(s)/horário(s) diferente(s). Por padrão, o valor é 0.
        
        modalidade (int): indica a modalidade da aula específica; 0 para presencial e 1 para on-line. Por padrão 0.
        
        disciplina (obj): objeto da classe Disciplina.
        
        professor (obj): objeto da classe Professor.
        
        turma (obj): objeto da classe Turma.
        
        dia (str): dia em que a aula deve ocorrer. Exemplo: 'Seg'.
        
        horario (list[Horario]): uma lista de objetos da classe Horário. A aula pode consistir em somente 1 horário, ou, como ocorre na maioria das vezes, consiste em 2 horários.
    """
    
    def __init__(self, id=0, modalidade=0, *,disciplina, professor, turma, dia, horario):
        self.id = id
        self.modalidade = modalidade
        self.disciplina = disciplina
        self.professor = professor 
        self.turma = turma
        self.dia = dia
        self.horario = []
        self.horario.extend(horario)