-- Table to store user information
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    user_surname VARCHAR(255) NOT NULL,
    user VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    user_token VARCHAR(16) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL
);

-- Table to store friendship information
CREATE TABLE friends (
    user_id INTEGER REFERENCES users(user_id) NOT NULL,
    friend_id INTEGER REFERENCES users(user_id) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    PRIMARY KEY (user_id, friend_id)
);

-- Table to store chat information
CREATE TABLE chats (
    chat_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL
);

-- Table to store chat membership information
CREATE TABLE chat_members (
    chat_id INTEGER REFERENCES chats(chat_id) NOT NULL,
    user_id INTEGER REFERENCES users(user_id) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    PRIMARY KEY (chat_id, user_id)
);

-- Table to store messages
CREATE TABLE messages (
    message_id SERIAL PRIMARY KEY,
    chat_id INTEGER REFERENCES chats(chat_id) NOT NULL,
    sender_id INTEGER REFERENCES users(user_id) NOT NULL,
    message TEXT NOT NULL,
    message_time TIMESTAMP NOT NULL
);


CREATE TABLE income_outcome (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    income_outcome BOOLEAN NOT NULL,
    amount NUMERIC(10,2) NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE plans (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    target NUMERIC(10,2) NOT NULL,
    description VARCHAR(255) NOT NULL
);