Elias Emmanuel Barea Peralta | 202373580-9 | San Joaquin
Catalina Monserrat Isabel Díaz Cofré | 202473507-1 | San Joaquin

La tarea esta pensada para usarse en Linux (cualquier distro) o con wsl (Windows/Mac).

Primero encargate de usar el docker para empezar la DB, para eso ocupa el siguiente comando:

    docker-compose -f deploy-202373580-9-202473508-1.yml up -d

Usa tu bash de preferencia para esto.

Luego, usando mongosh (bash de MongoDB), empieza el replica set con el siguiente comando:

    rs.initiate({
        _id: "my-replica-set",
        members: [
            {_id: 0, host: "mongo1:30001"},
            {_id: 1, host: "mongo2:30002"},
            {_id: 2, host: "mongo3:30003"}
        ]
    })

De ser necesario, modifica el archivo host:

    127.0.0.1 mongo1 mongo2 mongo3

Este se ubicara en:

    Linux/Mac ~ /etc/hosts
    Windows ~ C:\Windows\System32\drivers\etc\hosts

Para el uso del Notebook, ejecutalo con:

    jupyter notebook pymongo-202373580-9-202473508-1.ipynb

Ejecuta los bloques de codigo en orden para que no existan problemas con dependencias, instalaciones, etc.