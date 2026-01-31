# Avance del Proyecto Final – Sistemas Operativos
Servidor y Cliente TCP para Gestión de Procesos

## Descripción del sistema
Este proyecto implementa un sistema cliente-servidor que permite administrar procesos del sistema operativo de forma remota usando comunicación TCP/IP.  
El servidor se ejecuta en una máquina y permite listar procesos, iniciar nuevos procesos, detenerlos y monitorear el uso de CPU y memoria.  
El cliente se conecta al servidor mediante sockets y envía los comandos.

Este sistema simula un entorno de sistemas operativos distribuidos, donde un cliente puede administrar recursos de otra máquina.

---

## Arquitectura
El sistema está compuesto por dos programas:

- **server.py** → Servidor que gestiona procesos y recursos del sistema operativo.
- **client.py** → Cliente que se conecta al servidor y permite al usuario enviar comandos.

La comunicación se realiza usando sockets TCP/IP sobre el puerto 5050.

---

## Funcionalidades implementadas

| Opción | Función |
|------|--------|
| 1 | PING – Verifica conexión con el servidor |
| 2 | LIST – Lista los procesos activos |
| 3 | START – Inicia un nuevo proceso |
| 4 | STOP – Detiene un proceso por PID |
| 5 | INFO – Muestra CPU y RAM |
| 6 | EXIT – Cierra el cliente |

---

## Descripción del servidor (server.py)
El servidor:
- Escucha conexiones TCP en el puerto 5050
- Recibe comandos del cliente
- Usa la librería psutil para:
  - Listar procesos
  - Iniciar procesos
  - Detener procesos
  - Obtener uso de CPU y RAM
- Envía las respuestas al cliente en formato JSON

---

## Descripción del cliente (client.py)
El cliente:
- Se conecta al servidor por sockets TCP
- Muestra un menú interactivo
- Envía comandos al servidor
- Recibe y muestra las respuestas

---

## Pruebas realizadas

Se realizaron las siguientes pruebas:

### 1. Prueba de conexión (PING)
El cliente envió el comando PING al servidor y recibió la respuesta:
{“ok”: true, “msg”: “pong”}
### 2. Lista de procesos (LIST)
El cliente solicitó la lista de procesos activos y el servidor devolvió una lista con los nombres y PID.

### 3. Inicio de proceso (START)
Se inició el proceso usando el comando:
open
El servidor devolvió el PID del proceso iniciado.

### 4. Monitoreo del sistema (INFO)
El servidor devolvió el uso de CPU y memoria RAM en tiempo real.

Estas pruebas demuestran que la comunicación TCP y la gestión de procesos funcionan correctamente.

---

## Conclusión
El sistema cumple con los requisitos del proyecto ya que implementa:
- Gestión de procesos
- Comunicación cliente-servidor
- Monitoreo del sistema
- Arquitectura distribuida básica
