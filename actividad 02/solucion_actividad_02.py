# Solución completa para la Actividad 02: Extracción y Revisión de Datos
# IMT 2200 - Introducción a Ciencia de Datos

import requests
import pandas as pd
import matplotlib.pyplot as plt

print("=== SOLUCIÓN ACTIVIDAD 02 ===\n")

# ============================================================================
# 1. EXTRAER DATOS
# ============================================================================
print("1. EXTRAYENDO DATOS DE POKÉMON...")

# Definir la URL base de la API
url_base = "https://pokeapi.co/api/v2/pokemon/"

# Inicializar lista para almacenar los datos de los pokémones
pokemones = []

# Primero probamos con 2 pokémones para verificar que funciona
print("Probando con 2 pokémones primero...")
for i in range(1, 3):
    try:
        url = f"{url_base}{i}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemones.append(pokemon_data)
            print(f"Pokémon {i} ({pokemon_data['name']}) extraído exitosamente")
        else:
            print(f"Error al extraer Pokémon {i}: {response.status_code}")
    except Exception as e:
        print(f"Error al procesar el pokémon {i}: {e}")

print(f"\nSe extrajeron {len(pokemones)} pokémones de prueba")

# Ahora extraemos los 151 pokémones originales
print("\nExtrayendo los 151 pokémones originales...")
pokemones = []  # Reiniciamos la lista

for i in range(1, 152):
    try:
        url = f"{url_base}{i}"
        response = requests.get(url)
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemones.append(pokemon_data)
            if i % 20 == 0:  # Mostrar progreso cada 20 pokémones
                print(f"Progreso: {i}/151 pokémones extraídos")
        else:
            print(f"Error al extraer Pokémon {i}: {response.status_code}")
    except Exception as e:
        print(f"Error al procesar el pokémon {i}: {e}")

print(f"\n¡Completado! Se extrajeron {len(pokemones)} pokémones exitosamente")

# Verificar que se extrajeron los datos correctamente
print(f"\nTotal de pokémones extraídos: {len(pokemones)}")
print(f"Primer pokémon: {pokemones[0]['name']}")
print(f"Último pokémon: {pokemones[-1]['name']}")
print(f"\nEstructura del primer pokémon:")
print(f"Claves disponibles: {list(pokemones[0].keys())}")

# Mostrar ejemplo de la estructura de un pokémon
print("\nEjemplo de la estructura de datos:")
print(f"Nombre: {pokemones[0]['name']}")
print(f"Tipos: {[t['type']['name'] for t in pokemones[0]['types']]}")
print(f"Stats: {[(s['stat']['name'], s['base_stat']) for s in pokemones[0]['stats']]}")

# ============================================================================
# 2. FORMATO DE DATOS
# ============================================================================
print("\n" + "="*60)
print("2. FORMATO DE DATOS")
print("="*60)

print("Los datos extraídos de la PokeAPI están en formato JSON (JavaScript Object Notation),")
print("que es un formato de datos SEMI-ESTRUCTURADOS.")
print("\n¿Por qué semi-estructurados?")
print("1. Estructura definida: Cada pokémon tiene una estructura consistente")
print("2. Formato estandarizado: Los datos siguen un esquema predefinido de la API")
print("3. No completamente estructurados: No están en tabla relacional tradicional")
print("4. Anidación de datos: Contienen estructuras anidadas (types, stats)")
print("5. Flexibilidad: Algunos campos pueden estar presentes o ausentes")

# ============================================================================
# 3. DATAFRAME DE ANÁLISIS
# ============================================================================
print("\n" + "="*60)
print("3. CREANDO DATAFRAME DE ANÁLISIS")
print("="*60)

# Crear listas para almacenar los datos del DataFrame
nombres = []
tipos1 = []
tipos2 = []
hps = []
attacks = []
defenses = []
sp_attacks = []
sp_defenses = []
speeds = []

# Extraer datos de cada pokémon
for pokemon in pokemones:
    # Nombre
    nombres.append(pokemon['name'])
    
    # Tipos
    tipos = [t['type']['name'] for t in pokemon['types']]
    tipos1.append(tipos[0] if len(tipos) > 0 else None)
    tipos2.append(tipos[1] if len(tipos) > 1 else None)
    
    # Stats
    stats_dict = {s['stat']['name']: s['base_stat'] for s in pokemon['stats']}
    hps.append(stats_dict.get('hp', 0))
    attacks.append(stats_dict.get('attack', 0))
    defenses.append(stats_dict.get('defense', 0))
    sp_attacks.append(stats_dict.get('special-attack', 0))
    sp_defenses.append(stats_dict.get('special-defense', 0))
    speeds.append(stats_dict.get('speed', 0))

# Crear el DataFrame
df_pokemon = pd.DataFrame({
    'name': nombres,
    'type1': tipos1,
    'type2': tipos2,
    'hp': hps,
    'attack': attacks,
    'defense': defenses,
    'special-attack': sp_attacks,
    'special-defense': sp_defenses,
    'speed': speeds
})

print("DataFrame creado exitosamente:")
print(f"Dimensiones: {df_pokemon.shape}")
print("\nPrimeras 5 filas:")
print(df_pokemon.head())

# Guardar el DataFrame en un archivo CSV
df_pokemon.to_csv('pokemon_stats.csv', index=False)
print("\nDataFrame guardado como 'pokemon_stats.csv'")

# Mostrar información del DataFrame
print("\nInformación del DataFrame:")
print(df_pokemon.info())

