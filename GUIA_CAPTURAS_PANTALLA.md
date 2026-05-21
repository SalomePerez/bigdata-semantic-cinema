# 📸 GUÍA RÁPIDA PARA TOMAR CAPTURAS DE PANTALLA

## 🎯 OBJETIVO
Tomar las capturas necesarias para completar el informe del proyecto.

---

## ✅ PARTE 2: PYSPARK/PANDAS (30 minutos)

### PASO 1: Ejecutar el Análisis

#### Opción A: Usando el archivo .bat (MÁS FÁCIL)
1. Ir a la carpeta: `Proyecto_PySpark`
2. Hacer **doble clic** en: `EJECUTAR_ANALISIS.bat`
3. Se abrirá una ventana de CMD con los resultados

#### Opción B: Usando PowerShell
1. Abrir PowerShell
2. Ejecutar:
```powershell
cd "Proyecto_PySpark"
python analisis_pandas.py
```

### PASO 2: Tomar Capturas

#### Captura 1: Ejecución Completa (IMPORTANTE)
**Qué capturar:**
- Toda la ventana de CMD/PowerShell con los 10 análisis
- Desde el inicio hasta "Análisis finalizado correctamente"

**Cómo capturar:**
1. Presionar `Windows + Shift + S` (Herramienta de recorte)
2. Seleccionar toda la ventana
3. Guardar como: `evidencias/pyspark_ejecucion_completa.png`

**O usar:**
- `Alt + PrtScn` para capturar solo la ventana activa
- Pegar en Paint y guardar

#### Captura 2: Análisis 1 - Distribución por Género
**Qué capturar:**
```
============================================================
ANÁLISIS 1: Distribución de películas por género
============================================================
genero
Terror             5
Acción             5
Animación          5
...
```
**Guardar como:** `evidencias/pyspark_analisis1_genero.png`

#### Captura 3: Análisis 2 - Duración Promedio
**Qué capturar:**
```
============================================================
ANÁLISIS 2: Duración promedio de películas
============================================================
Duración promedio: 129.05 minutos
...
```
**Guardar como:** `evidencias/pyspark_analisis2_duracion.png`

#### Captura 4: Análisis 3 - Películas Largas
**Qué capturar:**
```
============================================================
ANÁLISIS 3: Películas con duración mayor a 120 minutos
============================================================
Total de películas largas: 10
...
```
**Guardar como:** `evidencias/pyspark_analisis3_largas.png`

### PASO 3: Capturar Gráficos Generados

#### Captura 5: Gráfico de Barras - Género
1. Abrir: `Proyecto_PySpark/resultados/peliculas_por_genero.png`
2. Capturar la imagen completa
3. Guardar como: `evidencias/grafico_genero.png`

#### Captura 6: Gráfico Circular - Idioma
1. Abrir: `Proyecto_PySpark/resultados/peliculas_por_idioma.png`
2. Capturar la imagen completa
3. Guardar como: `evidencias/grafico_idioma.png`

#### Captura 7: Gráfico de Barras - Duración
1. Abrir: `Proyecto_PySpark/resultados/duracion_por_genero.png`
2. Capturar la imagen completa
3. Guardar como: `evidencias/grafico_duracion.png`

### PASO 4: Capturar Archivos Generados

#### Captura 8: Carpeta de Resultados
1. Abrir explorador de archivos
2. Ir a: `Proyecto_PySpark/resultados/`
3. Cambiar vista a "Detalles" o "Lista"
4. Capturar mostrando todos los archivos:
   - peliculas_por_genero.png
   - peliculas_por_idioma.png
   - duracion_por_genero.png
   - analisis_genero.csv
   - analisis_duracion.csv
5. Guardar como: `evidencias/archivos_generados.png`

---

## ⚠️ PARTE 1: APACHE JENA (2 horas)

### REQUISITO PREVIO: Instalar Apache Jena

#### PASO 1: Descargar Apache Jena
1. Ir a: https://jena.apache.org/download/
2. Descargar: `apache-jena-X.X.X.zip` (última versión)
3. Extraer en cualquier ubicación (ejemplo: `C:\apache-jena`)

