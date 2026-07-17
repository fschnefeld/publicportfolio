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
    {"num": "6", "label": "Years in analytics &amp; data"},
    {"num": "40+", "label": "Client data stacks built"},
    {"num": "3", "label": "Production ML systems shipped"},
    {"num": "3", "label": "People hired &amp; developed"},
]

SKILLS: list[Skill] = [
    {
        "icon": "◉",
        "title": "ML & Forecasting Systems",
        "body": (
            "Architected and shipped a production demand planning platform supplying predictions "
            "for wholesale and online buyers at a multi-brand fashion group. "
            "Full CI/CD modernisation built on Databricks and FastAPI, "
            "with multi-model cascades and automated champion selection."
        ),
        "tags": ["Python", "Databricks", "FastAPI", "LightGBM", "Prophet", "MLflow"],
    },
    {
        "icon": "◈",
        "title": "Data Platform Architecture",
        "body": (
            "Own end-to-end data platform decisions from source ingestion to BI-ready marts. "
            "Set up the Microsoft Fabric infrastructure at current company and designed "
            "the Git-supported deployment workflows. Deep experience with dbt project structure, "
            "Dagster asset graphs, and materialisation strategies for daily production jobs."
        ),
        "tags": ["dbt", "Dagster", "dltHub", "Databricks", "Microsoft Fabric", "Delta Lake"],
    },
    {
        "icon": "◇",
        "title": "Analytics Engineering",
        "body": (
            "3–4 years hands-on with Power BI alongside deep SQL and dbt experience. "
            "Built ABT model architectures serving both BI and data science consumers. "
            "Designed Git-supported deployment workflows in Microsoft Fabric "
            "and comfortable reviewing complex analytical SQL at scale."
        ),
        "tags": ["SQL", "Power BI", "dbt", "Incremental models", "Microsoft Fabric"],
    },
    {
        "icon": "△",
        "title": "Infrastructure & DevOps",
        "body": (
            "Hands-on with the full modern data infrastructure stack in production: "
            "Kubernetes, Terraform, Azure, and container-based CI/CD pipelines. "
            "Comfortable setting engineering standards and reviewing infrastructure "
            "decisions across the stack."
        ),
        "tags": ["Kubernetes", "Terraform", "Azure", "CI/CD", "Docker"],
    },
    {
        "icon": "⬡",
        "title": "Applied AI & LLM Systems",
        "body": (
            "Set up an internal self-hosted LLM system — Ollama + Open WebUI including hardware — "
            "approximately two years before this became a mainstream enterprise pattern. "
            "Runs point on agentic workflows for large organisations and introduced "
            "spec-driven agentic development into the team's workflow."
        ),
        "tags": ["Ollama", "Open WebUI", "Agentic workflows", "Local LLM", "Spec-driven dev"],
    },
    {
        "icon": "◻",
        "title": "Stakeholder & Change Management",
        "body": (
            "Developed over four years as a consultant working with 40+ clients — "
            "scoping and delivering modern data stack solutions while managing "
            "stakeholders resistant to change. "
            "Comfortable leading decisions where people feel they have something to lose."
        ),
        "tags": ["Stakeholder management", "Change management", "Consulting", "Scoping"],
    },
]

PROJECTS: list[Project] = [
    {
        "num": "01",
        "title": "Demand Planning Forecasting Platform",
        "body": (
            "Architected and delivered a production ML forecasting platform supplying "
            "predictions for buyers across online and wholesale purchasing at a "
            "multi-brand Danish fashion group. "
            "Led a full CI/CD modernisation — moving to Databricks and FastAPI — "
            "replacing ad hoc models with an automated, auditable pipeline buyers use daily."
        ),
        "pills": ["Python", "Databricks", "FastAPI", "dbt", "CI/CD", "MLflow"],
        "impact": "Buyer-facing ML predictions in daily use · full pipeline modernisation",
        "year": "2024–2025",
    },
    {
        "num": "02",
        "title": "Store Replenishment Forecasting",
        "body": (
            "Built a 10-day-ahead replenishment forecasting model for physical retail stores, "
            "using XGBoost alongside classical time-series techniques to predict store-level "
            "demand — giving replenishment planners a reliable, automated signal for stock "
            "allocation instead of manual, rule-based reordering."
        ),
        "pills": ["Python", "XGBoost", "Time Series", "Forecasting"],
        "impact": "10-day-ahead store-level forecasts · automated replenishment signal",
        "year": "2023",
    },
    {
        "num": "03",
        "title": "Internal LLM Infrastructure",
        "body": (
            "Set up a self-hosted internal LLM system — Ollama + Open WebUI, including hardware "
            "sourcing and configuration — approximately two years before this became a mainstream "
            "enterprise pattern. Gave the organisation a private inference capability "
            "and laid the technical groundwork for the agentic workflows adopted later."
        ),
        "pills": ["Ollama", "Open WebUI", "Local LLM", "Infrastructure"],
        "impact": (
            "Private LLM capability ~2 years ahead of mainstream · "
            "foundation for later agentic work"
        ),
        "year": "2022–2023",
    },
]

PRINCIPLES: list[Principle] = [
    {
        "num": "01",
        "title": "Translate data into decisions",
        "body": (
            "The job of an analytics leader is to make data legible to the business. "
            "Every initiative should connect to a decision someone needs to make — "
            "not a metric someone is vaguely interested in."
        ),
    },
    {
        "num": "02",
        "title": "Change management is the hard part",
        "body": (
            "Technical implementation is rarely the blocker. Getting people to trust new systems "
            "and actually change behaviour is. Stakeholder resistance is a signal — "
            "it usually means someone feels they have something to lose."
        ),
    },
    {
        "num": "03",
        "title": "Build the discipline, not just the project",
        "body": (
            "Projects end; disciplines compound. Investing in clear standards, deliberate hiring, "
            "and a coherent strategy creates value that outlasts any single deliverable."
        ),
    },
    {
        "num": "04",
        "title": "Stay close to the work",
        "body": (
            "Even in a leadership role, I maintain enough technical depth to challenge engineering "
            "decisions, review code, and be a credible counterpart to senior ICs. "
            "Technical credibility is earned, not assumed."
        ),
    },
]

TEAM: list[TeamMember] = [
    {"role": "Data Science", "badge_class": "badge-ds", "badge_label": "DIRECT REPORT"},
    {"role": "Data Delivery", "badge_class": "badge-ds", "badge_label": "DIRECT REPORT"},
    {
        "role": "Analytics Engineer × 2",
        "badge_class": "badge-analytics",
        "badge_label": "SOFT REMIT",
    },
]
