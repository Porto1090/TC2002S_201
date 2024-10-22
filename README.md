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

### Documentación - Avance 22 de Octubre

1. **Despliegue en Azure**
   - Desplegamos la Function App en Azure, lo que nos permitió obtener una URL para acceder a la función.
   ![Página deploy de Azure](public/deploy-functionapi.png)


   - La URL generada fue la función firstfunctionapi donde la master host key URL es:
   - `https://eduardo-porto.azurewebsites.net/api/firstfunctionapi?`
   ![UrlDeployedAzure](public/deployed-url.png)

2. **Utilizar completionAPI**
   - Creamos una nueva función llamada `completionApi` que utiliza la API de OpenAI para que te conteste un prompt.
   - Si contamos con una API Key válida, podemos hacer uso de la función para obtener una respuesta de la API.
   - Por medio de un req.body en formato:
   ```json
   {  
      "model": "gpt-3.5-turbo", 
      "prompt": "Dame los primeros 10 números de la serie de Fibonacci", 
      "max_tokens": 100, 
      "temperature": 1 
   }
   ``` 
   - La API responderá con los primeros 10 números de la serie de Fibonacci.
   ![Respuesta de la API](public/completionapi.png)

3. **Utilizar imageAPI**
   - Creamos una nueva función llamada `imageApi` que utiliza la API de OpenAI para generar una imagen.
   - Si contamos con una API Key válida, podemos hacer uso de la función para obtener una imagen de la API.
   - Ya que no está aún desplagada en Azure, debemos usar un consumidor de API como ThunderClient para probarla.
   - Por medio de un req.body en formato:
   ```json
   {  
      "prompt": "Un paisaje de una noche estrellada"
   }
   ``` 
   - La API responderá con el url de una imagen siguiendo el prompt de una noche estrellada.
   ![Respuesta de la API](public/imageapi.png)


> [!NOTE]
> Por temas de configuración estuve más de lo previsto en la implementación, una vez que ya había acabado todo, la llave del profesor se había eliminado, por lo que no pude consumirla y no tengo evidencia de que mande un resultado, pero si se puede ver que la función está bien implementada y que se puede consumir.

