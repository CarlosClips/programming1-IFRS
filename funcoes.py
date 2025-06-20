#Faça uma função que recebe por parâmetro o raio de uma esfera e calcula o seu
def calcular_volume_esfera(raio: int | float) -> float:
    volume = (4 * 3.14 * raio) / 3 
    return volume


#Questão 2. Escreva uma função que recebe as 3 notas de um aluno por parâmetro e uma letra.
#Se a letra for A o procedimento calcula a média aritmética das notas do aluno, se for P, a sua média
#ponderada (pesos: 5, 3 e 2) e se for H, a sua média harmônica. A média calculada também deve
#retornar por parâmetro.


def calcular_media_nota (nota1: int | float, nota2: int | float, nota3: int | float, letra: str) -> float:

    if letra == "A":
         media_aritmetica = (nota1 + nota2 + nota3) / 3
         return media_aritmetica
    elif letra == "P":
        media_ponderada = ((nota1 + 5) + (nota2 + 3) + (nota1 + 2)) / 10
        return media_ponderada
    elif letra == "H":
        media_harmônica = 3 / ((1/nota1) + (1/nota2) + (1/nota3))
        return media_harmônica
    
#Faça uma função que recebe por parâmetro um valor inteiro e positivo e retorna o
#valor lógico Verdadeiro caso o valor seja primo e Falso em caso contrário.

def verificar_eh_primo (valor: int):
    primo = True

    for div in range(2,valor):
        if(valor%div == 0):
            primo = False
    if(div > 1 and primo):
        return True
    else:
        return False
    

#Faça uma função que recebe por parâmetro os valores necessário para o cálculo da
#fórmula de báskara e retorna, também por parâmetro, as suas raízes, caso seja possível calcular.

def calcular_baskara (a: int | float, b: int | float, c: int | float) -> float:
    delta = b**2 - 4*a*c

    if a == 0:
        return print('Nao é possivel calcular')
    elif delta < 0:
        return print('Nao é possivel calcular')
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta **0.5) / (2*a)
        return raiz1, raiz2
      
      
      

#Faça uma função que recebe por parâmetro o tempo de duração de uma fábrica 
#expressa em segundos e retorna também por parâmetro esse tempo em horas, minutos e segundos

def calcular_seg_para_horas(segundos_duracao: int | float) -> float:
    horas = segundos_duracao // 3600
    resto = segundos_duracao % 3600
    minutos = resto // 60
    segundos = resto % 60

    return horas, minutos, segundos


#Questão 6. Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna 
#essa idade expressa em dias.

def calcular_idade_em_dias(anos: int, meses: int, dias: int) -> int:
    anos_para_dias = anos * 365
    meses_para_dias = meses * 30
    
    return anos_para_dias + meses_para_dias + dias


#Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito 
#quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3, 
#que são seus divisores). A função deve retornar um valor booleano.

def verificar_valor_perfeito(valor: int) -> bool:
    divisores = []

    for x in range(1,valor):
        if valor%x == 0:
            divisores.append(x)
    
    soma = sum(divisores)

    if soma == valor:
        return True
    else:
        return False
    
#Faça uma função que recebe a idade de um nadador por parâmetro e retorna , tamb
#ém por parâmetro, a categoria desse nadador de acordo com a tabela abaixo:

def verificar_categoria_nadador(idade: int) -> str:

    if  5 <= idade <= 7:
        return 'Infantil A'
    elif 8 <= idade <= 10:
        return 'Infantil B'
    elif 11 <= idade <= 13:
        return 'Juvenil A'
    elif 14 <= idade <= 17:
        return 'Juvenil B'
    elif 18 <= idade <= 80:
        return 'Adulto'
    else:
        return 'Sem categoria'
    
#Faça  uma  função  que  recebe  um  valor  inteiro  e  verifica  se  o  valor  é  positivo  ou 
#negativo. A função deve retornar um valor booleano.

def verificar_num_positivo_negativo(num: int | float) -> bool:
    return num > 0


