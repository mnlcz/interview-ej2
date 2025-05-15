# Ejercicio 2

## Enunciado

Se necesita obtener del siguiente [link](http://b2b.sif.com.ar/Servicios/Aplicaciones/Cotizacion/CotizacionesList.asp)
una lista de cotizaciones, las cuales se deberán actualizar a diario y mantener un histórico de los valores obtenidos.

## Diagramas

- Los diagramas de clase y proceso los realicé mediante [drawio](https://www.drawio.com) y pueden ser visualizados en
  dicha página (son archivos `.drawio`).
- El diagrama de secuencia lo realicé mediante [sequencediagram](https://sequencediagram.org) y debe ser interpretado
  por dicha página (es un archivo `.txt`).

## Recurso a consumir

Los datos de las cotizaciones, como se dijo previamente, se obtienen consultando el sitio. El mismo provee un campo
para especificar la fecha en la que se quiere consultar.

### Apartado técnico

Haciéndo una request `GET` al recurso se obtienen las cotizaciones para la fecha actual. La respuesta está en formato
html, y la información relevante se encuentra en una tabla, puntualmente en una sección de XML.

Mediante cualquier lenguaje de programación moderno es muy sencillo tomar esa respuesta devuelta por el sitio y parsear
la información relevante. A su vez, si en vez de una `GET` request, se hace `POST` (enviando como payload una fecha),
se puede obtener el listado para dicha fecha en particular.

Con la información ya parseada basta con armar un sistema alrededor de dicha funcionalidad, de manera que la información
de X fecha persista, tal como indica el enunciado.

#### Clases

- `Divisa`: entidad individual correspondiente a 1 fila de la tabla.
- `Cotizaciones`: consiste en una fecha y un listado de `Divisa`. Mapea 1 a 1 con lo parseado del recurso.
- `Gestor`: clase abstracta en la que se parsea el recurso web, devolviendo un objeto `Cotizaciones`.
- `Sistema`: contiene el histórico (una lista de `Cotizaciones`).

#### Lógica de parseo

Opté por utilizar Python como lenguaje de programación. La lógica de parseo la encapsulé en una clase estática `Gestor`,
de manera tal que sea fácilmente reutilizable y sin necesidad de instanciarla (puede utilizarse de manera aislada, por
fuera de la clase `Sistema`).