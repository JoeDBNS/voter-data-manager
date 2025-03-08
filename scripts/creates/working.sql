CREATE TABLE working (
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(100),
    name_suffix VARCHAR(6),
    birth_year INTEGER(4),
    gender CHAR(1),
    date_of_registration date,
    house_number_character CHAR(1),
    residence_street_number NUMERIC(38),
    house_suffix VARCHAR(4),
    pre_direction VARCHAR(2),
    street_name VARCHAR(40),
    street_type VARCHAR(4),
    suffix_direction VARCHAR(2),
    residence_extension VARCHAR(13),
    city VARCHAR(100),
    state VARCHAR(6),
    zip VARCHAR(10),
    mail_address_1 VARCHAR(255),
    mail_address_2 VARCHAR(255),
    mail_address_3 VARCHAR(255),
    mail_address_4 VARCHAR(255),
    mail_address_5 VARCHAR(255),
    voter_id NUMERIC(38),
    county_code CHAR(2),
    county_name VARCHAR(40),
    jurisdiction_code VARCHAR(5),
    jurisdiction_name VARCHAR(40),
    precinct VARCHAR(6),
    ward VARCHAR(6),
    school_district_code VARCHAR(5),
    school_district_name VARCHAR(100),
    state_house_district_code VARCHAR(5),
    state_house_district_name VARCHAR(100),
    state_enate_district_code VARCHAR(5),
    state_senate_district_name VARCHAR(100),
    us_congress_district_code VARCHAR(5),
    us_congress_district_name VARCHAR(100),
    county_commissioner_district_code VARCHAR(5),
    county_commissioner_district_name VARCHAR(100),
    village_district_code VARCHAR(2),
    village_district_name VARCHAR(100),
    village_precinct VARCHAR(6),
    school_precinct VARCHAR(6),
    is_permanent_absentee_voter CHAR(1),
    voter_status_type_code VARCHAR(2),
    UOCAVA_status_code CHAR(1),
    UOCAVA_status_name VARCHAR(40),
    primary key(voter_id)
);

-- TEMP - impliment above and in plan
ALTER TABLE mi MODIFY voter_id decimal(38,0);
ALTER TABLE mi MODIFY voter_id int(38);
ALTER TABLE mi MODIFY voter_id varchar(20);

ALTER TABLE mi MODIFY is_permanent_absentee_application_voter char(1);
ALTER TABLE mi MODIFY is_permanent_absentee_application_voter varchar(12);

ALTER TABLE mi MODIFY county_code char(2);
ALTER TABLE mi MODIFY county_code varchar(12);

ALTER TABLE mi MODIFY jurisdiction_code char(2);
ALTER TABLE mi MODIFY jurisdiction_code varchar(12);

ALTER TABLE mi MODIFY precinct char(2);
ALTER TABLE mi MODIFY precinct varchar(14);

ALTER TABLE mi MODIFY residence_street_number decimal(38,0);
ALTER TABLE mi MODIFY residence_street_number int(8);