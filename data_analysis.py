
import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Salary_Data_clean.csv")


def show_menu():
    print("\n" + "=" * 55)
    print("       SALARY DATA ANALYSIS SYSTEM")
    print("=" * 55)

    print("1.  Display Dataset")
    print("2.  Dataset Shape")
    print("3.  Column Information")
    print("4.  Statistical Summary")
    print("5.  Missing Values Analysis")
    print("6.  Duplicate Records Analysis")
    print("7.  Gender Distribution")
    print("8.  Education Level Distribution")
    print("9.  Job Title Distribution")
    print("10. Average Salary by Gender")
    print("11. Average Salary by Education")
    print("12. Average Salary by Job Title")
    print("13. Experience vs Salary Analysis")
    print("14. Age vs Salary Analysis")
    print("15. Correlation Analysis")
    print("16. Salary Distribution Graph")
    print("17. Experience Distribution Graph")
    print("18. Salary by Education Graph")
    print("19. Salary by Gender Graph")
    print("20. Exit")

    print("=" * 55)


def display_dataset():
    print("\nDATASET:")
    print(df.to_string(index=False))


def dataset_shape():
    print("\nTotal Rows:", df.shape[0])
    print("Total Columns:", df.shape[1])


def column_information():
    print("\nCOLUMN INFORMATION:")
    df.info()


def statistical_summary():
    print("\nSTATISTICAL SUMMARY:")
    print(df.describe())


def missing_values():
    print("\nMISSING VALUES:")
    print(df.isnull().sum())

    total = df.isnull().sum().sum()
    print("\nTotal Missing Values:", total)


def duplicate_analysis():
    duplicates = df.duplicated().sum()
    print("\nTotal Duplicate Records:", duplicates)


def gender_distribution():
    print("\nGENDER DISTRIBUTION:")
    print(df["gender"].value_counts())


def education_distribution():
    print("\nEDUCATION LEVEL DISTRIBUTION:")
    print(df["education_level"].value_counts())


def job_distribution():
    print("\nJOB TITLE DISTRIBUTION:")
    print(df["job_title"].value_counts())


def salary_by_gender():
    print("\nAVERAGE SALARY BY GENDER:")
    print(df.groupby("gender")["salary"].mean())


def salary_by_education():
    print("\nAVERAGE SALARY BY EDUCATION:")
    print(df.groupby("education_level")["salary"].mean())


def salary_by_job():
    print("\nAVERAGE SALARY BY JOB TITLE:")
    print(df.groupby("job_title")["salary"].mean().sort_values(ascending=False))


def experience_salary():
    print("\nEXPERIENCE VS SALARY:")
    print(df.groupby("years_of_experience")["salary"].mean())

    plt.scatter(df["years_of_experience"], df["salary"])
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")
    plt.grid()
    plt.show()


def age_salary():
    print("\nAGE VS SALARY:")
    print(df.groupby("age")["salary"].mean())

    plt.scatter(df["age"], df["salary"])
    plt.xlabel("Age")
    plt.ylabel("Salary")
    plt.title("Age vs Salary")
    plt.grid()
    plt.show()


def correlation_analysis():
    print("\nCORRELATION MATRIX:")
    print(df.select_dtypes(include="number").corr())


def salary_distribution_graph():
    plt.hist(df["salary"], bins=20, edgecolor="black")
    plt.xlabel("Salary")
    plt.ylabel("Frequency")
    plt.title("Salary Distribution")
    plt.grid(axis="y")
    plt.show()


def experience_distribution():
    plt.hist(df["years_of_experience"], bins=15, edgecolor="black")
    plt.xlabel("Years of Experience")
    plt.ylabel("Frequency")
    plt.title("Experience Distribution")
    plt.grid(axis="y")
    plt.show()


def education_salary_graph():
    data = df.groupby("education_level")["salary"].mean().sort_values()

    data.plot(kind="bar", edgecolor="black")
    plt.xlabel("Education Level")
    plt.ylabel("Average Salary")
    plt.title("Average Salary by Education")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()


def gender_salary_graph():
    data = df.groupby("gender")["salary"].mean()

    data.plot(kind="bar", edgecolor="black")
    plt.xlabel("Gender")
    plt.ylabel("Average Salary")
    plt.title("Average Salary by Gender")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()


# Main menu-driven program

while True:

    show_menu()

    choice = input("Enter your choice (1-20): ")

    if choice == "1":
        display_dataset()

    elif choice == "2":
        dataset_shape()

    elif choice == "3":
        column_information()

    elif choice == "4":
        statistical_summary()

    elif choice == "5":
        missing_values()

    elif choice == "6":
        duplicate_analysis()

    elif choice == "7":
        gender_distribution()

    elif choice == "8":
        education_distribution()

    elif choice == "9":
        job_distribution()

    elif choice == "10":
        salary_by_gender()

    elif choice == "11":
        salary_by_education()

    elif choice == "12":
        salary_by_job()

    elif choice == "13":
        experience_salary()

    elif choice == "14":
        age_salary()

    elif choice == "15":
        correlation_analysis()

    elif choice == "16":
        salary_distribution_graph()

    elif choice == "17":
        experience_distribution()

    elif choice == "18":
        education_salary_graph()

    elif choice == "19":
        gender_salary_graph()

    elif choice == "20":
        print("\nThank you for using Salary Data Analysis System!")
        break

    else:
        print("\nInvalid choice! Please enter a number between 1 and 20.")
