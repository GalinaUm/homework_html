def load_contacts_page():
    """Возвращает страницу с контактами"""
    with open("views/contacts.html", "r", encoding="utf-8") as f:
        return f.read()