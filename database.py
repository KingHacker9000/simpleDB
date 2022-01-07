# Import SQLITE Module
import sqlite3


class Database:

    def __init__(self, filename):
        self.conn = sqlite3.connect(filename, check_same_thread=False)
        self.conn.row_factory = sqlite3.Row


    def execute(self, command, *args):

        
        if command == ".schema;":
            rV = []

            self.conn.row_factory = sqlite3.Row
            c = self.conn.cursor()
            c.execute("SELECT name, sql FROM sqlite_master WHERE type='table';")
            rows = c.fetchall()
            
            for row in rows:
                rV.append(dict(row))

            self.conn.commit()
            if __name__ == '__main__':
                print(rV)
                pass
            return rV if len(rV) != 0 else None


        elif "SELECT" in command[0:8].upper():

            rV = []

            self.conn.row_factory = sqlite3.Row
            c = self.conn.cursor()
            c.execute(command, *args)
            rows = c.fetchall()

            for row in rows:
                rV.append(dict(row))

            self.conn.commit()
            if __name__ == '__main__':
                print(rV)
            return rV if len(rV) != 0 else None
        
        else:
            c = self.conn.cursor()
            c.execute(command, *args)
            self.conn.commit()
            return None


    def __del__(self):
        self.conn.close()


if __name__ == '__main__':

    db = Database(input("Enter File Name: "))
    try:
        while True:
            db.execute(input(">>> "))

    except KeyboardInterrupt:
        quit()
