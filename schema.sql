CREATE TABLE IF NOT EXISTS companies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    ticker TEXT UNIQUE,
    sector TEXT,
    industry TEXT,
    country TEXT,
    market_cap REAL,
    pe_ratio REAL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
