CREATE TABLE game_instances(
    id SERIAL PRIMARY KEY,
    code VARCHAR(5) NOT NULL UNIQUE,
    name TEXT NOT NULL,
    status TEXT NOT NULL,
    length TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    title TEXT,
    first_name TEXT,
    last_name TEXT,
    portrait TEXT,
    public_description TEXT,
    private_description_cover_story TEXT,
    private_description_truth TEXT,
    starting_information_other_characters TEXT,
    starting_information_hints TEXT,
    character_secret TEXT,
    character_clue TEXT,
    primary_goal TEXT,
    secondary_goal TEXT,
    tertiary_goal TEXT,
    round_one_reveal JSON,
    round_two_reveal JSON,
    round_three_reveal JSON,
    starting_inventory TEXT[],
    abilites TEXT[]
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    type TEXT NOT NULL,
    uses INT
);

CREATE TABLE abilites(
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    type TEXT NOT NULL
);

CREATE TABLE player_characters (
    id SERIAL PRIMARY KEY,
    game VARCHAR(5) NOT NULL REFERENCES game_instances(code),
    email TEXT NOT NULL,
    character_id INT REFERENCES characters(id),
    primary_player BOOLEAN DEFAULT FALSE NOT NULL, 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE player_items (
    id SERIAL PRIMARY KEY,
    item_id INT REFERENCES items(id),
    player_id INT REFERENCES player_characters(id),
    uses_remaining INT
);

CREATE TABLE game_log(
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    player_char_id INT REFERENCES player_characters(id) ,
    action_type TEXT,
    action_information JSON
);

CREATE TABLE chat(
    id SERIAL PRIMARY KEY,
    game VARCHAR(5) NOT NULL REFERENCES game_instances(code),
    room TEXT NOT NULL,
    player INT REFERENCES characters(id),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- SELECT
--   'DROP TABLE IF EXISTS "' || tablename || '" CASCADE;' 
-- from
--   pg_tables WHERE schemaname = 'public';