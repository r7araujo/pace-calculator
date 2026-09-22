from functions import (
    formatar_pace,
    formatar_tempo,
    ler_distancia,
    ler_pace,
    ler_tempo,
)


DISTANCIAS_PADRAO = [200, 400, 600, 800, 1000]


def imprimir_tabela(pace_por_km):
    distancias = DISTANCIAS_PADRAO.copy()

    resposta = input('Deseja adicionar uma distância personalizada? (s/n): ').strip().lower()
    if resposta == 's':
        distancias.append(ler_distancia())

    print('\n--- Tempos previstos ---')
    print(f'{"Distância":<12} {"Pace":<16} Tempo')
    print('-' * 42)

    for distancia in sorted(distancias):
        tempo_previsto = pace_por_km * distancia / 1000
        print(
            f'{distancia:>5} m       '
            f'{formatar_pace(pace_por_km):<16} '
            f'{formatar_tempo(tempo_previsto)}'
        )


def escolher_opcao():
    while True:
        print('\nSelecione uma opção:')
        print('1 - Fornecer tempo e distância; receber pace e tabela de tempos.')
        print('2 - Fornecer distância e pace; receber tempo e tabela.')
        print('3 - Fornecer distância e tempo; receber pace e tabela de tempos.')

        opcao = input('Digite o número da opção: ').strip()
        if opcao in ('1', '2', '3'):
            return opcao
        print('Selecione uma opção válida.')


def main():
    opcao = escolher_opcao()

    if opcao == '2':
        distancia = ler_distancia()
        pace_por_km = ler_pace()
        tempo_total = pace_por_km * distancia / 1000
        print(f'\nTempo previsto: {formatar_tempo(tempo_total)}')
    else:
        distancia = ler_distancia()
        tempo_total = ler_tempo()
        pace_por_km = tempo_total / (distancia / 1000)
        print(f'\nPace: {formatar_pace(pace_por_km)}')

    imprimir_tabela(pace_por_km)


if __name__ == '__main__':
    main()
