# 🎬 Proyecto Big Data + Web Semántica - Cine Colombia

## 📋 Descripción General

Este repositorio contiene un proyecto académico completo que integra dos tecnologías fundamentales:

1. **Base de Datos Semántica** con Apache Jena, RDF/XML y SPARQL
2. **Análisis Big Data** con Apache PySpark

Ambos proyectos trabajan sobre el mismo dominio: **Películas en cartelera de Cine Colombia**, creando un ecosistema completo de gestión y análisis de datos.

---

## 🏗️ Estructura del Repositorio

```
bigdata-semantic-cinema/
│
├── Proyecto_Jena/              # Base de Datos Semántica
│   ├── src/
│   │   └── Main.java           # Programa principal Java
│   ├── lib/                    # Librerías Apache Jena (.jar)
│   ├── consultas/              # 10 consultas SPARQL (.rq)
│   ├── evidencias/             # Capturas de pantalla
│   ├── peliculas.rdf           # Base de datos RDF/XML
│   └── README.md               # Documentación detallada
│
├── Proyecto_PySpark/           # Análisis Big Data
│   ├── analisis.py             # Script principal PySpark
│   ├── peliculas.csv           # Dataset con 20 películas
│   ├── resultados/             # Gráficos y análisis generados
│   └── README.md               # Documentación detallada
│
├── INSTRUCCIONES_INSTALACION.md  # Guía completa paso a paso
└── README.md                   # Este archivo
```

---

## 🎯 PARTE 1: Base de Datos Semántica (Apache Jena)

### Tecnologías
- **RDF/XML**: Formato de almacenamiento semántico
- **Apache Jena**: Framework Java para datos RDF
- **SPARQL**: Lenguaje de consulta semántica
- **Java**: Lenguaje de implementación

### Características
✅ 10 películas con información completa (título, género, director, actor, duración, clasificación, idioma, país, año)
✅ 10 consultas SPARQL variadas (SELECT, FILTER, ORDER BY, COUNT, DISTINCT)
✅ Modelo semántico rico con múltiples propiedades
✅ Código Java documentado y explicado

### Consultas Implementadas
1. Todas las películas
2. Películas de acción
3. Películas en español
4. Todos los directores
5. Películas con duración > 120 minutos
6. Películas clasificación +15
7. Películas ordenadas alfabéticamente
8. Contar total de películas
9. Géneros únicos
10. Películas con director y actor

### Ejemplo de Consulta SPARQL
```sparql
PREFIX cine: <http://www.cinecolombia.com/peliculas#>

SELECT ?titulo ?duracion
WHERE {
  ?pelicula cine:titulo ?titulo ;
            cine:duracion ?duracion .
  FILTER(?duracion > 120)
}
ORDER BY DESC(?duracion)
```

---

## 🎯 PARTE 2: Análisis Big Data (PySpark)

### Tecnologías
- **Apache PySpark**: Framework de procesamiento distribuido
- **Python**: Lenguaje de implementación
- **Pandas**: Manipulación de datos
- **Matplotlib**: Visualización de datos

### Características
✅ 20 películas con datos completos
✅ 10 análisis diferentes con PySpark
✅ Procesamiento distribuido y paralelo
✅ Generación de gráficos estadísticos
✅ Comparación con Python tradicional

### Análisis Implementados
1. Distribución por género
2. Duración promedio general y por género
3. Películas largas (>120 min)
4. Distribución por idioma
5. Distribución por clasificación
6. Directores más prolíficos
7. Películas por país
8. Estadísticas generales de duración
9. Análisis específico de películas de terror
10. Películas disponibles en español

### Ejemplo de Código PySpark
```python
# Análisis distribuido de películas por género
df.groupBy("genero").count().orderBy(desc("count")).show()

# Filtrado paralelo de películas largas
peliculas_largas = df.filter(col("duracion") > 120)
```

---

## 🚀 Inicio Rápido

