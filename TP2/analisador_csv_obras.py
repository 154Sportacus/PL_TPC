import re

pattern = re.compile(r'^(\w+);(\w+);(\w+);(\w+);(\w+);(\w+);(\w+)$')

compositores = set()          
periodo_counts = {}           
periodo_titles = {}

           
with open('obras.csv', 'r', encoding='utf-8') as f:
    header = f.readline()  # Skip cabeçalho dude
    for line in f:
        line = line.strip()
        if not line:
            continue
        match = pattern.match(line)
        if not match:
            print("Erro ao processar a linha:", line)
            continue

       
        nome, desc, anoCriacao, periodo, compositor, duracao, _id = match.groups()
        
       
        compositores.add(compositor)
        
        # Update that count ;)
        periodo_counts[periodo] = periodo_counts.get(periodo, 0) + 1
        
        
        if periodo not in periodo_titles:
            periodo_titles[periodo] = []
        periodo_titles[periodo].append(nome)


lista_compositores = sorted(compositores)

for p in periodo_titles:
    periodo_titles[p] = sorted(periodo_titles[p])

#print("Lista de compositores (ordenada):")
#print(lista_compositores)
#print("\nDistribuição de obras por período:")
#print(periodo_counts)
#print("\nDicionário de obras por período (títulos ordenados):")
#print(periodo_titles)
