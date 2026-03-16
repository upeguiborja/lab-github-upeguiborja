def greet(name: str, hour: int | None = None) -> str:
    if not name or not name.strip():
        raise ValueError("El nombre no puede estar vacío.")

    name = name.strip()

    if hour is None:
        return f"Hola, {name}!"

    if not isinstance(hour, int) or hour < 0 or hour > 23:
        raise ValueError("La hora debe estar entre 0 y 23.")

    if 5 <= hour < 12:
        greeting = "Buenos días"
    elif 12 <= hour < 19:
        greeting = "Buenas tardes"
    else:
        greeting = "Buenas noches"

    return f"{greeting}, {name}."

