# cancel-scope-replay

## Français

Montrer les tâches Python qui continuent après annulation du parent.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m cancel_scope_replay examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Exécute de vraies tâches asyncio sous TaskGroup, détachement et shield. Des portes Event fixent l’ordre annulation/effet sans pari sur des délais ; le reçu montre quel enfant survit.

### Limites

Effets en mémoire et scénarios bornés ; ne démontre pas la sûreté d’un orchestrateur réel ni l’annulation d’une requête distante déjà acceptée.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Show Python tasks continuing after their parent is cancelled.

Synthetic data; no network access or secret required.

```sh
python -m cancel_scope_replay examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Runs actual asyncio tasks under TaskGroup, detachment and shield. Event gates fix cancellation/effect ordering without timing races; receipts show which child survives.

### Limits

In-memory effects and bounded scenarios; does not prove a real orchestrator safe or cancel a remote request already accepted.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Mostrar tareas Python que continúan tras cancelar al padre.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m cancel_scope_replay examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Ejecuta tareas asyncio reales con TaskGroup, separación y shield. Puertas Event fijan el orden de cancelación/efecto sin carreras temporales; recibos muestran qué hijo sobrevive.

### Límites

Efectos en memoria y escenarios acotados; no demuestra seguridad de un orquestador real ni cancela solicitudes remotas ya aceptadas.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://docs.python.org/3.11/library/asyncio-task.html
