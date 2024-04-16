CREATE DATABASE sqlvulndb;

CREATE TABLE users(
    user_id uuid PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_name VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    user_address VARCHAR(255),
    last_purchase VARCHAR(255)
);

INSERT INTO users(user_name, user_password, user_address, last_purchase) VALUES
('jason', 'k25sal', '200 George St', 'Brioche Bread'),
('kitty', 'z942ja', '123 Haymarket', 'Sourdough Bread'),
('dini', 'znfw234', 'yo mama house idk', 'INTRO_TO_CTF{i_Love_Eating_Bred}');