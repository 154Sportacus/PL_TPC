import re

header = re.compile(r'^(#{1,3})\s+(.*)$')
bold = re.compile(r'\*\*(.+?)\*\*')
italic = re.compile(r'\*(.+?)\*')
lista = re.compile(r'^\d+\.\s+(.*)$')
link = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
imagem = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')

def converte_md_html(texto):
    resultado, in_lista = [], False
    for linha in texto.splitlines():
        m = header.match(linha)
        if m:
            nivel = len(m.group(1))
            resultado.append(f'<h{nivel}>{m.group(2)}</h{nivel}>')
            continue
        m = lista.match(linha)
        if m:
            if not in_lista:
                resultado.append('<ol>')
                in_lista = True
            resultado.append(f'<li>{m.group(1)}</li>')
            continue
        elif in_lista:
            resultado.append('</ol>')
            in_lista = False
        linha = imagem.sub(r'<img src="\2" alt="\1"/>', linha)
        linha = link.sub(r'<a href="\2">\1</a>', linha)
        linha = bold.sub(r'<b>\1</b>', linha)
        linha = italic.sub(r'<i>\1</i>', linha)
        resultado.append(linha)
    if in_lista:
        resultado.append('</ol>')
    return '\n'.join(resultado)

with open('in', 'r', encoding='utf-8') as f:
    conteudo = f.read()

resultado = converte_md_html(conteudo)

with open('out', 'w', encoding='utf-8') as f:
    f.write(resultado)
