import os
from SimpleQIWI import *


token = input('Введите Вашь токен: ')
phone = input('Номер телефона: ')

api = QApi(token=token, phone=phone)


while True:
	print('Вот мои команды:\n1) Баланс\n2) Перевод\n3) Очистка\n4) Выход')

	comand = input('Введите команду: ').lower()

	if comand == '1' or comand == 'баланс':
		print()
		print('==================================================')
		print('Вашь баланс составляет: ' + str(api.balance))
		print('==================================================\n')

	elif comand == '2' or comand == 'перевод':
		try:
			try:
				api.pay(account=str(input('Введите Номер: ')), amount=int(input('Введите Сумму: ')), comment='-_-')
				print('Перевод прошёл успешно!')
			except ValueError:
				print('')
				print('========')
				print('Ошибка')
				print('========\n')
		except QIWIAPIError:
			print()
			print('=========')
			print('Ошибка')
			print('=========\n')
	
		

	elif comand == '3' or comand == 'очистка':
		os.system('cls')

	elif comand == 'Выход' or comand == '4':
		break

	else:
		os.system('cls')
		print('========================')
		print('Я незнаю такой команды')
		print('========================\n')

input()
