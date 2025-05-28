DELITOS INFORMATICOS EN COLOMBIA (2006 - 2025)


Se realiza el siguiente DashBoard con el fin de consultar por (Años - Mes - Departamentos - Municipios - Delito Informaticos) respondiendo las siguientes preguntas: 

1. ¿Cuál ha sido la evolución anual de los delitos informáticos?
2. ¿Qué municipios presentan el mayor número de delitos informáticos?
3. ¿Cuál es la distribución mensual de los delitos informáticos a lo largo de los años?
4. ¿Qué tipo de conducta delictiva es la más común?
5. ¿Cómo ha cambiado la frecuencia de una conducta específica (por ejemplo, "ACCESO ABUSIVO A UN SISTEMA") a lo largo del tiempo?
6. ¿Qué municipio tiene el crecimiento más acelerado en delitos informáticos?
7. ¿Cuál fue el año con mayor número de delitos registrados en total?
8. ¿Cómo se distribuyen los delitos informáticos por municipio y tipo de conducta?

- Las cuales cuentan cada una con su grafico correspondiente para validar informacion puntual.

TECNOLOGIAS UTILIZADAS
![Presentación1_page-0001](https://github.com/user-attachments/assets/1dda18cd-12c0-4d6a-bab5-4bbae8eb261e)

CODIGO (FUNCIONALIDAD)
![{161DACC0-21FA-4EDE-A7B3-5E26D8A1058A}](https://github.com/user-attachments/assets/508d5921-ae68-4420-a8cc-db660d92d6c3)
- Realizamos el importe de las librerias (Python) correspondientes para que nos permita correr el Script sin problema
- utilizamos pn.extension('plotly') el cual Carga los recursos JavaScript y CSS necesarios para que los gráficos plotly funcionen en el navegador.
- Utilizamos df = pd.read_csv para leer la data (.csv) y trabajar a partir de lo que alli se aloje

![{56C54F66-717E-4D0B-8883-4365DF1139CF}](https://github.com/user-attachments/assets/bbfad355-e7dd-4ee9-bb68-9cda9272935a)
- Estas líneas de código están preparando la columna de fechas de nuestro DataFrame para que se pueda hacer análisis por año y mes, con el fin de poder hacer filtros mas puntuales


  ![{14E44B1F-2148-48D5-8A5B-C056EC4BC849}](https://github.com/user-attachments/assets/baaac386-167a-454b-9633-ebe000b7fb58)
- Definimos nuestros filtros de acuerdo a las preguntas formuladas 

PASO A PASO PARA CARGUE Y PREPARACION EN LA NUBE
1.	Creación de Instancia en AWS
- Asignamos nombre y elegimos el sistema operativo a utilizar

  ![imagen](https://github.com/user-attachments/assets/be405f58-3270-4782-92e3-ab42d15e2a90)
- Creamos la clave de Acceso para permitir la conexión

  ![imagen](https://github.com/user-attachments/assets/95222e64-30ba-47fe-8ba5-c068ed9ab19d)

- Esto nos genera un archivo .pem el cual nos permite realizar la conexión.
- Ejecutamos el comando 
ssh -i "C:\Users\stive\Downloads\Clave5.pem" ubuntu@18.188.235.203 ---> para permitir la conexión a la Instancia creada anteriormente.

  ![{C20429D5-F2C7-4222-9C0D-D47525D148B3}](https://github.com/user-attachments/assets/b3b1e3ce-6f95-4bb9-9348-21b15347574c)
  
2. Instalacion de Librerias correspondientes (pandas --- plotly --- panel)

   ![imagen](https://github.com/user-attachments/assets/41e08a88-f9c9-4105-a532-b73497973a7c)

3. Entorno Virtual (Creacion y Clonacion del repositorio) GIT BASH
- Realizamos la creacion del entorno virtual y posteriormente clonamos el repositorioa para alojar nuestros archivos, esto con el fin de dejar todo en un mismo entorno.
- Hacemos el cargue de los archivos (Archivo.py - Archivo.csv)
   ![{8425D374-6909-4011-8EE8-4339FD9C64FE}](https://github.com/user-attachments/assets/1242dd06-84b5-4dae-8fed-77e34fdb88ad)

- Validamos el funcionamiento el local, tanto visual como funcionamiento logico, una vez confirmado, procedemos a realizar el cargue a la Instancia

- ![imagen](https://github.com/user-attachments/assets/bedfbdf8-712c-4ab3-84ca-b01942831153)


4. Instancia AWS (Puertos - Configuracion de Seguridad)
- para permitir la conexion, AWS (Instancia creada) nos brinda un puerto por defecto, el cual utilizaremos si nos lo permite sin problema, si no debemos configurar (reglas de entrada) para permitir
  conexiones de puertos (Security Group en AWS)

- ![{D55FCE6A-3498-43BC-A58F-7EAA609F259D}](https://github.com/user-attachments/assets/dffe0a5a-97f8-4639-b03f-d1b3af4f3551) Configuracion de Regla de tipo: TCP ---> PUERTO 8000 ---> Con Origen 0.0.0.0/0
  nos pemritira conexiones de cualquier IP (NO RECOMENDADO POR BAJA SEGURIDAD)

5. Puesta en Marcha (venv) ubuntu@ip-172-31-13-106:~/dashboard-plotly$ python dashboard_interactivo_plotly.py
  python dashboard_interactivo_plotly.py
el siguiente comando nos permite ejecutar el Script, el cual nos habilitara una direccion IP en este caso generada para visualizar el contenido

![imagen](https://github.com/user-attachments/assets/e6694e76-ed75-4eb2-bbaf-630c21306651)
![imagen](https://github.com/user-attachments/assets/6cd6c660-2d25-4a0d-9d1b-4537e9eb9cfe)

- podemos visualizar que el DashBoard se visualiza de manera correcta y funcional, al aplicar filtros

6. Pruebas
- Se realiza test en 6 Dispositivos al tiempo (2 PC + 4 Moviles) para visualizar si los cambios se evidencian, el comportaminento de las graficas, de los filtros y demas (se Anexan evidencias)

  
![imagen](https://github.com/user-attachments/assets/ef2d35a8-188e-4744-95f0-78a9d1da23ad)
![imagen](https://github.com/user-attachments/assets/d833baa3-2540-4b72-bf10-3414c0594a81)
![imagen](https://github.com/user-attachments/assets/38c8cff4-dae4-4a0f-abda-a89a7890051b)
![imagen](https://github.com/user-attachments/assets/b8e47d2c-0d05-4227-b80b-87931cf5c29d)
![imagen](https://github.com/user-attachments/assets/de1dab82-0758-4268-9f26-1304cae56222)

No se evidencian errores, el comportamiento es optimo. 
URL: http://18.188.235.203:8000/







 

  

  
