from classes import *

# Horários: Manhã
horario_m1 = Horario('08:20', '09:10')
horario_m2 = Horario('09:10', '10:00')
horario_m3 = Horario('10:10', '11:00')
horario_m4 = Horario('11:00', '11:50')
horario_m5 = Horario('11:50', '12:40')

# Horários: Noite
horario_n1 = Horario('18:30', '19:20')
horario_n2 = Horario('19:20', '20:10')
horario_n3 = Horario('20:20', '21:10')
horario_n4 = Horario('21:10', '22:00')

# Disciplinas
disc1 = Disciplina(nome='Redes de Computadores', matricula='XXXXXXXX', curso=0)
disc2 = Disciplina(nome='Redes de Computadores', matricula='XXXXXXXX', curso=1)

# Turmas
turma_3adsA = Turma(0, 'FAP0400103NMA', '3-ADS-A')
turma_3adsB = Turma(0, 'FAP0400103NMB', '3-ADS-B')

# Professores
professor1 = Professor('Fulano')
professor2 = Professor('Cicrano')

professor1.horarios_disponibilidade.append(('Segunda', horario_m1))

aula1 = Aula(disciplina=disc1, professor=professor1, turma=turma_3adsA, dia='Segunda', horario=[horario_m1])