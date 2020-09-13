CREATE TABLE game_instances(
    id SERIAL PRIMARY KEY,
    code VARCHAR(5) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE log(
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    player_char_id INT REFERENCES ,
    action_type TEXT,
    action_information JSON,
    CONSTRAINT fk_player_id
        FOREIGN KEY (player_char_id)
            REFERENCES player_characters(id)
)

CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    title TEXT,
    first_name TEXT,
    last_name TEXT,
    portrait TEXT,
    public_description TEXT,
    private_description TEXT,
    starting_information TEXT,
    character_secret TEXT,
    character_clue TEXT,
    starting_tips JSON,
    primay_goal TEXT,
    secondary_goal TEXT,
    tertiary_goal TEXT,
    round_one_reveal JSON,
    round_two_reveal JSON,
    round_three_reveal JSON,
    starting_inventory TEXT[]
);

CREATE TABLE player_characters (
    id SERIAL PRIMARY KEY,
    game VARCHAR(5) NOT NULL,
    title TEXT,
    first_name TEXT,
    last_name TEXT,
    portrait TEXT,
    public_description TEXT,
    private_description TEXT,
    starting_information TEXT,
    character_secret TEXT,
    character_clue TEXT,
    starting_tips JSON,
    primay_goal TEXT,
    secondary_goal TEXT,
    tertiary_goal TEXT,
    round_one_reveal JSON,
    round_two_reveal JSON,
    round_three_reveal JSON,
    starting_inventory TEXT[],
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_game_id
        FOREIGN KEY (game)
            REFERENCES game_instances(code)
);