# 1.1 Fundamentos del lenguaje Python

Este módulo introduce los conceptos esenciales para comenzar a programar en Python.  
Se trabajará con un entorno en la nube, variables, operadores y estructuras de control básicas.


# 1.1.1 Entorno de programación: GitHub Codespaces con VS Code

## Introducción
**GitHub Codespaces** te ofrece un entorno de desarrollo completo basado en **VS Code en la nube**, ligado a tu repositorio. No necesitas instalar Python localmente: el contenedor ya trae intérprete, extensiones y dependencias reproducibles mediante configuración.

---

## Características
- **VS Code en el navegador** (o app) con terminal, extensiones y depuración.
- **Entorno reproducible** por repo usando `.devcontainer/`.
- **Integración total con Git y GitHub** (branches, PRs, Issues).
- **Configurable**: versiones de Python, paquetes, herramientas (linters, formatters, etc.).
- **Soporte Jupyter** dentro de VS Code (notebooks `.ipynb`).

### Limitaciones
- Requiere conexión estable a Internet.
- Los recursos de cómputo dependen del plan de GitHub.
- El contenedor “duerme” si no lo usas por un tiempo (se reactiva rápido).

---

## Requisitos previos
- Cuenta en **GitHub** con acceso a **GitHub Codespaces**.
- Un repositorio (por ejemplo, `python-ciencia-datos`) con permisos para abrir Codespaces.

---

## Primeros pasos (crear y abrir un Codespace)
1. Entra a tu repo en GitHub.
2. Haz clic en **Code → Codespaces → Create codespace on main** (o la rama que prefieras).
3. Espera 1–2 minutos a que se construya el contenedor e instale extensiones.
4. Se abrirá **VS Code Web** con el repo listo para trabajar (explorador, terminal, etc.).

> Tip: si tienes extensión de **GitHub Codespaces** instalada en VS Code de escritorio, puedes “**Open in VS Code**”.

---

## Hola Mundo (archivo `.py`)
1. Crea un archivo `hello.py` en la raíz del repo:
   ```python
   print("Hola mundo desde Codespaces 👋")
   ```
   
Abre la Terminal en VS Code y ejecuta:

```bash
python hello.py
```

Verás la salida en la terminal.


Notas: 
-Si el repo incluye requirements.txt, se instalarán automáticamente tras crear el Codespace.
- Si modificas requirements.txt y ya está creado el Codespace abre la Terminal en VS Code y ejecuta:
```bash
   pip install -r requirements.txt
```

# Programas que utilizan **funciones predefinidas** (Clase 3 – Python Intro)

> 12 mini-programas listos para ejecutar que practican *built-in functions* de Python.

## Cómo usar
Copia y pega cada bloque en tu entorno (REPL/archivo `.py`) y ejecútalo. Algunos piden entrada con `input()`.

---

## 1) Resumen estadístico
**Usa:** `input`, `split`, `int`, `list`, `len`, `sum`, `min`, `max`, `sorted`, `round`, `print`
```python
raw = input("Números enteros separados por comas: ")  # ej: 10, 5, 3, 12, 7
nums = [int(x.strip()) for x in raw.split(",")]
prom = round(sum(nums) / len(nums), 2)
print("n:", len(nums),
      "| suma:", sum(nums),
      "| min:", min(nums),
      "| max:", max(nums),
      "| prom:", prom,
      "| ord:", sorted(nums))
```

## 2) Top-3 ventas del mes
**Usa:** `sorted`, `print`
```python
ventas = [1200, 550, 3000, 1800, 950, 2200]
top3 = sorted(ventas, reverse=True)[:3]
print("Top 3:", top3)
```

## 3) Validador de contraseña
**Usa:** `any`, `all`, `len`, `print`
```python
pwd = input("Contraseña: ")
tiene_mayus = any(c.isupper() for c in pwd)
tiene_num   = any(c.isdigit() for c in pwd)
ok = all([len(pwd) >= 8, tiene_mayus, tiene_num])
print("Fuerte" if ok else "Débil")
```

## 4) Lista numerada de tareas
**Usa:** `enumerate`, `print`
```python
tareas = ["Lavar datos", "Entrenar modelo", "Presentar resultados"]
for i, t in enumerate(tareas, start=1):
    print(f"{i}. {t}")
```

## 5) Emparejar alumnos con calificaciones
**Usa:** `zip`, `print`
```python
alumnos = ["Ana", "Luis", "Sofía"]
scores  = [95, 81, 88]
for nombre, sc in zip(alumnos, scores):
    print(f"{nombre}: {sc}")
```

## 6) Normalizar calificaciones (0–100 → 0–1)
**Usa:** `map`, `round`, `list`, `print`
```python
scores = [78, 95, 62, 88]
norm = list(map(lambda s: round(s/100, 2), scores))
print(norm)  # [0.78, 0.95, 0.62, 0.88]
```

## 7) Filtrar números pares
**Usa:** `filter`, `list`, `print`
```python
nums = list(range(1, 21))
pares = list(filter(lambda x: x % 2 == 0, nums))
print(pares)
```

## 8) Convertir segundos a h:m:s
**Usa:** `divmod`, `print`
```python
seg = int(input("Segundos totales: "))
m, s = divmod(seg, 60)
h, m = divmod(m, 60)
print(f"{h:02d}:{m:02d}:{s:02d}")
```

## 9) Tabla de multiplicar (n × 1..10)
**Usa:** `int`, `range`, `print`
```python
n = int(input("Número: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")
```

## 10) ¿Es primo?
**Usa:** `int`, `range`, `all`, `print`, `pow`
```python
n = int(input("Entero ≥ 2: "))
es_primo = n >= 2 and all(n % k for k in range(2, int(pow(n, 0.5)) + 1))
print("Primo" if es_primo else "No primo")
```

## 11) Decimal → binario / octal / hex
**Usa:** `int`, `bin`, `oct`, `hex`, `print`
```python
n = int(input("Decimal: "))
print("bin:", bin(n), "| oct:", oct(n), "| hex:", hex(n))
```

## 12) Detector de palabras prohibidas
**Usa:** `any`, `print`
```python
texto = input("Texto: ").lower()
baneadas = {"spam", "oferta", "gratis"}
hay_ban = any(p in texto for p in baneadas)
print("Contiene prohibidas" if hay_ban else "Limpio")
```


