# 📚 GUÍA COMPLETA DE INSTALACIÓN Y EJECUCIÓN
## Proyecto Big Data + Web Semántica - Cine Colombia

---

## 🎯 PARTE 1: APACHE JENA (Base de Datos Semántica)

### PASO 1: Descargar Apache Jena

1. Ir a: https://jena.apache.org/download/
2. Descargar la versión más reciente (ejemplo: `apache-jena-4.10.0.zip`)
3. Extraer el archivo ZIP en una ubicación de tu preferencia

### PASO 2: Configurar el Proyecto en IntelliJ IDEA

#### Opción A: Crear proyecto desde cero
1. Abrir IntelliJ IDEA
2. `File → New → Project`
3. Seleccionar `Java`
4. Nombrar el proyecto: `Proyecto_Jena`
5. Click en `Create`

#### Opción B: Usar el proyecto ya creado
1. Abrir IntelliJ IDEA
2. `File → Open`
3. Seleccionar la carpeta `Proyecto_Jena`

### PASO 3: Agregar Librerías de Apache Jena

1. **Copiar archivos JAR**:
   - Ir a la carpeta donde extrajiste Apache Jena
   - Entrar a `apache-jena-X.X.X/lib/`
   - Copiar **TODOS** los archivos `.jar`
   - Pegarlos en `Proyecto_Jena/lib/`

2. **Configurar en IntelliJ**:
   - `File → Project Structure` (o `Ctrl+Alt+Shift+S`)
   - Ir a `Libraries`
   - Click en `+` → `Java`
   - Seleccionar la carpeta `lib` de tu proyecto
   - Click en `OK`
   - Click en `Apply` y luego `OK`

### PASO 4: Verificar Archivos del Proyecto

Asegúrate de tener esta estructura:
```
Proyecto_Jena/
├── lib/                    # Todos los .jar de Jena
├── src/
│   └── Main.java          # Código principal
├── peliculas.rdf          # Base de datos RDF
├── consultas/             # 10 archivos .rq
│   ├── consulta1.rq
│   ├── consulta2.rq
│   └── ...
└── evidencias/            # Para capturas
```

### PASO 5: Ejecutar el Proyecto

#### Método 1: Desde IntelliJ
1. Abrir `src/Main.java`
2. Click derecho en el archivo
3. Seleccionar `Run 'Main.main()'`
4. Ver resultados en la consola

#### Método 2: Desde Terminal
```bash
# Compilar
javac -cp "lib/*" src/Main.java

# Ejecutar (Windows)
java -cp "lib/*;src" Main

# Ejecutar (Linux/Mac)
java -cp "lib/*:src" Main
```

### PASO 6: Ejecutar Consultas SPARQL Individuales

Para probar cada consulta:

1. Modificar `Main.java` y cambiar la variable `consulta` por el contenido de cada archivo `.rq`
2. O crear un método que lea archivos `.rq`:

```java
import java.nio.file.Files;
import java.nio.file.Paths;

// Leer consulta desde archivo
String consultaTexto = new String(Files.readAllBytes(
    Paths.get("consultas/consulta1.rq")
));
```

### PASO 7: Tomar Capturas de Pantalla

Para cada consulta ejecutada:
1. Capturar la salida de la consola
2. Guardar en `evidencias/consulta1.png`, `consulta2.png`, etc.
3. Incluir en el informe

---

## 🎯 PARTE 2: PYSPARK (Análisis Big Data)

### PASO 1: Instalar Python

1. Descargar Python 3.8 o superior desde: https://www.python.org/downloads/
2. Durante la instalación, marcar "Add Python to PATH"
3. Verificar instalación:
```bash
python --version
```

### PASO 2: Instalar Java (Requerido para PySpark)

1. Descargar Java JDK 8 o superior desde: https://www.oracle.com/java/technologies/downloads/
2. Instalar siguiendo el asistente
3. Configurar variable de entorno `JAVA_HOME`:
   - Windows: `Panel de Control → Sistema → Variables de entorno`
   - Agregar `JAVA_HOME` apuntando a la carpeta de instalación de Java
4. Verificar:
```bash
java -version
```

