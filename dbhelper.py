import mysql.connector



class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user = 'root',
                password = 'Kaynat@73',
                database = 'flights'
            )
            self.mycursor = self.conn.cursor()
            print('Connection established')

        except:
            print('Connection error!')

    def fetch_city_name(self):
        city = []
        self.mycursor.execute("""
            SELECT DISTINCT(Destination) FROM flights
            UNION
            SELECT DISTINCT(Source) FROM flights;
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
            SELECT airline , Route , Dep_time , duration , price FROM flights
            WHERE source = '{}' and Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()

        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []
        self.mycursor.execute("""
        SELECT Airline ,COUNT(*) FROM flights
        GROUP BY airline
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline,frequency

    def busy_airport(self):

        city = []
        frequency = []
        self.mycursor.execute("""
        SELECT Source,COUNT(*) FROM (SELECT Source FROM flights
							UNION ALL
							SELECT Destination FROM flights) t
        GROUP BY t.source
        ORDER BY COUNT(*) DESC
        """)

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):

        date = []
        frequency = []
        self.mycursor.execute("""
        select date_of_journey , COUNT(*) FROM flights
        GROUP BY date_of_journey
        """)

        data = self.mycursor.fetchall()

        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency
