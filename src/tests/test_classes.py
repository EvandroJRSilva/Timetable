
from algoritmo_genetico.classes import *
import numpy as np

# Horários: Manhã
horarios_manha = [('08:20', '09:10'), ('09:10', '10:00'), ('10:10', '11:00'), ('11:00', '11:50'),
                  ('11:50', '12:40')]
horarios_noite = [('18:30', '19:20'), ('19:20', '20:10'), ('20:20', '21:10'), ('21:10', '22:00')]

dias = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')


# Disciplinas
disciplinas_ads = [Disciplina(nome='Redes de Computadores', matricula='XXXXXXXX', curso=0),
               Disciplina(nome='Matemática Aplicada', matricula='XXXXXXXX', curso=0)]

disciplinas_cc = [Disciplina(nome='Redes de Computadores', matricula='XXXXXXXX', curso=1),
               Disciplina(nome='Matemática Aplicada', matricula='XXXXXXXX', curso=1)]


# Turmas
turmas_ads = [Turma(0, 'FAP0400103NMA', '3-ADS-A'), Turma(0, 'FAP0400103NMB', '3-ADS-B')]

turmas_cc = [Turma(1, 'FAP0790103NMA', '3-CC-M'), Turma(1, 'FAP0790101NNA', '1-CC-N')]

#---------------------------------------------------
# TODO: checkbox para ligar uma turma às disciplinas
#---------------------------------------------------

# Professores
professores = [Professor('Fulano'), Professor('Cicrano'), Professor('Deltano')]

professores[0].horarios_disponibilidade.append((dias[0], horarios_manha[0]))
professores[0].horarios_disponibilidade.append((dias[0], horarios_manha[1]))

aulas = np.array([
    Aula(disciplina=disciplinas_ads[0], professor=professores[0], turma=turmas_ads[0], dia=dias[0], horario=[horarios_manha[0], horarios_manha[1]])
])

print(f'Disponibilidade do professor {professores[0].nome}:')
for hd in professores[0].horarios_disponibilidade:
    print(hd)
    #print(f'{hd[0][0]}: {hd[0][1]}')

print(f'Dados da aula {aulas[0].id}:')
print(f'\tDia: {aulas[0].dia}.')
print(f'\tHorário: {aulas[0].horario}')
print(f'\tDisciplina: {aulas[0].disciplina.nome}.')
