import codecs
from triplet import Triplet


class Dechiffreur:
    def __init__(self, code: str):
        self.code = code
        self.triplets = []
        self.letters = []

    def __is_correct(self) -> bool:
        """Vérifie si la forme du code donnée est bonne"""
        if (len(self.code.replace("-", "")) % 3) != 0:
            return False
        return True

    def __extract_bits(self):
        """Extrait les différents bits du code donné, et les convertit en triplets"""
        bits_in_triplet = ()
        for bit in self.code.replace("-", ""):
            if len(bits_in_triplet) == 3:
                self.triplets.append(Triplet(bits_in_triplet))
                bits_in_triplet = ()
            bits_in_triplet += bit,
        self.triplets.append(Triplet(bits_in_triplet))

    def __get_triplets_letters(self):
        """Fait calculer les lettres des différents triplets"""
        for triplet in self.triplets:
            self.letters.append(triplet.get_letter())

    def __decode_rot13(self):
        """Utilise la bibli codecs pour déchiffrer le rot13, lettre par lettre"""
        for i in range(len(self.letters)):
            self.letters[i] = codecs.decode(self.letters[i], "rot13")

    def decode_the_code(self):
        """Déchiffre le code :)"""
        if self.__is_correct():
            self.__extract_bits()
            self.__get_triplets_letters()
            self.__decode_rot13()
            return self.letters
        return None

