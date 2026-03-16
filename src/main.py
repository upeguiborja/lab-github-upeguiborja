import sys
from src.greeter import greet

def main():
    if len(sys.argv) < 2:
        print("Uso: python -m src.main <nombre> [hora]")
        return

    name = sys.argv[1]
    hour = None

    if len(sys.argv) >= 3:
        try:
            hour = int(sys.argv[2])
        except ValueError:
            print("La hora debe ser un entero entre 0 y 23.")
            return

    try:
        print(greet(name, hour))
    except ValueError as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()

