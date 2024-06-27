-- Script to initialize football collection database

-- Create tables
CREATE TABLE IF NOT EXISTS leagues (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(255) NOT NULL,
    season YEAR(4) NOT NULL
);

CREATE TABLE IF NOT EXISTS teams (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(255),
    league_id INT,
    FOREIGN KEY (league_id) REFERENCES leagues(id)
);

CREATE TABLE IF NOT EXISTS matches (
    id INT AUTO_INCREMENT PRIMARY KEY,
    league_id INT,
    home_team_id INT,
    away_team_id INT,
    match_date DATE,
    result VARCHAR(10),
    home_goals INT,
    away_goals INT,
    FOREIGN KEY (league_id) REFERENCES leagues(id),
    FOREIGN KEY (home_team_id) REFERENCES teams(id),
    FOREIGN KEY (away_team_id) REFERENCES teams(id)
);

-- Insert initial data
INSERT INTO leagues (name, country, season)
VALUES ('Premier League', 'England', '2024'),
       ('La Liga', 'Spain', '2024'),
       ('Serie A', 'Italy', '2024');

INSERT INTO teams (name, country, league_id)
VALUES ('Chelsea FC', 'England', 1),
       ('Real Madrid', 'Spain', 2),
       ('Juventus', 'Italy', 3);

INSERT INTO matches (league_id, home_team_id, away_team_id, match_date, result, home_goals, away_goals)
VALUES (1, 1, 2, '2024-06-26', '3-1', 3, 1),
       (2, 3, 1, '2024-06-27', '2-2', 2, 2),
       (1, 2, 1, '2024-06-28', '1-0', 1, 0);

-- Add indexes for faster queries
CREATE INDEX idx_league_id ON teams (league_id);

