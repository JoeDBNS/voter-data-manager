import mysql.connector, time

start_time = time.time()

cnx = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)
cursor = cnx.cursor()
bulk_insert_amount = 10000
total_processed = 0
table_name = 'working'
source_path = ''

try:
    with open(source_path, 'r') as file:
        pos = 1
        insert_command = """
            INSERT INTO {format_table_name}
                (last_name, first_name, middle_name, name_suffix, birth_year, gender, date_of_registration, house_number_character, residence_street_number, house_suffix, pre_direction, street_name, street_type, suffix_direction, residence_extension, city, state, zip, mail_address_1, mail_address_2, mail_address_3, mail_address_4, mail_address_5, voter_id, county_code, county_name, jurisdiction_code, jurisdiction_name, precinct, ward, school_district_code, school_district_name, state_house_district_code, state_house_district_name, state_senate_district_code, state_senate_district_name, us_congress_district_code, us_congress_district_name, county_commissioner_district_code, county_commissioner_district_name, village_district_code, village_district_name, village_precinct, school_precinct, is_permanent_absentee_voter, voter_status_type_code, UOCAVA_status_code, UOCAVA_status_name, is_permanent_absentee_application_voter)
            VALUES
        """.format(format_table_name = table_name)
        insert_records = []

        for line in file:
            line_inspect = line.replace('\n', '').replace('\\', '')[1:-1].split('","')

            # MySQL doesn't line empty string for no int
            if (line_inspect[8] == ''):
                line_inspect[8] = '0'

            insert_records.append('("' + '","'.join(line_inspect) + '")')

            if (pos == bulk_insert_amount):
                cur_time = time.time()
                elapsed_time = cur_time - start_time

                try:
                    cursor.execute(insert_command + ', '.join(insert_records) + ';')
                    cnx.commit()

                    if (cursor.rowcount == bulk_insert_amount):
                        print('SUCCESS\t\t' + (str(total_processed) + ' ---> ' + str(total_processed + bulk_insert_amount)) + ' - ' + str(round(elapsed_time, 2)) + ' sec')
                        total_processed += bulk_insert_amount

                    else:
                        print('ERROR\t\t', total_processed + ' - ' + str(round(elapsed_time, 2)) + ' sec')

                except Exception as error:
                    last_insert_attempt = insert_command + ', '.join(insert_records) + ';'
                    print(last_insert_attempt)
                    print(error)

                pos = 1
                insert_command = """
                    INSERT INTO {format_table_name}
                        (last_name, first_name, middle_name, name_suffix, birth_year, gender, date_of_registration, house_number_character, residence_street_number, house_suffix, pre_direction, street_name, street_type, suffix_direction, residence_extension, city, state, zip, mail_address_1, mail_address_2, mail_address_3, mail_address_4, mail_address_5, voter_id, county_code, county_name, jurisdiction_code, jurisdiction_name, precinct, ward, school_district_code, school_district_name, state_house_district_code, state_house_district_name, state_senate_district_code, state_senate_district_name, us_congress_district_code, us_congress_district_name, county_commissioner_district_code, county_commissioner_district_name, village_district_code, village_district_name, village_precinct, school_precinct, is_permanent_absentee_voter, voter_status_type_code, UOCAVA_status_code, UOCAVA_status_name, is_permanent_absentee_application_voter)
                    VALUES
                """.format(format_table_name = table_name)
                insert_records = []

            else:
                pos += 1


except Exception as error:
    print(error)

finally:
    cnx.close()
    end_time = time.time()
    elapsed_time_total = end_time - start_time

    print(str(round(elapsed_time_total, 2)) + ' sec')
    # Last Run Time: 1059.13 sec
