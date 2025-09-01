# 🔍 Find NAS Services

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/) 
[![SMB](https://img.shields.io/badge/Protocol-SMB-red)](https://wiki.samba.org/index.php/SMB) 
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📖 Descripción
**Find NAS Services** es una herramienta ligera que detecta servidores en la red local utilizando el protocolo **SMB**.  
Escanea el rango **192.168.101.0/24** para identificar servidores disponibles de forma rápida y eficiente.  

---

## ℹ️ Información del Proyecto
- 🔗 **Protocolo usado:** SMB (Puerto 445)  
- 🌐 **Rango escaneado:** 192.168.101.0/24  
- ⚡ **Enfoque:** Simplicidad y velocidad  
- 🖥️ **Interfaz:** Sin GUI (ejecución en consola)  

---

## ✨ Características
- 🔍 Escaneo rápido en redes locales.
- 📡 Basado en el protocolo SMB.  
- 🛠️ Implementado en **Python**.  
- 📂 Útil para detectar NAS y servidores compartidos.  

---

## 🖼️ Capturas
📌 *(Próximamente se añadirán imágenes y ejemplos de ejecución en consola)*  

---

## 🖥️ Requisitos del Sistema
- **Sistema operativo:** Windows 10 o superior (futuro soporte para Linux/Mac).  
- **Python:** 3.10+  
- **RAM mínima:** 1 GB  
- **Espacio en disco:** 100 MB  
- **Dependencias:**  
  - `pysmb`  
  - `threading` (nativo en Python)  

---

## 🔧 Solución de Problemas
- ❌ **No encuentra servidores** → Verifica que los NAS estén encendidos y conectados a la red.  
- ❌ **Error SMB** → Asegúrate de que el protocolo SMB (puerto 445) esté habilitado.  
- ❌ **Tiempo de espera agotado** → Revisa firewall, permisos de red o credenciales.  

---

## 🤝 Contribuciones y Soporte
- ✅ Pull Requests y sugerencias son bienvenidas.  
- 📩 **Soporte técnico:** soporte@nrcoriginals.com  

---

## 🏷️ Hoja de Ruta
- 📌 **Versión 1.1** → Soporte para rangos de red configurables.  
- 📌 **Versión 2.0** → Integración directa con *CloudNasManager*.  
- 📌 **Versión 3.0** → Detección avanzada (hostname, SO, estado del servidor).  
