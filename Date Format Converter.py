'''
PROGRAM DESCRIPTION:
Date Formatter Program
This script detects and reformats various date formats into a standard format (Month Day, Year).
It supports the following date formats:
    - DMY (Day Month Year) -> e.g. 25 December 1992
    - YMD (Year Month Day) -> e.g. 2008 April 13
    - ISO (YYYY-MM-DD) -> e.g. 2023-05-27
    - USA (MM/DD/YYYY) -> e.g. 07/04/2015
    - EUR (DD.MM.YYYY) -> e.g. 28.02.2024
    - JIS (YYYYMMDD) -> e.g. 19851101

PROGRAM BY:
Bustamante, Ezekiel G.          -> Programmer
Erosa, Carl Melvin A.           -> Programmer
Republica, Jhered Miguel C.     -> Programmer

PROGRAM DATE:
March 13, 2025 - March 14, 2025

SUBMITTED TO:
Engr. Jerico I. Sarcillo

'''

# READ THE USER MANUAL/INSTRUCTIONS BEFORE USING THE PROGRAM!!!

'''
Instructions:
- Please enter only the available date formats mentioned above.
- When entering single-digit months or days, always use a leading zero (e.g., 07 for July, 09 for the 9th day).
'''


def format_date(input_date: str) -> str:
    """
    Detects the format of the given date string and calls the appropriate function to reformat it.
    """

    try:
        if " " in input_date[2]:
            print("DMY Format Detected")
            dmy(input_date)
        elif " " in input_date[4]:
            print("YMD Format Detected")
            ymd(input_date)
        elif "-" in input_date and input_date[0].isdigit():
            print("ISO Format Detected")
            iso(input_date)
        elif "/" in input_date and input_date[0].isdigit():
            print("USA Format Detected")
            usa(input_date)
        elif "." in input_date and input_date[0].isdigit():
            print("EUR Format Detected")
            eur(input_date)
        elif "" in input_date and input_date.isdigit() and len(input_date) == 8:
            print("JIS Format Detected")
            jis(input_date)
        else:
            print("Invalid Input")
    except IndexError:
        print("Invalid Input")


months = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}


def dmy(date: str) -> str:  # e.g. 30 February 1992
    """
    Converts DMY (Day Month Year) format to Month Day, Year.
    """

    parts = date.replace(",", "").split()  # replace inputted comma to blank

    if len(parts) == 3:
        day, month, year = parts
        if month == "February":
            if 0 < int(day) <= 28:
                formatted_date = f"{month} {int(day)}, {year}"
                print(f"\nFormatted Date: {formatted_date}")
            else:
                print("\nInvalid Day Range")
        elif month in months:
            if 0 < int(day) <= 31:
                formatted_date = f"{month} {int(day)}, {year}"
                print(f"\nFormatted Date: {formatted_date}")
            else:
                print("\nInvalid Day Range")

        else:
            print("\nInvalid Month")


def ymd(date: str) -> str:  # e.g. 2008 April 13
    """
    Converts YMD (Year Month Day) format to Month Day, Year.
    """
    try:
        parts = date.split(" ")

        if len(parts) == 3:
            year, month, day = parts

            if month in months:
                if 0 < int(day) <= 28 if month == "February" else 0 < int(day) <= 31:
                    formatted_date = f"{month} {int(day)}, {year}"
                    print(f"\nFormatted Date: {formatted_date}")
                else:
                    print("\nInvalid Day Range")
            else:
                print("\nInvalid Month")
        else:
            print("\nInvalid Input")
    except ValueError:
        print("\nInvalid Day Range")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


def iso(date: str) -> str:  # e.g. 2023-05-27
    """
    Converts ISO (YYYY-MM-DD) format to Month Day, Year.
    """

    parts = date.split("-")

    try:
        if len(parts) != 3:
            print("\nInvalid Date Format.")

        year, month, day = parts

        if month not in months.values():
            print("\nInvalid month.")
            return

        if not (day.isdigit() and 1 <= int(day) <= 31):
            print("\nInvalid day range.")
            return

        if month == "02" and int(day) >= 29:
            print("\nInvalid day range for February.")
            return

        month_name = [name for name, num in months.items() if num == month][0]
        formatted_date = f"{month_name} {int(day)}, {year}"
        print(f"\nFormatted Date: {formatted_date}")
    except Exception as e:
        print("Unexpected Error.")


def usa(date: str) -> str:  # e.g. 07/04/2015
    """
    Converts USA (MM/DD/YYYY) format to Month Day, Year.
    """

    parts = date.split("/")
    month, day, year = parts

    if len(parts) == 3:
        if month in months.values():
            month_name = [name for name in months if months[name] == month][0]
            if 0 < int(day) <= 28 if month_name == "February" else 0 < int(day) <= 31:
                formatted_date = f"\nFormatted Date: {month_name} {day}, {year}"
                print(formatted_date)
            else:
                print("\nInvalid Day Range")
        else:
            print("\nInvalid Month Range")


def eur(date: str) -> str:  # e.g. 28.02.2024
    """
    Converts EUR (DD.MM.YYYY) format to Month Day, Year.
    """

    try:
        parts = date.split(".")

        if len(parts) == 3:
            day, month, year = parts

            if month in months.values():
                month_name = [name for name in months if months[name] == month][0]

                if 0 < int(day) <= 28 if month == "02" else 0 < int(day) <= 31:
                    formatted_date = f"{month_name} {int(day)}, {year}"
                    print(f"\nFormatted Date: {formatted_date}")
                else:
                    print("\nInvalid Day Range")
            else:
                print("\nInvalid Month")
        else:
            print("\nError: Invalid EUR format. Please use 'DD.MM.YYYY'.")

    except ValueError:
        print("\nError: Invalid input. Please enter a valid number for the day.")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


def jis(date: str) -> str:  # e.g. 19851101
    """
    Converts JIS (YYYYMMDD) format to Month Day, Year.
    """

    try:
        if len(date) == 8 and date.isdigit():  # Checks if the input is exactly 8 digits
            year = date[:4]
            month = date[4:6]
            day = date[6:]

            jis_months = {
                "01": "January", "02": "February", "03": "March", "04": "April",
                "05": "May", "06": "June", "07": "July", "08": "August",
                "09": "September", "10": "October", "11": "November", "12": "December"
            }

            if month in jis_months:  # Ensures the month is valid
                if month == "02":
                    if 0 < int(day) <= 28:
                        month_name = jis_months[month]
                        print(f"\nFormatted Date: {month_name} {int(day)}, {year}")
                    else:
                        print("\nInvalid Day Range")
                elif 0 < int(day) <= 31:
                    month_name = jis_months[month]
                    print(f"\nFormatted Date: {month_name} {int(day)}, {year}")
                else:
                    print("\nInvalid Day Range")
            else:
                print("\nInvalid Month")

    except ValueError:
        print("\nInput integers only.")


def main():
    """
    Main function to handle user input and process date conversion.
    """

    print(
        "\n\nAvailable Date Formats: (Enter '0' to exit) \no	DMY (Day Month, Year)\no	YMD (Year Month Day)\no	ISO (YYYY-MM-DD)\no	USA (MM/DD/YYYY)\no	EUR (DD.MM.YYYY)\no	JIS (YYYYMMDD)\n\n")

    user_input = " ".join(input("Enter a date  : ").title().split())

    if user_input == "0":
        print("\nExiting, thank you for using our program :D")
        exit()
    elif user_input != "0":
        format_date(user_input)
        main()

    format_date(user_input)


main()