class Main_Control_Panel:
    def main(self):
        # Create new User objects and add them to the system
        print("===== Adding Users =====")
        print(self.add_user("U001", "Alice Johnson", "123 Main St", "1234567890", "alice@example.com"))
        print(self.add_user("U002", "Bob Smith", "456 Oak St", "0987654321", "bob@example.com"))


if __name__ == "__main":
    Main_Control_Panel().main()