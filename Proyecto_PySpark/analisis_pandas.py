"""
ANÁLISIS DE PELÍCULAS CINE COLOMBIA - Versión Pandas
(Alternativa sin PySpark para demostración)

NOTA: Este script usa Pandas en lugar de PySpark para demostración.
Para la versión completa con PySpark, instala Java primero.
"""

import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("ANÁLISIS DE PELÍCULAS - CINE COLOMBIA")
print("Usando Pandas (Versión de demostración)")
print("=" * 60)

# ============================================
# CARGA DE DATOS
# ============================================
print("\n[1] Cargando datos desde CSV...")
df = pd.read_csv("peliculas.csv")

print(f"✓ Total de películas cargadas: {len(df)}")
print("\n[2] Muestra de datos:")
print(df.head())

# ============================================
# ANÁLISIS 1: PELÍCULAS POR GÉNERO
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 1: Distribución de películas por género")
print("=" * 60)
peliculas_por_genero = df['genero'].value_counts().sort_values(ascending=False)
print(peliculas_por_genero)

# ============================================
# ANÁLISIS 2: DURACIÓN PROMEDIO
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 2: Duración promedio de películas")
print("=" * 60)
duracion_promedio = df['duracion'].mean()
print(f"Duración promedio: {duracion_promedio:.2f} minutos")

print("\nDuración promedio por género:")
duracion_por_genero = df.groupby('genero')['duracion'].mean().sort_values(ascending=False)
print(duracion_por_genero)

# ============================================
# ANÁLISIS 3: PELÍCULAS LARGAS (>120 MIN)
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 3: Películas con duración mayor a 120 minutos")
print("=" * 60)
peliculas_largas = df[df['duracion'] > 120]
print(f"Total de películas largas: {len(peliculas_largas)}")
print(peliculas_largas[['titulo', 'duracion', 'genero']].sort_values('duracion', ascending=False))

# ============================================
# ANÁLISIS 4: PELÍCULAS POR IDIOMA
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 4: Distribución por idioma")
print("=" * 60)
peliculas_por_idioma = df['idioma'].value_counts()
print(peliculas_por_idioma)

# ============================================
# ANÁLISIS 5: PELÍCULAS POR CLASIFICACIÓN
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 5: Distribución por clasificación")
print("=" * 60)
peliculas_por_clasificacion = df['clasificacion'].value_counts()
print(peliculas_por_clasificacion)

# ============================================
# ANÁLISIS 6: DIRECTORES MÁS PROLÍFICOS
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 6: Directores con más películas")
print("=" * 60)
directores = df['director'].value_counts().head(10)
print(directores)

# ============================================
# ANÁLISIS 7: PELÍCULAS POR PAÍS
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 7: Películas por país de origen")
print("=" * 60)
peliculas_por_pais = df['pais'].value_counts()
print(peliculas_por_pais)

# ============================================
# ANÁLISIS 8: ESTADÍSTICAS GENERALES
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 8: Estadísticas generales de duración")
print("=" * 60)
print(df['duracion'].describe())

# ============================================
# ANÁLISIS 9: PELÍCULAS DE TERROR
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 9: Análisis específico - Películas de Terror")
print("=" * 60)
peliculas_terror = df[df['genero'] == 'Terror']
print(f"Total de películas de terror: {len(peliculas_terror)}")
print(peliculas_terror[['titulo', 'duracion', 'clasificacion']])

# ============================================
# ANÁLISIS 10: PELÍCULAS EN ESPAÑOL
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 10: Películas disponibles en español")
print("=" * 60)
peliculas_espanol = df[df['idioma'] == 'Español']
print(f"Total de películas en español: {len(peliculas_espanol)}")
print(peliculas_espanol[['titulo', 'genero', 'clasificacion']])

# ============================================
# GENERACIÓN DE GRÁFICOS
# ============================================
print("\n" + "=" * 60)
print("GENERANDO VISUALIZACIONES...")
print("=" * 60)

# Gráfico 1: Películas por género
plt.figure(figsize=(10, 6))
peliculas_por_genero.plot(kind='bar', color='skyblue')
plt.xlabel('Género')
plt.ylabel('Cantidad de Películas')
plt.title('Distribución de Películas por Género - Cine Colombia')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('resultados/peliculas_por_genero.png', dpi=300)
print("✓ Gráfico guardado: resultados/peliculas_por_genero.png")
plt.close()

# Gráfico 2: Películas por idioma
plt.figure(figsize=(8, 6))
plt.pie(peliculas_por_idioma.values, labels=peliculas_por_idioma.index, 
        autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Películas por Idioma')
plt.tight_layout()
plt.savefig('resultados/peliculas_por_idioma.png', dpi=300)
print("✓ Gráfico guardado: resultados/peliculas_por_idioma.png")
plt.close()

# Gráfico 3: Duración promedio por género
plt.figure(figsize=(10, 6))
duracion_por_genero.plot(kind='barh', color='coral')
plt.xlabel('Duración Promedio (minutos)')
plt.ylabel('Género')
plt.title('Duración Promedio por Género')
plt.tight_layout()
plt.savefig('resultados/duracion_por_genero.png', dpi=300)
print("✓ Gráfico guardado: resultados/duracion_por_genero.png")
plt.close()

# ============================================
# EXPORTAR RESULTADOS
# ============================================
print("\n" + "=" * 60)
print("EXPORTANDO RESULTADOS...")
print("=" * 60)

# Guardar análisis en CSV
peliculas_por_genero.to_csv('resultados/analisis_genero.csv', header=['cantidad'])
print("✓ Análisis por género exportado")

duracion_por_genero.to_csv('resultados/analisis_duracion.csv', header=['duracion_promedio'])
print("✓ Análisis de duración exportado")

# ============================================
# FINALIZACIÓN
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS COMPLETADO EXITOSAMENTE")
print("=" * 60)
print("\nNOTA: Esta es una versión con Pandas para demostración.")
print("Para usar PySpark (procesamiento distribuido), instala Java:")
print("1. Descargar Java JDK: https://www.oracle.com/java/technologies/downloads/")
print("2. Instalar y configurar JAVA_HOME")
print("3. Ejecutar: python analisis.py")

print("\n✓ Análisis finalizado correctamente")
