CREATE TABLE users(
    user_id         UUID PRIMARY KEY,
    first_name      TEXT,
    last_name       TEXT,
    email           TEXT UNIQUE NOT NULL,
    password_hash   TEXT NOT NULL, 
    created_at      TIMESTAMP DEFAULT NOW()
);

CREATE TABLE categories(
    category_name   TEXT PRIMARY KEY,
    color           TEXT
); 

CREATE TABLE budgets(
    budget_id       UUID PRIMARY KEY,
    budget_name     TEXT NOT NULL, 
    start_date      DATE NOT NULL, 
    end_date        DATE NOT NULL, 
    user_id         UUID NOT NULL,

    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE entries(
    entry_id        UUID PRIMARY KEY,
    amount          NUMERIC NOT NULL, 
    entry_date      DATE NOT NULL,
    entry_name      TEXT NOT NULL,
    type            TEXT CHECK (type IN ('income', 'expense')), 
    notes           TEXT,
    user_id         UUID NOT NULL,
    budget_id       UUID NOT NULL,
    category_name   TEXT NOT NULL,

    FOREIGN KEY user_id REFERENCES users(user_id),
    FOREIGN KEY budget_id REFERENCES budgets(budget_id),
    FOREIGN KEY category_name REFERENCES categories(category_name)    
);

CREATE TABLE recurring_entries(
    recurring_id    UUID PRIMARY KEY,
    entry_id        UUID NOT NULL,
    frequency       TEXT CHECK (frequency IN ('daily', 'weekly', 'monthly', 'yearly')),

    FOREIGN KEY entry_id REFERENCES entries(entry_id)
);