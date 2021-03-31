
import sqlite3
conn = sqlite3.connect('BGIT.db')
# https://www.tutorialspoint.com/sqlite/sqlite_python.htm

#conn.execute('''CREATE TABLE About( Id INTEGER PRIMARY KEY AUTOINCREMENT,DESCRIPTION TEXT NOT NULL,ISACTIVE BOOLEAN NOT NULL)''')
#cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
#for row in cursor:
   #print("ID = ", row[0])
   #print("NAME = ", row[1])
   #print("ADDRESS = ", row[2])
   #print("SALARY = ", row[3], "\n")
#print("Records created successfully")
decription = '''Brazil's far-right President Jair Bolsonaro, who came to power two years ago, has consistently opposed lockdown measures, arguing that the damage to the economy would be worse than the effects of the coronavirus itself.
He has also told Brazilians to "stop whining" about the situation.
But last week, Mr Bolsonaro, who has previously raised doubts about vaccines and defended unproven drugs as treatment, said that he would make 2021 the year of vaccinations. "Very soon we'll resume our normal lives," he said.
The president's popularity has plummeted over his handling of the pandemic, with 43% of Brazilians saying Mr Bolsonaro is to blame for the Covid crisis, according to a Datafolha poll published in mid-March.
The poll suggests that 54% rate his performance in connection with the pandemic as bad or very bad, up from 48% in late January.'''
conn.execute("INSERT INTO About (DESCRIPTION,ISACTIVE) VALUES (?, ?)", (decription, 1))
print('created and inserted successfully')
conn.commit()
conn.close()


