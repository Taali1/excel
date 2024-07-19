from generate_html import create_page
from get_data import get_xml, group_xml, filter_xml

groups = [
    ['/FIRANY/FIRANY GOTOWE/ŻAKARDOWE'], # Firany gotowe
    ['/FIRANY/FIRANY GOTOWE/MAKRAMY', '/FIRANY/FIRANY GOTOWE/PANELE'], #Makramy i Panele
    ['/KOCE I NARZUTY/NARZUTY'], # Narzuty
    ['/OBRUSY I BIEŻNIKI/OBRUSY', '/OBRUSY I BIEŻNIKI/BIEŻNIKI I SERWETY'], # Obrusy i bierzniki
    ['/POSZEWKI I PODUSZKI/POSZEWKI', '/POSZEWKI I PODUSZKI/PODUSZKI'], # Poszewki i poduszki
    ['/POŚCIEL I PRZEŚCIERADŁA/POŚCIEL', '/POŚCIEL I PRZEŚCIERADŁA/PRZEŚCIERADŁA'], # Pościele i prześcieradła
    ['/RĘCZNIKI I ŚCIERKI/RĘCZNIKI', '/RĘCZNIKI I ŚCIERKI/ŚCIERKI KUCHENNE'], # Ręczniki i ścierki
    ['/TKANINY I ZASŁONY/ZASŁONY GOTOWE/JEDNOBARWNE'] # Zasłony gotowe
]

groups_titles = [
    'Firany gotowe',
    'Makramy i panele',
    'Narzuty',
    'Obrusy i bierzniki',
    'Poszewki i poduszki',
    'Pościele i prześcieradła',
    'Ręczniki i ścierki',
    'Zasłony gotowe',
]

if __name__ == "__main__":
    for x in range(8):
        products = group_xml(filter_xml(get_xml()), groups[x])
        create_page(products, groups_titles[x])
        print("HTML for "+groups_titles[x]+" done")
