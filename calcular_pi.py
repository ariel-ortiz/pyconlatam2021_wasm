def calcular_pi(num_rects):
    suma = 0.0
    ancho = 1.0 / num_rects;
    for i in range(num_rects):
        medio = (i + 0.5) * ancho
        alto = 4.0 / (1.0 + medio * medio)
        suma += alto
    return ancho * suma
