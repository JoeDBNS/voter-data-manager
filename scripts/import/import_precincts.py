import mysql.connector, time

start_time = time.time()

cnx = mysql.connector.connect(
    user='',
    password='',
    host='',
    database=''
)
cursor = cnx.cursor()
bulk_insert_amount = 500
total_processed = 0
table_name = 'precincts'
source_path = ''

# Source: Precinct Codes.csv
# Columns: COUNTY CODE, COUNTY NAME, JURISDICTION CODE, JURISDICTION NAME, PRECINCT CODE, PRECINCT NAME
# Note: county_name and jurisdiction_name are skipped — already stored in their respective tables

try:
    with open(source_path, 'r') as file:
        pos = 1
        insert_command = """
            INSERT INTO {format_table_name}
                (county_id, jurisdiction_id, precinct_id, precinct_name)
            VALUES
        """.format(format_table_name=table_name)
        insert_records = []

        for line in file:
            line = line.strip()

            # Skip header
            if line.upper().startswith('COUNTY CODE'):
                continue

            parts = line.split(',')
            county_id       = parts[0].strip()
            # parts[1] = county_name (skipped)
            jurisdiction_id = parts[2].strip()
            # parts[3] = jurisdiction_name (skipped)
            precinct_id     = parts[4].strip()
            precinct_name   = parts[5].strip()

            insert_records.append('("{}", "{}", "{}", "{}")'.format(
                county_id, jurisdiction_id, precinct_id, precinct_name
            ))

            if pos == bulk_insert_amount:
                cur_time = time.time()
                elapsed_time = cur_time - start_time

                try:
                    cursor.execute(insert_command + ', '.join(insert_records) + ';')
                    cnx.commit()

                    if cursor.rowcount == bulk_insert_amount:
                        print('SUCCESS\t\t{} ---> {} - {} sec'.format(
                            total_processed,
                            total_processed + bulk_insert_amount,
                            round(elapsed_time, 2)
                        ))
                        total_processed += bulk_insert_amount

                    else:
                        print('ERROR\t\t{} - {} sec'.format(total_processed, round(elapsed_time, 2)))

                except Exception as error:
                    last_insert_attempt = insert_command + ', '.join(insert_records) + ';'
                    print(last_insert_attempt)
                    print(error)

                pos = 1
                insert_command = """
                    INSERT INTO {format_table_name}
                        (county_id, jurisdiction_id, precinct_id, precinct_name)
                    VALUES
                """.format(format_table_name=table_name)
                insert_records = []

            else:
                pos += 1

        # Insert any remaining records
        if insert_records:
            cur_time = time.time()
            elapsed_time = cur_time - start_time

            try:
                cursor.execute(insert_command + ', '.join(insert_records) + ';')
                cnx.commit()
                total_processed += cursor.rowcount
                print('SUCCESS\t\t{} total records - {} sec'.format(total_processed, round(elapsed_time, 2)))

            except Exception as error:
                last_insert_attempt = insert_command + ', '.join(insert_records) + ';'
                print(last_insert_attempt)
                print(error)

except Exception as error:
    print(error)

finally:
    cnx.close()
    end_time = time.time()
    elapsed_time_total = end_time - start_time
    print(str(round(elapsed_time_total, 2)) + ' sec')
