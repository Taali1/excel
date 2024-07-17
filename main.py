from generate_html import create_page
from get_data import get_xml, group_xml, filter_xml

groups = [
    ['/FIRANY/FIRANY GOTOWE/ŻAKARDOWE'], # Firany gotowe
    ['/FIRANY/FIRANY GOTOWE/MAKRAMY', '/FIRANY/FIRANY GOTOWE/PANELE'], #Makramy i Panele
    ['/KOCE I NARZUTY/NARZUTY'], # Narzuty
    ['/OBRUSY I BIEŻNIKI/OBRUSY', '/OBRUSY I BIEŻNIKI/BIEŻNIKI I SERWETY'], # Obrusy i bierzniki
    ['POSZEWKI I PODUSZKI/POSZEWKI', 'POSZEWKI I PODUSZKI/PODUSZKI'], # Poszewki i poduszki
    ['/POŚCIEL I PRZEŚCIERADŁA/POŚCIEL', '/POŚCIEL I PRZEŚCIERADŁA/PRZEŚCIERADŁA'], # Pościele i prześcieradła
    ['/RĘCZNIKI I ŚCIERKI/RĘCZNIKI', '/RĘCZNIKI I ŚCIERKI/ŚCIERKI KUCHENNE'], # Ręczniki i ścierki
    ['/TKANINY I ZASŁONY/ZASŁONY GOTOWE/JEDNOBARWNE'] # Zasłony gotowe
]

groups_titles = [
    '1 - Firany gotowe',
    '2 - Makramy i panele',
    '3 - Narzuty',
    '4 - Obrusy i bierzniki',
    '5 - Poszewki i poduszki',
    '6 - Pościele i prześcieradła',
    '7 - Ręczniki i ścierki',
    '8 - Zasłony gotowe',
    '9 - Wszystkie'
]

def menu():
    for line in groups_titles:
        print(line)
    choice = input('Wybierz kategorię lub wpisz 0 aby wyjść: ')
    return int(choice)


if __name__ == "__main__":
    while True:
        choice = menu()

        if choice == 9:
            for x in range(9):
                products = group_xml(filter_xml(get_xml()), groups[x])
                create_page(products, groups_titles[x][4:])
                print("HTML for "+groups_titles[x][:4]+" done")

        elif choice > 0 and choice < 9:
            products = group_xml(filter_xml(get_xml()), groups[choice-1])
            create_page(products, groups_titles[choice-1][4:])

        elif choice == 0:
            break

        else:
            continue
