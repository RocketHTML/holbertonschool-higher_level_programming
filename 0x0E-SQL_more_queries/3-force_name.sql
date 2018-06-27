-- This command creates a table named force_name, it shouldn't fail if table exists
CREATE TABLE IF NOT EXISTS force_name (
id INT(6), name VARCHAR(256) NOT NULL
);