#### PASO 2: Copiar Librerías
1. Ir a: `C:\apache-jena\lib\` (donde extrajiste)
2. Seleccionar **TODOS** los archivos `.jar` (Ctrl+A)
3. Copiar (Ctrl+C)
4. Ir a: `Proyecto_Jena\lib\`
5. Pegar (Ctrl+V)

**Verificar:** Deberías tener 50-60 archivos .jar en `Proyecto_Jena\lib\`

#### PASO 3: Configurar IntelliJ IDEA

##### Si NO tienes IntelliJ:
**Opción 1: Descargar IntelliJ Community (GRATIS)**
1. Ir a: https://www.jetbrains.com/idea/download/
2. Descargar "Community Edition" (gratis)
3. Instalar

**Opción 2: Usar Eclipse**
1. Abrir Eclipse
2. `File → Open Projects from File System`
3. Seleccionar `Proyecto_Jena`
4. Click derecho en el proyecto → `Build Path → Configure Build Path`
5. `Libraries → Add External JARs`
6. Seleccionar todos los .jar de `lib/`

**Opción 3: Compilar desde CMD (Sin IDE)**
```cmd
cd Proyecto_Jena
javac -cp "lib/*" src/EjecutarConsultas.java
java -cp "lib/*;src" EjecutarConsultas
```

##### Si tienes IntelliJ:
1. Abrir IntelliJ IDEA
2. `File → Open`
3. Seleccionar carpeta `Proyecto_Jena`
4. `File → Project Structure` (Ctrl+Alt+Shift+S)
5. Ir a `Libraries`
6. Click en `+` → `Java`
7. Seleccionar carpeta `lib/`
8. Click `OK` → `Apply` → `OK`

#### PASO 4: Ejecutar el Programa

##### Desde IntelliJ:
1. Abrir: `src/EjecutarConsultas.java`
2. Click derecho en el archivo
3. Seleccionar: `Run 'EjecutarConsultas.main()'`
4. Ver resultados en la consola (abajo)

##### Desde CMD:
```cmd
cd Proyecto_Jena
java -cp "lib/*;src" EjecutarConsultas
```

### PASO 5: Tomar Capturas de Jena

#### Captura 9: Encabezado del Programa
**Qué capturar:**
```
======================================================================
BASE DE DATOS SEMÁNTICA - CINE COLOMBIA
Apache Jena + RDF/XML + SPARQL
======================================================================

✓ Modelo RDF cargado exitosamente
✓ Total de tripletas: XX
```
**Guardar como:** `evidencias/jena_inicio.png`

#### Capturas 10-19: Cada Consulta (10 capturas)

**Para cada consulta capturar:**
- Número de consulta
- Código SPARQL
- Resultados en tabla

**Ejemplo Consulta 1:**
```
======================================================================
CONSULTA 1
Archivo: consultas/consulta1.rq
======================================================================
Consulta SPARQL:
  PREFIX cine: <http://www.cinecolombia.com/peliculas#>
  SELECT ?titulo
  WHERE {
    ?pelicula cine:titulo ?titulo .
  }

