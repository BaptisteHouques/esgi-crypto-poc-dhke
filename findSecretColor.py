def findSecretColor(pub_alice_color, pub_bob_color, common_color):
    red = pub_bob_color[0] * 2 - common_color[0]
    green = pub_bob_color[1] * 2 - common_color[1]
    blue = pub_bob_color[2] * 2 - common_color[2]

    bob_secret = [red, green, blue]

    common_secret = secondMix(pub_alice_color, bob_secret)

    return common_secret

def secondMix(transported_color, secret_color):
    red = (int(transported_color[0]) * 2 + int(secret_color[0])) / 3
    green = (int(transported_color[1]) * 2 + int(secret_color[1])) / 3
    blue = (int(transported_color[2]) * 2 + int(secret_color[2])) / 3

    return [round(red), round(green), round(blue)]


base = input('Couleur en commun ? ').split(',')
pubAlice = input('Couleur public Alice ? ').split(',')
pubBob = input('Couleur public Bob ? ').split(',')

# Calcul du secret partagé (marron caca)
print(findSecretColor(pubAlice, pubBob, base))