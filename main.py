from dechiffreur import Dechiffreur


if __name__ == '__main__':
    code = "223-232-.2."
    code2 = ".2.-..3-2.2-3..-.23"

    dechiff = Dechiffreur(code)
    print(dechiff.decode_the_code())

    dechiff = Dechiffreur(code2)
    print(dechiff.decode_the_code())
