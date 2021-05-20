CREATE TABLE IF NOT EXISTS entries (
    id SERIAL PRIMARY KEY,
    title VARCHAR,
    date DATE,
    keywords VARCHAR,
    description VARCHAR,
    decision VARCHAR
    user_id INTEGER REFERENCES users(id);
);