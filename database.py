import psycopg2



class database:

    def __init__(self):
        self.hostname = 'localhost'
        self.database_name = 'habit_tracker_db'
        self.username = 'postgres'
        self.password = 'password'
        self.port_id = '5432'


    def add_id(self,id) -> bool:
        
        try:
            connection = psycopg2.connect(
                host = self.hostname,
                database = self.database_name,
                user = self.username,
                password = self.password,
                port = self.port_id
            )

            cur = connection.cursor()
            insert_query = 'INSERT INTO ids (id) VALUES(%s)'
            insert_val = (id,)
            cur.execute(insert_query,insert_val)
            print("Connection to database established")

            connection.commit()


        except Exception as error:
            print(error)
            return False
        finally:
            if connection:
                cur.close()
                connection.close()
                print("Connection to database closed")
        

database().add_id(42)

