# clienteFastAPI
Consumo de API creada con FastAPI. 

Comando para crear un entorno virtual llamado env
```shell
python -m venv env
```

Comando para activar entorno virtual en Windows
```shell
. env/Scripts/activate
```

Crear archivo requirements.txt (Dependencias)
```shell
pip freeze > requirements.txt
```

Instalar dependencias a partir del archivo requirments.txt.
```shell
pip install -r requirements.txt
```

Comando para ejecutar aplicación
```shell
uvicorn main:app --port 5000 --reload
```

Para revisar documentación de la API
```shell
localhost:5000/docs
```

Comando para desactivar el entorno virtual
```shell
deactivate
```
