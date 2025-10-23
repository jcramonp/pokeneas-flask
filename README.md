# Flask random pokeneas:

Se exponen 2 rutas:

-   `/api/pokenea` → JSON con el pokenea y `container_id`

-   `/imagen` → tarjeta con **nombre + imagen + habilidad + altura** y `container_id`

Las imágenes se sirven desde **Amazon S3**. Se despliega en **Docker Swarm** (1 líder + 3 managers) con **10 réplicas** y **routing mesh**.

Repositorios
------------

-   **GitHub**: <https://github.com/jcramonp/pokeneas-flask.git>

-   **Docker Hub**: https://hub.docker.com/r/juanof/pokeneas *(cambiar si tu repo es otro)*

Endpoints públicos (cualquiera funciona)
----------------------------------------

Gracias al routing mesh, la app responde en cualquier nodo del clúster:

-   Nodo 1: `http://54.226.151.5/api/pokenea` --- `http://54.226.151.5/imagen`

-   Nodo 2: `http://23.22.210.24/api/pokenea` --- `http://23.22.210.24/imagen`

-   Nodo 3: `http://100.27.198.52/api/pokenea` --- `http://100.27.198.52/imagen`

-   Nodo 4: `http://98.91.28.170/api/pokenea` --- `http://98.91.28.170/imagen`

Bucket S3
---------

-   **Nombre**: `pokeneas-juankyvale`

-   **Región**: `us-east-1`

-   Política: acceso público de **GetObject** para `arn:aws:s3:::pokeneas-juankyvale/*`.

Arquitectura de despliegue
--------------------------

-   4 instancias EC2 (Amazon Linux/Ubuntu), 1 **manager líder** + 3 **managers**.

-   **Docker Swarm** con servicio `pokeneas` en **10 réplicas** desde `juanof/pokeneas:latest`.

-   Seguridad:

    -   **HTTP 80** abierto a `0.0.0.0/0`.

    -   Puertos internos Swarm:

        -   `2377/TCP` (cluster management)

        -   `7946/TCP` y `7946/UDP` (gossip)

        -   `4789/UDP` (overlay/VXLAN)

    -   Origen de esos puertos: **el mismo Security Group** (o CIDR de VPC `172.31.0.0/16`).

Variables de entorno del servicio
---------------------------------

-   `S3_BUCKET=pokeneas-juankyvale`

-   `AWS_REGION=us-east-1`
