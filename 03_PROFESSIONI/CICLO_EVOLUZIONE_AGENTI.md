# Ciclo Evoluzione Agenti

## Scopo

Definire come MD_OS immagina, testa, migliora, sviluppa ed emula nuovi agenti prima di considerarli utili al sistema.

Un agente non nasce valido solo perche ha un nome interessante.
Un agente diventa valido quando migliora il sistema in modo osservabile.

## Ciclo completo

```text
1. Immagina
2. Definisci
3. Testa
4. Misura
5. Migliora
6. Sviluppa
7. Emula
8. Fai interagire
9. Integra o scarta
```

## 1. Immagina

Generare un nuovo agente quando emerge una funzione non coperta dagli agenti esistenti.

Domande:
- Quale capacita manca?
- Quale problema risolve?
- E una vera professione/funzione o solo un nome affascinante?
- Produce output riconoscibile?
- Riduce lavoro futuro?

Output:
- nome agente;
- funzione;
- famiglia;
- motivo di esistenza.

## 2. Definisci

Ogni agente deve avere una scheda minima.

Campi obbligatori:

| Campo | Descrizione |
|---|---|
| Nome | nome operativo |
| Famiglia | area di appartenenza |
| Funzione | cosa fa |
| Quando si attiva | trigger concreti |
| Quando non si attiva | limiti e casi da evitare |
| Input minimi | cosa deve ricevere |
| Output tipici | cosa produce |
| Skill collegate | capacita usate |
| Matrici collegate | criteri decisionali |
| Rischi | come puo peggiorare il sistema |
| Test | prove minime da superare |

## 3. Testa

Ogni nuovo agente deve essere provato su almeno tre richieste:

1. richiesta semplice;
2. richiesta complessa;
3. richiesta ambigua o rischiosa.

Durante il test si valuta se l'agente:

- migliora la qualita;
- riduce rumore;
- porta un punto di vista utile;
- produce output concreto;
- collabora con altri agenti;
- non duplica agenti esistenti.

## 4. Misura

Scala consigliata da 1 a 5.

| Criterio | Domanda | Soglia minima |
|---|---|---:|
| Utilita | migliora davvero il risultato? | 4 |
| Distinzione | e diverso da agenti gia esistenti? | 4 |
| Operativita | produce output concreto? | 4 |
| Leggerezza | non appesantisce troppo il runtime? | 3 |
| Collaborazione | interagisce bene con altri agenti? | 4 |
| Rischio | puo generare confusione? | massimo 2 |

Decisione:

| Esito | Azione |
|---|---|
| forte | integra nel menu agenti |
| utile ma acerbo | sviluppa ancora |
| duplicato | fondi con agente esistente |
| rumoroso | scarta |

## 5. Migliora

Se l'agente e utile ma debole, migliorare:

- nome;
- confini;
- trigger di attivazione;
- output;
- skill collegate;
- matrici;
- esempi;
- limiti.

Non migliorare aggiungendo solo descrizioni piu lunghe.
Migliorare significa renderlo piu selettivo e piu produttivo.

## 6. Sviluppa

Quando l'agente supera i test, creare o aggiornare la sua scheda.

La scheda deve permettere all'Orchestratore di sapere:

- quando attivarlo;
- con chi farlo collaborare;
- cosa chiedergli;
- cosa aspettarsi;
- quando spegnerlo.

## 7. Emula

Ultimo test prima dell'integrazione.

L'agente viene simulato come se fosse gia parte del sistema.

Formato:

```text
Richiesta utente:
...

Agente emulato:
...

Lettura dell'agente:
...

Contributo dell'agente:
...

Interazione con altri agenti:
...

Miglioramento prodotto:
...
```

L'emulazione e valida solo se il contributo cambia davvero la qualita dell'output.

## 8. Fai interagire

Chiedere al nuovo agente di interagire con il sistema.

Domande da porre all'agente emulato:

- Quale parte di MD_OS miglioreresti?
- Quale agente duplichi o completi?
- Quale skill ti serve?
- Quale matrice ti valuta meglio?
- In quali casi non dovresti essere attivato?
- Quale nuovo file o campo proporresti?

## 9. Integra o scarta

Un agente viene integrato solo se:

- ha funzione distinta;
- produce output utile;
- migliora almeno un preset runtime;
- non aumenta rumore;
- ha limiti chiari;
- supera verifica avversaria.

Se non passa, viene scartato o fuso.

## Esempio: agente Startupper

### Immagina

Manca un agente che trasformi idee visionarie in MVP, offerta e mercato.

### Definisci

Nome:
Startupper

Famiglia:
Innovatori / Visionari / Prodotto

Funzione:
Trasforma un'idea in ipotesi di prodotto, pubblico, valore, MVP e primi passi.

Quando si attiva:
- nuova idea di business;
- progetto da lanciare;
- prodotto da validare;
- MVP;
- monetizzazione;
- posizionamento iniziale.

Quando non si attiva:
- puro codice;
- pura estetica;
- ricerca senza prodotto;
- decisioni personali non legate a mercato o progetto.

Output:
- ipotesi di valore;
- target;
- MVP;
- rischi;
- primi esperimenti;
- criteri di validazione.

### Emula

Richiesta:
> Voglio trasformare MD_OS in un prodotto usabile da altri.

Contributo Startupper:
- definisce pubblico iniziale;
- distingue sistema personale da prodotto vendibile;
- propone MVP documentale;
- identifica rischio di eccessiva complessita;
- chiede metriche di utilita.

Miglioramento prodotto:
MD_OS non resta solo sistema personale, ma diventa prototipo validabile.

## Regola finale

MD_OS non colleziona agenti.
MD_OS sviluppa agenti che dimostrano valore.

Un agente nuovo deve guadagnarsi il posto nel sistema.