#Faça uma função que recebe um valor inteiro e verifica se o valor é par ou ímpar. A 
#função deve retornar um valor booleano

def verificar_par_ou_impar(num: int) -> bool:
    if num%2 == 0:
        return True
    else:
        return False

#Faça uma função que recebe a média final de um aluno por parãmetro e retorna o 
#seu conceito, conforme a tabela abaixo: 

def calcular_conceito(media: float) -> str:
    
    if  0.0 <= media <= 4.9:
        return 'D'
    elif 5.0 <= media <= 6.9:
        return 'C'
    elif 7.0 <= media <= 8.9:
        return 'B'
    elif 9.0 <= media <= 10:
        return 'A'
    
#Faça uma função que recebe, por parâmetro, a altura (alt) e o sexo de uma pessoa e 
#retorna o seu peso ideal. Para homens, calcular o peso ideal usando a fórmula peso ideal = 72.7 x 
#alt - 58 e, para mulheres, peso ideal = 62.1 x alt - 44.7

def calcular_peso_ideal(altura: float, sexo: str) -> float:
    if sexo == 'H':
        peso_ideal = (72.7 * altura) - 58
    elif sexo == "M":
        peso_ideal = (62.1 * altura) - 44.7

    return peso_ideal

#Faça uma função que recebe 3 valores inteiros por parâmetro e retorna-os ordenados 
#em ordem crescente

def ordenar_numeros(valor1: int, valor2: int, valor3: int) -> int:
    numeros = [valor1,valor2,valor3]

    return sorted(numeros)


#Faça uma função que recebe, por parâmetro, a hora de inicio e a hora de término de 
#um jogo, ambas subdivididas em 2 valores distintos: horas e minutos. O procedimento deve retornar, 
#também por parâmetro, a duração do jogo em horas e minutos, considerando que o tempo máximo 
#de duração de um jogo é de 24 horas e que o jogo pode começar em um dia e terminar no outro.

def calcular_duracao_jogo(hora_inicio: int, minuto_inicio: int, hora_final: int, minuto_final: int) -> tuple[int, int]:
    min_inicial_total = hora_inicio * 60 + minuto_inicio
    min_final_total = hora_final * 60 + minuto_final

    if min_final_total <= min_inicial_total:
        min_final_total += 24 * 60  

    duracao = min_final_total - min_inicial_total
    horas_usadas = duracao // 60
    minutos_usados = duracao % 60

    return horas_usadas, minutos_usados

#A prefeitura de uma cidade fez uma pesquisa entre os seus habitantes, coletando 
#dados sobre o salário e número de filhos. Faça uma função que leia esses dados para um número 
#não determinado de pessoas e retorne a média de salário da população, a média do número de 
#filhos, o maior salário e o percentual de pessoas com salário até R$1350,00.


def calcular_media_salario() -> float:
    total_salario = 0
    total_filhos = 0
    maior_salario = 0
    qtd_pessoas = 0
    qtd_salario_ate_1350 = 0

    continuar = True

    while continuar:
        salario = float(input("Digite o salário (ou um valor negativo para sair): "))
        if salario < 0:
            continuar = False
        else:
            filhos = int(input())

            total_salario += salario
            total_filhos += filhos
            qtd_pessoas += 1

            if salario > maior_salario:
                maior_salario = salario
            if salario <= 1350:
                qtd_salario_ate_1350 += 1

    
    media_salario = total_salario / qtd_pessoas
    media_filhos = total_filhos / qtd_pessoas
    percentual_ate_1350 = (qtd_salario_ate_1350 / qtd_pessoas) * 100

    return media_salario, media_filhos, maior_salario, percentual_ate_1350


resultado = calcular_media_salario()
print("\nResultados:")
print(f"Média de salário: R${resultado[0]:.2f}")
print(f"Média de filhos: {resultado[1]:.2f}")
print(f"Maior salário: R${resultado[2]:.2f}")
print(f"Percentual com salário até R$1350,00: {resultado[3]:.2f}%")
        