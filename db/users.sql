CREATE TABLE users (
    username VARCHAR(255) PRIMARY KEY,
    email VARCHAR(255) NOT NULL
);

INSERT INTO users (username, email)
VALUES
('ben1', 'ben1@example.com'),
('ben2', 'ben2@example.com'),
('ben3', 'ben3@example.com'),
('ben4', 'ben4@example.com');

