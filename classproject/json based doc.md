**Case Study: FastAPI-Based REST Integration for HR Systems**

**Client:** Global Modern Services Corporation  
**System Objective:** Automate integration between Workday (HCM) and external systems (Microsoft Active Directory & HR Announcement Platform).

---

### 1. Overview
Global Modern Services Corporation (GMS) aims to automate two core HR integrations:

- **INT-002:** Automatically provision accounts in Microsoft Active Directory for new hires.
- **INT-003:** Notify the HR team of changes in marital status for active employees.

The solution leverages **FastAPI** to develop RESTful services that replace manual data transformation, scheduling, and delivery using modern, scalable backend architecture. This project supports real-time integration with data validation, file formatting, transformation using XSLT, email notification, and secure data transmission via SFTP.

---

### 2. System Architecture

| Layer | Technology/Tools Used |
|-------|------------------------|
| API Framework | FastAPI (Python 3.11+) |
| ORM | SQLAlchemy with Alembic for migrations |
| Scheduler | APScheduler (for job automation) |
| Database | PostgreSQL |
| File Handling | Built-in Python file I/O and XSLT via lxml |
| SFTP Transfer | Paramiko or pysftp |
| Notification | SMTP with email.mime and smtplib |
| Timezone Handling | pytz and datetime modules |
| Logging | Python logging with rotating file handlers |
| Security | OAuth2 JWT, HTTPS, dotenv for secrets |

---

### 3. Core Entities and Relationships

| Entity | Attributes | Description |
|--------|------------|-------------|
| `Worker` | `id`, `employee_id`, `first_name`, `last_name`, `user_name`, `hire_date`, `entry_date`, `status`, `marital_status`, `last_marital_status_update`, `termination_date` | Master data for all employees |
| `HireEvent` | `id`, `worker_id`, `entry_date`, `effective_hire_date`, `created_at`, `is_processed` | Stores new hire activity to drive INT-002 |
| `MaritalStatusChange` | `id`, `worker_id`, `new_status`, `change_date`, `effective_date`, `is_notified` | Logs all marital status transitions for INT-003 |
| `IntegrationLog` | `id`, `integration_type`, `status`, `file_name`, `generated_on`, `record_count`, `duration_ms`, `error_message` | Tracks every run of integrations |
| `Notification` | `id`, `log_id`, `email_sent_to`, `subject`, `body`, `sent_on`, `status`, `error` | Records email status and linkage to integration logs |

#### ER Diagram (Textual)
```
Worker --< HireEvent
Worker --< MaritalStatusChange
IntegrationLog --< Notification
IntegrationLog --< Worker (via events)
```

---

### 4. FastAPI Endpoint Summary

| Method | URL | Description |
|--------|-----|-------------|
| `POST` | `/workers/` | Create or update a worker (includes hire and marital status info) |
| `POST` | `/workers/{id}/hire` | Log hire event for a worker |
| `POST` | `/workers/{id}/marital-status` | Log marital status change event |
| `GET` | `/integrations/new-hires/export` | Trigger INT-002 and generate file |
| `GET` | `/integrations/marital-status/export` | Trigger INT-003 and generate XML file |
| `GET` | `/logs/` | Fetch history of integration runs |
| `GET` | `/notifications/send/{log_id}` | Manually trigger email for completed integration run |
| `GET` | `/files/download/{log_id}` | Download the generated file for review/audit |

#### Sample JSON Response: `/integrations/new-hires/export`
```json
{
  "status": "success",
  "integration_type": "INT-002",
  "file": "examone_hire_account_04_15_2025_16_30_00_001.txt",
  "record_count": 2,
  "timestamp": "2025-04-15T16:30:00+00:00"
}
```

#### Sample JSON Response: `/integrations/marital-status/export`
```json
{
  "status": "success",
  "integration_type": "INT-003",
  "file": "examone_datachg_maritalstatus_04_15_2025_16_30_00_001.xml",
  "record_count": 1,
  "timestamp": "2025-04-15T16:30:00+00:00"
}
```

---

### 5. Integration Logic Details

