import csv

archivo_csv = 'csv\data_person.csv'
grupos = {'M': [], 'F': []}

with open(archivo_csv, newline='') as csvfile:
    for row in csv.DictReader(csvfile):
        grupos[row['Sexo'].strip()].append(row)

# Mostrar los datos en formato CSV
for genero, personas in grupos.items():
    print(f"{genero}:\n")
    if personas:
        print("Nombre,Sexo,Edad")
        for persona in personas:
            print(f"{persona['Nombre']},{persona['Sexo']},{persona['Edad']}")
    else:
        print("No hay personas en este grupo.")
    print("\n")
