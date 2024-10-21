# SEMANA TEC - OPEN AI

## Nombre: Eduardo Porto A01027893

### Documentación - Avance 21 de Octubre

1. **Registro y API Key**
   - Comenzamos registrándonos y logueándonos en la página de OpenAI, donde obtuvimos nuestra API Key.

2. **Configuración del Entorno**
   - Creamos un archivo `.env` para almacenar de manera segura nuestra API Key.
   - Generamos un archivo `.gitignore` para ignorar el archivo `.env` y proteger nuestra información sensible.

3. **Prueba de Conexión**
   - Desarrollamos un script llamado `basicopenai.py` para probar la conexión con la API.
   - Debido a que no teníamos saldo en nuestra cuenta, tuvimos que esperar a que el profesor nos proporcionara crédito, lo cual nos permitió continuar.
   - Ejecutamos el script y recibimos una respuesta exitosa de la API.
   ![Respuesta de la API](public/apiresponse.png)

4. **Implementación en Azure**
   - Accedimos a Azure para crear una Function App.
   - Obtuvimos una suscripción de Azure para estudiantes y configuramos correctamente la Function App, con la ayuda del profesor.
   - Una vez activo el servicio, instalamos la extensión de Azure y sincronizamos nuestra cuenta con el proyecto, lo que nos permitió desplegar la Function App, generando un nuevo archivo `function_app.py`.

5. **Depuración del Script**
   - Al depurar el script `function_app.py`, logramos obtener una respuesta de la función.
   ![Respuesta de la API](public/azure-debuger.png)

6. **Ejecución Exitosa**
   - Al ejecutar la función HTTP triggered, se solicitó un nombre en el cuerpo de la solicitud, y la API respondió con un saludo personalizado.
   ![Respuesta de la API](public/http-trigger.png)

7. **Interfaz en VSCode**
   - Finalmente, en VSCode se desplegó una pestaña que muestra el saludo personalizado con el nombre proporcionado en el cuerpo de la solicitud, lo que se puede ver en el Run Commander de la interfaz.
   ![Respuesta de la API](public/firstfunctionapi.png)
