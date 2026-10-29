-- voter_id                                | NUMERIC(38)   | NO   | PRI | NULL |
-- last_name                               | VARCHAR(100)  | YES  |     | NULL |
-- first_name                              | VARCHAR(100)  | YES  |     | NULL |
-- middle_name                             | VARCHAR(100)  | YES  |     | NULL |
-- name_suffix                             | VARCHAR(6)    | YES  |     | NULL |
-- birth_year                              | INTEGER(4)    | YES  |     | NULL |
-- gender                                  | CHAR(1)       | YES  |     | NULL |
-- is_permanent_absentee_voter             | CHAR(1)       | YES  |     | NULL |
-- voter_status_type_code                  | VARCHAR(2)    | YES  |     | NULL |
-- is_permanent_absentee_application_voter | CHAR(1)       | YES  |     | NULL |
-- date_of_registration                    | date          | YES  |     | NULL |
-- mail_address_1                          | VARCHAR(255)  | YES  |     | NULL |
-- mail_address_2                          | VARCHAR(255)  | YES  |     | NULL |
-- mail_address_3                          | VARCHAR(255)  | YES  |     | NULL |
-- mail_address_4                          | VARCHAR(255)  | YES  |     | NULL |
-- mail_address_5                          | VARCHAR(255)  | YES  |     | NULL |
-- address_id                              | NUMERIC(38)   | YES  | FGN | NULL | new

CREATE TABLE voters (
    voter_id NUMERIC(38) NOT NULL,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(100),
    name_suffix VARCHAR(6),
    birth_year INTEGER(4),
    gender CHAR(1),
    is_permanent_absentee_voter CHAR(1),
    voter_status_type_code VARCHAR(2),
    is_permanent_absentee_application_voter CHAR(1),
    date_of_registration date,
    mail_address_1 VARCHAR(255),
    mail_address_2 VARCHAR(255),
    mail_address_3 VARCHAR(255),
    mail_address_4 VARCHAR(255),
    mail_address_5 VARCHAR(255),
    address_id NUMERIC(38),
    PRIMARY KEY (voter_id),
    FOREIGN KEY (address_id) REFERENCES addresses_dev(address_id)
);


INSERT INTO voters (voter_id, last_name, first_name, middle_name, name_suffix, birth_year, gender, is_permanent_absentee_voter, voter_status_type_code, is_permanent_absentee_application_voter, date_of_registration, mail_address_1, mail_address_2, mail_address_3, mail_address_4, mail_address_5)
SELECT DISTINCT voter_id, last_name, first_name, middle_name, name_suffix, birth_year, gender, is_permanent_absentee_voter, voter_status_type_code, is_permanent_absentee_application_voter, date_of_registration, mail_address_1, mail_address_2, mail_address_3, mail_address_4, mail_address_5
FROM working;