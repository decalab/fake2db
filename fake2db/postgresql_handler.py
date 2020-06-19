import psycopg2
import sys
from .base_handler import BaseHandler
from .custom import faker_options_container
from .helpers import fake2db_logger, str_generator
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import extras


logger, extra_information = fake2db_logger()
d = extra_information
BATCH_SIZE = 1000

class Fake2dbPostgresqlHandler(BaseHandler):

    @staticmethod
    def _check_table_exists(conn, table_name):
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute("SELECT table_name FROM information_schema.tables WHERE table_name = '%s'" % table_name)
        return cur.rowcount > 0

    @staticmethod
    def _batch_execute(conn, cur, sql, argslist, page_size=100):
        extras.execute_batch(cur=cur, sql=sql, argslist=argslist, page_size=page_size)
        conn.commit()

    def fake2db_initiator(self, number_of_rows, **connection_kwargs):
        '''Main handler for the operation
        '''
        rows = number_of_rows
        cursor, conn = self.database_caller_creator(number_of_rows, **connection_kwargs)

        self.data_filler_detailed_registration(rows, cursor, conn)
        # self.data_filler_company(rows, cursor, conn)
        # self.data_filler_user_agent(rows, cursor, conn)
        # self.data_filler_customer(rows, cursor, conn)
        cursor.close()
        conn.close()

    def database_caller_creator(self, number_of_rows, username, password, host, port, name=None, custom=None):
        '''creates a postgresql db
        returns the related connection object
        which will be later used to spawn the cursor
        '''
        cursor = None
        conn = None

        if name:
            dbname = name
        else:
            dbname = 'postgresql_' + str_generator(self).lower()
        try:
            # createdb
            conn = psycopg2.connect(
                user=username, password=password, host=host, port=port)
            conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            cur = conn.cursor()
            cur.execute("SELECT * FROM pg_database WHERE datname = '%s'" % dbname)
            if cur.rowcount == 0:
                # create database if not exist
                cur.execute('CREATE DATABASE %s;' % dbname)
            cur.close()
            conn.close()
            # reconnect to the new database
            conn = psycopg2.connect(user=username, password=password,
                                    host=host, port=port, database=dbname)
            cursor = conn.cursor()
            logger.warning('Database created and opened succesfully: %s' % dbname, extra=d)
        except Exception as err:
            logger.error(err, extra=d)
            raise

        if custom:
            self.custom_db_creator(number_of_rows, cursor, conn, custom)
            cursor.close()
            conn.close()
            sys.exit(0)

        return cursor, conn

    def custom_db_creator(self, number_of_rows, cursor, conn, custom):
        '''creates and fills the table with simple regis. information
        '''

        custom_d = faker_options_container()
        sqlst = "CREATE TABLE custom (id serial PRIMARY KEY,"
        custom_payload = "INSERT INTO custom ("
        
        # form the sql query that will set the db up
        for c in custom:
            if custom_d.get(c):
                sqlst += " " + c + " " + custom_d[c] + ","
                custom_payload += " " + c + ","
                logger.warning("fake2db found valid custom key provided: %s" % c, extra=d)
            else:
                logger.error("fake2db does not support the custom key you provided.", extra=d )
                sys.exit(1)
                
        # the indice thing is for trimming the last extra comma
        sqlst = sqlst[:-1]
        sqlst += ");"
        custom_payload = custom_payload[:-1]
        custom_payload += ") VALUES ("

        for i in range(0, len(custom)):
            custom_payload += "%s, "
        custom_payload = custom_payload[:-2] + ")"
        cursor.execute(sqlst)
        conn.commit()

        multi_lines = []
        try:
            for i in range(0, number_of_rows):
                multi_lines.append([])
                for c in custom:
                    multi_lines[i].append(getattr(self.faker, c)())
            
            cursor.executemany(custom_payload, multi_lines)
            conn.commit()
            logger.warning('custom Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)
            
    def data_filler_detailed_registration(self, number_of_rows, cursor, conn):
        '''creates and fills the table with detailed regis. information
        '''

        if not self._check_table_exists(conn, "user_registration"):
            cursor.execute(
                "CREATE TABLE user_registration "
                "(id serial PRIMARY KEY, email varchar(150), password varchar(300), "
                "last_name varchar(300), first_name varchar(300), address varchar(300), phone varchar(300),"
                "created_at timestamp with time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'),"
                "updated_at timestamp with time zone NOT NULL DEFAULT (current_timestamp AT TIME ZONE 'UTC'));")
            conn.commit()
        detailed_registration_data = []
        batch_count = 0

        try:
            for i in range(0, number_of_rows):
                detailed_registration_data.append((self.faker.safe_email(), self.faker.md5(raw_output=False), self.faker.first_name(),
                                                   self.faker.last_name(), self.faker.address(), self.faker.phone_number()))
                batch_count += 1
                if batch_count > BATCH_SIZE:
                    sql = ("INSERT INTO detailed_registration "
                             "(email, password, first_name, last_name, address, phone) "
                             "VALUES (%s, %s, %s, %s, %s, %s)")

                    self._batch_execute(conn=conn, cur=cursor, sql=sql, argslist=detailed_registration_data,
                                        page_size=1000)
                    detailed_registration_data = []
                    batch_count = 0

            if batch_count > 0 and len(detailed_registration_data) > 0:
                self._batch_execute(conn, cursor, sql, detailed_registration_data)

            logger.warning('detailed_registration Commits are successful after write job!', extra=d)

        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_user_agent(self, number_of_rows, cursor, conn):
        '''creates and fills the table with user agent data
        '''

        cursor.execute(
            "CREATE TABLE user_agent (id serial PRIMARY KEY, ip varchar(300), countrycode varchar(300), useragent varchar(300));")
        conn.commit()

        user_agent_data = []

        try:

            for i in range(0, number_of_rows):

                user_agent_data.append((self.faker.ipv4(), self.faker.country_code(),
                 self.faker.user_agent()))

            user_agent_payload = ("INSERT INTO user_agent "
                               "(ip, countrycode, useragent) "
                               "VALUES (%s, %s, %s)")

            cursor.executemany(user_agent_payload, user_agent_data)
            conn.commit()

            logger.warning('user_agent Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_company(self, number_of_rows, cursor, conn):
        '''creates and fills the table with company data
        '''

        if not self._check_table_exists(conn, "company"):
            cursor.execute(
                "CREATE TABLE company (id serial PRIMARY KEY, "
                "name varchar(300), state varchar(200), email varchar(150), domain varchar(200), city varchar(200), country varchar(200));")
            conn.commit()
        company_data = []

        try:
            for i in range(0, number_of_rows):

                company_data.append((self.faker.company(), self.faker.date(pattern="%d-%m-%Y"),
                                     self.faker.company_email(), self.faker.safe_email(), self.faker.city()))

            company_payload = ("INSERT INTO company "
                               "(name, sdate, email, domain, city) "
                               "VALUES (%s, %s, %s, %s, %s)")

            cursor.executemany(company_payload, company_data)
            conn.commit()
            logger.warning('companies Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)

    def data_filler_customer(self, number_of_rows, cursor, conn):
        '''creates and fills the table with customer data
        '''

        cursor.execute(
            "CREATE TABLE customer (id serial PRIMARY KEY, "
            "name varchar(300), lastname varchar(300), address varchar(300), country varchar(300), "
            "city varchar(300), registry_date varchar(300), birthdate varchar(300), email varchar(300), "
            "phone_number varchar(300), locale varchar(300));")
        conn.commit()

        customer_data = []

        try:
            for i in range(0, number_of_rows):

                customer_data.append((self.faker.first_name(), self.faker.last_name(), self.faker.address(),
                                      self.faker.country(), self.faker.city(), self.faker.date(pattern="%d-%m-%Y"),
                                      self.faker.date(pattern="%d-%m-%Y"), self.faker.safe_email(), self.faker.phone_number(),
                                      self.faker.locale()))

            customer_payload = ("INSERT INTO customer "
                                "(name, lastname, address, country, city, registry_date, "
                                "birthdate, email, phone_number, locale)"
                                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

            cursor.executemany(customer_payload, customer_data)
            conn.commit()
            logger.warning('customer Commits are successful after write job!', extra=d)
        except Exception as e:
            logger.error(e, extra=d)
