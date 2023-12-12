import sys


def main():
    if len(sys.argv) != 4:
        print('Error: Nombre de paramètres incorrect !')
        return

    firstColor = sys.argv[2].split(',')
    secondColor = sys.argv[3].split(',')

    if sys.argv[1] == '--crypt' or sys.argv[1] == '-c':
        print(crypt(firstColor, secondColor))
    elif sys.argv[1] == '--decrypt' or sys.argv[1] == '-d':
        print(decrypt(firstColor, secondColor))
    else:
        print('Error')
        return

    decrypt(firstColor, secondColor)


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


main()
