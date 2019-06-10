# apipipedrive

Apipipedrive es una Api para realizar consultas CRUD a la plataforma de Pipedrive, las consultas son servidas por medio de vistas utilizando Django como framework.

## Descripción 

Actualmente TrueHome cuenta con una herramienta de CRM que ayuda a gestionar sus clientes y tener un seguimiento puntual de las diferentes actividades que se tiene con ellos. La herramienta es Pipedrive (https://www.pipedrive.com/es), la cual cuenta con un API que brinda diferentes funcionalidades para la administración de personas, deals y actividades. El proyecto consiste en generar un API que realice las siguientes funciones: 
1. • CRUD de Personas, Deals y Actividades. 
2. • Adjuntar Documentos en Deal, limitando por tipo de archivo en PDF.

## Solución propuesta

La solución propuesta es la siguiente: Se generó un archivo api.py el cual realiza la conexión a la api de pipedrive con los metodos de lectura, creación, modificación y eliminación de deals, personas y actividades, así como subir archivos pdf.

### la clase ApiPipedrive es la siguiente

class ApiPipedrive:
    api_version = "v1/"
    header = {"Accept": "application/json, */*", "content-type": "application/json"}

    def __init__(self, api_base_url):
        self.api_base_url = api_base_url
	#Token extraido de la pagina web
        self.token = "9d3f3e7ab1582ac6331856daa24a3d0972f2c9fa"

    def make_request(self, method, endpoint, data=None, json=None, **kwargs):

        if self.token:
            url = '{0}{1}{2}?api_token={3}'.format(self.api_base_url, self.api_version, endpoint, self.token)
            if method == "get":
                response = requests.request(method, url, headers=self.header, params=kwargs)

            else:
                response = requests.request(method, url, headers=self.header, data=data, json=json)

            return response.json()
        else:
            raise Exception("TOKEN ERROR")


### Metodos con los que cuenta la api para realizar consultas

    def _get(self, endpoint, data=None, **kwargs):
        return self.make_request('get', endpoint, data=data, **kwargs)

    def _post(self, endpoint, data=None, json=None, **kwargs):
        return self.make_request('post', endpoint, data=data, json=json, **kwargs)

    def _delete(self, endpoint, **kwargs):
        return self.make_request('delete', endpoint, **kwargs)

    def _put(self, endpoint, json=None, **kwargs):
        return self.make_request('put', endpoint, json=json, **kwargs)

### METODOS PARA CRUD DE DEALS
    def get_deals(self, deal_id=None, **kwargs):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
        else:
            url = "deals"
        return self._get(url, **kwargs)

    def add_deal(self, **kwargs):
        url = "deals"
        if kwargs is not None:
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_deal(self, deal_id, **kwargs):
        if deal_id is not None and kwargs is not None:
            url = "deals/{0}".format(deal_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_deal(self, deal_id):
        if deal_id is not None:
            url = "deals/{0}".format(deal_id)
            return self._delete(url)

### METODOS PARA CRUD DE PERSONAS
    def get_persons(self, person_id=None, **kwargs):
        if person_id is not None:
            url = "persons/{0}".format(person_id)
        else:
            url = "persons"
        return self._get(url, **kwargs)



    def add_person(self, **kwargs):
        if kwargs is not None:
            url = "persons"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_person(self, data_id, **kwargs):
        if data_id is not None and kwargs is not None:
            url = "persons/{0}".format(data_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_person(self, data_id):
        if data_id is not None:
            url = "persons/{0}".format(data_id)
            return self._delete(url)


### METODOS PARA CRUD DE ACTIVIDADES
    def get_activities(self, activity_id=None, **kwargs):
        if activity_id is not None:
            url = "activities/{0}".format(activity_id)
        else:
            url = "activities"
        return self._get(url, **kwargs)

    def add_activity(self, **kwargs):
        if kwargs is not None:
            url = "activities"
            params = {}
            params.update(kwargs)
            return self._post(url, json=params)

    def update_activity(self, activity_id, **kwargs):
        if activity_id is not None:
            url = "activities/{0}".format(activity_id)
            params = {}
            params.update(kwargs)
            return self._put(url, json=params)

    def delete_activity(self, activity_id):
        if activity_id is not None:
            url = "activities/{0}".format(activity_id)
            return self._delete(url)


### METODOS PARA FILES


    def get_files(self, file_id=None, **kwargs):
        if file_id is not None:
            url = "files/{0}".format(file_id)
        else:
            url = "files"
        return self._get(url, **kwargs)


    def add_files_to_deal(self, deal_id=None,file=None ,**kwargs):
        if deal_id is not None:
            url="files"
            if kwargs is not None:
                params = {}
                params.update(kwargs)

                f=open('/home/osiel/TH/apipipedrive/apiproject/apipipe/'+ file, 'rb')
                files={'file': f}
                data={'file_type':'pdf', 'deal_id':deal_id}
                return self._post(url,data=data, json=files)




Este archivo es importado al archivo views.py el cual hace uso de la clase Apipipedrive para generar las consultas, la forma de uso es la siguiente:


1. api = ApiPipedrive(api_base_url='https://osieltorres.pipedrive.com/')
2. api.get_deals()
2. api.get_persons()
3. api.get_activities()
4. api.add_deal(params)
5. api.add_persons(params)
7. api.delete_deals(params)
8. api.delete_persons(params)
9. api.delete_activities(params)
10. api.update_deals(params)
11. api.update_persons(params)
12. api.update_activities(params)



## Requerimientos

1. Django 2.1
2. Cuenta en pipedrive

#La gestión de la prueba fue realizada con base en los requerimientos como historias de usuarios

## Historias de usuario:

1. Como cliente quiero un CRUD de Deals
2. Como cliente quiero un CRUD de Actividades
3. Como cliente quiero un CRUD de Personas
4. Como cliente quiero subir archivos pdf a los deals
5. Como desarrollador quiero entender el funcionamiento de la Api de pipedrive
6. Como desarrollador quiero hacer un CRUD de deals
7. Como desarrollador quiero hacer un CRUD de personas
8. Como desarrollador quiero hacer un CRUD de actividades
9. Como desarrollador quiero hacer una Api para hacer los CRUD
10. Como desarrollador quiero mostrar la funcionalidad de la api en una pagina web
11. Como desarrollador quiero usar Django como framework para controlar las funcionalidades y presentar las vistas en la pagina
12. Como desarrollador quiero subir archivos pdf a los deals
13. Como desarrollador quiero realizar pruebas a la api y documentarlas

Tareas

## HU1  

## HU2  

## HU3  

## HU4  


## HU5 

- [x] 1. HU5[30min] Leer la documentación de la pagina 
- [x] 2. HU5[30min] Conectar proyecto con la api


## HU6 
- [x] 1. HU6[20min] Crear metodo para leer deals
- [x] 2. HU6[20min] Crear metodo para crear deals
- [x] 3. HU6[20min] Crear metodo para actualizar deals
- [x] 4. HU6[20min] Crear metodo para eliminar deals

## HU7 

- [x] 1. HU7[10min] Crear metodo para leer personas
- [x] 2. HU7[10min] Crear metodo para crear personas
- [x] 3. HU7[10min] Crear metodo para actualizar personas
- [x] 4. HU7[10min] Crear metodo para eliminar personas

## HU8 

- [x] 1. HU8[10min] Crear metodo para leer actividades
- [x] 2. HU8[10min] Crear metodo para crear actividades
- [x] 3. HU8[10min] Crear metodo para actualizar actividades
- [x] 4. HU8[10min] Crear metodo para eliminar actividades

## HU9 


- [x] 1. HU9[90min] Crear metodos GET,POST,PUT,DELETE para la api

## HU10 

- [x] 1. HU10[120min] Maquetar la plantilla en HTML Para mostrar los registros
- [x] 2. HU10[30min] Conectar la plantilla con la vista de Django

## HU11 

- [x] 1. HU11[5min] Crear un entorno virtual para las dependencias necesarias
- [x] 2. HU11[5min] Instalar Django en el entorno virtual
- [x] 3. HU11[5min] Crear un nuevo proyecto de Django 

## HU12

- [x] 1. HU12[20min] Crear metodo para leer los documentos
- [x] 2. HU12[25min] Crear metodo para subir archivos
- [ ] 3. HU12[30min] Limitar a solo archivos pdf
- [x] 4. HU12[15min] Mostrar los documentos actuales en la template

## HU13 

- [x] 1. HU13[120min] Documentar pruebas


## RESULTADOS OBTENIDOS

Se logró crear la api con todas las funcionalidades de las historias de usuario 1,2,3,5,6,7,8,9,10,11,13

Las pruebas que se realizaron fueron las inserción de datos, modificación y eliminación de deals, actividades y personas, todas tuvieron resultados exitosos.

El archivo con el codigo de la api se encuentra en apiproject/apipipe/api.py en este archivos se encuentran todas los metodos necesarios para los CRUD.
