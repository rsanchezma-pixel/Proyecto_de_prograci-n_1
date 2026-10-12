# ============================================================
# Archivo: ejercicio2_combustible.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
# Integrantes: Rony Sánchez Masís
# Fecha: 11/10/2026        Versión: 1.0
# Descripción: Calcula el combustible total y adicional y
# advierte cuando el margen adicional es menor que 10.
# ============================================================

# Declaración de constantes: reserva obligatoria y umbral de alerta.
RESERVA_COMBUSTIBLE = 10
MARGEN_MINIMO = 10

# Entrada de datos: recursos disponibles y necesarios por trayecto.
combustible_disponible = int(input("Combustible disponible: "))
combustible_ida = int(input("Combustible requerido para llegar: "))
combustible_regreso = int(input("Combustible requerido para regresar: "))

# Procesamiento: se contempla el regreso y la reserva de emergencia.
combustible_total = combustible_ida + combustible_regreso + RESERVA_COMBUSTIBLE
combustible_adicional = combustible_disponible - combustible_total

# Salida: se muestran siempre los seis datos requeridos.
print("\n--- VERIFICACIÓN DE COMBUSTIBLE ---")
print(f"Combustible disponible: {combustible_disponible} unidades")
print(f"Combustible requerido para llegar: {combustible_ida} unidades")
print(f"Combustible requerido para regresar: {combustible_regreso} unidades")
print(f"Reserva de emergencia: {RESERVA_COMBUSTIBLE} unidades")
print(f"Combustible total requerido: {combustible_total} unidades")
print(f"Combustible adicional: {combustible_adicional} unidades")

# Decisión simple: un margen menor a 10 activa la advertencia.
if combustible_adicional < MARGEN_MINIMO:
    print("Advertencia: el margen adicional de combustible es bajo.")