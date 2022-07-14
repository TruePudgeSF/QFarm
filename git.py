from pyfiglet import Figlet
a=open('bot-log.txt','a')

def main():
    preview_text = Figlet(font="slant")
    print(preview_text.renderText("Q I W I   F A R M !"))
    choose = int(input('''Добро пожаловать в фарм денег на киви!
Выберете пункт:
1 - создать и сохранить ферму(выбирайте вначале)
2 - запустить ферму(после создания)
Ваш выбор: '''))
    if choose == 1:
        number = input('''Создание и сохранение фермы!
Для начала введите номер телефона на который был зарегистрирован QIWI кошелек для фермы: ''')
        token = input('Теперь нужно ввести токен аккаунта(это можно сделать по ссылке https://qiwi.com/api): ')
        save = f'''
{number}
{token}

'''
        a.writelines(save)
    elif choose == 2:
        print('Ошибка! Возможно вы не создали ферму или ввели неправельные данные!')

    a.close()
    
main()
