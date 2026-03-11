def promedio_estudiante(calificaciones):
    suma = sum(calificaciones)          
    cantidad = len(calificaciones)      
    promedio = suma / cantidad          
    return float(promedio)   
