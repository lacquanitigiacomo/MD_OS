# BOOT — MD_OS v31

## Modalità di avvio

1. Leggere `MANIFEST.md`.
2. Leggere `CORE/config.yaml`.
3. Caricare `REGISTRY/*.registry.yaml`.
4. Caricare `CORE/routing.yaml`.
5. Usare `MESH/schema_mesh_index.yaml` per selezione minima.
6. Generare `runtime_packet`.
7. Eseguire skill/agenti/dataset richiesti.
8. Applicare `CORE/quality_gate.yaml`.
9. Se utile, produrre learning patch o export pack.

## Regola madre

Caricare poco.  
Incrociare bene.  
Rispondere con output utile.  
Salvare solo ciò che aumenta capacità futura.
