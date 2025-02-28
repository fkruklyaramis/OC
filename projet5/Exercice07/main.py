def square(number: int) -> int:
    if isinstance(number, (int, float)):
        return number ** 2
    else:
        print("Le paramètre doit être un nombre !")
        return None
    
print(square(4))