print("\nEstadísticas descriptivas:")
print(df_pokemon.describe())

# ============================================================================
# 4. PREGUNTAS
# ============================================================================
print("\n" + "="*60)
print("4. RESPUESTAS A LAS PREGUNTAS")
print("="*60)

# 4.1 Tipos más comunes
print("\n4.1 TIPOS MÁS COMUNES")
print("-" * 30)

# Contar tipos (tanto type1 como type2)
tipos_combinados = df_pokemon['type1'].tolist() + df_pokemon['type2'].dropna().tolist()
conteo_tipos = pd.Series(tipos_combinados).value_counts()

print("Los 3 tipos más comunes en la primera generación son:")
print(conteo_tipos.head(3))

# También mostrar solo type1 para comparar
print("\nTipos más comunes solo considerando type1:")
print(df_pokemon['type1'].value_counts().head(3))

# 4.2 Pokémon más rápido y más lento
print("\n4.2 POKÉMON MÁS RÁPIDO Y MÁS LENTO")
print("-" * 40)

# Encontrar el pokémon más rápido
pokemon_mas_rapido = df_pokemon.loc[df_pokemon['speed'].idxmax()]
print(f"Pokémon más rápido: {pokemon_mas_rapido['name']} (Speed: {pokemon_mas_rapido['speed']})")

# Encontrar el pokémon más lento
pokemon_mas_lento = df_pokemon.loc[df_pokemon['speed'].idxmin()]
print(f"Pokémon más lento: {pokemon_mas_lento['name']} (Speed: {pokemon_mas_lento['speed']})")

# Mostrar los 10 pokémones más rápidos
print("\nTop 10 pokémones más rápidos:")
top_rapidos = df_pokemon.nlargest(10, 'speed')[['name', 'type1', 'type2', 'speed']]
print(top_rapidos)

# 4.3 Columna total-stats
print("\n4.3 COLUMNA TOTAL-STATS")
print("-" * 25)

# Crear la columna total-stats
df_pokemon['total-stats'] = (df_pokemon['hp'] + df_pokemon['attack'] + 
                             df_pokemon['defense'] + df_pokemon['special-attack'] + 
                             df_pokemon['special-defense'] + df_pokemon['speed'])

print("Columna 'total-stats' creada exitosamente")
print(f"\nRango de valores:")
print(f"Valor mínimo: {df_pokemon['total-stats'].min()}")
print(f"Valor máximo: {df_pokemon['total-stats'].max()}")
print(f"Valor promedio: {df_pokemon['total-stats'].mean():.2f}")

# Mostrar los pokémones con stats totales más altos y más bajos
print("\nPokémon con stats totales más altos:")
top_stats = df_pokemon.nlargest(5, 'total-stats')[['name', 'type1', 'type2', 'total-stats']]
print(top_stats)

print("\nPokémon con stats totales más bajos:")
bottom_stats = df_pokemon.nsmallest(5, 'total-stats')[['name', 'type1', 'type2', 'total-stats']]
print(bottom_stats)

# 4.4 Histograma de total-stats
print("\n4.4 HISTOGRAMA DE TOTAL-STATS")
print("-" * 30)

try:
    # Crear histograma de total-stats
    plt.figure(figsize=(10, 6))
    plt.hist(df_pokemon['total-stats'], bins=20, edgecolor='black', alpha=0.7)
    plt.title('Distribución de Stats Totales de Pokémon (Primera Generación)')
    plt.xlabel('Stats Totales')
    plt.ylabel('Frecuencia')
    plt.grid(True, alpha=0.3)

    # Agregar líneas verticales para la media y mediana
    media = df_pokemon['total-stats'].mean()
    mediana = df_pokemon['total-stats'].median()
    plt.axvline(media, color='red', linestyle='--', label=f'Media: {media:.1f}')
    plt.axvline(mediana, color='green', linestyle='--', label=f'Mediana: {mediana:.1f}')
    plt.legend()

    plt.tight_layout()
    plt.savefig('histograma_total_stats.png', dpi=300, bbox_inches='tight')
    print("Histograma guardado como 'histograma_total_stats.png'")
    plt.show()

    # Mostrar estadísticas adicionales
    print(f"\nEstadísticas de total-stats:")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Desviación estándar: {df_pokemon['total-stats'].std():.2f}")
    print(f"Asimetría: {df_pokemon['total-stats'].skew():.2f}")
    print(f"Curtosis: {df_pokemon['total-stats'].kurtosis():.2f}")

except Exception as e:
    print(f"Error al crear el histograma: {e}")
    print("Asegúrate de tener matplotlib instalado: pip install matplotlib")

# ============================================================================
# RESUMEN FINAL
# ============================================================================
print("\n" + "="*60)
print("RESUMEN FINAL")
print("="*60)

print("✅ Se extrajeron exitosamente 151 pokémones de la PokeAPI")
print("✅ Se identificó el formato JSON como semi-estructurado")
print("✅ Se creó un DataFrame con todas las columnas requeridas")
print("✅ Se guardó el DataFrame en 'pokemon_stats.csv'")
print("✅ Se respondieron todas las preguntas de análisis")
print("✅ Se generó un histograma de stats totales")

print(f"\nArchivos generados:")
print("- pokemon_stats.csv (DataFrame con estadísticas)")
print("- histograma_total_stats.png (gráfico de distribución)")

print("\n¡Actividad 02 completada exitosamente!")
