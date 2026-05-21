# 🚀 Instrucciones de Ejecución - Apache Jena

## 📋 Requisitos Previos
- ✅ Java JDK 8 o superior instalado
- ✅ IntelliJ IDEA (o cualquier IDE Java)
- ✅ Apache Jena descargado

---

## 🔧 CONFIGURACIÓN INICIAL (Una sola vez)

### PASO 1: Descargar Apache Jena

1. Ir a: https://jena.apache.org/download/
2. Descargar la última versión (ejemplo: `apache-jena-4.10.0.zip`)
3. Extraer el archivo en una ubicación de tu preferencia

### PASO 2: Copiar Librerías

1. Navegar a la carpeta donde extrajiste Apache Jena
2. Entrar a la subcarpeta `lib/`
3. **Copiar TODOS los archivos `.jar`** (deberían ser aproximadamente 50-60 archivos)
4. Pegar en: `Proyecto_Jena/lib/`

**Archivos importantes que debes ver en `lib/`:**
- `jena-core-X.X.X.jar`
- `jena-arq-X.X.X.jar`
- `slf4j-api-X.X.X.jar`
- Y muchos más...

### PASO 3: Configurar IntelliJ IDEA

#### Opción A: Abrir el Proyecto
1. Abrir IntelliJ IDEA
2. `File → Open`
3. Seleccionar la carpeta `Proyecto_Jena`
4. Click en `OK`

#### Opción B: Crear Proyecto Nuevo
1. `File → New → Project`
2. Seleccionar `Java`
3. Nombrar: `Proyecto_Jena`
4. Copiar los archivos del proyecto a la nueva ubicación

### PASO 4: Agregar Librerías al Proyecto

1. En IntelliJ: `File → Project Structure` (o `Ctrl+Alt+Shift+S`)
2. En el panel izquierdo, seleccionar **"Libraries"**
3. Click en el botón **"+"** (arriba)
4. Seleccionar **"Java"**
5. Navegar a la carpeta `Proyecto_Jena/lib/`
6. Seleccionar **TODOS** los archivos `.jar`
7. Click en **"OK"**
8. Click en **"Apply"**
9. Click en **"OK"**

### PASO 5: Verificar Configuración

1. Abrir `src/Main.java`
2. Verificar que no haya errores de importación (líneas rojas)
3. Si hay errores, repetir el Paso 4

---

## ▶️ EJECUCIÓN

### OPCIÓN 1: Ejecutar Consulta Individual (Main.java)

Este programa ejecuta UNA consulta predefinida.

#### Desde IntelliJ:
1. Abrir `src/Main.java`
2. Click derecho en el archivo
3. Seleccionar `Run 'Main.main()'`
4. Ver resultados en la consola

#### Desde Terminal:
```bash
# Compilar
javac -cp "lib/*" src/Main.java

# Ejecutar (Windows)
java -cp "lib/*;src" Main

# Ejecutar (Linux/Mac)
java -cp "lib/*:src" Main
```

#### Modificar la Consulta:
Para ejecutar diferentes consultas, edita la variable `consulta` en `Main.java`:

```java
// Cambiar esta parte:
String consulta = 
    "PREFIX cine: <http://www.cinecolombia.com/peliculas#> " +
    "SELECT ?titulo ?genero " +
    "WHERE { " +
    "  ?pelicula cine:titulo ?titulo ; " +
    "            cine:genero ?genero . " +
    "}";

// Por el contenido de cualquier archivo .rq
// Ejemplo: copiar el contenido de consultas/consulta2.rq
```

---

### OPCIÓN 2: Ejecutar Todas las Consultas (EjecutarConsultas.java) - RECOMENDADO

Este programa ejecuta AUTOMÁTICAMENTE las 10 consultas.

#### Desde IntelliJ:
1. Abrir `src/EjecutarConsultas.java`
2. Click derecho en el archivo
3. Seleccionar `Run 'EjecutarConsultas.main()'`
4. Ver resultados de las 10 consultas en la consola

#### Desde Terminal:
```bash
# Compilar
javac -cp "lib/*" src/EjecutarConsultas.java

# Ejecutar (Windows)
java -cp "lib/*;src" EjecutarConsultas

# Ejecutar (Linux/Mac)
java -cp "lib/*:src" EjecutarConsultas
```

---

## 📸 TOMAR CAPTURAS DE PANTALLA

### Para el Informe Académico:

#### Captura 1: Ejecución de Main.java
1. Ejecutar `Main.java`
2. Capturar la consola completa
3. Guardar como: `evidencias/jena_main.png`

#### Capturas 2-11: Cada Consulta Individual
**Método A: Usando EjecutarConsultas.java (Más Rápido)**
1. Ejecutar `EjecutarConsultas.java`
2. Capturar cada sección de la consola (una por consulta)
3. Guardar como:
   - `evidencias/consulta1.png`
   - `evidencias/consulta2.png`
   - ...
   - `evidencias/consulta10.png`

**Método B: Modificando Main.java (Más Detallado)**
1. Abrir `Main.java`
2. Copiar contenido de `consultas/consulta1.rq` a la variable `consulta`
3. Ejecutar y capturar → `evidencias/consulta1.png`
4. Repetir para consulta2.rq, consulta3.rq, etc.

