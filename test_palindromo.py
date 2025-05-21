from palindromo import es_palindromo

def test_palabra_simple():
    assert es_palindromo("reconocer") is True

def test_palabra_con_espacios():
    assert es_palindromo("Anita lava la tina") is True

def test_palabra_no_palindromo():
    assert es_palindromo("python") is False

def test_palabra_con_mayusculas():
    assert es_palindromo("NeuQuen") is True

def test_palabra_con_signos():
    assert es_palindromo("¿Acaso hubo buhos aca?") is True
    
print(es_palindromo("NeuQuen"))  # Debería mostrar True
print(es_palindromo("python"))   # Debería mostrar False