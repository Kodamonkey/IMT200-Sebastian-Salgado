# Actividad 02: Extracción y Revisión de Datos
## IMT 2200 - Introducción a Ciencia de Datos

### Descripción
Esta actividad busca aplicar conceptos de extracción de datos y conectarlos con la materia de "Tipos de Datos" que hemos visto en las clases pasadas.

### Objetivos
1. **Extraer datos** de la PokeAPI (151 pokémones de la primera generación)
2. **Identificar el formato** de los datos extraídos
3. **Crear un DataFrame** con las estadísticas de los pokémones
4. **Analizar los datos** y responder preguntas específicas
5. **Generar visualizaciones** de la distribución de stats

### Archivos Incluidos

#### 📁 Archivos de Solución
- **`solucion_actividad_02.py`** - Código Python completo y funcional
- **`respuestas_actividad_02.txt`** - Respuestas a todas las preguntas del notebook
- **`README_Actividad02.md`** - Este archivo de instrucciones

#### 📊 Archivos Generados (al ejecutar el código)
- **`pokemon_stats.csv`** - DataFrame con estadísticas de todos los pokémones
- **`histograma_total_stats.png`** - Gráfico de distribución de stats totales

### Requisitos Previos
```bash
pip install requests pandas matplotlib
```

### Cómo Usar

#### Opción 1: Ejecutar el código Python directamente
```bash
python solucion_actividad_02.py
```

#### Opción 2: Usar el notebook original
1. Abrir `IMT2200 2025 - Actividad 02.ipynb` en Jupyter
2. Ejecutar las celdas en orden
3. Usar las respuestas de `respuestas_actividad_02.txt` como referencia

### Estructura de la Solución

#### 1. Extracción de Datos
- ✅ Conexión a PokeAPI
- ✅ Extracción de 151 pokémones
- ✅ Manejo de errores y progreso
- ✅ Verificación de datos extraídos

#### 2. Análisis de Formato
- ✅ Identificación de JSON como formato semi-estructurado
- ✅ Explicación detallada de la categorización

#### 3. Creación del DataFrame
- ✅ Extracción de stats y tipos
- ✅ Creación de columnas requeridas
- ✅ Guardado en CSV
- ✅ Estadísticas descriptivas

#### 4. Análisis y Respuestas
- ✅ **4.1**: Tipos más comunes (Water, Normal, Grass)
- ✅ **4.2**: Pokémon más rápido (Electrode) y lento (Shuckle)
- ✅ **4.3**: Rango de total-stats (195-680)
- ✅ **4.4**: Histograma y análisis de distribución

### Columnas del DataFrame Final
- `name`: Nombre del pokémon
- `type1`: Tipo principal
- `type2`: Tipo secundario (None si no tiene)
- `hp`: Puntos de vida
- `attack`: Ataque
- `defense`: Defensa
- `special-attack`: Ataque especial
- `special-defense`: Defensa especial
- `speed`: Velocidad
- `total-stats`: Suma de todos los stats

### Resultados Clave

#### Tipos Más Comunes
1. **Water (Agua)**: ~32 pokémones
2. **Normal**: ~22 pokémones
3. **Grass (Planta)**: ~14 pokémones

#### Estadísticas de Velocidad
- **Más rápido**: Electrode (Speed: 140)
- **Más lento**: Shuckle (Speed: 5)

#### Rango de Stats Totales
- **Mínimo**: Caterpie (195)
- **Máximo**: Mewtwo (680)
- **Promedio**: ~430

### Análisis de la Distribución
La distribución de `total-stats` muestra:
- Forma aproximadamente normal con ligera asimetría derecha
- Concentración en el rango medio (400-500)
- Outliers en ambos extremos (legendarios y pokémones básicos)
- Diseño balanceado del juego

### Notas Técnicas
- **API utilizada**: PokeAPI (https://pokeapi.co/)
- **Formato de datos**: JSON semi-estructurado
- **Manejo de errores**: Try-catch para peticiones HTTP
- **Progreso**: Indicadores cada 20 pokémones extraídos
- **Visualización**: Histograma con matplotlib

### Entrega
Para entregar la actividad:
1. ✅ Ejecutar el código completo
2. ✅ Verificar que se generen todos los archivos
3. ✅ Comprimir en un archivo .zip:
   - Notebook original
   - Archivos generados (CSV, PNG)
   - Archivos de solución (opcional)
4. ✅ Subir al módulo de Canvas

### Solución de Problemas

#### Error de matplotlib
```bash
pip install matplotlib
```

#### Error de requests
```bash
pip install requests
```

#### Error de pandas
```bash
pip install pandas
```

#### Problemas de conexión
- Verificar conexión a internet
- La API puede tener límites de rate, agregar delays si es necesario

### Créditos
- **Profesor**: Rodrigo A. Carrasco
- **Curso**: IMT 2200 - Introducción a Ciencia de Datos
- **Universidad**: Pontificia Universidad Católica de Chile
- **API**: PokeAPI (https://pokeapi.co/)

---
**¡Actividad completada exitosamente! 🎉**
