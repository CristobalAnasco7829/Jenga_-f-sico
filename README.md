# Jenga_-f-sico

Interactive Jenga game simulation developed in **Python**. Combines a 2D physics engine (**Pymunk**) to calculate block dynamics and collisions, with a 3D rendering pipeline in **OpenGL** via **Pyglet** and a **Scene Graph (Scenegraph)** architecture.
##
Simulación interactiva del juego de Jenga desarrollada en **Python**. Combina un motor de físicas 2D (**Pymunk**) para calcular la dinámica y colisiones de los bloques, con un pipeline de renderizado 3D en **OpenGL** a través de **Pyglet** y una arquitectura de **Grafo de Escena (Scenegraph)**.

## Video Example
Demonstration in `Jenga.mp4` file.
## 
Ejemplo en archivo Jenga.mp4

## Academic Context

* **Institution:** Universidad de Chile
* **Course:** Modeling and Computer Graphics for Engineers
* **Purpose:** Individual project 
* **Base Repository:** [cc3501-computer-graphics](https://github.com/PLUMAS-research/cc3501-computer-graphics)
##
* **Institución:** Universidad de Chile
* **Curso:** Modelación y computación gráfica para ingenieros
* **Propósito:** Proyecto individual 
* **Repositorio base:** [cc3501-computer-graphics][https://github.com/PLUMAS-research/cc3501-computer-graphics]

## Key Features

* **Real-time Physics:** Integration with Pymunk to simulate mass, friction, and gravity for each block as it is moved or stacked.
* **3D Shader-Based Rendering:** Implementation of custom vertex and fragment shaders using OpenGL (GLSL) and Pyglet.
* **Scene Graph Structure:** Hierarchical management of geometric transformations (translation, rotation, scale) to update the visual position of the blocks based on their physical bodies.
* **Multi-Camera Views:** Dynamic switching between different perspectives.
## 
* **Físicas en tiempo real:** Integración con Pymunk para simular la masa, fricción y gravedad de cada bloque al ser movido o apilado.
* **Renderizado 3D con Shaders:** Implementación de vertex y fragment shaders personalizados mediante OpenGL (GLSL) y Pyglet.
* **Estructura de Grafo de Escena:** Manejo jerárquico de transformaciones geométricas (traslación, rotación, escala) para actualizar la posición visual de los bloques a partir de sus cuerpos físicos.
* **Cámaras multicámara:** Cambio dinámico entre diferentes perspectivas.
  
## Interactive Features
| ENTER | Extracts a random available block and places it at the top of the tower. 
| SPACE | Toggles the camera view between the 3 created perspectives. 
## 
*| ENTER | Extrae un bloque aleatorio disponible y lo coloca en la cima de la torre. 
*| ESPACIO | Alterna la vista de la cámara a unas de las 3 vistas creadas. 
