from typing import TypedDict


class Stat(TypedDict):
    num: str
    label: str


class Skill(TypedDict):
    icon: str
    title: str
    body: str
    tags: list[str]


class Project(TypedDict):
    num: str
    title: str
    body: str
    pills: list[str]
    impact: str
    year: str


class Principle(TypedDict):
    num: str
    title: str
    body: str


class TeamMember(TypedDict):
    role: str
    badge_class: str
    badge_label: str


STATS: list[Stat] = [
    {"num": "8+", "label": "Years in analytics &amp; data science"},
    {"num": "12", "label": "Direct &amp; indirect reports managed"},
    {"num": "3", "label": "Production ML systems shipped"},
    {"num": "32", "label": "Markets covered by live forecasting platform"},
]

SKILLS: list[Skill] = [
    {
        "icon": "◉",
        "title": "ML & Forecasting Systems",
        "body": (
            "Designed and shipped production forecasting pipelines for 32 markets and 14 SKU families, "
            "using multi-model cascades (Prophet, ARIMA, Croston, LightGBM) with automated champion selection "
            "and continuous backtesting."
        ),
        "tags": ["Prophet", "LightGBM", "EM", "ARIMA", "MLflow", "Backtesting"],
    },
    {
        "icon": "◈",
        "title": "Data Platform Architecture",
        "body": (
            "Own end-to-end data platform decisions: from source ingestion to BI-ready marts. "
            "Deep experience structuring dbt projects, defining materialization strategies, "
            "and designing Dagster asset graphs for daily production jobs."
        ),
        "tags": ["dbt", "Dagster", "Databricks", "Microsoft Fabric", "Delta Lake"],
    },
    {
        "icon": "◇",
        "title": "Analytics Engineering",
        "body": (
            "Built layered ABT model architectures powering both BI (Power BI) and data science consumers. "
            "Comfortable writing and reviewing complex SQL — window functions, incremental models, "
            "fan-out analysis, anomaly investigation."
        ),
        "tags": ["SQL", "T-SQL / Synapse", "Power BI", "Incremental Models"],
    },
    {
        "icon": "△",
        "title": "Infrastructure & DevOps",
        "body": (
            "Led platform teams with skills in Kubernetes, Terraform, and cloud infrastructure. "
            "Managed skills matrices, defined coverage requirements, and drove hiring decisions "
            "to close critical single-points-of-failure."
        ),
        "tags": ["Kubernetes", "Terraform", "Azure", "CI/CD"],
    },
    {
        "icon": "⬡",
        "title": "Team Leadership & Growth",
        "body": (
            "Built and structured multi-disciplinary data teams. Own the skills matrix, "
            "quarterly capability reviews, onboarding, and individual growth plans. "
            "Passionate about closing expertise gaps through deliberate hiring and learning paths."
        ),
        "tags": ["People Management", "Hiring", "Skills Frameworks", "1:1s"],
    },
    {
        "icon": "◻",
        "title": "Technical Strategy & Documentation",
        "body": (
            "Author Architecture Decision Records, user stories, and system documentation "
            "that align engineering decisions with business goals. Strong communicator "
            "across technical and non-technical stakeholders."
        ),
        "tags": ["ADRs", "Roadmapping", "Stakeholder Comms", "OKRs"],
    },
]

