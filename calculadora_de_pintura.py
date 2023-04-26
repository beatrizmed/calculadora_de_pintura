'''
Programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem: 'Você necessita de x latas de tintas.'
'''

rendimento = int(input('Qual o rendimento da lata de tinta? '))
altura = int(input('Qual a altura da parede? '))
largura = int(input('Qual a largura da parede? '))


def calcular_tinta():
    area = altura * largura
    total = area/rendimento
    print(f'Você irá precisar de {total} latas de tinta.')


calcular_tinta()
