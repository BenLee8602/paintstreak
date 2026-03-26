CREATE TABLE users (
    userid int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password)
VALUES
('ben1', 'password'),
('ben2', 'abc123'),
('ben3', 'secret'),
('ben4', 'supersecret');