### PASO 3: Instalar Dependencias de Python

Abrir terminal/CMD y ejecutar:

```bash
# Instalar PySpark
pip install pyspark

# Instalar Pandas
pip install pandas

# Instalar Matplotlib
pip install matplotlib
```

Verificar instalación:
```bash
pip list | grep pyspark
```

### PASO 4: Verificar Estructura del Proyecto

```
Proyecto_PySpark/
├── peliculas.csv          # Dataset con 20 películas
├── analisis.py            # Script principal
├── resultados/            # Carpeta para resultados
└── README.md
```

### PASO 5: Ejecutar el Análisis

#### Método 1: Desde Terminal
```bash
# Navegar a la carpeta del proyecto
cd Proyecto_PySpark

# Ejecutar el script
python analisis.py
```

#### Método 2: Desde IDE (PyCharm, VS Code)
1. Abrir `analisis.py`
2. Click derecho → `Run`
3. Ver resultados en la consola

### PASO 6: Verificar Resultados

Después de ejecutar, deberías ver:
- Salida en consola con todos los análisis
- Carpeta `resultados/` con:
  - `peliculas_por_genero.png`
  - `peliculas_por_idioma.png`
  - `analisis_genero/` (archivos CSV)

### PASO 7: Tomar Capturas

1. Capturar la salida de la consola mostrando los análisis
2. Capturar los gráficos generados
3. Guardar en carpeta `evidencias/`

---

## 🔧 SOLUCIÓN DE PROBLEMAS COMUNES

### Problema 1: "No se encuentra Java"
**Solución**:
```bash
# Verificar JAVA_HOME
echo %JAVA_HOME%  # Windows
echo $JAVA_HOME   # Linux/Mac

# Si está vacío, configurar:
# Windows: Panel de Control → Variables de entorno
# Linux/Mac: Agregar a ~/.bashrc o ~/.zshrc
export JAVA_HOME=/ruta/a/java
```

### Problema 2: "ClassNotFoundException" en Jena
**Solución**:
- Verificar que TODOS los .jar estén en `lib/`
- Reconfigurar librerías en IntelliJ: `File → Project Structure → Libraries`

### Problema 3: "ModuleNotFoundError: No module named 'pyspark'"
**Solución**:
```bash
# Reinstalar PySpark
pip uninstall pyspark
pip install pyspark
```

### Problema 4: "FileNotFoundError: peliculas.csv"
**Solución**:
- Verificar que estás ejecutando desde la carpeta correcta
- O usar ruta absoluta en el código:
```python
df = spark.read.csv("C:/ruta/completa/peliculas.csv", header=True)
```

### Problema 5: Error de memoria en PySpark
**Solución**:
```python
spark = SparkSession.builder \
    .appName("Peliculas") \
    .config("spark.driver.memory", "2g") \
    .getOrCreate()
```

---

## 📊 CREAR EL INFORME

### Estructura Recomendada

```
INFORME.docx
│
├── 1. INTRODUCCIÓN
│   ├── Objetivos del proyecto
│   └── Tecnologías utilizadas
│
├── 2. PARTE 1: BASE DE DATOS SEMÁNTICA (JENA)
│   ├── 2.1 Descripción del modelo RDF
│   ├── 2.2 Estructura de datos
│   ├── 2.3 Consultas SPARQL (10 consultas)
│   │   ├── Consulta 1: Código + Captura + Explicación
│   │   ├── Consulta 2: Código + Captura + Explicación
│   │   └── ...
│   └── 2.4 Análisis del código Java
│       ├── Explicación de Model
│       ├── Explicación de Query
│       ├── Explicación de QueryExecution
│       └── Explicación de ResultSet
│
├── 3. PARTE 2: ANÁLISIS BIG DATA (PYSPARK)
│   ├── 3.1 Descripción del dataset
│   ├── 3.2 Análisis implementados (10 análisis)
│   │   ├── Análisis 1: Código + Captura + Explicación
│   │   ├── Análisis 2: Código + Captura + Explicación
│   │   └── ...
│   ├── 3.3 Análisis del código PySpark
│   │   ├── SparkSession
│   │   ├── DataFrame
│   │   ├── groupBy()
│   │   ├── filter()
│   │   └── Funciones de agregación
│   └── 3.4 Ventajas de PySpark vs Python tradicional
│
├── 4. INTEGRACIÓN DE AMBOS PROYECTOS
│   ├── Conexión temática
│   └── Ecosistema Big Data + Web Semántica
│
├── 5. CONCLUSIONES
│   ├── Aprendizajes
│   ├── Ventajas de las tecnologías
│   └── Aplicaciones reales
│
└── 6. BIBLIOGRAFÍA
```

