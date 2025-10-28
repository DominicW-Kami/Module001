class Publication:
    def __init__(self, name):
        self.name = name

    def print_details(self):
        print(f"Name: {self.name}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_details(self):
        super().print_details()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")

class Magazine(Publication):
    def __init__(self, name, editor_in_chief):
        super().__init__(name)
        self.editor_in_chief = editor_in_chief

    def print_details(self):
        super().print_details()
        print(f"Editor-in-Chief: {self.editor_in_chief}")


if __name__ == "__main__":
    aku_ankka = Magazine("Aku Ankka", "Aki Hyyppä")
    print("Aku Ankka's details:")
    aku_ankka.print_details()
    print("-" * 20)

    hytti_6 = Book("Hytti n:o 6", "Rosa Liksom", 200)
    print("Hytti n:o 6's details:")
    hytti_6.print_details()
