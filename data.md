

## 📚 **Master TOC – Full Guide to dbt (Data Build Tool)**

| S. No | Module | Topics Covered |
|-------|--------|----------------|
| **1** | 🔍 **Introduction to dbt** | <ul><li>What is dbt?</li><li>Key concepts: ELT vs ETL, Analytics Engineering</li><li>How dbt fits into the modern data stack</li><li>dbt CLI vs dbt Cloud</li></ul> |
| **2** | ⚙️ **Installation and Project Setup** | <ul><li>Installing dbt via pip</li><li>Initializing a dbt project (`dbt init`)</li><li>Folder structure explained</li><li>Connecting to data warehouses (BigQuery, Snowflake, Redshift, Postgres)</li></ul> |
| **3** | 🧱 **dbt Models (Core of dbt)** | <ul><li>What is a dbt model?</li><li>Writing SQL models using `SELECT` statements</li><li>Model dependencies using `ref()`</li><li>Materializations: `view`, `table`, `incremental`, `ephemeral`</li></ul> |
| **4** | 🧪 **Testing in dbt** | <ul><li>Built-in tests: `unique`, `not_null`, `accepted_values`, `relationships`</li><li>Custom tests using SQL and Jinja</li><li>Schema.yml test definitions</li><li>Running tests with `dbt test`</li></ul> |
| **5** | 🧾 **Documentation & Lineage** | <ul><li>Creating documentation with `dbt docs generate`</li><li>Lineage graph using `dbt docs serve`</li><li>Documenting models, columns, and tests</li><li>dbt Metadata</li></ul> |
| **6** | 🧮 **Jinja & Macros** | <ul><li>Templating with Jinja</li><li>Using variables, control flow (`if`, `for`)</li><li>Creating and using macros</li><li>Hooks & Operations</li></ul> |
| **7** | 🔁 **Incremental Models** | <ul><li>What is an incremental model?</li><li>Using `is_incremental()`</li><li>Managing historical data</li><li>Performance tuning tips</li></ul> |
| **8** | 🌍 **Environment Config & Versioning** | <ul><li>Using `dbt_project.yml`</li><li>Environments and targets (`dev`, `prod`)</li><li>vars, profiles.yml, secrets handling</li><li>Modular project structures</li></ul> |
| **9** | 🔄 **dbt Run & Build Lifecycle** | <ul><li>What happens in `dbt run`?</li><li>Model DAG generation</li><li>Using `dbt build` vs `run`</li><li>Execution order, ref(), and dependencies</li></ul> |
| **10** | 🧵 **Sources and Snapshots** | <ul><li>Using `source()`</li><li>Source freshness testing</li><li>Snapshotting slowly changing dimensions (SCD Type 2)</li><li>Use-cases and examples</li></ul> |
| **11** | 🧰 **Packages and Modularization** | <ul><li>Installing and using dbt packages</li><li>Creating reusable macros & packages</li><li>dbt Hub</li></ul> |
| **12** | 🛠️ **CI/CD and Deployment** | <ul><li>dbt Cloud job setup</li><li>GitHub Actions / GitLab CI pipelines</li><li>Testing, building, and deploying dbt projects</li><li>Alerting and scheduling</li></ul> |
| **13** | 🔒 **Security and Access Control** | <ul><li>Role-based access in dbt Cloud</li><li>Warehouse-specific permissions</li><li>Limiting user access to models</li></ul> |
| **14** | 📈 **Monitoring, Logging, and Observability** | <ul><li>dbt artifacts: `manifest.json`, `run_results.json`</li><li>Integration with observability tools (Monte Carlo, DataDog)</li><li>Logging success/failure</li></ul> |
| **15** | 📊 **Advanced Topics** | <ul><li>dbt Semantic Layer (Metrics Layer)</li><li>dbt with Python (dbt-python)</li><li>Building custom adapters</li><li>Unit testing with dbt-core and pytest-dbt</li></ul> |

---

## 🧪 Sample Hands-on Tasks

| Task | Command |
|------|---------|
| Initialize project | `dbt init my_project` |
| Run all models | `dbt run` |
| Test models | `dbt test` |
| Generate docs | `dbt docs generate` |
| Serve docs locally | `dbt docs serve` |
| Build DAG graph | `dbt build` |
| Snapshot a table | `dbt snapshot` |
| Debug profile/connection | `dbt debug` |

---

## 📂 Standard Project Structure

```
my_dbt_project/
│
├── models/
│   ├── staging/
│   ├── marts/
│   └── core/
│
├── snapshots/
├── tests/
├── macros/
├── dbt_project.yml
└── profiles.yml (in ~/.dbt/)
```

