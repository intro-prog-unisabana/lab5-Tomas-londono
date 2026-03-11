def promedio_estudiante(calificaciones):
    suma = sum(calificaciones)          
    cantidad = len(calificaciones)      
    promedio = suma / cantidad          
    return float(promedio)   
notas = [85, 92, 78]
resultado = promedio_estudiante(notas)
print(resultado)