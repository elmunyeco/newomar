import sqlite3

# Conectar a la base de datos SQLite de Django
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# Script para insertar 12,000 pacientes
for i in range(1, 12001):
    numero = i
    nombre = f"Nombre{i}"
    apellido = f"Apellido{i}"
    documento = f"{i:08d}"  # Documento de 8 dígitos

    # Inserción en la tabla HistoriaClinica
    cursor.execute('''
        INSERT INTO main_historiaclinica (numero, nombre, apellido, documento)
        VALUES (?, ?, ?, ?)
    ''', (numero, nombre, apellido, documento))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Se han insertado 12,000 pacientes en la base de datos.")

