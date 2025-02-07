import os

def somadorOnOff(texto):
    sum_flag = True
    result = 0
    i = 0
    while i < len(texto):
        line = ""
        while i < len(texto) and texto[i] != "\n":
            line = line + texto[i]
            i = i + 1
        if i < len(texto) and texto[i] == "\n":
            i = i + 1
        j = 0
        while j < len(line):
            if line[j] == "=":
                print(result)
                j = j + 1
            elif j <= len(line) - 3 and line[j:j+3].lower() == "off":
                sum_flag = False
                j = j + 3
            elif j <= len(line) - 2 and line[j:j+2].lower() == "on":
                sum_flag = True
                j = j + 2
            elif sum_flag and line[j].isdigit():
                num_str = line[j]
                k = j + 1
                while k < len(line) and line[k].isdigit():
                    num_str = num_str + line[k]
                    k = k + 1
                result = result + int(num_str)
                j = k
            else:
                j = j + 1
    print(result)
    return result

def main(ficheiro="demo.txt"):
    file = open(ficheiro, 'r', encoding='utf-8')
    conteudo = file.read()
    file.close()
    result = somadorOnOff(conteudo)


if __name__ == "__main__":
    main()
