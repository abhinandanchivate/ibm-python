Client (Frontend or Mobile App)
      ↓
   FastAPI App
  ┌─────────────┐
  │  Routers    │  ← define endpoints
  └────┬────────┘
       ↓
  ┌─────────────┐
  │ Dependencies│  ← Dependency Injection (DI)
  └────┬────────┘
       ↓
  ┌─────────────┐
  │  Services   │  ← Business logic
  └────┬────────┘
       ↓
  ┌─────────────┐
  │   Models    │  ← Pydantic (request/response) & SQLAlchemy (DB models)
  └────┬────────┘
       ↓
  ┌─────────────┐
  │  Database   │  ← PostgreSQL, MySQL, MongoDB, etc.
  └─────────────┘
