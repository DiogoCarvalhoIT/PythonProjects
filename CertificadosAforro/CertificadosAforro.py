import time
import requests
from bs4 import BeautifulSoup
import lxml

class Product:

    def __init__(self, taxaJuroAtual, mesAcquisicao,mesesProduto, anosAtivos, investimentoInicial, investimentoAcumulado, juroAcumulado):

        self.taxaJuroAtual = taxaJuroAtual
        self.mesAcquisicao = mesAcquisicao
        self.mesesProduto = mesesProduto
        self.anosAtivos = anosAtivos
        self.investimentoInicial = investimentoInicial
        self.investimentoAcumulado = investimentoAcumulado
        self.juroAcumulado = juroAcumulado

    def updateDates(self):

        if self.mesesProduto < total_months:
            self.mesesProduto = self.mesesProduto + 1


        if (self.mesesProduto%12) == 0 :
            self.anosAtivos = self.anosAtivos +1

    def calculate_monthly_yield(self, currentMonth):

        if currentMonth >= (self.mesAcquisicao+2):

            if  self.juroAcumulado == 0 and self.mesesProduto == 3:
                self.juroAcumulado = self.taxaJuroAtual*self.investimentoInicial
                self.investimentoAcumulado = self.juroAcumulado+self.investimentoInicial

            elif self.juroAcumulado != 0:
                if ((self.mesesProduto%3) == 0) and self.anosAtivos < 2:
                    self.juroAcumulado = self.juroAcumulado + (self.investimentoAcumulado*self.taxaJuroAtual)
                    self.investimentoAcumulado = self.investimentoAcumulado + (self.investimentoAcumulado*self.taxaJuroAtual)

                elif ((self.mesesProduto%3) == 0) and (self.anosAtivos >= 2 and self.anosAtivos <=5):
                    self.juroAcumulado = self.juroAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+secondFifthLiquid))
                    self.investimentoAcumulado = self.investimentoAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+secondFifthLiquid))

                elif ((self.mesesProduto%3) == 0) and (self.anosAtivos >= 6 and self.anosAtivos <=9):
                    self.juroAcumulado = self.juroAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+sixthNineLiquid))
                    self.investimentoAcumulado = self.investimentoAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+secondFifthLiquid))

                elif ((self.mesesProduto%3) == 0) and (self.anosAtivos >= 10 and self.anosAtivos <=11):
                    self.juroAcumulado = self.juroAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+tenElevenLiquid))
                    self.investimentoAcumulado = self.investimentoAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+secondFifthLiquid))

                elif ((self.mesesProduto%3) == 0) and (self.anosAtivos >= 12 and self.anosAtivos <=13):
                    self.juroAcumulado = self.juroAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+twelveThirteenLiquid))
                    self.investimentoAcumulado = self.investimentoAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+secondFifthLiquid))

                elif ((self.mesesProduto%3) == 0) and (self.anosAtivos >= 14 and self.anosAtivos <=15):
                    self.juroAcumulado = self.juroAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+fourteenFifteenLiquid))
                    self.investimentoAcumulado = self.investimentoAcumulado + (self.investimentoAcumulado*(self.taxaJuroAtual+secondFifthLiquid))


monthly_investment = int(input('How much money are you gonna invest each month: '))
accumulativeMoney = 0
months_per_year = 12
investment_duration_years = int(input('How many years do you wanna keep doing this monthly investment: '))
total_months = months_per_year*investment_duration_years
currentMonth = 1

anualYieldGross = 0.025
secondFifthGross= 0.0025
sixthNineGross = 0.005
tenElevenGross = 0.01
twelveThirteenGross = 0.015
fourteenFifteenGross= 0.0175

anualYieldLiquid = (anualYieldGross * 0.72)/4
secondFifthLiquid= (secondFifthGross * 0.72)/4
sixthNineLiquid = (sixthNineGross * 0.72)/4
tenElevenLiquid = (tenElevenGross * 0.72)/4
twelveThirteenLiquid = (twelveThirteenGross * 0.72)/4
fourteenFifteenLiquid= (fourteenFifteenGross * 0.72)/4

products = []
total_investimento_acumulado = 0
total_juro_acumulado = 0

lucroTotal = total_investimento_acumulado - (monthly_investment * 12)


while currentMonth <= 180:

    product = Product(anualYieldLiquid,currentMonth,0,0,monthly_investment,0,0)
    products.append(product)

    for i in range(len(products)):
        product = products[i]
        product.updateDates()
        product.calculate_monthly_yield(currentMonth)



    currentMonth +=1

for i in range(len(products)):
    product = products[i]
    total_juro_acumulado += product.juroAcumulado
    print(product.juroAcumulado)

#print()
#print(total_juro_acumulado)

totalInvestido = monthly_investment*total_months
percentagemJuroPeloInvestido = (total_juro_acumulado/totalInvestido)*100
print('######################')

print('Total Investido= ' + str(totalInvestido) + '$')
print('Total Juro Recebido= ' + str(round(total_juro_acumulado,2))+'$')
print('%Lucro= ' + str(round(percentagemJuroPeloInvestido, 2)) + '%')
