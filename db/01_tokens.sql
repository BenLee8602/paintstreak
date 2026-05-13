CREATE TABLE tokens (
    token VARCHAR(255) PRIMARY KEY,
    userid int NOT NULL,
    expires TIMESTAMP NOT NULL,
    CONSTRAINT fk_user FOREIGN KEY (userid) REFERENCES users(userid)
);

