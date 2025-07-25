# personal-finance-tool

A personal budgeting tool built with Python (FastAPI), PostgreSQL and React.

##Features
- Track expenses and income
- Categorize entries
- Create monthly budgets
- Analyze spending patterns
- Export to Excel

## Tech Stack
- **Frontend**: React
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Deployment**: Docker (optional)

## Project Structure
Explain briefly what's in `/backend`, `/frontend`, etc.

## Database Scheme

![E/R Diagram](docs/budgettool-er.png)

See `backend/database/schema.sql` for full table definitions.

## 🚀 Getting Started
### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