Resultados:
-----------------------------------------
| titulo                              |
=========================================
| Destino Final: Lazos de Sangre     |
| Misión Imposible: Sentencia Final  |
...
```

**Guardar como:**
- `evidencias/jena_consulta1.png`
- `evidencias/jena_consulta2.png`
- `evidencias/jena_consulta3.png`
- `evidencias/jena_consulta4.png`
- `evidencias/jena_consulta5.png`
- `evidencias/jena_consulta6.png`
- `evidencias/jena_consulta7.png`
- `evidencias/jena_consulta8.png`
- `evidencias/jena_consulta9.png`
- `evidencias/jena_consulta10.png`

#### Captura 20: Mensaje Final
**Qué capturar:**
```
======================================================================
TODAS LAS CONSULTAS EJECUTADAS EXITOSAMENTE
======================================================================
```
**Guardar como:** `evidencias/jena_final.png`

---

## 📊 RESUMEN DE CAPTURAS NECESARIAS

### PySpark/Pandas (8 capturas):
- [ ] `pyspark_ejecucion_completa.png` - Consola completa
- [ ] `pyspark_analisis1_genero.png` - Análisis 1
- [ ] `pyspark_analisis2_duracion.png` - Análisis 2
- [ ] `pyspark_analisis3_largas.png` - Análisis 3
- [ ] `grafico_genero.png` - Gráfico de barras
- [ ] `grafico_idioma.png` - Gráfico circular
- [ ] `grafico_duracion.png` - Gráfico de barras horizontal
- [ ] `archivos_generados.png` - Carpeta resultados/

### Apache Jena (12 capturas):
- [ ] `jena_inicio.png` - Encabezado
- [ ] `jena_consulta1.png` - Consulta 1
- [ ] `jena_consulta2.png` - Consulta 2
- [ ] `jena_consulta3.png` - Consulta 3
- [ ] `jena_consulta4.png` - Consulta 4
- [ ] `jena_consulta5.png` - Consulta 5
- [ ] `jena_consulta6.png` - Consulta 6
- [ ] `jena_consulta7.png` - Consulta 7
- [ ] `jena_consulta8.png` - Consulta 8
- [ ] `jena_consulta9.png` - Consulta 9
- [ ] `jena_consulta10.png` - Consulta 10
- [ ] `jena_final.png` - Mensaje final

**TOTAL: 20 capturas**

---

## 💡 CONSEJOS PARA BUENAS CAPTURAS

### Calidad:
✅ Usar resolución alta (no pixeladas)
✅ Capturar texto legible
✅ Incluir contexto suficiente
✅ No cortar información importante

### Herramientas:
- **Windows + Shift + S**: Herramienta de recorte (Windows 10/11)
- **Alt + PrtScn**: Captura ventana activa
- **PrtScn**: Captura pantalla completa
- **Snipping Tool**: Herramienta de recortes de Windows

### Formato:
✅ Guardar como PNG (mejor calidad)
✅ Nombres descriptivos
✅ Organizar en carpeta `evidencias/`

---

## 🎯 ORDEN RECOMENDADO

### AHORA (30 minutos):
1. ✅ Ejecutar `analisis_pandas.py`
2. ✅ Tomar 8 capturas de PySpark

### HOY (2 horas):
3. ⏱️ Descargar e instalar Apache Jena
4. ⏱️ Configurar IntelliJ/Eclipse
5. ⏱️ Ejecutar `EjecutarConsultas.java`
6. ⏱️ Tomar 12 capturas de Jena

### MAÑANA (2 horas):
7. ⏱️ Crear informe con todas las capturas

---

## 📁 ESTRUCTURA FINAL DE EVIDENCIAS

```
evidencias/
├── pyspark_ejecucion_completa.png
├── pyspark_analisis1_genero.png
├── pyspark_analisis2_duracion.png
├── pyspark_analisis3_largas.png
├── grafico_genero.png
├── grafico_idioma.png
├── grafico_duracion.png
├── archivos_generados.png
├── jena_inicio.png
├── jena_consulta1.png
├── jena_consulta2.png
├── jena_consulta3.png
├── jena_consulta4.png
├── jena_consulta5.png
├── jena_consulta6.png
├── jena_consulta7.png
├── jena_consulta8.png
├── jena_consulta9.png
├── jena_consulta10.png
└── jena_final.png
```

---

## ⚡ ATAJOS DE TECLADO ÚTILES

- `Windows + Shift + S`: Herramienta de recorte
- `Alt + PrtScn`: Capturar ventana activa
- `Ctrl + V`: Pegar en Paint/Word
- `Ctrl + S`: Guardar archivo

---

## 🆘 SI TIENES PROBLEMAS

### PySpark no ejecuta:
✅ **SOLUCIÓN:** Usa `analisis_pandas.py` (ya funciona)
- Es equivalente para el informe
- Genera los mismos resultados
- No requiere Java

### Apache Jena no compila:
❌ **PROBLEMA:** Faltan librerías
✅ **SOLUCIÓN:** Verificar que todos los .jar estén en `lib/`

### No tienes IntelliJ:
✅ **SOLUCIÓN 1:** Descargar Community Edition (gratis)
✅ **SOLUCIÓN 2:** Usar Eclipse
✅ **SOLUCIÓN 3:** Compilar desde CMD

---

## 📞 RECURSOS

- **Apache Jena:** https://jena.apache.org/download/
- **IntelliJ IDEA:** https://www.jetbrains.com/idea/download/
- **Eclipse:** https://www.eclipse.org/downloads/

---

**¡Empieza con PySpark que ya funciona! 🚀**
**Luego continúa con Apache Jena.**