---

## 📊 RESULTADOS ESPERADOS

### Consulta 1: Todas las películas
```
-----------------------------------------
| titulo                              |
=========================================
| Destino Final: Lazos de Sangre     |
| Misión Imposible: Sentencia Final  |
| Minecraft: La Película              |
...
```

### Consulta 2: Películas de acción
```
-----------------------------------------
| titulo                              |
=========================================
| Misión Imposible: Sentencia Final  |
| Rápidos y Furiosos 11               |
...
```

### Consulta 5: Películas largas (>120 min)
```
---------------------------------------------------------
| titulo                              | duracion        |
=========================================================
| Avatar: Fuego y Ceniza              | 190             |
| Misión Imposible: Sentencia Final  | 165             |
| Wicked: Parte 2                     | 155             |
...
```

---

## 🔧 SOLUCIÓN DE PROBLEMAS

### Error: "ClassNotFoundException"
**Causa:** Las librerías no están configuradas correctamente.
**Solución:**
1. Verificar que todos los .jar estén en `lib/`
2. Reconfigurar librerías: `File → Project Structure → Libraries`
3. Eliminar y volver a agregar todos los .jar

### Error: "FileNotFoundException: peliculas.rdf"
**Causa:** El programa no encuentra el archivo RDF.
**Solución:**
1. Verificar que `peliculas.rdf` esté en la raíz de `Proyecto_Jena/`
2. Si ejecutas desde terminal, asegúrate de estar en la carpeta correcta:
   ```bash
   cd Proyecto_Jena
   ```

### Error: "QueryParseException"
**Causa:** Error de sintaxis en la consulta SPARQL.
**Solución:**
1. Verificar que copiaste correctamente el contenido del archivo .rq
2. Asegurarte de incluir el PREFIX completo
3. Revisar que no falten llaves `{}` o puntos y comas `;`

### Error: "No se reconoce 'java'"
**Causa:** Java no está instalado o no está en el PATH.
**Solución:**
1. Instalar Java JDK: https://www.oracle.com/java/technologies/downloads/
2. Configurar JAVA_HOME (ver `INSTRUCCIONES_INSTALACION.md`)
3. Reiniciar la terminal

---

## 📝 PARA EL INFORME

### Información a Incluir:

#### 1. Descripción del Modelo RDF
- 10 películas de Cine Colombia
- 10 propiedades por película
- Namespace: `http://www.cinecolombia.com/peliculas#`

#### 2. Código Java
Incluir y explicar:
- `Model modelo = FileManager.get().loadModel("peliculas.rdf");`
  - Carga el archivo RDF en memoria
  - Crea un grafo de tripletas
  
- `Query query = QueryFactory.create(consulta);`
  - Construye la consulta SPARQL
  - Valida la sintaxis
  
- `QueryExecution qexec = QueryExecutionFactory.create(query, modelo);`
  - Ejecuta la consulta sobre el modelo
  - Gestiona recursos
  
- `ResultSet resultados = qexec.execSelect();`
  - Almacena los resultados
  - Permite iteración

#### 3. Cada Consulta SPARQL
Para cada una de las 10 consultas:
- Código SPARQL
- Captura de pantalla del resultado
- Explicación de qué hace
- Número de resultados obtenidos

#### 4. Análisis
- Ventajas de RDF/SPARQL vs bases de datos relacionales
- Aplicaciones de Web Semántica
- Escalabilidad del modelo

---

## ✅ CHECKLIST DE EJECUCIÓN

### Configuración:
- [ ] Apache Jena descargado
- [ ] Archivos .jar copiados a `lib/`
- [ ] Librerías configuradas en IntelliJ
- [ ] Proyecto compila sin errores

### Ejecución:
- [ ] Main.java ejecutado correctamente
- [ ] EjecutarConsultas.java ejecutado correctamente
- [ ] Todas las consultas muestran resultados

### Capturas:
- [ ] Captura de Main.java
- [ ] Captura de consulta 1
- [ ] Captura de consulta 2
- [ ] Captura de consulta 3
- [ ] Captura de consulta 4
- [ ] Captura de consulta 5
- [ ] Captura de consulta 6
- [ ] Captura de consulta 7
- [ ] Captura de consulta 8
- [ ] Captura de consulta 9
- [ ] Captura de consulta 10

### Informe:
- [ ] Código incluido y explicado
- [ ] Capturas agregadas
- [ ] Análisis de componentes
- [ ] Conclusiones

---

## 🎯 TIEMPO ESTIMADO

- **Configuración inicial:** 30 minutos (una sola vez)
- **Ejecución de consultas:** 15 minutos
- **Capturas de pantalla:** 30 minutos
- **TOTAL:** 1 hora 15 minutos

---

## 📞 SOPORTE

Si tienes problemas:
1. Revisa la sección "Solución de Problemas"
2. Verifica que Java esté instalado: `java -version`
3. Consulta `INSTRUCCIONES_INSTALACION.md`
4. Revisa `README.md` del proyecto

---

**¡Éxito con la ejecución! 🚀**
