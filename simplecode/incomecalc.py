month = str(input('Месяц\n'))
lube = []
money = 'our_input'
while str(money) != '<built-in function input>':
    try:
        money = int(input('Количество смазок\n'))
        lube.append(money)
    except ValueError:
        money = str(input)
        if money == '<built-in function input>':
            print('Список по смазкам сформирован\n')

service = []
money = 'our_input'
while str(money) != '<built-in function input>':
    try:
        money = int(input('Сумма по сервису\n'))
        service.append(money)
    except ValueError:
        money = str(input)
        if money == '<built-in function input>':
            print('Список по сервису сформирован\n')

lube_total = sum(lube) * 50
service_total = sum(service) * 0.25
all_total = lube_total + service_total
print(f'В месяце {month}')
print(f'Общее количество смазок: {sum(lube)}')
print(f'Общий заработок по ним составляет: {lube_total} UAH')
print(f'Общая сумма по сервису составляет: {sum(service)} UAH')
print(f'Общий заработок по сервису составляет: {service_total} UAH')
print(f'Общий заработок в этом месяце составляет: {all_total} UAH')
    
