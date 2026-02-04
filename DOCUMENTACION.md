# Documentación Técnica – Avance Proyecto Final

## Objetivo
Desarrollar un sistema cliente-servidor que permita controlar procesos del sistema operativo de forma remota usando sockets TCP/IP.

## Arquitectura
El sistema está formado por:
- server.py (servidor)
- client.py (cliente)

Se comunican mediante mensajes JSON enviados por sockets TCP.

## Arquitectura del sistema

El sistema utiliza una arquitectura cliente-servidor basada en sockets TCP/IP.
El cliente envía comandos al servidor y el servidor responde con información del sistema.

## Funcionalidades
El servidor puede:
- Listar procesos
- Iniciar procesos
- Detener procesos
- Consultar CPU y RAM

El cliente envía comandos al servidor usando un menú interactivo.

## Sistemas distribuidos
El servidor puede ejecutarse en dos puertos (5050 y 5051), simulando múltiples servidores disponibles para clientes, funcionando como una arquitectura distribuida básica.
