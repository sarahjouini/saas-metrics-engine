# SaaS Metrics Engine

Analisi delle metriche chiave di un business SaaS (Software as a Service) a partire da un dataset di abbonamenti: churn, MRR, ARR, retention e segmentazione dei ricavi.

Progetto di analisi dati end-to-end sviluppato in Python/pandas, pensato come esercizio di analisi descrittiva orientata al business.

---

## Obiettivo

Costruire un "motore di metriche" che, a partire dai dati grezzi degli abbonamenti, calcoli in automatico gli indicatori che una startup SaaS monitora quotidianamente e ne estragga insight utili al business.

Le domande a cui il progetto risponde:

- Quanto vale il ricavo ricorrente (MRR/ARR) e quanto se ne perde per abbandono?
- Qual è il tasso di abbandono (churn) e da cosa dipende?
- Dove si concentra il valore della base clienti?
- Quanto durano gli abbonamenti prima di chiudersi?

---

## Dataset

Dataset di **5.000 abbonamenti** con **14 colonne**. Si tratta di dati **sintetici** (generati artificialmente), utilizzati a scopo di esercizio.

| Colonna | Significato |
|---|---|
| `subscription_id` | Codice univoco dell'abbonamento |
| `account_id` | Codice del cliente (un cliente può avere più abbonamenti) |
| `start_date` | Data di inizio dell'abbonamento |
| `end_date` | Data di fine (vuota se ancora attivo) |
| `plan_tier` | Piano sottoscritto (Basic / Pro / Enterprise) |
| `seats` | Numero di postazioni/licenze acquistate |
| `mrr_amount` | Ricavo ricorrente mensile (MRR) |
| `arr_amount` | Ricavo ricorrente annuale (ARR) |
| `is_trial` | L'abbonamento proviene da una prova gratuita? |
| `upgrade_flag` | Il cliente ha fatto un upgrade di piano? |
| `downgrade_flag` | Il cliente ha fatto un downgrade di piano? |
| `churn_flag` | Il cliente ha abbandonato? |
| `billing_frequency` | Frequenza di fatturazione (mensile / annuale) |
| `auto_renew_flag` | Rinnovo automatico attivo? |

---

## Pulizia dei dati (data cleaning)

Prima dell'analisi sono stati eseguiti alcuni controlli di qualità sui dati:

- **Valori mancanti**: verificati su tutte le colonne. L'unica con valori mancanti è `end_date` (4.514 su 5.000). Il dato è corretto e atteso: gli abbonamenti ancora attivi non hanno una data di fine.
- **Tipi di dato**: `start_date` e `end_date` venivano lette come testo. Sono state convertite in formato data (`datetime`) per poter effettuare calcoli temporali.

---

## Metriche calcolate

### Churn (abbandono)
- **Churn rate complessivo**: 9,7% (486 abbonamenti chiusi su 5.000).
- **Churn per segmento** (piano, rinnovo automatico, trial): risultato omogeneo intorno al 9–10% in tutti i segmenti.

### Ricavi ricorrenti
- **MRR totale**: ~11,34 mln
- **MRR attivo** (soli abbonamenti attivi): ~10,16 mln
- **MRR perso per churn**: ~1,18 mln (≈ 10,4% del totale)
- **ARR attivo**: ~121,9 mln — verificato come coerente con MRR attivo × 12.

### Segmentazione dei ricavi per piano
| Piano | Clienti attivi | MRR |
|---|---|---|
| Basic | 1.450 | ~688 k |
| Pro | 1.513 | ~1,92 mln |
| Enterprise | 1.551 | ~7,55 mln |

### Ciclo di vita
- **Durata media degli abbonamenti chiusi**: 88 giorni (~3 mesi).

---

## Insight principali

**1. Il valore è fortemente concentrato nel segmento Enterprise.**
A fronte di una base clienti equamente distribuita fra i tre piani (~1.500 clienti ciascuno), il segmento Enterprise genera circa il **74% dell'MRR totale**. Un cliente Enterprise vale in media ~10 volte un cliente Basic (~4.866 vs ~475 di MRR). Implicazione: la perdita di un cliente Enterprise ha un impatto molto più grave, quindi le strategie di retention dovrebbero dare priorità a questo segmento.

**2. Il churn non dipende dai segmenti analizzati.**
Il tasso di abbandono è risultato omogeneo (~9–10%) rispetto a piano, rinnovo automatico e provenienza da trial. Nessuna di queste variabili è quindi un fattore predittivo dell'abbandono in questo dataset: un risultato utile perché indirizza l'attenzione verso altri possibili fattori.

**3. L'abbandono si concentra nella fase iniziale.**
Gli abbonamenti che si chiudono durano in media ~3 mesi. Questo suggerisce che i primi mesi del ciclo di vita del cliente sono i più critici e che gli sforzi di onboarding e retention andrebbero concentrati in quella fase.

---

## Nota metodologica

Il dataset è **sintetico** e il churn risulta distribuito in modo casuale rispetto alle altre variabili (verificato incrociando il churn con piano, rinnovo automatico, trial e MRR medio). Per questo motivo il progetto è stato impostato come **analisi descrittiva** (misurare e raccontare le metriche) anziché come modello **predittivo** (prevedere il churn), che richiederebbe un dataset con relazioni reali fra le variabili.

Durante l'analisi è stata applicata la **verifica incrociata** delle metriche (es. MRR perso ≈ churn rate; ARR = MRR × 12) come controllo di coerenza dei risultati.

---

## Tecnologie utilizzate

- **Python** / **pandas** — pulizia dei dati e calcolo delle metriche
- **Git** / **GitHub** — versionamento del progetto
- **Codespaces** — ambiente di sviluppo

---

## Struttura del progetto

```
saas-metrics-engine/
├── data/           # dataset (CSV)
├── src/            # script Python
│   ├── esplora.py     # esplorazione e controllo qualità dei dati
│   └── metriche.py    # calcolo delle metriche
├── sql/            # query SQL (in sviluppo)
├── notebooks/      # esplorazione
├── dashboard/      # dashboard (in sviluppo)
└── README.md
```

---

## Come eseguire

```bash
pip install pandas
python src/metriche.py
```