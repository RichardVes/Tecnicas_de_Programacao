horas = int(input("Quantas horas voce ficou?"))
if horas < 2:
  print("Valor total igual a R$ 5,00 reais")
if horas >=2 and horas <4: 
  print("O total ficou R$ 8,00 reais")
if horas >=4:
  print("Voce passou de 4 horas")
  h_ext=horas-4
  print("Quantidade de horas extas: ",h_ext,".")