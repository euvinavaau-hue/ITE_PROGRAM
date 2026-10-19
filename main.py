def get_resident_info():
    name = input("Enter your full name: ")
    address = input("Enter your purok / street address: ")
    return name, address


def main():
    while True:
        print("\n========================================")
        print("   BARANGAY DOCUMENT REQUEST SYSTEM     ")
        print("========================================")
        print("1. Barangay Clearance")
        print("2. Certificate of Indigency")
        print("3. Certificate of Residency")
        print("4. Exit")
        print("----------------------------------------")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            print("\n--- Processing: Barangay Clearance ---")
            name, address = get_resident_info()
            purpose = input("Enter purpose (e.g., Job Application, ID): ")

            print("\n✅ [SUCCESS] Barangay Clearance generated!")
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Purpose: {purpose}")
            print("Status: Ready for verification and pick-up at the Barangay Hall.")

        elif choice == '2':
            print("\n--- Processing: Certificate of Indigency ---")
            name, address = get_resident_info()
            reason = input("Enter reason (e.g., Medical assistance, Scholarship): ")

            print("\n✅ [SUCCESS] Certificate of Indigency generated!")
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Reason: {reason}")
            print("Status: Ready for verification and pick-up at the Barangay Hall.")

        elif choice == '3':
            print("\n--- Processing: Certificate of Residency ---")
            name, address = get_resident_info()
            years = input("How many years have you lived in this barangay? ")

            print("\n✅ [SUCCESS] Certificate of Residency generated!")
            print(f"Name: {name}")
            print(f"Address: {address}")
            print(f"Years of Residency: {years} years")
            print("Status: Ready for verification and pick-up at the Barangay Hall.")

        elif choice == '4':
            print("\nThank you for using the system. Mabuhay!")
            break

        else:
            print("\n❌ [ERROR] Invalid choice. Please enter a number from 1 to 4.")

        input("\nPress Enter to return to the main menu...")


if __name__ == "__main__":
    main()