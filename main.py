import sys


def main():
    # if len(sys.argv) != 4:
    #     print('Error: Nombre de paramètres incorrect !')
    #     return

    firstColor = input('Couleur en commun ? ').split(',')
    secondColor = input('Couleur secrète ? ').split(',')

    printColors(crypt(firstColor, secondColor))

    transportedColor = input('Couleur de votre correspondant ? ').split(',')

    printColors(decrypt(firstColor, transportedColor))


def crypt(common_color, secret_color):
    red = (int(common_color[0]) + int(secret_color[0])) / 2
    green = (int(common_color[1]) + int(secret_color[1])) / 2
    blue = (int(common_color[2]) + int(secret_color[2])) / 2

    return [round(red), round(green), round(blue)]


def decrypt(transported_color, secret_color):
    red = (int(transported_color[0]) * 2 + int(secret_color[0])) / 3
    green = (int(transported_color[1]) * 2 + int(secret_color[1])) / 3
    blue = (int(transported_color[2]) * 2 + int(secret_color[2])) / 3

    return [round(red), round(green), round(blue)]


def printColors(text):
    print('-' * 30)
    print('Couleur:')
    print(text)
    print()
    print('-' * 30)


main()
