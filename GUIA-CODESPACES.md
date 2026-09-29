# 🚀 Guía de GitHub Codespaces

**Programación I — UNIAJC**  
Guía para trabajar en el curso usando GitHub Codespaces.

---

## 📖 ¿Qué es GitHub Codespaces?

**GitHub Codespaces** es un entorno de desarrollo completo que funciona **directamente en tu navegador**. No necesitas instalar Python, VS Code ni nada en tu computadora.

Cuando abres un Codespace, obtienes:

- ✅ Un editor de código (VS Code) en el navegador
- ✅ Una terminal integrada para ejecutar comandos
- ✅ Python 3.11 instalado
- ✅ pytest instalado (para ejecutar pruebas)
- ✅ Extensiones de Python preconfiguradas
- ✅ Todo tu código sincronizado con GitHub

**Ventaja:** Puedes programar desde cualquier computadora (incluso prestada) sin instalar nada.

---

## ⚡ Antes de empezar

Necesitas:

1. **Una cuenta de GitHub** (gratuita). Si no tienes, créala en [github.com/signup](https://github.com/signup)
2. **Un navegador moderno** (Chrome, Firefox, Edge o Safari actualizado)
3. **Conexión a internet**

**No necesitas:**
- ❌ Instalar Python
- ❌ Instalar VS Code
- ❌ Instalar Git
- ❌ Configurar nada en tu computadora

---

## 🎯 Flujo de trabajo del curso

Este es el flujo que seguirás **para cada taller**:

```
1. Crea tu repositorio desde la plantilla
        ↓
2. Abre un Codespace en ese repositorio
        ↓
3. Edita los archivos del taller
        ↓
4. Ejecuta las pruebas localmente
        ↓
5. Haz commit y push
        ↓
6. Verifica el resultado en la pestaña Actions
```

---

## Paso 1: Crear tu repositorio desde la plantilla

1. Ve al repositorio plantilla del curso:
   👉 [https://github.com/Programacion-I-UNIAJC/template-curso-programacion](https://github.com/Programacion-I-UNIAJC/template-curso-programacion)

2. Haz clic en el botón verde **"Use this template"** (Usar esta plantilla)

3. Selecciona **"Create a new repository"**

4. En la nueva pantalla:
   - **Repository name:** `taller-01-tu-nombre`  
     (ejemplo: `taller-01-juan-perez`)
   - **Description** (opcional): `Taller 01 - Programación I`
   - **Visibility:** selecciona **Private** (privado)

5. Haz clic en **"Create repository"**

**Listo.** Ahora tienes tu propio repositorio con todos los archivos del taller.

---

## Paso 2: Abrir un Codespace

1. En tu **nuevo repositorio** (no en el de la plantilla), haz clic en el botón verde **"Code"**

2. Se abrirá un menú desplegable. Selecciona la pestaña **"Codespaces"**

3. Haz clic en **"Create codespace on main"**

4. **Espera 1-2 minutos** mientras GitHub construye tu entorno

5. Cuando termine, verás una interfaz de **VS Code en tu navegador** con:
   - Panel de archivos a la izquierda
   - Editor de código al centro
   - Terminal integrada abajo

---

## Paso 3: Conocer la interfaz

Una vez dentro de tu Codespace, verás algo así:

```
┌──────────────────────────────────────────────────┐
│  ARCHIVOS           EDITOR                        │
│  📁 taller-01/      (aquí escribes tu código)     │
│  📄 programa.py                                   │
│  📄 test_programa.py                              │
│                                                   │
├──────────────────────────────────────────────────┤
│  TERMINAL                                         │
│  $ (aquí ejecutas comandos)                       │
└──────────────────────────────────────────────────┘
```

**Elementos importantes:**

| Elemento | ¿Para qué sirve? |
|:---|:---|
| **Panel izquierdo** | Ver y abrir archivos |
| **Editor central** | Escribir código |
| **Terminal (abajo)** | Ejecutar comandos y pruebas |
| **Panel Source Control** | Hacer commit y push |

---

## Paso 4: Editar el código del taller

1. En el panel izquierdo, haz clic en `taller-01/` para expandir

2. Lee los archivos **en orden**:
   - `README.md` — Instrucciones generales
   - `01-problema.md` — Enunciado del problema
   - `02-algoritmo.md` — Aquí escribes tu análisis
   - `04-pruebas.md` — Aquí documentas tus pruebas
   - `programa.py` — Aquí escribes tu código Python

3. **Edita `programa.py`** para completar la función `calcular_potencia`:

   Busca la línea que dice:
   ```python
   return 0.0  # <-- Aquí debe ir: return V * I
   ```
   
   Y cámbiala por:
   ```python
   return V * I
   ```

4. **Completa las secciones TODO** del archivo:
   - En la sección de entradas: `V = float(input("..."))`
   - En la sección de entradas: `I = float(input("..."))`
   - En la sección de salida: `print(f"La potencia es: {P} W")`

---

## Paso 5: Ejecutar tu programa

Para probar tu código:

1. Abre la **terminal** en Codespaces:
   - Presiona `` Ctrl + ` `` (o `Cmd + ` en Mac)
   - O ve a **View → Terminal** en el menú

2. Navega a la carpeta del taller:
   ```bash
   cd taller-01
   ```

3. Ejecuta tu programa:
   ```bash
   python programa.py
   ```

4. El programa te pedirá el voltaje y la corriente. Ingresa valores y verifica el resultado.

**Ejemplo:**
```
Digite el voltaje (V): 120
Digite la corriente (A): 5
La potencia es: 600.0 W
```

---

## Paso 6: Ejecutar las pruebas automáticas

Antes de hacer commit, verifica que tu código pasa todas las pruebas.

En la terminal (dentro de `taller-01/`):

```bash
pytest test_programa.py -v
```

Verás algo como:

```
test_programa.py::test_potencia_basica PASSED                     [ 12%]
test_programa.py::test_potencia_decimales PASSED                  [ 25%]
test_programa.py::test_potencia_voltaje_cero PASSED               [ 37%]
test_programa.py::test_potencia_corriente_cero PASSED             [ 50%]
test_programa.py::test_potencia_valores_grandes PASSED            [ 62%]
test_programa.py::test_potencia_valores_pequenos PASSED           [ 75%]
test_programa.py::test_funcion_existe PASSED                      [ 87%]
test_programa.py::test_funcion_retorna_numero PASSED              [100%]

===================== 8 passed in 0.05s =====================
```

**Si todas las pruebas pasan (8 passed):** ✅ ¡Tu código está correcto!
**Si alguna prueba falla:** ❌ Lee el mensaje de error y corrige tu código.

---

## Paso 7: Hacer commit y push

Cuando tu código pase todas las pruebas:

1. En el panel izquierdo, haz clic en el ícono de **Source Control** (parece una rama con un punto)

2. Verás una lista de archivos modificados

3. En el campo de texto **"Message"**, escribe:
   ```
   Completar Taller 01
   ```

4. Haz clic en el botón **"Commit"** (o presiona `Ctrl + Enter`)

5. Haz clic en el botón **"Sync Changes"** (o **"Push"**) para subir los cambios a GitHub

---

## Paso 8: Verificar el resultado en GitHub

1. Ve a tu repositorio en [github.com](https://github.com)

2. Haz clic en la pestaña **"Actions"**

3. Verás una nueva ejecución del workflow con el mensaje de tu commit

4. Haz clic en ella para ver el resultado:
   - ✅ **Check verde** — ¡Todo pasó!
   - ❌ **X roja** — Alguna prueba falló
   - 🟡 **Círculo amarillo** — Todavía está corriendo

5. Haz clic en el job **"Evaluación automática con pytest"** para ver el detalle

---

## 💡 Consejos para no agotar tu cuota

GitHub Codespaces tiene una **cuota gratuita mensual** (120 horas para cuentas Free).

**Reglas importantes:**

1. **Detén el Codespace cuando no lo uses:**
   - Ve a [github.com/codespaces](https://github.com/codespaces)
   - Busca tu Codespace activo
   - Haz clic en los tres puntos `...` → **"Stop"**

2. **Cierra la pestaña del navegador** después de detener el Codespace

3. **Reabre el mismo Codespace** en lugar de crear uno nuevo cada vez:
   - Abrir un Codespace existente no consume cuota extra de inicio
   - Crear uno nuevo cada vez sí lo hace

4. **Configura el timeout:**
   - Ve a [github.com/settings/codespaces](https://github.com/settings/codespaces)
   - Configura **"Default idle timeout"** a **30 minutos**

5. **No dejes Codespaces abiertos por horas sin usar**

---

## ❓ Preguntas frecuentes

### ¿Qué pasa si cierro el Codespace?

Tu código queda guardado automáticamente en GitHub **siempre que hagas commit y push**. Si cierras sin guardar, perderás los cambios no guardados.

### ¿Puedo trabajar desde varios dispositivos?

Sí. Solo abre el mismo Codespace desde otro navegador y verás todo tu código tal como lo dejaste.

### ¿Necesito instalar algo?

No. Todo está preconfigurado en el Codespace.

### ¿Qué hago si no aparecen las pruebas en pytest?

Verifica que estás en la carpeta correcta:
```bash
cd taller-01
pytest test_programa.py -v
```

### ¿Qué hago si el Codespace no abre?

1. Espera 2-3 minutos (a veces tarda en construirse)
2. Recarga la página
3. Si sigue sin funcionar, detén el Codespace y crea uno nuevo

---

## 📞 ¿Necesitas ayuda?

Si tienes problemas:

1. **Consulta este archivo primero**
2. **Revisa los mensajes de error** en la terminal
3. **Pregunta en clase** o por el canal del curso
4. **Pídele ayuda a un compañero** (pero no copies su código)

---

## 🎓 ¡Listo para empezar!

Ya sabes cómo:
- ✅ Crear tu repositorio desde la plantilla
- ✅ Abrir un Codespace
- ✅ Editar el código
- ✅ Ejecutar las pruebas
- ✅ Hacer commit y push
- ✅ Ver tus resultados en GitHub

**¡Mucho éxito en el Taller 01!** 🚀
