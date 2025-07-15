# Algoritmo Genético - TCC do Chrystien

## 5. UM ALGORITMO GENÉTICO PARA GERAÇÃO DE GRADE DE HORÁRIOS

### 5.1. Codificação do indivíduo

> As tabelas foram ajustadas para poder manter as notações padrões.

O indivíduo é um `array` com um período em cada posição.

<style type="text/css">
.tg  {border-collapse:collapse;border-color:#9ABAD9;border-spacing:0;}
.tg td{background-color:#EBF5FF;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#444;
  font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{background-color:#409cff;border-color:#9ABAD9;border-style:solid;border-width:1px;color:#fff;
  font-family:Arial, sans-serif;font-size:14px;font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-baqh{text-align:center;vertical-align:top}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-7btt{border-color:inherit;font-weight:bold;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .tg-0lax{text-align:left;vertical-align:top}
</style>

<table class="tg"><thead>
  <tr>
    <th class="tg-7btt" colspan="4">Indivíduo</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Período 1</td>
    <td class="tg-0pky">Período 2</td>
    <td class="tg-0pky">...</td>
    <td class="tg-0pky">Período P</td>
  </tr>
</tbody>
</table>

Para cada período existe uma matriz:

<table class="tg"><thead>
  <tr>
    <th class="tg-7btt"></th>
    <th class="tg-c3ow">Dia 1</th>
    <th class="tg-c3ow">Dia 2</th>
    <th class="tg-c3ow">...</th>
    <th class="tg-baqh">Dia D</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Horário 1</td>
    <td class="tg-c3ow">A<sub>0,0</sub></td>
    <td class="tg-c3ow">A<sub>0,1</sub></td>
    <td class="tg-c3ow">...</td>
    <td class="tg-baqh">A<sub>0,D-1</sub></td>
  </tr>
  <tr>
    <td class="tg-0lax">Horário 2</td>
    <td class="tg-baqh">A<sub>1,0</sub></td>
    <td class="tg-baqh">A<sub>1,1</sub></td>
    <td class="tg-baqh">...</td>
    <td class="tg-baqh">A<sub>1,D-1</sub></td>
  </tr>
  <tr>
    <td class="tg-baqh">...</td>
    <td class="tg-baqh">...</td>
    <td class="tg-baqh">...</td>
    <td class="tg-baqh">...</td>
    <td class="tg-baqh">...</td>
  </tr>
  <tr>
    <td class="tg-0lax">Horário H</td>
    <td class="tg-baqh">A<sub>H-1,0</sub></td>
    <td class="tg-baqh">A<sub>H-1,1</sub></td>
    <td class="tg-baqh">...</td>
    <td class="tg-baqh">A<sub>H-1,D-1</sub></td>
  </tr>
</tbody>
</table>

Onde $H = [0,H[$ e $D = [0,D[$. Cada elemento da matriz é uma aula, a qual possui os seguintes campos:

* **Disciplina**: *null* | nome
* **Professor**: *null* | nome
* **Turma**: *null* | nome
* **ID**: 0 | ...

## Adaptação para a Uninassau

Na Uninassau os coordenadores precisam criar grades horárias para diversas turmas. Em cada semestre todas as turmas estarão em um período ímpar (primeiro semestre do ano), ou um período par (segundo semestre do ano). A partir disso, o componente principal do `indivíduo` deixa de ser o **período** e passa a ser a **turma**.

O indivíduo passa a ser codificado da seguinte forma:

<table class="tg"><thead>
  <tr>
    <th class="tg-7btt" colspan="4">Indivíduo</th>
  </tr></thead>
<tbody>
  <tr>
    <td class="tg-0pky">Turma 1</td>
    <td class="tg-0pky">Turma 2</td>
    <td class="tg-0pky">...</td>
    <td class="tg-0pky">Turma T</td>
  </tr>
</tbody>
</table>

Cada **Turma** passa a consistir em uma matriz contendo sua grade horária, e os elementos da matriz continuam sendo as aulas. Para uma melhor organização dos elementos pertencentes a este problema, o paradigma de Programação Orientada a Objetos se mostra vantajoso.