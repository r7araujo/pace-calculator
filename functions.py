import re


def ler_tempo():
    """Lê HH\"MM\"SS e devolve o total em segundos."""
    while True:
        texto = input('Digite o tempo no formato HH"MM"SS: ')
        resultado = re.fullmatch(r'(\d{2,})"(\d{2})"(\d{2})', texto)
        if resultado is None:
            print('Formato inválido. Exemplo: 01"23"45.')
            continue

        horas, minutos, segundos = map(int, resultado.groups())
        if minutos >= 60 or segundos >= 60:
            print('Minutos e segundos devem estar entre 00 e 59.')
            continue

        return horas * 3600 + minutos * 60 + segundos


def ler_distancia():
    """Lê KM\"METROS e devolve a distância total em metros."""
    while True:
        texto = input('Digite a distância no formato KM"METROS (ex.: 2"500): ')
        resultado = re.fullmatch(r'(\d+)"(\d{1,3})', texto)
        if resultado is None:
            print('Formato inválido. Exemplo: 2"500.')
            continue

        quilometros, metros = map(int, resultado.groups())
        if metros >= 1000:
            print('A parte dos metros deve estar entre 0 e 999.')
            continue

        distancia_total = quilometros * 1000 + metros
        if distancia_total == 0:
            print('A distância precisa ser maior que zero.')
            continue

        return distancia_total


def ler_pace():
    """Lê MM\"SS por km e devolve segundos por quilômetro."""
    while True:
        texto = input('Digite o pace no formato MM"SS por km: ')
        resultado = re.fullmatch(r'(\d{1,2})"(\d{2})', texto)
        if resultado is None:
            print('Formato inválido. Exemplo: 05"30.')
            continue

        minutos, segundos = map(int, resultado.groups())
        if segundos >= 60:
            print('Os segundos devem estar entre 00 e 59.')
            continue

        return minutos * 60 + segundos


def formatar_tempo(total_segundos):
    total_segundos = round(total_segundos)
    horas, resto = divmod(total_segundos, 3600)
    minutos, segundos = divmod(resto, 60)
    return f'{horas:02d}:{minutos:02d}:{segundos:02d}'


def formatar_pace(segundos_por_km):
    minutos, segundos = divmod(round(segundos_por_km), 60)
    return f'{minutos:02d}:{segundos:02d} min/km'
