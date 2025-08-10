# Actividad 01: Herramientas Computacionales para Ciencia de Datos

**IMT2200 - Introducción a la Ciencia de Datos**  
**Pontificia Universidad Católica de Chile**  
**Instituto de Ingeniería Matemática y Computacional**  
**Semestre 2025-S2**  
**Profesor:** Rodrigo A. Carrasco  
**Estudiante:** Sebastian Salgado

---

## Descripción de la Actividad

Esta actividad tiene como objetivo principal **probar el ambiente de programación** de cada estudiante y la **instalación de librerías de Python** necesarias para el curso. El segundo objetivo es aprender a usar **GitHub**, configurar el repositorio personal y entregar la actividad correctamente.

## Librerías Utilizadas

- **`numpy`**: Para operaciones numéricas y cálculos matemáticos
- **`pandas`**: Para manipulación y análisis de datos estructurados
- **`geopandas`**: Para el manejo de datos geoespaciales y creación de mapas
- **`matplotlib`**: Para la generación de gráficos y visualizaciones

## Dataset

### Datos del Censo 2017

### Archivos de entrada

- `Censo2017_Manzanas.csv`: Datos demográficos por manzana censal
- `R13/MANZANA_IND_C17.shp`: Mapa de manzanas de la Región Metropolitana
- `R13/COMUNA_C17.shp`: Mapa de comunas de la Región Metropolitana

### Análisis realizado

- Población total de Chile en 2017
- Distribución de población por edad y región
- Mapa de densidad poblacional por manzana en la RM

## Resultado Final

La actividad genera un **mapa de la Región Metropolitana** que muestra la distribución de población total por manzana censal, utilizando datos del Censo 2017. El mapa incluye:

- Visualización de densidad poblacional por manzana
- Límites de comunas
- Etiquetas de nombres de comunas
- Escala de colores para interpretar la densidad

## Archivos de Salida

- `PoblacionRM_C2017_SebastianSalgado.jpg`: Mapa final de la RM con población por manzana
- `IMT2200 - Actividad 01.ipynb`: Notebook de Jupyter con todo el código ejecutado

## Instrucciones de Ejecución

1. **Verificar librerías**: Asegurarse de que todas las librerías estén instaladas
2. **Ejecutar notebook**: Correr todas las celdas del notebook en orden secuencial
3. **Editar personalización**: Cambiar el nombre en el título y nombre del archivo de salida por su apellido (Ejemplo: 'Salgado')
4. **Generar visualización**: Crear el mapa final de la RM y verificar que tenga el nombre deseado
5. **Subir a GitHub**: Entregar el notebook y la imagen en el repositorio personal