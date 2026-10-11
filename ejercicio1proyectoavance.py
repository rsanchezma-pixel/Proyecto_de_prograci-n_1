# ============================================================
# Archivo: ejercicio1_recursos.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrante: Rony Sánchez Masís
# Fecha: 11/10/2026        Versión: 1.0
# Descripción: Calcula los recursos necesarios para una misión
# espacial de ida y regreso, incluidas las reservas.
# ============================================================

# Declaración de constantes
CONSUMO_COMBUSTIBLE = 8
RESERVA_COMBUSTIBLE = 10
CONSUMO_OXIGENO = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA = 5
ENERGIA_EXPLORACION = 10
CONSUMO_PROVISIONES = 1
RESERVA_PROVISIONES = 3
TRAYECTOS = 2

# Entrada de datos
nombre_mision = input("Nombre de la misión: ")
tripulantes = int(input("Cantidad de tripulantes: "))
dias_viaje = int(input("Días estimados hasta el destino: "))

# Procesamiento de los recursos
combustible_ida = dias_viaje * CONSUMO_COMBUSTIBLE
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE

combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE

oxigeno_requerido = dias_viaje * CONSUMO_OXIGENO * tripulantes + RESERVA_OXIGENO

energia_requerida = dias_viaje * CONSUMO_ENERGIA * TRAYECTOS + ENERGIA_EXPLORACION

provisiones_requeridas = dias_viaje * tripulantes * TRAYECTOS * CONSUMO_PROVISIONES + RESERVA_PROVISIONES

# Salida de resultados
print("\n--- RESUMEN DE LA MISIÓN ---")
print(f"Misión: {nombre_mision}")
print(f"Tripulantes: {tripulantes}")
print(f"Duración estimada hasta el destino: {dias_viaje} días")
print(f"Combustible para llegar: {combustible_ida} unidades")
print(f"Combustible para regresar: {combustible_regreso} unidades")
print(f"Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades")
print(f"Combustible total requerido: {combustible_total} unidades")
print(f"Oxígeno requerido: {oxigeno_requerido} unidades")
print(f"Energía requerida: {energia_requerida} unidades")
print(f"Provisiones requeridas: {provisiones_requeridas} unidades")