### Requisitos Previos
- Java JDK 8 o superior
- Python 3.8 o superior
- Apache Jena (descargar de https://jena.apache.org/download/)

### Instalación Rápida

#### Para Apache Jena:
```bash
# 1. Copiar librerías de Jena a Proyecto_Jena/lib/
# 2. Configurar en IntelliJ: File → Project Structure → Libraries
# 3. Ejecutar Main.java
```

#### Para PySpark:
```bash
# Instalar dependencias
pip install pyspark pandas matplotlib

# Ejecutar análisis
cd Proyecto_PySpark
python analisis.py
```

### Guía Completa
Para instrucciones detalladas paso a paso, consulta: **[INSTRUCCIONES_INSTALACION.md](INSTRUCCIONES_INSTALACION.md)**

---

## 📊 Resultados Esperados

### Apache Jena
```
=== BASE DE DATOS SEMÁNTICA - CINE COLOMBIA ===

--------------------------------------------------
| titulo                              | genero   |
==================================================
| Destino Final: Lazos de Sangre     | Terror   |
| Misión Imposible: Sentencia Final  | Acción   |
| Avatar: Fuego y Ceniza              | Ciencia Ficción |
...
```

### PySpark
```
============================================================
ANÁLISIS 1: Distribución de películas por género
============================================================
+------------------+-----+
|genero            |count|
+------------------+-----+
|Terror            |5    |
|Acción            |4    |
|Animación         |4    |
...
```

---

## 🎓 Conceptos Clave

### Web Semántica (Jena)
- **RDF (Resource Description Framework)**: Modelo de datos basado en tripletas (sujeto-predicado-objeto)
- **SPARQL**: Lenguaje de consulta para datos RDF, similar a SQL pero para grafos
- **Ontologías**: Representación formal del conocimiento del dominio
- **Inferencia**: Capacidad de deducir nueva información a partir de datos existentes

### Big Data (PySpark)
- **Procesamiento Distribuido**: División de datos en particiones procesadas en paralelo
- **Lazy Evaluation**: Optimización de operaciones antes de ejecutarlas
- **DataFrames**: Estructuras de datos distribuidas e inmutables
- **Catalyst Optimizer**: Motor de optimización automática de consultas

---

## 🔍 Comparación: PySpark vs Python Tradicional

### Python Tradicional
```python
# Procesamiento secuencial
total = 0
for pelicula in peliculas:
    if pelicula['duracion'] > 120:
        total += 1
```
❌ Procesamiento secuencial (una por una)
❌ Limitado por memoria RAM
❌ No escalable

### PySpark
```python
# Procesamiento distribuido
df.filter(col("duracion") > 120).count()
```
✅ Procesamiento paralelo en múltiples cores
✅ Manejo de datos que exceden la RAM
✅ Escalable horizontalmente
✅ Optimización automática

---

## 📈 Visualizaciones

El proyecto PySpark genera automáticamente:
- 📊 Gráfico de barras: Distribución de películas por género
- 🥧 Gráfico circular: Distribución de películas por idioma
- 📁 Archivos CSV con análisis detallados

---

## 🔗 Integración de Ambos Proyectos

Este proyecto demuestra cómo **Web Semántica** y **Big Data** se complementan:

| Aspecto | Apache Jena | PySpark |
|---------|-------------|---------|
| **Enfoque** | Modelado semántico | Análisis estadístico |
| **Fortaleza** | Consultas complejas, razonamiento | Procesamiento masivo, escalabilidad |
| **Lenguaje** | SPARQL | Python/SQL |
| **Uso ideal** | Relaciones complejas, ontologías | Grandes volúmenes, análisis numérico |

**Juntos crean un ecosistema completo**: Jena para la estructura semántica y consultas inteligentes, PySpark para análisis masivo y estadísticas.

---

## 📚 Documentación Adicional

- [README Proyecto Jena](Proyecto_Jena/README.md) - Documentación detallada de la base semántica
- [README Proyecto PySpark](Proyecto_PySpark/README.md) - Documentación detallada del análisis Big Data
- [Instrucciones de Instalación](INSTRUCCIONES_INSTALACION.md) - Guía paso a paso completa

---

## 🎯 Aplicaciones Reales

### Apache Jena (Web Semántica)
- **Google Knowledge Graph**: Búsquedas semánticas
- **DBpedia**: Wikipedia estructurada
- **Healthcare**: Ontologías médicas (SNOMED, ICD)
- **E-commerce**: Recomendaciones basadas en relaciones

### PySpark (Big Data)
- **Netflix**: Recomendaciones de contenido
- **Uber**: Análisis de rutas y precios dinámicos
- **Spotify**: Análisis de preferencias musicales
- **Amazon**: Análisis de comportamiento de compra

---

## ✅ Checklist de Entrega

### Proyecto Jena:
- [x] 10 películas en RDF/XML
- [x] 10 consultas SPARQL variadas
- [x] Código Java funcional
- [x] README completo
- [ ] Capturas de pantalla (agregar en `evidencias/`)

### Proyecto PySpark:
- [x] 20 películas en CSV
- [x] Script de análisis completo
- [x] 10 análisis diferentes
- [x] Generación de gráficos
- [x] README completo

### Documentación:
- [x] README principal
- [x] Instrucciones de instalación
- [x] Documentación de cada proyecto
- [ ] Informe académico (crear según estructura en INSTRUCCIONES_INSTALACION.md)

---

## 🤝 Contribuciones

Este es un proyecto académico. Para mejoras o sugerencias:
1. Fork el repositorio
2. Crea una rama para tu feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto es de uso académico y educativo.

---

## 👨‍💻 Autor

Proyecto académico - Big Data y Web Semántica
**Cine Colombia - 2026**

---

## 🌟 Características Destacadas

✨ **Proyecto completo e integrado** sobre un dominio real (Cine Colombia)
✨ **Dos tecnologías complementarias** (Web Semántica + Big Data)
✨ **Código documentado y explicado** en detalle
✨ **Consultas y análisis variados** que demuestran dominio de las tecnologías
✨ **Visualizaciones profesionales** con gráficos estadísticos
✨ **Guías completas de instalación** paso a paso
✨ **Comparaciones técnicas** entre enfoques tradicionales y modernos

---

## 📞 Soporte

Para problemas o dudas:
1. Revisa [INSTRUCCIONES_INSTALACION.md](INSTRUCCIONES_INSTALACION.md)
2. Consulta los README de cada proyecto
3. Revisa la documentación oficial de las tecnologías

---

**¡Éxito con tu proyecto! 🚀🎬**
