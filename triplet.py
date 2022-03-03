class Triplet:
    def __init__(self, bits: tuple):
        self.ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.bits = bits
        self.decimal = 0
        self.letter = ''

    def __convert_to_usable(self):
        """Convertit les bits pour les rendre utilisables"""
        converted = ()
        for bit in self.bits:
            if bit == '.':
                converted += 0,
            else:
                converted += (int(bit) - 1),
        self.bits = converted

    def __calculate_decimal(self):
        """Calcule la valeur décimale du triplet"""
        poids = 2  # on commence à 2, parce qu'il n'y a que 3 bits
        for bit in self.bits:
            self.decimal += (bit*3**poids)
            poids -= 1

    def __calculate_letter(self):
        """Associe une lettre à la valeure décimale"""
        self.letter = self.ALPHA[self.decimal-1]

    def get_letter(self) -> str:
        """Renvoie la lettre du triplet"""
        self.__convert_to_usable()
        self.__calculate_decimal()
        self.__calculate_letter()
        return self.letter
