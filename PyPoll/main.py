import os
import csv
import sys
sumacandidato=[]
candidato=[]
sumavotos=0
ayuda=0

base_csv = os.path.join('', 'Resources', 'election_data.csv')
with open(base_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for line in csvreader: 
      if ayuda>=1:
         if line[2] not in candidato:
           candidato.append(line[2])
           sumacandidato.append(0)   
         if line[2] in candidato:
           a=candidato.index(line[2])
           sumacandidato[a]=sumacandidato[a]+1
      ayuda=ayuda+1
     
c=sumacandidato.index(max(sumacandidato))
print(candidato[c])
print(candidato)
print(sumacandidato)
print(sum(sumacandidato))


#sys.stdout = open('analysis.txt','wt')
print(f'Election Results')
print(f'_________________________________')
print(f'Total Votes: ',sum(sumacandidato))
print(f'_________________________________')
for candidatos in candidato:
  a=candidato.index(candidatos)
  promedio=float((sumacandidato[a]/sum(sumacandidato))*100)
  print(candidatos," : ","{0:.2f}".format(promedio)," %   "," (",sumacandidato[a],")")
print(f'_________________________________')
c=sumacandidato.index(max(sumacandidato))
print(f'Winner: ',candidato[c])
