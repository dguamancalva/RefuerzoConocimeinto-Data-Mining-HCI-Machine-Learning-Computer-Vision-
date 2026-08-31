# 📊 Bitácora de Aprendizaje - Itinerario de Sistemas Inteligentes

¡Bienvenido a tu panel de control de aprendizaje! Aquí registraremos tu progreso en el dominio de Python, Pandas, SQL y Machine Learning para prepararte para tu 7mo/8vo ciclo y tu futuro rol Junior.

## 🧑‍💻 Perfil del Estudiante
- **Carrera:** Ingeniería en Computación (Ecuador)
- **Ciclos en curso:** 7mo (Data Mining, HCI) y 8vo (Machine Learning, Computer Vision)
- **Meta:** Autonomía en programación y preparación para puestos Junior (Data Analyst Jr., QA, Soporte).

## 📅 Metodología de Estudio (Bloques de Enfoque)
- **Mañana (2 horas - Bloques 50/10):** Enfoque teórico (videos, documentación). Aplicar **Técnica Feynman Oral** (explicar en voz alta o grabar audios de 1 min basándose en esquemas y dibujos rápidos en papel).
- **Tarde (Práctica activa):** Resolución de retos de código, depuración de errores y feedback interactivo (sin ayudas automáticas).

---

## 📈 Tabla de Progreso (Módulo 1: Pandas y Preprocesamiento)

| Reto | Tema Principal | Conceptos Clave | Estado | Nota |
| :---: | :--- | :--- | :---: | :---: |
| **1** | [Introducción a DataFrames](file:///home/deivy/Documentos/Aprendizaje/modulo_1_pandas/ActividaD1.py) | Creación, selección de columnas, filtros booleanos | Completado | 10/10 |
| **2** | [Columnas & Agrupación](file:///home/deivy/Documentos/Aprendizaje/modulo_1_pandas/ActividadD2.py) | Operaciones vectoriales, `.groupby()`, agregaciones (`.sum()`) | Completado | 10/10 |
| **3** | [Limpieza de Datos](file:///home/deivy/Documentos/Aprendizaje/modulo_1_pandas/ActividadD3.py) | Manejo de nulos (`NaN`), `.fillna()`, `.dropna()` | Completado | 10/10 |
| **4** | [Combinación de Datos (Joins)](file:///home/deivy/Documentos/Aprendizaje/modulo_1_pandas/ActividadD4.py) | `pd.merge()`, conceptos de Inner Join vs. Left Join | Completado | 10/10 |
| **5** | [Codificación de Categorías](file:///home/deivy/Documentos/Aprendizaje/modulo_1_pandas/ActividadD5.py) | Label Mapping (`.map()`), One-Hot Encoding (`pd.get_dummies()`) | Completado | 10/10 |
| **6** | [Reto Integrador Final](file:///home/deivy/Documentos/Aprendizaje/modulo_1_pandas/ActividadD6.py) | Consolidación de todos los temas anteriores en un pipeline completo | Completado | 10/10 |

---

## 🎨 Tabla de Progreso (Módulo 2: Visualización de Datos - Seaborn & Matplotlib)

| Reto | Tema Principal | Conceptos Clave | Estado | Nota |
| :---: | :--- | :--- | :---: | :---: |
| **7** | [Primeros Gráficos con Seaborn](file:///home/deivy/Documentos/Aprendizaje/modulo_2_visualizacion/ActividadD7.py) | `sns.barplot()`, `sns.scatterplot()`, títulos con `plt.title()` y `plt.show()` | **En Progreso** | Pendiente |

---

## 🧠 Conceptos Clave para Entrevistas y Exámenes
1. **DataFrames vs Dicts:** Un DataFrame procesa datos vectorialmente (en paralelo), los diccionarios requieren bucles `for` (lentos).
2. **Boolean Masks:** Filtrar filas pasando una serie de `True`/`False`. `df[df['A'] > 5]`.
3. **Left Join vs Inner Join:** Inner busca intersección exacta; Left conserva toda la tabla izquierda y rellena vacíos con `NaN`.
4. **Dummies vs Mapping:** Mapping si hay orden lógico (ordinal); Dummies (One-Hot) si las categorías son independientes (nominal) para evitar sesgos en modelos de ML.
