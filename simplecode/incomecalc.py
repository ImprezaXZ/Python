total = 0
month = str(input("Месяц\n"))
lube_income = []
num_lube = int(input("Количество смазок\n"))
for i in range (num_lube):
    lube_income.append(float(input("Общее количество смазок\n")))

total1 = 0
service_income = []
num_service = int(input("Количество работ\n"))
for i in range (num_service):
    service_income.append(float(input("Сумма работы\n")))


total = sum(lube_income) * 50
total1 = sum(service_income) * 0.25
total2 = total + total1 

print ( "В месяце ", month, 
        "\n Количество смазок составляет: ", str(sum(lube_income)),
    "\n Общая сумма по сервису составляет: ", str(sum(service_income)), 
    "\n Общий заработок по смазкам составляет:", str(total) + "UAH",
    "\n Общий заработок по сервису составляет:", str(total1) + "UAH", 
    "\n Общий доп. заработок составляет:", str(total2) + "UAH")
