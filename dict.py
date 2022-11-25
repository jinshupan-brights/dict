import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user",
   password="abc123"
)

print('''
Hello and welcome to the phone list, available commands:
    add - add a phone number
    delete - delete a contact
    list - list all phone numbers
    quit - quit the program''')

# read_dict: returns the list of all dictionary entries:
# argument: c - the database connection.
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELEcT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
# add_word: adds a word and its translation to dictionary entries:
# argument: c - the database connection.
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
# delete_word: deletes a entry from the dictionary based on the id:
# argument: c - the database connection.
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
# save_dict: commits all changes to the database
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("cOMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("command: ").upper().strip()
    if cmd == "list":
        print(read_dict(conn))
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()
