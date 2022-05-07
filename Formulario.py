nome = str(input("Qual o seu nome completo?" '\n'))
print("Ola", nome)
idade = int(input("Qual a sua idade atualmente?" '\n'))
print("Entao voce tem", idade , "anos")
altura = float(input("Qual a sua altura?" '\n')) 
print("Entao voce tem", altura , "metros")
peso = float(input("Qual o seu peso?" '\n'))
print("Entao voce pesa", peso)
print("---------------------------------------------------------------")
print("Estou processando as suas informacoes, por favor aguarde!")
print("---------------------------------------------------------------")
if idade >= 0 and idade <= 20:
        print("Voce esta na Primeira idade da vida! Com", idade, "anos")
elif idade >= 21 and idade <= 49:
            print("Voce esta na Segunda idade da vida! Com", idade, "anos")
elif idade >=50 and idade <= 77:
                print("Voce esta na Terceira idade da Vida! Com", idade, "anos")
else:
                    print("Voce esta na Quarta idade da Vida! Com", idade, "anos")
print("=========================================================================")
imc = float(peso / altura ** 2) 
print("Seu IMC é: %.4f" % imc)
if imc < 18.5:
    print("Abaixo do peso! procure um medico para efetuar exames e se alimente bem.")
    print("Fique atento este IMC pode causar: queda de cabelo, infertilidade, ausência menstrual(MULHERES")
    print("Fadiga, stress, ansiedade")
elif imc >= 18.6 and imc <= 24.9:
        print("O seu peso esta ideal! Parabens continue assim.")
        print("Dentro desta faixa voce tem menor risco de doenças cardíacas e vasculares")
elif imc >= 25 and imc <= 29.9:
            print("Esta levemente acima do peso! Tome cuidado faça exercicios fisicos e faça educação alimentar.")
            print("Voce esta propenso a fadiga, má circulação, varizes")
elif imc >= 30 and imc <= 34.9:
                print("Esta com obesidade grau 1! Faça um acompanhamento medico e faça educação alimentar.")
                print("Voce pode esta com inicio ou risco de diabetes, angina, infarto, aterosclerose")
elif imc >= 35 and imc <= 39.9:
                    print("Esta com obesidade grau 2(SEVERA)! Faça um acompanhamento medico e faça educação alimentar urgente.")
                    print("Voce pode ter apneia do sono, falta de ar")
else:
                        print("Esta com obesidade grau 3(MORBIDA)! Faça um acompanhamento medico e faça educação alimentar rapidamente.")
                        print("Voce tem risco elevado de refluxo, dificuldade para se mover, escaras, diabetes, infarto, AVC")
