# Proyecto Base de Datos Semántica - Cine Colombia
## Apache Jena + RDF/XML + SPARQL

### 📋 Descripción
Este proyecto implementa una base de datos semántica sobre películas en cartelera de Cine Colombia utilizando tecnologías de Web Semántica.

### 🛠️ Tecnologías Utilizadas
- **RDF/XML**: Formato de almacenamiento de datos semánticos
- **Apache Jena**: Framework Java para manejar datos RDF
- **SPARQL**: Lenguaje de consulta para datos RDF
- **Java**: Lenguaje de programación principal

### 📁 Estructura del Proyecto
```
Proyecto_Jena/
│
├── peliculas.rdf          # Base de datos RDF con 10 películas
├── consultas/             # 10 consultas SPARQL
│   ├── consulta1.rq       # Todas las películas
│   ├── consulta2.rq       # Películas de acción
│   ├── consulta3.rq       # Películas en español
│   ├── consulta4.rq       # Directores
│   ├── consulta5.rq       # Duración > 120 min
│   ├── consulta6.rq       # Clasificación +15
│   ├── consulta7.rq       # Ordenar alfabéticamente
│   ├── consulta8.rq       # Contar películas
│   ├── consulta9.rq       # Géneros únicos
│   └── consulta10.rq      # Películas con director y actor
│
├── src/
│   └── Main.java          # Programa principal
│
├── lib/                   # Librerías de Apache Jena
├── evidencias/            # Capturas de pantalla
└── README.md
```

### 🎬 Modelo de Datos
Cada película contiene:
- **título**: Nombre de la película
- **género**: Categoría (Terror, Acción, Animación, etc.)
- **director**: Director de la película
- **actor**: Actor principal
- **duración**: Duración en minutos
- **clasificación**: Clasificación por edad (+7, +12, +15, Todo Público)
- **idioma**: Idioma disponible (Español, Inglés)
- **país**: País de origen
- **año**: Año de producción
- **estreno**: Fecha de estreno

### 🚀 Instalación

#### 1. Descargar Apache Jena
```bash
# Descargar desde: https://jena.apache.org/download/
# Versión recomendada: Apache Jena 4.x o superior
```

#### 2. Configurar librerías en IntelliJ IDEA
1. Copiar todos los archivos `.jar` de `apache-jena/lib` a `Proyecto_Jena/lib`
2. En IntelliJ: `File → Project Structure → Libraries`
3. Agregar todos los `.jar` del directorio `lib`

#### 3. Compilar y ejecutar
```bash
javac -cp "lib/*" src/Main.java
java -cp "lib/*:src" Main
```

### 📊 Consultas SPARQL Implementadas

#### Consulta 1: Todas las películas
```sparql
SELECT ?titulo WHERE {
  ?p cine:titulo ?titulo .
}
```

#### Consulta 2: Películas de acción
```sparql
SELECT ?titulo WHERE {
  ?p cine:titulo ?titulo ;
     cine:genero "Acción" .
}
```

#### Consulta 5: Películas largas (>120 min)
```sparql
SELECT ?titulo ?duracion WHERE {
  ?p cine:titulo ?titulo ;
     cine:duracion ?duracion .
  FILTER(?duracion > 120)
}
```

### 🔍 Análisis del Código

#### Model (Modelo RDF)
```java
Model modelo = FileManager.get().loadModel("peliculas.rdf");
```
- Carga el archivo RDF en memoria
- Crea un grafo de tripletas (sujeto-predicado-objeto)
- Permite navegación semántica de los datos

#### Query (Consulta SPARQL)
```java
Query query = QueryFactory.create(consulta);
```
- Construye la consulta SPARQL
- Valida la sintaxis
- Optimiza la ejecución

#### QueryExecution (Ejecución)
```java
QueryExecution qexec = QueryExecutionFactory.create(query, modelo);
```
- Ejecuta la consulta sobre el modelo RDF
- Gestiona recursos y conexiones
- Retorna resultados estructurados

#### ResultSet (Resultados)
```java
ResultSet resultados = qexec.execSelect();
```
- Almacena los resultados de la consulta
- Permite iteración sobre las soluciones
- Formato tabular de datos

### 📈 Resultados Esperados
```
=== BASE DE DATOS SEMÁNTICA - CINE COLOMBIA ===

--------------------------------------------------
| titulo                              | genero   |
==================================================
| Destino Final: Lazos de Sangre     | Terror   |
| Misión Imposible: Sentencia Final  | Acción   |
| Minecraft: La Película              | Aventura |
| Wicked: Parte 2                     | Musical  |
...
```

### 🎯 Características Destacadas
✅ 10 películas con información completa
✅ 10 consultas SPARQL variadas
✅ Géneros diversos (Terror, Acción, Animación, Musical, etc.)
✅ Diferentes clasificaciones por edad
✅ Múltiples idiomas
✅ Información de directores y actores
✅ Datos de países y fechas de estreno

### 📝 Ventajas de RDF/SPARQL
- **Flexibilidad**: Fácil agregar nuevas propiedades
- **Interoperabilidad**: Estándar W3C compatible con otras bases
- **Consultas semánticas**: Búsquedas complejas con SPARQL
- **Inferencia**: Posibilidad de razonamiento lógico
- **Escalabilidad**: Manejo eficiente de grandes grafos

### 👨‍💻 Autor
Proyecto académico - Base de Datos Semántica
Cine Colombia - 2026
