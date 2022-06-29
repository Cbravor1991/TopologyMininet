# tp3-SDN-IntroDistribuidos
Trabajo Práctico 3: SDN - Introduccion a sistemas distribuidos - 1C 2022


`sudo mn --custom topo.py  --topo mytopo,<#switches> --test pingall`
`sudo mn --custom topo.py --topo mytopo,2 --mac --arp --switch ovsk --controller remote`
## Cómo levantar la topología para poder ejecutar los controladores
```
$ sudo mn --custom topo.py --topo mytopo,<#switches> --mac --arp --switch ovsk --controller remote.

ejemplo con 3 switches

sudo mn --custom topo.py --topo mytopo,3 --mac --arp --switch ovsk --controller remote

```

## Ejecutar controladores
Copiar los archivos 'topo_ctl.py', 'l2_learning.py' que se encuentran en el directorio pox/ext, al directorio de mismo nombre en la distribución de pox que se tenga instalada. 
Despues ejecutar esos archivos desde consola usando tenes que estar en la raiz no dentro de pox parta que ande
```
$ pox/pox.py topo_ctl (al hacer esto se ejecutan los controladores importados en topo_ctl en este caso l2_learnig.py)
