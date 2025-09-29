# Extractor de Texto de PDF con Streamlit y Firebase

Esta es una aplicación web simple construida con Streamlit que permite a los usuarios extraer texto de archivos PDF. La aplicación cuenta con autenticación de usuarios y almacena el historial de extracciones utilizando Firebase.

## Características

- **Autenticación de Usuarios:** Sistema completo de registro e inicio de sesión a través de Firebase Authentication.
- **Extracción de Texto de PDF:** Sube archivos PDF y extrae su contenido de texto utilizando la librería `PyPDF2`.
- **Historial de Extracciones:** Guarda un registro de todos los textos extraídos por cada usuario en una base de datos Firestore.
- **Descarga de Texto:** Permite descargar el texto extraído en un archivo `.txt`.
- **Interfaz Reactiva:** Construida con Streamlit para una experiencia de usuario fluida y sencilla.

## Cómo Empezar

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### Prerrequisitos

- Python 3.7 o superior.
- Una cuenta de Firebase para configurar la autenticación y la base de datos.

### 1. Clona el Repositorio

```bash
git clone <URL-del-repositorio>
cd <nombre-del-directorio>
```

### 2. Crea un Entorno Virtual (Recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

### 3. Instala las Dependencias

El archivo `requirements.txt` contiene todas las librerías necesarias.

```bash
pip install -r requirements.txt
```

### 4. Configura las Credenciales de Firebase

1.  Ve a la consola de tu proyecto de Firebase.
2.  Navega a **Configuración del proyecto** > **Cuentas de servicio**.
3.  Haz clic en **"Generar nueva clave privada"** y descarga el archivo JSON.
4.  Renombra el archivo descargado a `firebase_credentials.json` y colócalo en la raíz del directorio del proyecto.

**Importante:** Asegúrate de que el archivo `firebase_credentials.json` esté incluido en tu `.gitignore` para no exponer tus credenciales.

### 5. Ejecuta la Aplicación

Una vez que las dependencias y las credenciales estén configuradas, puedes iniciar la aplicación Streamlit con el siguiente comando:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web.

## Estructura del Proyecto

```
.
├── .gitignore
├── app.py                 # Lógica principal de la aplicación Streamlit
├── requirements.txt       # Dependencias de Python
├── firebase_credentials.json # (No versionado) Credenciales de Firebase
└── README.md
```
