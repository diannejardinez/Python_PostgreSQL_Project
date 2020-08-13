#  database.py s database store file

entries = []

# Function that adds an entry for storage
def add_entry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date})

def get_entries():
    # Getting data from entries list
    return entries
