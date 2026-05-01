CREATE TABLE users (
    userid int PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (username, password) VALUES
('ben1', '$2b$12$Lznr.wwWGLbzEI8GuVD4jePR3g3Kt2cMtj0mh.DBPtZuKXG9cGTZG'), --password
('ben2', '$2b$12$wPDqOo7FjMh421y2Sd//lu5azF7b9jSCI/kdaGuhjQ/gDGhVvobEK'), --abc123
('ben3', '$2b$12$QU6IPO5F4Z1dBYntoBAhZuv89i8caFS5WmdhWAJy1Rbi/iU6JdI1a'), --secret
('ben4', '$2b$12$OZX9SyWduii7iTDfHi6xSOLy3DwH9qO2Iqqf/3Qpr5S8fjxnKC5I6'); --supersecret

