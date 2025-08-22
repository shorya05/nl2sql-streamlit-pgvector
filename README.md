# NL2SQL + pgvector

🧭 **Natural Language to SQL Query Interface** using PostgreSQL, pgvector, and a small LLM (Flan-T5). This project allows you to ask natural language questions about employees, departments, and orders, and get SQL results with semantic search capabilities.

---

## Table of Contents

- [Objective](#objective)
- [Tech Stack](#tech-stack)
- [Database Schema](#database-schema)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Objective

Build a prototype that allows users to query a PostgreSQL database using natural language. The system also supports semantic search using vector embeddings.

---

## Tech Stack

- **Backend & SQL**: Python, SQLAlchemy, PostgreSQL
- **Vector Search**: pgvector
- **LLM (Language Model)**: Hugging Face `flan-t5-small`
- **Web Interface**: Streamlit
- **Python Libraries**: `transformers`, `torch`, `psycopg2-binary`, `sqlalchemy`
- **Deployment / DevOps**: Docker (optional)

---

## Database Schema

### 1️⃣ Employees
| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | SERIAL PRIMARY KEY | Unique identifier |
| name        | VARCHAR(100) | Full name |
| department_id | INT | Foreign key → departments.id |
| email       | VARCHAR(255) | Email address |
| salary      | DECIMAL(10,2) | Monthly salary |

### 2️⃣ Departments
| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | SERIAL PRIMARY KEY | Unique department ID |
| name        | VARCHAR(100) | Department name (HR, Engineering, etc.) |

### 3️⃣ Orders
| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | SERIAL PRIMARY KEY | Unique order ID |
| customer_name | VARCHAR(100) | Customer name |
| employee_id | INT | Foreign key → employees.id |
| order_total | DECIMAL(10,2) | Total amount |
| order_date  | DATE | Date of order |

### 4️⃣ Products
| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| id          | SERIAL PRIMARY KEY | Unique product ID |
| name        | VARCHAR(100) | Product name |
| price       | DECIMAL(10,2) | Price per unit |

**Relationships**:

- `employees.department_id → departments.id`
- `orders.employee_id → employees.id`

---

## Setup

1. **Clone the repo**
```bash
git clone https://github.com/shorya05/nl2sql-streamlit-pgvector.git
cd nl2sql-streamlit-pgvector

2. Create Python environment

conda create -n nl2sql python=3.11
conda activate nl2sql
pip install -r requirements.txt


Set up PostgreSQL database

Create database and user.

Run setup_db.py to create tables and populate sample data.

Set your environment variables

OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=postgresql://user:password@localhost:5432/your_db


Download LLM model

git lfs install
git clone https://huggingface.co/google/flan-t5-small flan-t5-small

Usage

Run the Streamlit app:

streamlit run app.py


Features:

Ask natural language questions about employees, departments, or orders.

Semantic search for similar names or products using vector embeddings.

Hybrid search: SQL + pgvector.

Example Queries:

Show top 5 employees by salary

Who earns the most in Sales?

List employees in Engineering with salary > 65000

Find employees similar to "Alice"
