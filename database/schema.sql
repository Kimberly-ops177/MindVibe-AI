-- database/schema.sql
CREATE DATABASE IF NOT EXISTS mindvibe_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE mindvibe_db;
CREATE TABLE IF NOT EXISTS entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL,
    mood_label VARCHAR(128),
    mood_scores JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4;