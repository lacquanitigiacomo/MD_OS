# Routing estrazione dati

Questo modulo definisce quando attivare il reparto ESTRAZIONE_DATI.

## Attivazione obbligatoria

Attivare ESTRAZIONE_DATI quando il task richiede di recuperare dati da:

- PDF;
- immagini;
- scansioni;
- documenti testuali;
- tabelle;
- fogli;
- moduli;
- cedolini;
- contratti;
- comunicazioni;
- file con layout complesso;
- documenti poco leggibili.

## Attivazione consigliata

Attivare ESTRAZIONE_DATI quando:

- il file è lungo;
- il file contiene molte pagine;
- il layout è complesso;
- ci sono valori numerici da recuperare;
- ci sono campi ripetuti;
- i dati devono poi essere confrontati;
- serve distinguere dato estratto e interpretazione;
- la qualità della lettura può essere incerta.

## Routing agenti

| Esigenza | Agente |
|---|---|
| Estrarre dati da documenti | `estrattore-documentale` |
| Controllare qualità e completezza dell'estrazione | `revisore-estrazione` |

## Ordine operativo

1. Verificare inventario fonti.
2. Selezionare la fonte da leggere.
3. Eseguire estrazione dati.
4. Marcare qualità e incertezza.
5. Far revisionare l'estrazione.
6. Consegnare i dati ai reparti specialistici.

## Regola anti-interpretazione

Se durante l'estrazione emerge un possibile problema, il reparto deve registrarlo come dato o campo da verificare.

Non deve trasformarlo in anomalia conclusiva.
