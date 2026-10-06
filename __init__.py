import os.path
import numpy as np
import pyglet
import pyglet.gl as GL
from pathlib import Path
import grafica.transformations as tr
from grafica.scenegraph import Scenegraph
import random
import pymunk

vertex_source = """#version 330 core
in vec3 position;

uniform mat4 transform;
uniform mat4 view;
uniform mat4 projection;

void main() {
gl_Position = projection * view * transform * vec4(position, 1.0);

}
"""

fragment_source = """#version 330 core
uniform vec3 color;
out vec4 fragColor;

void main() {
fragColor = vec4(color, 1.0);
}

"""
pose_actual=0
posiciones_jenga={}
bloques_fisicos=[]
bloques_disponibles=[]
conteo=1          
conteoaltura=1    
view_matrix=None  
projection_matrix=None 

def tarea():

 global bloques_fisicos
 global bloques_disponibles
 global posiciones_jenga
 global gpu_data


 window=pyglet.window.Window(width=800,height=800)
 vert_shader=pyglet.graphics.shader.Shader(vertex_source,"vertex")
 frag_shader=pyglet.graphics.shader.Shader(fragment_source,"fragment")
 pipeline=pyglet.graphics.shader.ShaderProgram(vert_shader,frag_shader)


 grafo=Scenegraph("personaje")
 grafo.load_and_register_mesh('cube',"assets/cube.off",fix_normals=True)
 grafo.register_pipeline("basic_pipeline",pipeline)




 espacio=pymunk.Space()
 espacio.gravity=(0,-9.8)

 suelo=pymunk.Body(body_type=pymunk.Body.STATIC)
 suelo.position=(0,0)

 suelo_=pymunk.Segment(suelo,(-50, 0.0),(50, 0.0),0.5)
 suelo_.friction=0.9
 espacio.add(suelo,suelo_)



 num_pisos=10
 bloques_por_piso=3
 colores=[np.array([1,0.65,0.45],dtype=np.float32),np.array([0.65,0.45,1],dtype=np.float32),]


 for piso in range(num_pisos):
    for b in range(bloques_por_piso):
        id_=f"piso_{piso}_bloque_{b}"
        pos=f"pos_{id_}"
        rot=f"rot_{id_}"
        scale=f"scale_{id_}" 
        mesh=f"mesh_{id_}" 

        color=colores[piso%2]

        grafo.add_mesh_instance(mesh,"cube","basic_pipeline",color=color)
        grafo.add_transform(scale,tr.scale(1.5,1.5,6))


        grafo.add_edge("personaje",pos)  
        grafo.add_edge(pos,rot)  
        grafo.add_edge(rot,scale)  
        grafo.add_edge(scale,mesh)

        body=pymunk.Body(body_type=pymunk.Body.DYNAMIC)
        y_f=1+2*piso*(99/100)


        if piso%2==0:
            x_f=0
            if b == 1: 
                x_f=-2.25
            elif b== 2: 
                x_f=2.25
            z_0=0


            forma=pymunk.Poly.create_box(body,(2.25,1.98))
            
        else:
            x_f=0
            z_0=0
            if b==1:
                z_0=2.25
            elif b==2: 
                z_0=-2.25


            forma=pymunk.Poly.create_box(body,(6.75,1.98))
            forma.filter=pymunk.ShapeFilter(group=piso+1)

        body.position=(x_f,y_f)
        forma.friction=0.6
        forma.mass=1.0
        
        espacio.add(body,forma)
        
        bloques_fisicos.append({"piso_original":piso,"piso_actual":piso,"b":b,"body":body,"shape":forma,"pos":pos,"rot":rot,"z_original":z_0,"movido":False,"conteo_en_cima":0})

        if piso<9:
            bloques_disponibles.append((piso,b))
  

 pose_actual=0
 gpu_data=grafo

 conteo=1
 conteoaltura=1


 def Move_():
    global conteo
    global conteoaltura
    global bloques_disponibles

    if not bloques_disponibles:
        return 

    ran=random.randint(0,len(bloques_disponibles)-1)
    altura,a_b_c=bloques_disponibles.pop(ran)

    
    actual=None
    for blk in bloques_fisicos:
        if blk["piso_actual"]==altura and blk["b"]==a_b_c:
            actual=blk
            break
            
    cu=actual["body"]
    nuevo_piso=9+conteoaltura
    
    nueva_y=4.0+2.0*nuevo_piso 
    
    cu.velocity=(0,0)
    cu.angular_velocity=0
    cu.angle=0
    
    actual["piso_actual"]=nuevo_piso
    actual["movido"]=True
    actual["conteo_en_cima"]=conteo

    
    if nuevo_piso%2==0:
        if conteo%3==0:
            x_f=0
            conteo=1
            conteoaltura+= 1
        elif conteo==2:
            x_f=-2.25
            conteo+=1
        else:
            x_f=2.25
            conteo+=1
            
        cu.position=(x_f,nueva_y)
        
        espacio.remove(actual["shape"])
        n_forma=pymunk.Poly.create_box(cu, (2.25, 1.98))
        n_forma.mass=1.0  
        n_forma.friction=0.6
        espacio.add(n_forma)
        actual["shape"]=n_forma
    else:
        x_f=0
        if conteo%3==0:
            conteo=1
            conteoaltura+=1
        elif conteo==2:
            conteo+=1
        else:
            conteo+=1
            
        cu.position=(x_f,nueva_y)
        
        espacio.remove(actual["shape"])
        n_forma=pymunk.Poly.create_box(cu,(6.75,1.98))
        n_forma.mass=1.0  
        n_forma.filter=pymunk.ShapeFilter(group=nuevo_piso + 1)
        n_forma.friction=0.6
        espacio.add(n_forma)
        actual["shape"]=n_forma


    
 def update(dt):
     for k in range(3):
        espacio.step(1/180.0)
    
     for blk in bloques_fisicos:
        x, y=blk["body"].position
        angulo=blk["body"].angle
        
        if blk["movido"]:
            piso_cima=blk["piso_actual"]
            c=blk["conteo_en_cima"]
            
            if piso_cima%2==0:
                grafo.add_transform(blk["pos"], tr.translate(x,y,0))
                grafo.add_transform(blk["rot"], tr.rotationZ(angulo))
            else:
                z_cima=0
                if c==2: 
                    z_cima=-2.25
                elif c==1: 
                    z_cima=2.25
                
                grafo.add_transform(blk["pos"], tr.translate(x,y,z_cima))
                grafo.add_transform(blk["rot"], tr.matmul([tr.rotationZ(angulo),tr.rotationY(np.pi/2)]))
                
        else:
            if blk["piso_original"] % 2 == 0:
                grafo.add_transform(blk["pos"],tr.translate(x,y,0))
                grafo.add_transform(blk["rot"],tr.rotationZ(angulo))
            else:
                grafo.add_transform(blk["pos"],tr.translate(x,y,blk["z_original"]))
                grafo.add_transform(blk["rot"],tr.matmul([tr.rotationZ(angulo),tr.rotationY(np.pi/2)]))

 pyglet.clock.schedule_interval(update,1/60.0)


 def actualizar_pose_gpu(): 
    global pose_actual
    global view_matrix
    global projection_matrix

    if pose_actual==0:

        view_matrix=tr.lookAt(np.array([0.0,13.0, 20.0]),np.array([0.0,13,0.0]),np.array([0.0,1.0,0.0]))
        projection_matrix=tr.perspective(90,window.aspect_ratio,0.1,100.0)


    elif pose_actual==1:

        view_matrix=tr.lookAt(np.array([-20,25,20]),np.array([0,7,0]),np.array([0.0,1.0,0.0]))
        projection_matrix=tr.perspective(75,window.aspect_ratio,0.1,100.0)

       
    elif pose_actual==2:

        view_matrix=tr.lookAt(np.array([0.0,40,0.0]),np.array([0.0,0.0,0.0]),np.array([0.0,0.0,1.0]))
        projection_matrix=tr.perspective(90,window.aspect_ratio,0.1,100.0)


 actualizar_pose_gpu()



 @window.event
 def on_key_press(symbol,modifiers):
    global pose_actual
    if symbol==pyglet.window.key.SPACE:
        pose_actual=(pose_actual+1)%3
        actualizar_pose_gpu()
    if symbol==pyglet.window.key.ENTER:
        Move_()




 @window.event
 def on_draw():
    GL.glClearColor(0.2, 0.2, 0.2, 1.0)
    window.clear()
    GL.glEnable(GL.GL_DEPTH_TEST)

    if gpu_data is not None:
        gpu_data.register_view_transform(view_matrix)
        gpu_data.set_global_attributes(projection=projection_matrix)
        gpu_data.render()

 pyglet.app.run()

