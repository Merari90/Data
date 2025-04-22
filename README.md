# DataDiscoverViolence-Related

# 🧠 Application of Data Science to Discover Violence-Related Issues in Iraq

---

## 🇪🇸 Español

### 📋 Resumen

Este proyecto aplica principios de ciencia de datos y aprendizaje automático para identificar problemas sociales relacionados con la violencia en Irak, utilizando datos abiertos no gubernamentales de la base GDELT.

### 🧰 Tecnologías utilizadas

- Python 2.7.12
- Scikit-learn
- Pandas, NumPy
- BigQuery (para extracción de datos)
- TKinter (interfaz gráfica)

### 🧪 Algoritmos aplicados

- K-Nearest Neighbors (KNN)
- Näive Bayes
- Árboles de Decisión 🌳
- Regresión Logística

### 📊 Evaluación

Se llevaron a cabo 104 experimentos (26 combinaciones de eventos × 4 algoritmos), usando una división 70/30 para entrenamiento y prueba. Los mejores resultados se obtuvieron para:

| Evento                        | Precisión | Recall | F1-score |
|------------------------------|-----------|--------|----------|
| Refugiados (0)               | 0.76      | 0.76   | 0.76     |
| Combates con artillería (194)| 0.74      | 0.75   | 0.75     |

### 🗺️ Validación

Los resultados fueron comparados con mapas oficiales de UNHCR y Liveuamap, identificando correctamente zonas como Erbil, Ramadi y Bagdad.

### 🖥️ Software

Se desarrolló un prototipo en Python donde el usuario puede ingresar coordenadas geográficas y obtener una clasificación del evento violento correspondiente.

### 📦 Cómo usar

1. Clona el repositorio.
2. Instala dependencias (recomendado con Anaconda).
3. Ejecuta la interfaz gráfica (`main.py` si existe).
4. Introduce coordenadas para obtener una clasificación.

### 🌍 Enlaces útiles

- [Datos GDELT](https://www.gdeltproject.org/)
- [Dataset y código fuente](https://drive.google.com/drive/folders/0B6LEG8jNfAY9MEJBTkZoYlRIZHc)
- [Video de demostración](https://vimeo.com/268047670)

### 📈 Futuro

- Extender a otros países de Medio Oriente
- Integración con Apache Spark para procesamiento en tiempo real
- Mejora de la interfaz con mapas interactivos

### 📄 Licencia

Este proyecto está disponible bajo licencia MIT (o especificar si aplica).


---

## 🇬🇧 English

### 📋 Overview

This project applies data science and machine learning principles to identify violence-related social issues in Iraq, using non-governmental open data from the GDELT database.

### 🧰 Technologies Used

- Python 2.7.12
- Scikit-learn
- Pandas, NumPy
- BigQuery (for data extraction)
- TKinter (for GUI)

### 🧪 Applied Algorithms

- K-Nearest Neighbors (KNN)
- Näive Bayes
- Decision Trees 🌳
- Logistic Regression

### 📊 Evaluation

A total of 104 experiments were conducted (26 combinations of events × 4 algorithms), using a 70/30 training/testing split. Best results:

| Event                         | Precision | Recall | F1-score |
|------------------------------|-----------|--------|----------|
| Refugees (0)                 | 0.76      | 0.76   | 0.76     |
| Fights with artillery (194)  | 0.74      | 0.75   | 0.75     |

### 🗺️ Validation

Results were validated against official maps from UNHCR and Liveuamap, accurately identifying zones like Erbil, Ramadi, and Baghdad.

### 🖥️ Software

A Python prototype was developed that allows users to input coordinates (latitude/longitude) and receive a classification of the corresponding violent event.

### 📦 How to Use

1. Clone the repository.
2. Install dependencies (Anaconda recommended).
3. Run the GUI (`main.py` if applicable).
4. Input coordinates to receive a classification.

### 🌍 Useful Links

- [GDELT Data](https://www.gdeltproject.org/)
- [Dataset and source code](https://drive.google.com/drive/folders/0B6LEG8jNfAY9MEJBTkZoYlRIZHc)
- [Demo video](https://vimeo.com/268047670)

### 📈 Future Work

- Extend analysis to other Middle East countries
- Integrate Apache Spark for real-time data processing
- Improve the user interface with interactive maps

### 📄 License

This project is licensed under the MIT License (or specify if different).
