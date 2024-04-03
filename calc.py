import math


def verifica_operador():
    print()
    print("C = para limpar x = mult, / = div, * = poten, + = adição  , - = subtração"
          "R = raiz, % = porcent -----  Sair = Fechar calculadora")
    print()
    esc_operacao = str(input("Digite o operador que deseja usar: "))
    print()
    if esc_operacao in ['+','-','x','X','/','*',"R",'%','C','c','SAIR','Sair','sair']:
        print(esc_operacao)
        return esc_operacao
        
    else:
        print("-"*30)
        print("Digite um operador válido")
        verifica_operador()


def multiplicacao(num1,num2,resultado):
    resultado = num1 * num2
    return resultado


def div(num1,num2,resultado):
    resultado = num1 / num2
    return resultado


def potencia(num1,num2,result):
    result = num1 ** num2
    return result


def raiz(num1, resultado):
    resultado = math.sqrt(num1)
    return resultado


def porcentagem(num1,num2, resultado):
    resultado = (num1 / 100) * num2
    return resultado


def soma(num1,num2,result):
    result = num1 + num2
    return result


def sub(num1, num2, resultado):
    resultado = num1 - num2
    return resultado


while True:
    #Entrada de dados efetuada pelo cliente
    print("-"*30)
    num1 = float(input("Digite o primeiro número: "))
    
    while True:#loop para continuar utilizando o resultado
        operador = verifica_operador()#Entrada e verificação se o operador é valido
        if operador == 'R':
            pass
        elif operador == 'C' or operador == 'c':
            print("Numero deletado")
            break
        elif operador in ['sair', 'SAIR','Sair']:
            break
        else:
            num2 = float(input("Digite o segundo número: "))
        print("-"*30)


        #Verificação do operador e resolução da operação matemática
        resultado = None
        if operador == 'x' or operador == 'X':
            resultado = multiplicacao(num1,num2,resultado)
            print(f"Resultado: {resultado}")
            num1 = resultado
        elif operador == '/':
            resultado = div(num1,num2,resultado)
            print(f"Resultado: {resultado}")
            num1 = resultado
        elif(operador == '*'):
            resultado = potencia(num1,num2,resultado)
            print(f"Resultado: {resultado}")  
            num1 = resultado
        elif(operador == 'R'):
            resultado = raiz(num1,resultado)
            print(f"Resultado: {resultado}")
            num1 = resultado
        elif(operador == '+'):
            resultado = soma(num1,num2,resultado)
            print(f"Resultado: {resultado}")
            num1 = resultado
        elif(operador == '-'):
            resultado = sub(num1,num2,resultado)
            print(f"Resultado: {resultado}")
            num1 = resultado
        else:
            resultado = porcentagem(num1,num2,resultado)
            print(f"Resultado: {resultado}")
            num1 = resultado
        print("-"*30)
    
        verifica_sair = verifica_operador()
        if verifica_sair in ['Sair','sair','Sair']:
            print("FECHANDO SISTEMA")
        else:
            pass