PROJECTS: list[Project] = [
    {
        "num": "01",
        "title": "Demand Planning Forecasting Platform",
        "body": (
            "Architected and delivered a production multi-model forecasting system covering 32 markets "
            "and 14 SKU families. The pipeline runs a model cascade (Prophet → ETS → ARIMA → Croston) "
            "per platform/brand combination, with automated champion selection via cross-validation "
            "and continuous backtesting against actuals. Integrated a variant-aware feature store "
            "resolving style, platform, and seasonality signals at prediction time."
        ),
        "pills": ["Prophet", "LightGBM", "MLflow", "Dagster", "dbt", "Databricks"],
        "impact": "↑ Forecast accuracy across 32 markets · Multi-model champion selection in production",
        "year": "2025–2026",
    },
    {
        "num": "02",
        "title": "ABT Data Architecture Restructure",
        "body": (
            "Led the redesign of the core analytics base table (ABT) layer supporting both BI "
            "and data science consumers. Consolidated business logic into a single abt_salesonline "
            "model, introduced separate folder structures for YODA-bound and data science models, "
            "de-scoped the demand planning job to only run actuals-producing models, "
            "and reduced duplication across daily/weekly/monthly aggregations."
        ),
        "pills": ["dbt", "Dagster", "Microsoft Fabric", "Power BI", "SQL"],
        "impact": "Eliminated logic duplication · Aligned BI and Data Science data contracts",
        "year": "2026",
    },
    {
        "num": "03",
        "title": "Team Skills Repository & Capability Framework",
        "body": (
            "Designed and implemented a structured skills repository covering 7 core technologies "
            "across a 14-person team (beginner / mid / expert). Used to identify single-points-of-failure "
            "(Terraform, Kubernetes concentrated in 1–2 people), inform hiring prioritisation, "
            "and build individual learning paths. Updated quarterly."
        ),
        "pills": ["People Leadership", "Skills Assessment", "Hiring Strategy", "Documentation"],
        "impact": "Surfaced 3 critical coverage gaps · Drove 2 targeted hires",
        "year": "2025",
    },
    {
        "num": "04",
        "title": "Cold-Start Forecasting with Expectation Maximization",
        "body": (
            "Explored and prototyped EM-based matrix factorisation to solve the cold-start problem "
            "for new styles and low-volume platform/brand combinations. The approach leverages "
            "shared latent factors (brand affinity, platform effect, seasonality) estimated from "
            "rich data to make principled predictions for sparse series — avoiding the instability "
            "of Prophet on insufficient data."
        ),
        "pills": ["Expectation Maximization", "Matrix Factorisation", "Python", "Sparse Demand"],
        "impact": "Extended forecast coverage to new style launches",
        "year": "2025",
    },
]

PRINCIPLES: list[Principle] = [
    {
        "num": "01",
        "title": "Systems over heroics",
        "body": (
            "I build processes — ADRs, skills matrices, documentation, deployment standards — "
            "so the team isn't dependent on any one person, including me."
        ),
    },
    {
        "num": "02",
        "title": "Technical credibility earns trust",
        "body": (
            "I stay close to the craft. I review code, challenge architectural decisions, "
            "and pair on hard problems. People follow leaders who understand the work."
        ),
    },
    {
        "num": "03",
        "title": "Clarity before consensus",
        "body": (
            "I'd rather write a clear ADR that people disagree with than run an ambiguous "
            "discussion that ends without a decision. Alignment comes after clarity, not before."
        ),
    },
    {
        "num": "04",
        "title": "Grow the team's ceiling, not just output",
        "body": (
            "Career development is a first-class responsibility. I invest time in skill frameworks, "
            "deliberate stretch assignments, and making growth visible in the organisation."
        ),
    },
]

TEAM: list[TeamMember] = [
    {"role": "Lead Data Scientist — Forecasting", "badge_class": "badge-ds", "badge_label": "DATA SCIENCE"},
    {"role": "ML Engineer — Pipelines", "badge_class": "badge-ds", "badge_label": "DATA SCIENCE"},
    {"role": "Data Platform Lead", "badge_class": "badge-eng", "badge_label": "ENGINEERING"},
    {"role": "Senior Data Engineer × 2", "badge_class": "badge-eng", "badge_label": "ENGINEERING"},
    {"role": "Data Engineer × 4", "badge_class": "badge-eng", "badge_label": "ENGINEERING"},
    {"role": "Analytics Engineer × 3", "badge_class": "badge-analytics", "badge_label": "ANALYTICS"},
    {"role": "Data Analyst × 3", "badge_class": "badge-analytics", "badge_label": "ANALYTICS"},
]
