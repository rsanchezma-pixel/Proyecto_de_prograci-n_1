
# ============================================================
# Archivo: ejercicio3_soporte_tripulacion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Rony Sánchez Masís
# Fecha: 12/10/2026        Versión: 1.0
# Descripción: Verifica si hay oxígeno y provisiones suficientes.
# ============================================================

# Entrada de datos: cantidades disponibles y requeridas.
oxigeno_disponible = int(input("Oxígeno disponible: "))
oxigeno_requerido = int(input("Oxígeno requerido: "))
provisiones_disponibles = int(input("Provisiones disponibles: "))
provisiones_requeridas = int(input("Provisiones requeridas: "))

# Decisión: ambos recursos deben alcanzar el mínimo requerido.
if oxigeno_disponible >= oxigeno_requerido and provisiones_disponibles >= provisiones_requeridas:
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")
