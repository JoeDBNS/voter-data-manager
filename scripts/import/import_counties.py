import mysql.connector, time, json, os

start_time = time.time()

config_path = os.path.join(os.path.dirname(__file__), '..', '_config', 'db_config.json')
with open(config_path, 'r') as config_file:
    db_config = json.load(config_file)

cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()
bulk_insert_amount = 50  # only 83 counties total
total_processed = 0
table_name = 'counties'
source_path = ''

# Source: County Codes.csv
# Columns: County Code, County Name

try:
    with open(source_path, 'r') as file:
        pos = 1
        insert_command = """
            INSERT INTO {format_table_name}
                (county_id, county_name)
            VALUES
        """.format(format_table_name=table_name)
        insert_records = []

        for line in file:
            line = line.strip()

            # Skip header
            if pos == 1 and line.lower().startswith('county code'):
                continue

            parts = line.split(',')
            county_id   = parts[0].strip()
            county_name = parts[1].strip()

            insert_records.append('("{}", "{}")'.format(county_id, county_name))
            pos += 1

        # Insert all at once (small table)
        if insert_records:
            cur_time = time.time()
            elapsed_time = cur_time - start_time

            try:
                cursor.execute(insert_command + ', '.join(insert_records) + ';')
                cnx.commit()
                total_processed += cursor.rowcount
                print('SUCCESS\t\t{} records - {} sec'.format(total_processed, round(elapsed_time, 2)))

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