#### INT-002: New Hire to Active Directory
- **Data Source**: `Worker` + `HireEvent`
- **Selection Criteria**:
  - Worker.status == 'Active'
  - Hire date is **not future-dated** (<= today)
  - Entry date within last 24 hours (simulated change detection)
- **Transformation Logic**:
  - `EMPLOYEEID`: Padded to 10 chars (left-aligned)
  - `FNAME`: Uppercase, 5 characters max, right-padded
  - `LNAME`: Uppercase, 15 characters max, right-padded
  - `ADUSERNAME`: "ad_" + user_name or first initial + last name (lowercase, 15 chars max)
  - Add header row with column names
  - Add footer row: `COUNT     |<timestamp>` (COUNT is left-aligned, timestamp from system clock)
- **Delivery**:
  - Output file format: `.txt` (vertical bar delimited)
  - Upload to SFTP folder (with credentials and path from `.env`)
  - Archive file and log result
- **Retention**: 30 days (auto-clean job to delete old files)

#### INT-003: Marital Status Change Notification
- **Data Source**: `Worker` + `MaritalStatusChange`
- **Selection Criteria**:
  - Effective date = today
  - Worker.status == 'Active'
- **Transformation Logic**:
  - XML format with:
    - `<Employee_ID>`, `<First_Name>`, `<Last_Name>`, `<CHANGED_MS>`
    - Format driven by schema or XSLT (for advanced use cases)
- **Delivery**:
  - Send file to SFTP in secure XML format
  - Update logs with timestamps and row counts
- **Notification**:
  - Trigger email on successful run completion
  - SMTP credentials securely stored in `.env`
  - Subject: *HR Announcements Integration Fired.*
  - Body: *HR Marital Status changes have occurred. Check for announcement events.*
  - Recipient: Project admin (configurable)

---

### 6. Sample Outputs

#### INT-002: Hire File Sample
```
EMPLOYEEID|FNAME|LNAME          |ADUSERNAME     |EFFECTDATE|ENTRYDATE
21001     |LOGAN|MCNEIL         |ad_lmcneil     |2023-10-03|2023-10-03T13:46:48.531
COUNT     1|2024-10-04T18:17:52.498+05:30
```

#### INT-003: Marital Status Change XML
```xml
<Worker>
    <Employee_ID>21001</Employee_ID>
    <First_Name>Logan</First_Name>
    <Last_Name>McNeil</Last_Name>
    <CHANGED_MS>Married</CHANGED_MS>
</Worker>
```

---

### 7. Scheduling & Sequence
- **Scheduler**: APScheduler (background task + cron-style job)
- **Execution Time**: Daily at 4:30 PM Pacific (adjusted to UTC based on server location)
- **Sequence & File Naming**:
  - Pattern: `examone_hire_account_MM_DD_YYYY_HH_MM_SS_SEQ.txt`
  - Pattern: `examone_datachg_maritalstatus_MM_DD_YYYY_HH_MM_SS_SEQ.xml`
  - Sequence ID: Auto-incremented integer managed in DB

---

### 8. Testing & Simulation Data

| Test Case | Input Details | Expected Output |
|-----------|---------------|-----------------|
| Past-Dated Hire | Name: ExamOne PastDated, Hire Date: 01-Jan-2018 | Included in INT-002 |
| Current Hire | Name: ExamOne Current, Hire Date: Today | Included in INT-002 |
| Future Hire | Name: ExamOne Future, Hire Date: 01-Dec-2025 | Excluded |
| FtoCurr1 | Hire Date: Today + 1 Day | Excluded until future date |
| FtoCurr2 | Hire Date: Today + 2 Days | Excluded |
| Marital Change | Kevin Gibson, Married today | Included in INT-003 |
| Gender Change | Meg Saunders, Gender update | Excluded |
| Termination | Aidan Mitzner, Voluntary | Excluded |

---

### 9. Security and Access Control
- All endpoints secured using OAuth2 with JWT Bearer tokens
- Encrypted environment variables for credentials using `.env` + `python-decouple`
- Audit trails with IP logs, timestamps, and user IDs
- Access control based on roles (admin, read-only, scheduler)
- File integrity validated using checksum during file upload

---

