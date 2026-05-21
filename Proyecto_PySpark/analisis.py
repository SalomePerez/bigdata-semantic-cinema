from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count, col, desc, sum as spark_sum
import matplotlib.pyplot as plt
import pandas as pd

# ============================================
# CONFIGURACIÓN DE SPARK SESSION
# ============================================
print("=" * 60)
print("ANÁLISIS BIG DATA - PELÍCULAS CINE COLOMBIA")
print("Usando Apache PySpark")
print("=" * 60)

# Crear sesión Spark
spark = SparkSession.builder \
    .appName("Peliculas Cine Colombia - Análisis Big Data") \
    .master("local[*]") \
    .getOrCreate()

# Configurar nivel de log
spark.sparkContext.setLogLevel("ERROR")

# ============================================
# CARGA DE DATOS
# ============================================
print("\n[1] Cargando datos desde CSV...")
df = spark.read.csv("peliculas.csv", header=True, inferSchema=True)

print(f"✓ Total de películas cargadas: {df.count()}")
print("\n[2] Muestra de datos:")
df.show(5, truncate=False)

# ============================================
# ANÁLISIS 1: PELÍCULAS POR GÉNERO
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 1: Distribución de películas por género")
print("=" * 60)
peliculas_por_genero = df.groupBy("genero").count().orderBy(desc("count"))
peliculas_por_genero.show()

# ============================================
# ANÁLISIS 2: DURACIÓN PROMEDIO
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 2: Duración promedio de películas")
print("=" * 60)
duracion_promedio = df.select(avg("duracion").alias("duracion_promedio"))
duracion_promedio.show()

# Duración promedio por género
print("\nDuración promedio por género:")
df.groupBy("genero").agg(avg("duracion").alias("duracion_promedio")) \
    .orderBy(desc("duracion_promedio")).show()

# ============================================
# ANÁLISIS 3: PELÍCULAS LARGAS (>120 MIN)
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 3: Películas con duración mayor a 120 minutos")
print("=" * 60)
peliculas_largas = df.filter(col("duracion") > 120)
print(f"Total de películas largas: {peliculas_largas.count()}")
peliculas_largas.select("titulo", "duracion", "genero").orderBy(desc("duracion")).show(truncate=False)

# ============================================
# ANÁLISIS 4: PELÍCULAS POR IDIOMA
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 4: Distribución por idioma")
print("=" * 60)
df.groupBy("idioma").count().orderBy(desc("count")).show()

# ============================================
# ANÁLISIS 5: PELÍCULAS POR CLASIFICACIÓN
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 5: Distribución por clasificación")
print("=" * 60)
df.groupBy("clasificacion").count().orderBy(desc("count")).show()

# ============================================
# ANÁLISIS 6: DIRECTORES MÁS PROLÍFICOS
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 6: Directores con más películas")
print("=" * 60)
df.groupBy("director").count().orderBy(desc("count")).show(10)

# ============================================
# ANÁLISIS 7: PELÍCULAS POR PAÍS
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 7: Películas por país de origen")
print("=" * 60)
df.groupBy("pais").count().orderBy(desc("count")).show()

# ============================================
# ANÁLISIS 8: ESTADÍSTICAS GENERALES
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 8: Estadísticas generales de duración")
print("=" * 60)
df.describe("duracion").show()

# ============================================
# ANÁLISIS 9: PELÍCULAS DE TERROR
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 9: Análisis específico - Películas de Terror")
print("=" * 60)
peliculas_terror = df.filter(col("genero") == "Terror")
print(f"Total de películas de terror: {peliculas_terror.count()}")
peliculas_terror.select("titulo", "duracion", "clasificacion").show(truncate=False)

# ============================================
# ANÁLISIS 10: PELÍCULAS EN ESPAÑOL
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS 10: Películas disponibles en español")
print("=" * 60)
peliculas_espanol = df.filter(col("idioma") == "Español")
print(f"Total de películas en español: {peliculas_espanol.count()}")
peliculas_espanol.select("titulo", "genero", "clasificacion").show(truncate=False)

# ============================================
# GENERACIÓN DE GRÁFICOS
# ============================================
print("\n" + "=" * 60)
print("GENERANDO VISUALIZACIONES...")
print("=" * 60)

# Convertir a Pandas para visualización
generos_pd = peliculas_por_genero.toPandas()
idiomas_pd = df.groupBy("idioma").count().toPandas()

# Gráfico 1: Películas por género
plt.figure(figsize=(10, 6))
plt.bar(generos_pd['genero'], generos_pd['count'], color='skyblue')
plt.xlabel('Género')
plt.ylabel('Cantidad de Películas')
plt.title('Distribución de Películas por Género - Cine Colombia')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('resultados/peliculas_por_genero.png', dpi=300)
print("✓ Gráfico guardado: resultados/peliculas_por_genero.png")

# Gráfico 2: Películas por idioma
plt.figure(figsize=(8, 6))
plt.pie(idiomas_pd['count'], labels=idiomas_pd['idioma'], autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Películas por Idioma')
plt.tight_layout()
plt.savefig('resultados/peliculas_por_idioma.png', dpi=300)
print("✓ Gráfico guardado: resultados/peliculas_por_idioma.png")

# ============================================
# EXPORTAR RESULTADOS
# ============================================
print("\n" + "=" * 60)
print("EXPORTANDO RESULTADOS...")
print("=" * 60)

# Guardar análisis en CSV
peliculas_por_genero.coalesce(1).write.mode("overwrite").csv("resultados/analisis_genero", header=True)
print("✓ Análisis por género exportado")

# ============================================
# FINALIZACIÓN
# ============================================
print("\n" + "=" * 60)
print("ANÁLISIS COMPLETADO EXITOSAMENTE")
print("=" * 60)
print("\nVentajas de PySpark sobre Python tradicional:")
print("✓ Procesamiento distribuido y paralelo")
print("✓ Escalabilidad para grandes volúmenes de datos")
print("✓ Optimización automática de consultas")
print("✓ Manejo eficiente de memoria con DataFrames")
print("✓ Procesamiento lazy evaluation para mejor rendimiento")

# Cerrar sesión Spark
spark.stop()
print("\n✓ Sesión Spark finalizada correctamente")
