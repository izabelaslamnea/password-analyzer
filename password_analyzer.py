
import getpass
import string


def analyze_password(password):
    score = 0
    feedback = []

    # 1. Comprobar longitud
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Utiliza al menos 8 caracteres.")

    # 2. Comprobar variedad de caracteres
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Añade letras minúsculas.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Añade letras mayúsculas.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Añade números.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("Añade símbolos especiales.")

    # 3. Detectar contraseñas y patrones comunes
    common_passwords = [
        "123456", "password", "qwerty",
        "12345678", "admin", "letmein"
    ]

    common_patterns = ["123", "abc", "qwerty", "password"]

    if password.lower() in common_passwords:
        score -= 3
        feedback.append("La contraseña es demasiado común.")
    elif any(p in password.lower() for p in common_patterns):
        score -= 2
        feedback.append("Evita secuencias o palabras predecibles.")

    # Mantener la puntuación entre 0 y 6
    score = max(0, min(score, 6))

    # 4. Clasificar la contraseña
    if score <= 2:
        strength = "DEBIL"
    elif score <= 4:
        strength = "MEDIA"
    else:
        strength = "FUERTE"

    return score, strength, feedback


def main():
    print("================================")
    print("     ANALIZADOR DE CONTRASEÑAS")
    print("================================")

    password = getpass.getpass("Introduce una contraseña: ")

    if not password:
        print("No has introducido ninguna contraseña.")
        return

    score, strength, feedback = analyze_password(password)

    print("\nResultado:", strength)
    print(f"Puntuación: {score}/6")

    if feedback:
        print("\nRecomendaciones:")
        for item in feedback:
            print("-", item)
    else:
        print("\n¡Buen resultado! Cumple todos los criterios básicos.")


if __name__ == "__main__":
    main()
