

# backend_student_table = """
# CREATE TABLE IF NOT EXISTS student (
#     id integer PRIMARY KEY,
#     name text,
#     course test
# );
# """

# backend_exam_table = """
# CREATE TABLE IF NOT EXISTS exam (
#      id integer PRIMARY KEY,
#      name text NOT NULL
#  );
# """

# backend_task_table = """
# CREATE TABLE IF NOT EXISTS task (
#      id integer PRIMARY KEY,
#      name text NOT NULL
#      FOREIGN KEY (exam_id) REFERENCES exam (id)
#      points_max integer
#      bonus_max integer
#      abstract text
#     );
# """

# backend_answer_table = """
# CREATE TABLE IF NOT EXISTS answer (
#      id integer PRIMARY KEY,
#      FOREIGN KEY (task_id) REFERENCES tasks (id)
#      FOREIGN KEY (student_id) REFERENCES students
#      points integer
#      bonus integer
#      comment text
#     );
# """

class Backend:
    def __init__(self):
        self.db = None

    def open(self):
        try:
            self.db = sqlite3.connect('data/grdx.db')
            print('SQLite3 ',sqlite3.version)
        except sqlite3.Error as e:
            print(e)
        finally:
            pass

    def __del__(self):
        self.close()
        
    def close(self):
        try:
            self.db.close()
        except sqlite3.Error as e:
            print(e)
        finally:
            pass


    def update(self):
        self.__setup_tables()

    def ready(self):
        return self.db != None

    def __execute(self,sql):
        try:
            c = self.db.cursor()
            c.execute(sql)
        except sqlite3.Error as e:
            print(e)


    def __setup_tables(self):
        if self.db != None:
            self.__execute(backend_student_table)
            self.__execute(backend_exam_table)


# -- submission table
# CREATE TABLE IF NOT EXISTS exam (
#     id integer PRIMARY KEY,
#     name text NOT NULL
#     FOREIGN KEY (exam_id) REFERENCES exam (id)
# );

# -- submission table
# CREATE TABLE IF NOT EXISTS exam (
#     id integer PRIMARY KEY,
#     name text NOT NULL
#     FOREIGN KEY (exam_id) REFERENCES exam (id)
# );

def main():

    s = Student(name='Hans Muster',reg_id=30303,year='2010')

    # print(s.csv())


    # print('Debug')
    # be = Backend()
    # be.open()
    # be.update()
	
if __name__ == '__main__':
    main()