# tp3-SDN-IntroDistribuidos
Trabajo Práctico 3: SDN - Introduccion a sistemas distribuidos - 1C 2022


`sudo mn --custom topo.py  --topo mytopo,<#switches> --test pingall`
`sudo mn --custom topo.py --topo mytopo,2 --mac --arp --switch ovsk --controller remote`

## Orden de pasos
1) Ejecutar el controlador
2) Ejecutar MININET

## Ejecutar controladores
para ejecutar el controlador firewall: 
Ir al root donde tengas instalado mininet, pox y openflow.

Opcion uno: Ingresar a la carpeta pox, luego a ext y abrir una consola luego tipear l-s y copiar el path completo donde tengas ubicado firewall.py entre comillas (tip parate sobre el archivo firewall del tp abri propiedades y obtene el path)


Opcion dos: copiar el archivo firewall del tp en la carpeta pox/ext 

Una vez echo esto desde las consola tipear  
```

pox/pox.py firewall

```

## Cómo levantar la topología para poder ejecutar los controladores
```
$ sudo mn --custom topo.py --topo mytopo,<#switches> --mac --arp --switch ovsk --controller remote.

ejemplo con 3 switches

sudo mn --custom topo.py --topo mytopo,3 --mac --arp --switch ovsk --controller remote

```
