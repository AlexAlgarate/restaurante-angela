# Restaurante Ostras Nin

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.3+-5646ED?style=for-the-badge&logo=reflex&logoColor=white&labelColor=101010)](https://reflex.dev)


## Proyecto web con Python para hacer el frontend de la página de mantenimiento del Restaurante Ostras Nin

![Picture of the bride and groom.](/assets/images/imagen_web_ostras_nin.jpg)

## Proyecto

Mientras terminan de desarrollar la página web final de *[Ostras Nin](https://ostrasnin.com/)*, he desarrollado su página de mantenimiento con Reflex. Reflex es un framework que usa Python y está enfocado en desarrollo web. Usa componentes de *[Radix](https://www.radix-ui.com/)*, a los cuales les puedes añadir cualquier propiedad *[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)*.

Estas son algunas de las cosas tan increíbles que se pueden hacer con Reflex con muy pocas líneas de código:

<a href="https://ostrasnin.com/"><img src="/assets/images_readme/pantalla_principal.png" alt="Imagen de la web en versión escritorio" style="height: 55%; width:100%;"/></a>

También se pueden hacer vistas responsive para tablet o móvil (iPhone SE):

<a href="https://ostrasnin.com/"><img src="/assets/images_readme/responsive_view.png" alt="Imagen de la web responsive en modo móvil Iphone SE" style="height: 100%; width:60%;"/></a>

## Cómo lanzar el proyecto

Para lanzar el proyecto, puedes seguir la introducción de *[Reflex](https://reflex.dev/docs/getting-started/installation/)* o seguir estos pasos:

### 1. Crea la carpeta del proyecto

```cmd
mkdir my_app_name
cd my_app_name
```

### 2. Crea el entorno virtual dependiendo de tu sistema operativo

Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```python
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instala Reflex

```python
pip install reflex
```

### 4. Inicializa el proyecto

```cmd
reflex init
```

### 5. Lanza la web en local

```cmd
reflex run
```

<a href="https://boda-vicky-alex.vercel.app/#confirmation_section"><img src="/assets/images_readme/reflex_run.webp" alt="Reflex run command in CMD" style="height: 75%; width:100%;"/></a>

El proyecto está desplegado en *[Vercel](https://vercel.com/)*, pero puedes usar el servicio de despliegue de Reflex (*[aquí puedes ver la documentación](https://reflex.dev/docs/hosting/self-hosting/#exporting-a-static-build)*).
En este caso, el proceso de despliegue está automatizado con una Github Action siguiendo las instrucciones de exportación del frontend de la documentación de Reflex. 

```sh
python -m pip install --upgrade pip
pip install -r requirements.txt
rm -fr public
isort restaurante_ostras_nin/
black restaurante_ostras_nin/
reflex init
reflex export --frontend-only
unzip frontend.zip -d public
rm -f frontend.zip
```

Si quisieras añadir estados y backend a la aplicación, tendrías que revisar este punto, ya que Vercel "no se lleva bien" con el código Python. La alternativa en este caso es usar *[Railway](https://railway.app/)*) para desplegar esta parte de la aplicación

### 💻 [Accede al código del proyecto](./restaurante_ostras_nin)

