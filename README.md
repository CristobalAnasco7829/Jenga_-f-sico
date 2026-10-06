# Jenga_-f-sico

Simulación interactiva del juego de Jenga desarrollada en **Python**. Combina un motor de físicas 2D (**Pymunk**) para calcular la dinámica y colisiones de los bloques, con un pipeline de renderizado 3D en **OpenGL** a través de **Pyglet** y una arquitectura de **Grafo de Escena (Scenegraph)**.

## Video ejemplo
Ejemplo en archivo Jenga.mp4

## Contexto Académico

* **Institución:** Universidad de Chile
* **Curso:** Modelación y computación gráfica para ingenieros
* **Propósito:** Proyecto individual 
* **Repositorio base:** [cc3501-computer-graphics][https://github.com/PLUMAS-research/cc3501-computer-graphics]
  

## Características Principales

* **Físicas en tiempo real:** Integración con Pymunk para simular la masa, fricción y gravedad de cada bloque al ser movido o apilado.
* **Renderizado 3D con Shaders:** Implementación de vertex y fragment shaders personalizados mediante OpenGL (GLSL) y Pyglet.
* **Estructura de Grafo de Escena:** Manejo jerárquico de transformaciones geométricas (traslación, rotación, escala) para actualizar la posición visual de los bloques a partir de sus cuerpos físicos.
* **Cámaras multicámara:** Cambio dinámico entre diferentes perspectivas.


## Aspectos interactivos

*| ENTER | Extrae un bloque aleatorio disponible y lo coloca en la cima de la torre. 
*| ESPACIO | Alterna la vista de la cámara a unas de las 3 vistas creadas. 
