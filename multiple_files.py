from utils import *
mensaje = input("Please type your message\n")
m_invertido = flip(mensaje)
cantidad_a = count_letters(mensaje, "a")
m_codificado = m_invertido + str(cantidad_a)
print(f"Your encoded message is: {m_codificado}")