### Contenido Clave para Buena Nota

#### Para Apache Jena:
✅ Explicar qué es RDF y por qué es útil
✅ Describir el modelo de tripletas (sujeto-predicado-objeto)
✅ Explicar cada componente del código Java
✅ Mostrar variedad en las consultas SPARQL
✅ Incluir capturas de TODAS las consultas

#### Para PySpark:
✅ Explicar qué es Big Data y procesamiento distribuido
✅ Describir cada componente de PySpark
✅ Comparar con Python tradicional (IMPORTANTE)
✅ Mostrar gráficos generados
✅ Explicar ventajas de escalabilidad

#### Análisis Crítico (MUY IMPORTANTE):
✅ "PySpark permite procesamiento distribuido y escalable para grandes volúmenes de datos, mientras que Python tradicional trabaja de manera secuencial y limitada por memoria."
✅ "RDF/SPARQL permite consultas semánticas complejas y razonamiento lógico que SQL tradicional no puede realizar."

---

## ✅ CHECKLIST FINAL

### Antes de Entregar:

#### Proyecto Jena:
- [ ] 10 películas en `peliculas.rdf` con información completa
- [ ] 10 archivos `.rq` con consultas variadas
- [ ] `Main.java` funciona correctamente
- [ ] Capturas de todas las consultas
- [ ] README.md completo

#### Proyecto PySpark:
- [ ] 20 películas en `peliculas.csv`
- [ ] `analisis.py` ejecuta sin errores
- [ ] Gráficos generados en `resultados/`
- [ ] Capturas de análisis
- [ ] README.md completo

#### Informe:
- [ ] Portada con datos del estudiante
- [ ] Índice
- [ ] Introducción clara
- [ ] Explicación detallada de ambos proyectos
- [ ] Capturas de pantalla de TODAS las ejecuciones
- [ ] Análisis crítico y comparativo
- [ ] Conclusiones sólidas
- [ ] Bibliografía

---

## 📚 RECURSOS ADICIONALES

### Documentación Oficial:
- Apache Jena: https://jena.apache.org/documentation/
- PySpark: https://spark.apache.org/docs/latest/api/python/
- SPARQL: https://www.w3.org/TR/sparql11-query/
- RDF: https://www.w3.org/RDF/

### Tutoriales:
- Jena Tutorial: https://jena.apache.org/tutorials/
- PySpark Tutorial: https://spark.apache.org/docs/latest/quick-start.html

---

## 🎓 CONSEJOS PARA SACAR 5.0

1. **Variedad**: Usa diferentes tipos de consultas SPARQL (SELECT, FILTER, ORDER BY, COUNT, DISTINCT)
2. **Complejidad**: Incluye consultas simples Y complejas
3. **Análisis**: No solo muestres código, EXPLICA qué hace y por qué
4. **Comparación**: Compara PySpark con Python tradicional (esto suma muchos puntos)
5. **Visualización**: Los gráficos hacen el proyecto más profesional
6. **Integración**: Conecta ambos proyectos bajo el tema "Cine Colombia"
7. **Documentación**: README completos y bien estructurados
8. **Capturas**: Incluye capturas de TODAS las ejecuciones
9. **Código limpio**: Comenta tu código y usa buenas prácticas
10. **Conclusiones**: Reflexiona sobre lo aprendido y aplicaciones reales

---

## 📞 SOPORTE

Si tienes problemas:
1. Revisa la sección "Solución de Problemas"
2. Verifica que todas las dependencias estén instaladas
3. Consulta la documentación oficial
4. Revisa los README de cada proyecto

---

**¡Éxito con tu proyecto! 🚀**
