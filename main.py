from typing import List


def show_menu() -> None:
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. + Yangi kontakt qoshish")
    print("2. 📄 Barcha kontaktlarni korish")
    print("3. 🔍 Kontaktni ism boyicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni korish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contact: List) -> bool:
    name, phone, email = contact
    
    def check_name(name: str) -> bool:
        if len(name) < 2:
            return False
        
        for i in name.split():
            if not i.isalpha():
                return False

        return True
    
    def check_phone(phone: str) -> bool:
        if phone.startswith("+"):
            if len(phone) != 13:
                return False
            else:
                return phone[1:].isdigit()

        return len(phone) == 9 and phone.isdigit()
    
    def check_email(email: str) -> bool:
        if email.count("@") != 1:
            return False

        local, domain = email.split("@")

        if not local or not domain:
            return False
        
        if "." not in domain:
            return False

        for ch in local:
            if not (ch.isalnum() or ch in "-_."):
                return False    
            
        return True
    
    return check_name(name) and check_phone(phone) and check_email(email)


def add_contact(contact_list: List[List]) -> None:
    name = input("Name: ").strip().title()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    contact = [name, phone, email]

    if is_valid_contact(contact):
        contact_list.append(contact)
        print("Contact added successfully.")
    else:
        print("You entered the contact incorrectly.")


def list_contacts(contact_list: List[List]) -> None:
    for contact in contact_list:
        name, phone, email = contact
        print(f"Name: {name}, Phone: {phone}, email: {email}")


def search_contact(contact_list: List[List]) -> None:
    search = input("Search: ").strip().lower()
    found = False

    for name, phone, email in contact_list:
        if search in name.lower():
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
            found = True

    if not found:
        print("Not found!")


def filter_gmail_contacts(contact_list: List[List]) -> None:
    found = False

    for name, phone, email in contact_list:
        if email.lower().endswith("@gmail.com"):
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
            found = True

    if not found:
        print("Not found")

def main() -> None:
    contacts: List[List] = [["Ali", "987654321", "ali@gmail.com"]]

    while True:
        show_menu()
        choice = input("Tanlov (1-5): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            list_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            filter_gmail_contacts(contacts)
        elif choice == "5":
            print("👋 Dasturni yakunlayapmiz. Xayr!")
            break
        else:
            print("Notogri tanlov. Iltimos, 1 dan 5 gacha son kiriting.")

main()
