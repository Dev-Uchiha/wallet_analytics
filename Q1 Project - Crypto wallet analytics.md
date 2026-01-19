**By end of Q1 you will have:**

* A repeatable **on-chain data pipeline**
* Cleaned, structured **wallet-level analytics**
* A **Tableau dashboard** answering concrete questions
* A project that demonstrates **on-chain literacy + data engineering basics**

**Scope (intentionally constrained):**

* 1 blockchain (Ethereum mainnet)
* 10–50 wallets (start small)
* Read-only analytics (no signing, no smart contracts yet)

-----------------------------------------------------------------------------------

## Phase 0 — Orientation & Tooling (Week 1)

### Concepts to Master (non-negotiable)

* Wallet vs address (EOA vs contract)
* Transactions vs internal transactions
* Gas, value, token transfers
* Block time, confirmations, reorgs (high level)

### Tools You Will Use

| Layer         | Tool                         |
| ------------- | ---------------------------- |
| Data source   | Etherscan API **or** Alchemy |
| Extraction    | Python                       |
| Storage       | CSV → SQLite / Postgres      |
| Transform     | Pandas                       |
| Visualization | Tableau                      |
| Versioning    | Git + GitHub                 |

**Deliverable**

* Local dev environment ready
* API key obtained
* Git repo initialized

------------------------------------------------------------------------------------------

## Phase 1 — Raw On-Chain Data Ingestion (Weeks 2–3)

### Choose Data Source (start simple)

**Use Etherscan API first**
Reason: simpler mental model than node RPCs.

You will pull:

* Normal transactions
* ERC-20 token transfers

### Data Model (Raw Tables)

**transactions**

```
tx_hash
block_number
timestamp
from_address
to_address
value_eth
gas_used
gas_price
status
```

**token_transfers**

```
tx_hash
token_symbol
token_contract
from_address
to_address
value
timestamp
```

### Engineering Rules (important)

* Never transform during ingestion
* Store raw responses as-is
* Log failures and rate limits

**Deliverable**

* Script that pulls data for 1 wallet
* Raw tables saved locally
* Re-runnable without manual edits

-------------------------------------------------------------------------------------

## Phase 2 — Wallet-Level Analytics (Weeks 4–5)

This is where you stop being “API user” and become an **analyst**.

### Derived Metrics (Core)

Per wallet:

* Total ETH received / sent
* Net ETH balance (from txs, not live balance)
* Gas spent (ETH)
* Transaction count
* Active days
* First / last activity

Token-level:

* Tokens interacted with
* Net token inflow/outflow
* Frequency by token

### Behavioral Metrics (Differentiator)

* Avg tx size
* Tx frequency over time
* % outgoing vs incoming
* Gas per transaction trend
* Dormant periods

### Output Tables

**wallet_summary**

```
wallet
first_tx_date
last_tx_date
tx_count
total_eth_sent
total_eth_received
net_eth
total_gas_spent
```

**wallet_activity_daily**

```
wallet
date
tx_count
eth_sent
eth_received
gas_spent
```

**Deliverable**

* Clean analytical tables
* Documented metric definitions
* Deterministic transformations

--------------------------------------------------------------------------------------

## Phase 3 — Tableau Dashboard (Weeks 6–7)

### Core Dashboards (Minimum Viable Portfolio)

1. **Wallet Overview**

   * Net ETH
   * Tx count
   * Lifetime gas spent
2. **Activity Timeline**

   * Daily tx count
   * ETH flow over time
3. **Token Interaction**

   * Top tokens by volume
   * Inflow vs outflow

### Tableau Expectations

* Filters by wallet
* Clear metric definitions
* No clutter
* Insight-driven titles (“Wallet became inactive after…”)

**Deliverable**

* Published Tableau workbook
* Screenshots for GitHub
* README explaining insights

--------------------------------------------------------------------------------------

## Phase 4 — Pipeline Automation (Weeks 8–9)

Now you turn scripts into a **pipeline**.

### Improvements

* Parameterize wallet list
* Incremental pulls (last block processed)
* Scheduled execution (cron / Task Scheduler)
* Schema validation

### Optional Upgrade

* Move storage to Postgres
* Add token price data (CoinGecko)

**Deliverable**

* One-command pipeline run
* Fresh data → updated Tableau extract

-------------------------------------------------------------------------------------

## Phase 5 — Professionalization (Weeks 10–11)

This is what turns the project into **career leverage**.

### Documentation

* Architecture diagram
* Data flow explanation
* Metric definitions
* Limitations & assumptions

### GitHub Repo Structure

```
/data_ingestion
/transformations
/dashboard
/docs
README.md
```

### Narrative (Critical)

You should be able to answer:

* Why these metrics matter
* How on-chain data differs from TradFi
* What breaks at scale
* How this could evolve (indexer, smart contracts, MEV)

--------------------------------------------------------------------------------

## How This Bridges to Blockchain Development

Once this project exists, the next steps are natural:

### Data Analyst → Blockchain Engineer Path

1. Replace Etherscan with node RPCs
2. Decode contract ABIs
3. Track protocol-specific events
4. Build your own indexer
5. Write contracts whose data you already understand

This avoids the common trap:

> “I learned Solidity but don’t know what real blockchain data looks like.”

You will.

----------------------------------------------------------------------------------

## Reality Check (Important)

* This will **not** make you a blockchain dev yet
* It **will** make you credible
* It **will** give you something most beginners lack:
  **on-chain intuition + end-to-end data ownership**


