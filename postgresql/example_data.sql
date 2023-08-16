-- Create a sample table
CREATE TABLE sample_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Insert 5 sample rows
INSERT INTO sample_table (name) VALUES ('John');
INSERT INTO sample_table (name) VALUES ('Jane');
INSERT INTO sample_table (name) VALUES ('Doe');
INSERT INTO sample_table (name) VALUES ('Alice');
INSERT INTO sample_table (name) VALUES ('Bob');
