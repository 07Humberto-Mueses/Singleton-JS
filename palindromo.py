def es_palindromo(palabra):
    palabra_limpia = ''.join(c.lower() for c in palabra if c.isalnum())
    return palabra_limpia == palabra_limpia[::-1]