from generate_pdf import create_pdf

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



if __name__ == "__main__":
    create_pdf(groups[0])
    