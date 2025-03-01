# Archi websocket kube

Petit projet pour montrer comment installer une application type websocket / backend / frontend sur kube

## La subtilité

La subtilité réside dans l'accès au websocket, qui n'est pas accessible en http et donc pas accessible via exposition ingress nginx. Il faut donc passer dans le cluster

## Les applis 

Un backend qui se connecte au websocket
Un frontend qui se connecte au websocket et peut faire des choses
Un serveur websocket qui se connecte au reste

> Par contre le code est très court, l'objectif ici est de voir comment déployer

## La simplicité

Vous pouvez également héberger le service websocket et l'api sur le même serveur.
(donc en fusionnant la partie websocket et la partie api en montant le websocket sur votre fastapi)