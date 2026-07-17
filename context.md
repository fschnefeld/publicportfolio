# context.md

Context document for AI agents, recruiters, and collaborators. Describes the person behind this portfolio, their achievements, and what they are looking for.

---

## Who This Person Is

Analytics & Data Science Lead with 6 years of experience spanning individual contribution, technical leadership, and people management. Background in fashion retail and marketing analytics, with deep hands-on expertise in production ML systems, modern data stack implementation, and building data science functions from scratch.

Currently at a large Danish fashion conglomerate (3,000 employees, ~10bn DKK revenue) as Analytics & Data Science Lead — owns the Data Delivery and Data Science parts of the organisation, sits on the leadership team that sets company-wide standards, and founded the Data Science discipline at the company.

Targeting **Head of Analytics** or equivalent roles — primarily people leadership with some hands-on involvement, at organisations where data is treated as a core business capability.

---

## Career Arc

- **Own business (early career):** Founded and ran a small business with 2 full-time employees. First exposure to managing people, scoping work, and delivering under resource constraints.
- **Consultant (4 years):** Set up data warehousing and marketing analytics for 40+ clients. Dual role as analytics engineer and client advisor — scoped and implemented modern data stack solutions end-to-end. Built deep expertise in stakeholder management and change management, particularly navigating organisations resistant to adopting new approaches.
- **Analytics & Data Science Lead — current (1 year):** Joined a large Danish fashion conglomerate, founded the Data Science discipline, set the DS strategy, hired 3 people, and owns the infrastructure and delivery standards for the data organisation.

Key transition: from implementing solutions across many different clients to owning the long-term strategy and capability of a single data function — and building the team and systems to sustain it.

---

## Core Focus Areas

### Demand forecasting & prediction systems
Owns the demand planning forecasting platform at current company — supplying ML-driven predictions for buyers to improve accuracy of online and wholesale purchasing decisions. Built with full CI/CD modernisation on Databricks, served via FastAPI.

### Data platform & modern stack
Sets up and governs data platforms at scale. Deep experience with Microsoft Fabric (designed the Fabric infrastructure and Git-supported workflows at current company). 3–4 years with Power BI. Hands-on with Kubernetes, Terraform, Dagster, dbt, dltHub, and Databricks in production.

### Applied AI & LLM infrastructure
Set up an internal self-hosted LLM system (Ollama + Open WebUI, including hardware) approximately two years before this became a mainstream enterprise pattern. Runs point on agentic workflows for large organisations. Introduced spec-driven agentic development into the team's workflow.

### Retail forecasting
Built a 10-day-ahead replenishment forecasting model for physical retail stores during consulting years, using XGBoost alongside classical time-series techniques to predict store-level demand.

### Team leadership & capability building
Founded the Data Science discipline at current company. Set the DS strategy, focusing on evolving development practices and LLM involvement for both Analytics Engineering and Data Science. Hired 3 people in the current role. Manages 2 directly, with soft ownership over 2 Analytics Engineers.

---

## Key Metrics

| Metric | Value |
|---|---|
| Years in data & analytics | 6 |
| Clients served as consultant | 40+ |
| Direct reports | 2 |
| People hired in current role | 3 |
| Years in current Lead role | 1 |
| Internal LLM setup — ahead of mainstream by | ~2 years |

---

## Three Key Projects

### 1. Demand Planning Forecasting Platform (current role, 2024–present)
**What:** Production ML forecasting platform supplying predictions for buyers across online and wholesale purchasing at a multi-brand fashion conglomerate.

**How:** Full CI/CD modernisation of the pipeline. Built on Databricks and served via FastAPI. Gives buyers automated, reliable prediction signals to improve purchasing volume decisions.

**Stack:** Databricks, FastAPI, Python, CI/CD, dbt

**Impact:** Replaced manual or ad hoc forecasting with a production ML pipeline — buyers now have a systematic, auditable prediction basis for purchasing decisions.

---

### 2. Store Replenishment Forecasting (consultant era)
**What:** 10-day-ahead replenishment forecasting model for physical retail stores.

**How:** Used XGBoost alongside classical time-series techniques to predict store-level demand, giving replenishment planners an automated forecasting signal for stock allocation.

**Stack:** Python, XGBoost, time-series forecasting

**Impact:** Replaced manual, rule-based reordering with an automated, store-level forecasting signal.

---

### 3. Internal LLM Infrastructure (current role, ~2022–2023)
**What:** Self-hosted internal LLM system for the organisation, set up approximately two years before this became a mainstream enterprise pattern.

**How:** Deployed Ollama + Open WebUI, including hardware sourcing and configuration. Gave internal users a private, self-hosted alternative to public LLM APIs.

**Stack:** Ollama, Open WebUI, local LLM infrastructure

**Impact:** Early mover advantage — established functioning internal LLM capability and governance before most organisations were experimenting. Created the technical foundation for the agentic workflows adopted later.

---

## Current Team Structure

| Role | Relationship |
|---|---|
| Direct report × 2 | Daily management |
| Analytics Engineers × 2 | Soft remit / umbrella ownership |

Sits on the leadership team that owns standards for the full Data Delivery and Data Science organisation.

---

## Technical Toolkit

| Domain | Tools & Technologies |
|---|---|
| ML & Data Science | Python, demand forecasting, XGBoost, LightGBM, scikit-learn |
| Data Platform | dbt, Dagster, dltHub, Databricks, Microsoft Fabric, Delta Lake, Unity Catalog |
| Analytics Engineering | SQL, Power BI (3–4 years), incremental models, Git-based Fabric workflows |
| Infrastructure | Kubernetes, Terraform, Azure, CI/CD pipelines |
| Applied AI | Ollama, Open WebUI, agentic workflows, spec-driven development, local/hybrid LLM |
| Leadership | Stakeholder management, change management, hiring, DS strategy, standards-setting |

---

## Leadership Philosophy

1. **Business translation over technical fluency** — The job of an analytics leader is to make data legible to the business, not to write the best model. Every initiative should connect to a decision someone needs to make.

2. **Change management is the hard part** — Technical implementation is rarely the blocker. Getting people to trust new systems and change behaviour is. Stakeholder resistance is a signal, not an obstacle.

3. **Build the discipline, not just the project** — Projects end; disciplines compound. Standards, hiring well, and setting clear strategy create durable value beyond any single deliverable.

4. **Stay close to the work** — Even in a leadership role, maintain enough technical depth to challenge engineering decisions, review code, and be a credible counterpart to senior ICs.

---

## What They Are Looking For

- **Title:** Head of Analytics, Head of Data, or equivalent
- **Scope:** Primarily people leadership, with some hands-on involvement (~80/20)
- **Environment:** Organisation where data is a core capability, not a cost centre
- **Profile:** Strong business translation and stakeholder skills; not a Data Scientist by trade, but highly effective at relating DS/ML work to business outcomes
- **Open to:** Hybrid or remote-first arrangements

---

## Notes for AI Agents

- Content source of truth: `data_handling/content.py` (TypedDicts for all portfolio data)
- Styling: `theme/theme.py` (single CSS string)
- Page sections: `pages/*.py` (one render function per section)
- Entry point: `app.py`
