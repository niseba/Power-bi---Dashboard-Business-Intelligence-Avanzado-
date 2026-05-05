# 📊 Dashboard de Business Intelligence con Pipeline ETL en Python – Power BI

<p align="center">
  <img src="Dashboard.gif" alt="PowerBI Dashboard" width="600"/>
</p>

## 📌 Descripción General

Solución integral de **Business Intelligence** para análisis de desempeño comercial, rentabilidad y eficiencia operativa, construida sobre un **pipeline ETL completo en Python** que integra múltiples fuentes de datos, las transforma y las entrega como insumo limpio y estructurado para Power BI.

Se implementó un modelo dimensional bajo **Star Schema (metodología Kimball)**, garantizando:

✔️ Alto rendimiento en consultas
✔️ Escalabilidad del modelo
✔️ Claridad analítica
✔️ Confiabilidad en los KPIs

---

## 🎯 Valor para el Negocio

Este dashboard permite:

- 📈 Identificar productos, regiones y segmentos de mayor y menor desempeño
- 💰 Analizar tendencias de ingresos, utilidad y margen
- 🚚 Evaluar eficiencia logística
- 📊 Monitorear crecimiento interanual
- 🧭 Apoyar procesos de planeación estratégica y forecasting

---

## 📂 Dataset

- **📍 Fuente:** Dataset público de ventas de una multinacional tecnológica
- **📍 Granularidad:** Línea de orden de venta

### Variables principales

- Sales, Profit, Quantity, Discount
- Order Date, Ship Date
- Customer, Product, Geography, Ship Mode

---

## 🧹 Pipeline ETL en Python

El proceso ETL fue desarrollado de forma modular en Python con **pandas**, estructurado en tres capas independientes:

### ⚙️ Extracción
- Detección y carga dinámica de múltiples archivos CSV mediante `glob`
- Soporte para encoding `utf-8-sig` y manejo de líneas con errores

### 🔄 Transformación
- Eliminación de duplicados por clave compuesta (`Order ID`, `Product ID`, `Customer ID`)
- Estandarización de fechas con manejo de formatos mixtos y detección de valores inválidos
- Normalización de campos de texto (strip + title case) para garantizar consistencia

### 📤 Carga
- Exportación a CSV procesado como fuente directa para Power BI
- Generación automática de **log de auditoría** con timestamp, conteo de filas exportadas y columnas del dataset

### Transformaciones complementarias en Power Query
- Corrección de formatos numéricos y monetarios por configuración regional
- Depuración de datos geográficos (ciudad–estado) para garantizar unicidad
- Generación de surrogate keys e integración de dimensiones con FactSales mediante merges validados

---

## 🧩 Arquitectura del Modelo de Datos

Se implementó un esquema en estrella con la siguiente estructura:

### 📍 Tabla de Hechos

**FactSales**

- Sales, Profit, Quantity, Discount
- Order Date, Ship Date
- CustomerKey, ProductKey, GeographyKey, ShipModeKey

### 📍 Tablas Dimensión

- **DimCustomer:** Cliente y Segmento
- **DimProduct:** Producto, Categoría y Subcategoría
- **DimGeography:** País, Estado, Ciudad, Región
- **DimShipMode:** Tipo de Envío
- **DimDate:** Construcción dinámica mediante DAX (CALENDAR) basada en rango real de datos

### ⚙️ Decisiones de Modelado

- Integración de Categoría y Subcategoría en DimProduct (evitando Snowflake)
- Implementación de surrogate keys en todas las dimensiones
- Definición de granularidad a nivel de línea de venta
- Relaciones 1:\* con filtrado unidireccional

---

## 📈 Diseño del Dashboard y Navegación

La navegación se gestiona mediante:

🔖 Bookmarks &nbsp; 🔘 Botones interactivos &nbsp; 🔄 Reset de filtros

### 📊 Secciones Principales

- Overview
- Segmentación
- Análisis Regional
- Análisis de Producto
- Product Insights
- Forecasting
- Actual vs Año Anterior
- Análisis Semanal

---

## 🧠 Retos Técnicos y Soluciones

🔹 Múltiples archivos CSV sin clave unificada → Extracción dinámica y deduplicación por clave compuesta en Python

🔹 Fechas en formatos mixtos → Estandarización con `pd.to_datetime` y detección de valores inválidos

🔹 Formato incorrecto de datos monetarios → Ajuste de configuración regional en Power Query

🔹 Ausencia de claves geográficas → Diseño e implementación de surrogate keys

🔹 Cálculo correcto de porcentajes dinámicos → Gestión avanzada del filter context con `ALLSELECTED`

🔹 Navegación compleja → Implementación de bookmarks y control de estados

---

## 🚀 Habilidades Demostradas

✔️ Pipeline ETL modular en Python (pandas)
✔️ Integración de múltiples fuentes de datos CSV
✔️ Auditoría automatizada del proceso de carga
✔️ Modelado dimensional bajo Star Schema (Kimball)
✔️ Limpieza y estandarización avanzada de datos
✔️ Desarrollo de métricas y KPIs en DAX (Time Intelligence, YoY, acumulados, variaciones)
✔️ Gestión avanzada de contextos de filtro en DAX
✔️ Análisis temporal mediante tablas calendario
✔️ Diseño de dashboards ejecutivos orientados a toma de decisiones
✔️ Optimización de rendimiento mediante reducción de cardinalidad y buenas prácticas de modelado

---

> 🎯 **Nota:** Este proyecto fue desarrollado con enfoque en escenarios empresariales reales, mejores prácticas de Business Intelligence y un pipeline de datos estructurado de extremo a extremo.
