from typing import List


def show_menu() -> None:
    print("\n====== 📱 Contact Book v2.2 ======")
    print("1. + Yangi kontakt qoshish")
    print("2. 📄 Barcha kontaktlarni korish")
    print("3. 🔍 Kontaktni ism boyicha qidirish")
    print("4. 📧 Faqat @gmail.com kontaktlarni korish")
    print("5. 🚪 Dasturni yakunlash")


def is_valid_contact(contact: List) -> bool:
    pass


def add_contact(contact_list: List[List]) -> None:
    pass


def list_contacts(contact_list: List[List]) -> None:
    pass


def search_contact(contact_list: List[List]) -> None:
    pass


def filter_gmail_contacts(contact_list: List[List]) -> None:
    pass


def main() -> None:
    contacts: List[List] = []

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
