# Recopets

Este proyecto consiste en una aplicación web diseñada como parte del trabajo final de la asignatura de Tecnologías Multimedia e Interacción. La aplicación tiene como objetivo principal reconocer animales a través de imágenes subidas por el usuario.

### Características principales

- **Reconocimiento de animales**: Utilizando AWS Rekognition, la aplicación puede identificar el animal presente en una imagen subida por el usuario.
  
- **Descripciones de animales**: Una vez reconocido el animal, la aplicación proporciona una breve descripción extraída de Wikipedia mediante su API.

- **Sistema de inicio de sesión**: La aplicación ofrece un sistema de inicio de sesión basado en reconocimiento facial. Los usuarios deben registrarse previamente, realizandose una fotografía para su identificación.

- **Historial de reconocimiento**: Se mantiene un historial de los últimos animales reconocidos por cada usuario.

### Tecnologías utilizadas

- **AWS Rekognition**: Se emplea este servicio de Amazon Web Services para el reconocimiento de imágenes y reconocimento facial.
  
- **API de Wikipedia**: Para obtener las descripciones de los animales reconocidos.
  
- **Base de datos**: Se utiliza una mini base de datos (JSON) para almacenar la información de los usuarios y su historial de reconocimiento.
  
- **Tecnologías web**: El proyecto está desarrollado utilizando tecnologías web estándar como HTML, CSS, JavaScript, y posiblemente un framework como React o Angular para la interfaz de usuario.

### Uso

Para utilizar la aplicación, los usuarios deben registrarse previamente proporcionando una fotografía para su identificación facial. Una vez registrados, pueden subir imágenes de animales para ser reconocidos y obtener información sobre ellos.


### Licencia

Este proyecto se proporciona bajo la licencia [MIT](LICENSE).
