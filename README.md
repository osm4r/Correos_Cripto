# Correos_Cripto

<h1 align="center" class="h1"> ⭐️ Criptografía  Grupo 63 ⭐️ </h1>
<h1 align="center" class="h1"> 💚️ Docente: Lic. Alejandro Muñiz Solorio 💚️ </h1>
<h1 align="center" class="h1"> ⭐️ ENVIO DE CORREOS CON BLOCKCHAIN ⭐️ </h1>
<h1 align="center" class="h1"> ️💚️ Integrantes: 💚 </h1>
<div align="center">
    <img src="https://avatars.githubusercontent.com/u/103228889?v=4" width="125px;" /><br>
    <a href="https://github.com/osm4r">Osmar Abelardo Bustos Vázquez 1912361</a>
</div>
<div align="center">
    <img src="https://avatars.githubusercontent.com/u/99228295?v=4" width="125px;" /><br>
    <a href="https://github.com/PHernandez04">Patricia Rubí Hernández Cepeda</a>
</div>
<div align="center">
    <img src="https://avatars.githubusercontent.com/u/103228912?v=4" width="125px;" /><br>
    <a href="https://github.com/JesusMS17">Jesús Alejandro Meza Solís</a>
</div>
<div align="center">
    <img src="https://avatars.githubusercontent.com/u/117962406?v=4" width="125px;" /><br>
    <a href="https://github.com/EleventhD">Erik Gabriel Zúñiga Hernández</a>
</div>
<div align="center">
    <img src="https://avatars.githubusercontent.com/u/103225759?v=4" width="125px;" /><br>
    <a href="https://github.com/JJRivera9">Juan José Rivera Arroyo</a>
</div>
<div align="center">
    <img src="https://avatars.githubusercontent.com/u/103234851?v=4" width="125px;" /><br>
    <a href="https://github.com/may018">Mayela Judith Briones Nuñez</a>
</div>

### Installation for windows

```sh
$ virtualenv ${env_name}
$ .\${envname}\Scripts\activate
$ python -m pip install -r requeriments.txt
```

### Configuración de archivo config.ini

config.ini sirve para especificar el Servidor RPC, el chain ID y la frase nmemoric que se visualiza en ganache (si tiene nuestro workspace no tendrá que  configurar el nmemoric)
Ejemplo:

```sh
; config.ini
[GANACHE]
RPCSERVER = HTTP://localhost:7545
CHAINID = 1337
MNEMONIC = fault squeeze wink clinic skull manual camp slide perfect hope suspect toe
```

### About the proyect

Proyecto de envío de correos en blockchain mediante transacciones a través de un smartcontract en solidity elaborado en el lenguaje de programación Python. Pruebas realizadas con el software Ganache.

PUNTOS A CUMPLIR DE LA RÚBRICA

Método de encriptado simétrico:
Se utiliza el cifrado asimétrico Fernet para cifrar los correos recibidos/enviados que se obtienen mediante el smartcontract y almacenarlos de manera segura.

Método de encriptado asimétrico:
Se utiliza el cifrado por curvas elípticas ECC para la creación de certificados(clave pública) y la llave privada. En este caso, ciframos la Address y la private key de Ethereum generada en Ganache. Es decir, utilizamos doble cifrado por así decirse.

Método de encriptado libre (distinto a los dos anteriores):
Se utiliza el cifrado base64 para cifrar el archivo json que se genera al despliegar(deploy) el smartcontract dentro del script.

Uso de clave publica/clave privada:
Se utiliza llave pública y privada debido al uso de blockchain y curvas elípticas.

Guardado de certificados en archivos:
La generación de certificados se generan al un usuario registrarse, se guardan en la carpeta usuarios y dentro de una carpeta llamada con el nombre del usuario. El nombre del archivo es la address de ethereum con extensión .cer. Además la llave se guarda con el mismo nombre pero con la extension .key.

Uso de llaves de blockchain o curvas elípticas:
Si se usan en todo el proyecto en general:).

Firmado de la información:
Blockchain para generar transacciones utiliza en medio de este proceso las firmas digitales. Estas son básicamente, la combinación entre una llave privada y un hash de los datos a firmar (como los de una transacción), lo que otorga una identificación digital única para establecer la autenticidad e integridad del mensaje, sin revelar la llave privada del firmante.
Lo usa en el enviado de correos cuando hace la transacción y se guarda en ganache ahi es donde firma blockchain automáticamente el documento o lo hace identificable.

Identificación del usuario por certificado:
Existe la opción de iniciar sesión, que es donde se inicia sesión con el certificado.

Creación de DApp (Opcional):
El proyecto envío de correos es una DApp debido a que todo se guarda en transacciones de blockchain, cada usuario puede enviar y acceder a sus correos mediante este medio, por lo tanto, es descentralizada.

