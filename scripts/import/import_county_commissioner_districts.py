import mysql.connector, time, json, os

start_time = time.time()

config_path = os.path.join(os.path.dirname(__file__), '..', '_config', 'db_config.json')
with open(config_path, 'r') as config_file:
    db_config = json.load(config_file)

cnx = mysql.connector.connect(**db_config)
cursor = cnx.cursor()
total_processed = 0
table_name = 'county_commissioner_districts'
source_path = os.path.join(os.path.dirname(__file__), '..', 'reference_data', 'county_commissioner_districts.csv')

# Source: county_commissioner_districts.csv
# Columns: COUNTY_COMMISSIONER_DISTRICT_CODE, COUNTY_COMMISSIONER_DISTRICT_NAME

try:
    with open(source_path, 'r') as file:
        insert_command = """
            INSERT INTO {format_table_name}
                (county_commissioner_district_id, county_commissioner_district_name)
            VALUES
        """.format(format_table_name=table_name)
        insert_records = []

        for line in file:
            line = line.strip()

            if not line:
                continue

            # Skip header
            if line.upper().startswith('COUNTY_COMMISSIONER_DISTRICT_CODE'):
                continue

            parts = line.split(',')
            district_id   = parts[0].strip()
            district_name = parts[1].strip()

            insert_records.append('("{}", "{}")'.format(district_id, district_name))

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
