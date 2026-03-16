def greet(name: str) -> str:
    return f"Hola, {name}!"

if __name__ == "__main__":
    nom = input("¿Cómo te llamas? ")
    print(greet(nom))

