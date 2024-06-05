---
layout: page
#menubar: docs_menu
title: Descripción Avanzada
subtitle: Descripción mas detallada de este módulo
show_sidebar: false
hero_height: is-fullwidth
---

>La aplicación tiene que gestionar todos los datos necesarios para llevar a buen termino un proceso de recogida y transporte de mercancias de un punto **A** a un punto **B** registrando todos los documentos necesarios para la toma de decisiones de cada departamento de la empresa y para que el conductor pueda en un momento dado consultar los datos imprescindibles para poder realizar su trabajo correctamente.

#### Tenemos tres procesos diferenciados y complementarios

  * Orden de trabajo
  * Parte de trabajo 
  * Viajes

#### **Orden de trabajo**

###### La orden de trabajo se obtiene de una aplicación externa mediante una archivo XML que tiene la siguiente estructura

```      
        <Transporte>
        <Cliente>
            <Nombre>María García</Nombre> <!-- [45C] -->
            <Codigo>CLT123456</Codigo> <!-- [45C] -->
            <Telefono>+34 660 453 275</Telefono> <!-- [15C] -->
            <Email>maria.garcia@example.com</Email> <!-- [45C] -->
        </Cliente>
        <Origen>
            <NombreContacto>Juan Pérez</NombreContacto> <!-- [45C] -->
            <Telefono1ContactoOrigen>+34 612 345 678</Telefono1ContactoOrigen> <!-- [15C] -->
            <Telefono2ContactoOrigen>+34 631 456 789</Telefono2ContactoOrigen> <!-- [15C] -->
            <DireccionRecogida>Calle Mayor 12, Madrid, España</DireccionRecogida> <!-- [45C] -->
            <FechaRecogida>2024-06-10</FechaRecogida> <!-- [12C] -->
            <HoraRecogida>08:30</HoraRecogida> <!-- [12C] -->
            <UnidadesCarga>10</UnidadesCarga> <!-- [10C] -->
            <TipoCarga>General</TipoCarga> <!-- [45C] -->
            <Observaciones>Ninguna</Observaciones> <!-- [45C] -->
        </Origen>
        <Destino>
            <NombreContacto>Luis Fernández</NombreContacto> <!-- [45C] -->
            <Telefono1ContactoDestino>+34 623 123 456</Telefono1ContactoDestino> <!-- [15C] -->
            <Telefono2ContactoDestino>+34 635 654 320</Telefono2ContactoDestino> <!-- [15C] -->
            <DireccionDescarga>Avenida de la Constitución 50, Barcelona, España</DireccionDescarga> <!-- [45C] -->
            <FechaDescarga>2024-06-11</FechaDescarga> <!-- [12C] -->
            <HoraDescarga>14:00</HoraDescarga> <!-- [12C] -->
        </Destino>
        </Transporte>
``` 

EL programa comprueba los datos que aparecen en el documento XML si el cliente de la orden no existe, el departamento de transporte recibirá un correo para advertir de la incidencia, y la orden no se procesará.

  >La base de datos donde se creará un registro es: **Ordentrabajo**.  
   La base de datos a la que se accede para comprobar datos es: **Cliente**.

El procedimiento que se realiza internamente para almacenar el archivo XML se representa en el diagrama de flujo del proceso de carga del fichero XML.

<p class="content">
  Para más detalles sobre el proceso, consulta la documentación completa en el siguiente 
  <a href="./procesoxml">[enlace]</a>.
</p>

Para acceder a la ventana de datos en la aplicación hay que seleccionar en el menú La primera pestaña que tiene como título **ORDEN DE TRABAJO**. Introduciendo el numero de orden en la cabecera del menú se accede al contenido de la orden. En esa ventana los usuarios de la aplicación que no son administradores pueden consultar los datos específicos de origen y destino de la orden de trabajo desplazándose por las pestañas de **ORIGEN** y **DESTINO**. El botón **ACTUALIZAR** permite recargar los datos de la orden.

Los administradores pueden modificar e incluso borrar la orden. Cualquier modificación o eliminación se quedará registrada en un fichero log. Se almacenará tanto el usuario que ha realizado la acción como la hora en la que se ha realizado y lo que se ha modificado o borrado. Se creará una función dedicada a registrar esas acciones.

Modificar o borrar una orden de trabajo obliga seguir un protocolo específico de rectificación de todos los elementos que intervienen en la orden.

>##### **Pasos a seguir para eliminar una orden de trabajo**

    1º Se guarda una copia de toda la orden de trabajo en el log.  
    2º Buscar orden en partes de trabajo.  
    3º Si en el punto 2º encontramos un parte de trabajo asociado a la orden, debemos avisar con un mensaje emergente.
    4º Iniciar el procedimiento de borrado de parte de trabajo tal como se indica al final de la siguiente sección Parte de trabajo.
    5º Se cambia el estado de la orden a "PENDIENTE".

#### **Parte de trabajo**

Una vez se ha creado una orden, se pone en marcha el proceso de parte de trabajo.
El procedimiento que genera el parte de trabajo sigue el algoritmo del diagrama de flujo del "proceso de busqueda de camión, conductor y preparación parte de trabajo" que se puede acceder desde el menú de este documento opción Documentación submenú Genera parte de trabajo.

<p class="content">
  Para más detalles sobre el proceso, consulta el diagrama de flujo en el siguiente 
  <a href="./partetrabajo">[enlace]</a>.
</p>


El programa una vez tiene una orden de trabajo validada, genera el parte de trabajo, utilizando las siguientes bases de datos:

>La base de datos donde se creará un registro es: **partedetrabajo**.  
 Las bases de datos a las que se accede para comprobar datos son:
   **Ordentrabajo**, **Camion** y **Conductor**  
 Las bases de datos donde se crean nuevos registros son:
        **datosviaje** y **docviaje**

Una vez se ha generado un registro en la base de datos **partedetrabajo** se envía un correo al departamento de transporte avisando que se ha creado un nuevo parte de trabajo y se aporta en el mensaje el **idparte** y el **iddatosviaje** que identifican el parte de trabajo y los datos asociados al viaje.

Para acceder a la ventana de datos en la aplicación hay que seleccionar en el menú La segunda pestaña que tiene como título **PARTE DE TRABAJO**. Introduciendo el numero de parte de trabajo en la cabecera del menú se accede a su contenido. En esa ventana los usuarios de la aplicación que no son administradores pueden consultar los datos específicos de origen y destino desplazándose por las pestañas de **ORIGEN** y **DESTINO**. El botón **ACTUALIZAR** permite recargar los datos.

Los administradores pueden modificar e incluso borrar el parte de trabajo. Cualquier modificación o eliminación se quedará registrada en un fichero log. Se almacenará tanto el usuario que ha realizado la acción como la hora en la que se ha realizado y lo que se ha modificado o borrado. Se creará una función dedicada a registrar esas acciones.

Modificar o borrar un parte de trabajo obliga seguir un protocolo específico de rectificación de todos los elementos que intervienen en ese parte de trabajo.

>##### **Pasos a seguir para eliminar un parte de trabajo**

    1º Se guarda una copia de todo el parte de trabajo en el log. Usuario y fecha_hora.
    2º Cambiamos los estados de los registros del camión y del conductor a "LIBRE".
    3º Se cambia el estado de la orden a "PENDIENTE"

#### **Viajes**