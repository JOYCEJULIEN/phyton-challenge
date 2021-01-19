import os
import csv
import sys

suma=0
cambio=0
ayuda=0
cambios_lis=[]
cambioaux=0
cambiomayor=0
cambiomenor=0
base_csv = os.path.join('', 'Resources', 'budget_data.csv')
with open(base_csv, encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    for line in csvreader: 
        if ayuda==0:
          line.append("Cambios")
          print(line)
        if ayuda==1:
            suma=int(line[1])+suma
            line.append("")
            cambioaux=int(line[1])
            print(line)
        if ayuda>1:
            suma=int(line[1])+suma
            cambioaux=int(line[1])-cambioaux
            line.append(int(cambioaux))
            cambios_lis.append(int(cambioaux))
            if cambioaux<cambiomenor:
                   cambiomenor=cambioaux
                   fechamenor=line[0]
            if cambioaux>cambiomayor:
                   cambiomayor=cambioaux
                   fechamayor=line[0]
            cambioaux=int(line[1])
            print(line)
        ayuda=ayuda+1
promediocambio=sum(cambios_lis) / len(cambios_lis)
print(suma,promediocambio,fechamenor,cambiomenor,fechamayor,cambiomayor,ayuda-1)
print(f'Financial Analysis')
print(f'Total: ',suma)
print(f'Average change: ',promediocambio)
print(f'Greatest increase : ',fechamayor,"(",cambiomayor,")")
print(f'Greatest decrease : ',fechamenor,"(",cambiomenor,")")

sys.stdout = open('analysis.txt','wt')
print(f'Financial Analysis')
print(f'Total: ',suma)
print(f'Average change: ',promediocambio)
print(f'Greatest increase : ',fechamayor,"(",cambiomayor,")")
print(f'Greatest decrease : ',fechamenor,"(",cambiomenor,")")

       
