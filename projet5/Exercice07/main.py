def square(number):
    try:
        return number ** 2
    except TypeError:
        print("Le paramètre doit être un nombre !")
        return None


square = square(8)
if square is not None:
    print(f"{square:.2f}")
