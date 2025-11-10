# from MIS_CLASES.Unidad_2.A11_Patrones06Modulo import *
from A11_Patrones06Modulo import *


# Dimensiones de la ventana (para coordenadas de píxeles)
ANCHO_VENTANA = 800
ALTO_VENTANA = 600


class Enemigo:
    """Clase que representa a un enemigo en el juego."""
    def __init__(self, tipo, x, y):
        self.tipo = tipo        # Tipo de alien (1 o 2)
        self.raster_x = x       # Posición en X
        self.raster_y = y       # Posición en Y
        self.esta_vivo = True   # Estado del enemigo



class Nave:
    """Clase que representa la nave del jugador."""
    def __init__(self, vidas, x, y):
        self.num_vida = vidas   # Número de vidas
        self.raster_x = x       # Posición en X
        self.raster_y = y       # Posición en Y


class Bala:    
    """Clase que representa una bala disparada por la nave."""
    def __init__(self):
        self.disparado = False  # Estado del disparo
        self.pos_x = 0          # Posición en X
        self.pos_y = 0          # Posición en Y



class Juego:
    
    """Clase principal que maneja el ciclo de vida del juego."""
    
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.ventana = self._iniciar_ventana()
        self.jugador = None
        self.misiles = []
        self.enemigos = []
        
    def _iniciar_ventana(self):
        """ Inicializamos la ventana """

        if not glfw.init():
            raise Exception("No se pudo iniciar GLFW")
        ventana = glfw.create_window(self.ancho, self.alto, "Space Invaders POO", None, None)
        if not ventana:
            glfw.terminate()
            raise Exception("No se pudo crear la ventana")
        glfw.make_context_current(ventana)
        
        # Configurar la proyección para usar coordenadas de píxeles
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        # glOrtho(left, right, bottom, top, near, far)
        # Esto mapea [0, ancho] en "X",  [0, alto] en "Y"  y [lejos, cerca] en "Z"
        glOrtho(0.0, self.ancho, 0.0, self.alto, -1.0, 1.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        # Nota: glRasterPos2i() funciona en coordenadas de ventana, 
        # por lo que es esencial configurar la proyección a coordenadas de ventana.
        return ventana

    def configurar_juego(self):
        # ⚠️ AQUÍ inicializarás las instancias de tus clases (Jugador, Enemigos, etc.)
        pass 
    


    def dibujar_mapa_bits(self):
        """Función que usa glRasterPos2i() y glBitmap() para dibujar el patrón."""
        
        # 1. Establecer el color para los píxeles encendidos (donde el bit es 1)
        glColor3f(1.0, 1.0, 0.0)  # Amarillo

        # 2. Establecer la posición de trama (Raster Position) en coordenadas de ventana
        # En este caso, usaremos coordenadas de ventana (píxeles), no las coordenadas -1 a 1 de OpenGL.
        glRasterPos2i(10, 10) # El mapa de bits empezará a dibujarse en el pixel (100, 100)
        
        # 3. Dibujar el mapa de bits
        # Parámetros: width, height, xorig, yorig, xmove, ymove, bitmap_data
        glBitmap(32, 32, 0.0, 0.0, 0.0, 0.0, Alien01M01)

        # glColor3f(1.0, 0.0, 0.0)
        # glRasterPos2i(100, 100) # El mapa de bits empezará a dibujarse en el pixel (100, 100)
        # glBitmap( BITMAP_WIDTH, BITMAP_HEIGHT, 0.0, 0.0, 0.0, 0.0, letra_x)





    def bucle_principal(self):
        # ... (Tu lógica del juego) ...
        pass
        while not glfw.window_should_close(self.ventana):
            glClear(GL_COLOR_BUFFER_BIT)
            # Llama a la función de dibujo de mapa de bits
            self.dibujar_mapa_bits()
            glfw.swap_buffers(self.ventana)
            glfw.poll_events()
        




    def _limpiar(self):
        glfw.terminate()






if __name__ == "__main__":
    juego = Juego(ANCHO_VENTANA, ALTO_VENTANA)
    # juego.configurar_juego()
    juego.bucle_principal()




"""

Naves    MiNave;        // Se declara la nave que usaremos
int      QueCapaNave=1; // Para mostrar la animacion del fuego del motor

Bala     Disparo;       // Para controlar el disparo


Enemigos Aliens[20];    // Declaramos 20 aliens
int      NumeroDeVuelta=0;      // Permite dos recorridos a la misma altura
int      QueCaraAlien=1;        // Controla el patron a mostrar cada 5 incrementos cambia
int      X_VelocidadAlien=1;    // El desplazamiento de los aliens en X
int      Y_VelocidadAlien=4;    // El desplazamiento de los aliens en Y


void InicializaPersonales()             // Inicializamos todos los personajes
{ int x=0;
  int PosIniX=10;
  int PosIniY=70;

  for (x=0;x<20;x++)                    // Para los aliens
  { Aliens[x].EstaVivo=true;
    if(x<10) {  Aliens[x].QueAlien=1; } // 10 aliens fila 1 patron 1 y otros 10 patron 2
             else { Aliens[x].QueAlien=2; }
    Aliens[x].RasterEnX=PosIniX;
    Aliens[x].RasterEnY=PosIniY;
    PosIniX+=8;
    if (x==9) {PosIniX=10; PosIniY=85;}
  }
                                        // Para la nave
  MiNave.NumVida=3;
  MiNave.RasterEnX=48;
  MiNave.RasterEnY=3;
                                        // Para el disparo
  Disparo.Disparado=false;
}

void MuestraAliens()
{    glColor3f(0.0,1.0,0.0);    // Loas aliens son de color verde
     for(int x=0; x<20; x++)
       {  if (Aliens[x].EstaVivo)       // Si esta vivo lo muestra
             { glRasterPos2i(Aliens[x].RasterEnX, Aliens[x].RasterEnY);
               // Se manejan rangos de 5 en 5 para retardar la animacion de los aliens
               switch ( Aliens[x].QueAlien ) {
                     case 1: if (QueCaraAlien>=1 && QueCaraAlien<=5)
                                    glBitmap(32,32,0.0,0.0,0.0,0.0,Alien01M01);
                             if (QueCaraAlien>=6 && QueCaraAlien<=10)
                                    glBitmap(32,32,0.0,0.0,0.0,0.0,Alien01M02);
                             if (QueCaraAlien>=11 && QueCaraAlien<=15)
                                    glBitmap(32,32,0.0,0.0,0.0,0.0,Alien01M03);
                             break;
                     case 2: if (QueCaraAlien>=1 && QueCaraAlien<=5)
                                    glBitmap(32,32,0.0,0.0,0.0,0.0,Alien02M01);
                             if (QueCaraAlien>=6 && QueCaraAlien<=20)
                                    glBitmap(32,32,0.0,0.0,0.0,0.0,Alien02M02);
                             if (QueCaraAlien>=11 && QueCaraAlien<=15)
                                    glBitmap(32,32,0.0,0.0,0.0,0.0,Alien02M03);
                             break;
                    }
              }
         }
 }


   void miTemporizador(int value)      // Agregamos un temporizador que hara mas lenta la escena
{
    glutPostRedisplay();
    glutTimerFunc(100, miTemporizador, 0); // Llama a la función timer cada 50 milisegundos
}



 void MuestraNave()
 {  if (MiNave.NumVida>0)       // Si tiene vidas la muestra
         {
           glColor3f(1.0,1.0,0.0);  // Movimiento uno capa uno
           glRasterPos2i(MiNave.RasterEnX, MiNave.RasterEnY);
           glBitmap(32,32,0.0,0.0,0.0,0.0,NaveM1C1);

           glColor3f(1.0,1.0,1.0);  // Movimiento uno capa uno
           glRasterPos2i(MiNave.RasterEnX, MiNave.RasterEnY);
           glBitmap(32,32,0.0,0.0,0.0,0.0,NaveM1C2);

           glColor3f(1.0,0.0,0.0);  // Para la tercer capa que es la unica que cambia
           glRasterPos2i(MiNave.RasterEnX, MiNave.RasterEnY);
           if(QueCapaNave==1) { glBitmap(32,32,0.0,0.0,0.0,0.0,NaveM1C3); }
           if(QueCapaNave==2) { glBitmap(32,32,0.0,0.0,0.0,0.0,NaveM2C1); }
           if(QueCapaNave==3) { glBitmap(32,32,0.0,0.0,0.0,0.0,NaveM3C1); }
         }
}


void MuestraDisparo()   // Para mostrar el disparo
{   glColor3f(1.0,1.0,1.0);
    glBegin(GL_QUADS);
      glVertex2i(Disparo.PosX, Disparo.PosY);
      glVertex2i(Disparo.PosX+1, Disparo.PosY);
      glVertex2i(Disparo.PosX+1, Disparo.PosY+3);
      glVertex2i(Disparo.PosX, Disparo.PosY+3);
    glEnd();
}


void teclas_especiales( int key, int PosX, int PosY )
{ switch ( key )
         { case GLUT_KEY_LEFT:  MiNave.RasterEnX-=2;
                                if (MiNave.RasterEnX<=1) MiNave.RasterEnX=1;
                                break;
           case GLUT_KEY_RIGHT: MiNave.RasterEnX+=2;
                                if (MiNave.RasterEnX>=97) MiNave.RasterEnX=96;
                                break;
           case GLUT_KEY_F1:    Disparo.PosX=MiNave.RasterEnX+2;
                                Disparo.PosY=MiNave.RasterEnY+4;
                                Disparo.Disparado=true;
                                break;
	      }
}


void ChecaColisiones( )
{   // Aqui solo valida el disparo conttra cada alien
    // falta validar cuando los aliens llegan abajo y tocan la nave
    // y ademas falta crear que los aliens disparen pero eso les toca a ustedes
    if (Disparo.Disparado)
        { for(int x=0;x<20;x++)
             { if (Aliens[x].EstaVivo)
                  { if ( Disparo.PosX>=Aliens[x].RasterEnX &&
                         Disparo.PosX<=(Aliens[x].RasterEnX+3) &&
                         Disparo.PosY>=Aliens[x].RasterEnY &&
                         Disparo.PosY<=(Aliens[x].RasterEnY+3) )
                         { Aliens[x].EstaVivo=false;
                           Disparo.Disparado=false; }
                  }
             }
        }
}


void ControlaJuego(void)
{ glClear (GL_COLOR_BUFFER_BIT);
  MuestraAliens();
  MuestraNave();
  ChecaColisiones();

  if (Disparo.Disparado) { MuestraDisparo();
                           Disparo.PosY+=8;
                           if (Disparo.PosY>100) Disparo.Disparado=false;
                           }
  QueCapaNave++;
  QueCaraAlien++;

  if (QueCapaNave==4) QueCapaNave=1;
  if (QueCaraAlien>=16) QueCaraAlien=1;

  for(int x=0;x<20;x++) { Aliens[x].RasterEnX+=X_VelocidadAlien; }
  if (Aliens[0].RasterEnX<=1 || Aliens[19].RasterEnX>=94)
          { X_VelocidadAlien*=-1;
            NumeroDeVuelta++; }
  if (NumeroDeVuelta==3) { NumeroDeVuelta=0;
                           for(int x=0;x<20;x++) { Aliens[x].RasterEnY-=Y_VelocidadAlien; }
                           }
  glFlush();
}

int main(int argc, char *argv[])
{ glutInit(&argc, argv);
  glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB );
  glutInitWindowPosition (250, 60);
  glutInitWindowSize (800,600);
  glutCreateWindow ("Ejemplo Space Invaders con patrones y estructuras en OpenGL");
  Inicializa();
  InicializaPersonales();
  glutDisplayFunc(ControlaJuego);
  glutTimerFunc(50, miTemporizador, 0);
  glutSpecialFunc(teclas_especiales);
  glutMainLoop();
  system("PAUSE");
  return EXIT_SUCCESS; }

"""