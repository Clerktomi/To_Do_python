import time
from datetime import datetime
tartalom = []

def leghosszabb_elem():
    max_dict = {}
    hossz = 0
    for elem in tartalom:
        if len(elem['Feladat']) > hossz:
            hossz = elem['Feladat']
            max_dict = elem

feladat = {}
with open('data.txt','r',encoding='utf-8') as file_rd:
    for sor in file_rd:
        data = sor.strip().split(';')
        feladat['Feladat'] = data[0]
        feladat['Dátum'] = data[1]
        feladat['Állapot'] = data[2]
        tartalom.append(feladat)
        feladat = {}
while True:   
    print()
    user_choice = input('Mit szeretne? (Kilépés: *) (Feladat hozzáadása: +) (Feladat törlése: -) (Kilistázás: lista): ').lower().strip()
    print()
    while user_choice not in ['*','+','-','lista']:
        print(f'Nem megfelelő művelet A(z): {user_choice}!')
        print()
        user_choice = input('Mit szeretne? (Kilépés: *) (Feladat hozzáadása: +) (Feladat törlése: -) (Kilistázás: lista): ').lower().strip()
        print()
    if user_choice == '*':
        print('Sikeres kilépés!')
        print()
        break
    elif user_choice == 'lista':
        print('A lista elemei:')
        print()
        for elem in tartalom:
            print(f'Feladat: {elem['Feladat']} | Dátum: {elem['Dátum']} | Állapot: {elem['Állapot']}')
            print()
    elif user_choice == '+':
        print()
        while True:
            user_add = input('Kérem adja meg a feladatot (kilépés: *): ').lower()
            if user_add == '*':
                print()
                print(f'Sikeres Kilpés!')
                print()
            print()
            user_data = input('Kérem adja meg a dátumot: (YYYY-MM-DD) (kilépés *): ')
            if user_data == '*':
                print()
                print(f'Sikeres Kilpés!')
                print()
                break
            with open('data.txt','a',encoding='utf-8') as file_add:
                print(f'{user_add};{user_data};nincs kész',end='\n',file=file_add)
            print()
            print(f'A feladat rögzíve!')
    elif user_choice == '-':
        print()
        while True:
            user_delete = input('Kérem adja meg a feladatot, amelyet szeretne törölni (kilépés: *): ').lower()
            if user_delete == '*':
                print()
                print(f'Sikeres Kilpés!')
                print()
            print()
            with open('data.txt','w',encoding='utf-8') as file_remove:
                for elem in tartalom:
                    if elem['Feladat'] == user_delete:
                        print()
                        user_sw =(f'Ezt szeretné Törlni?: {elem['Feladat']} | (igen / nem)')
                        while user_sw not in ['igen','nem']:
                            print()
                            print('Nem meg felelő formátum!')
                            print()
                            user_sw =(f'Ezt szeretné Törlni?: {elem['Feladat']} | (igen / nem)')
                        if user_sw == 'nem':
                            print()
                            print('Sikeres ki lépés!')
                            print()
                            break
                        else:
                            continue
                    else:
                        print(f'{elem['Feladat']};{elem['Dátum']};{elem['Állapot']}',file=file_remove)
                                