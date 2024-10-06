from entity.JobListing import JobListing
from entity.Company import Company
from entity.Applicant import Applicant
from entity.JobApplication import JobApplication
from DatabaseManager import DatabaseManager
from datetime import datetime
import sys


def main_menu():
    db_manager = DatabaseManager()

    
    print("Initializing database schema...")
    db_manager.initialize_database()
    print("Database initialized successfully.")

    while True:
        print("\n--- Job Board Application ---")
        print("1. Post a Job")
        print("2. Register a Company")
        print("3. Register an Applicant")
        print("4. Apply for a Job")
        print("5. View All Job Listings")
        print("6. View All Companies")
        print("7. View All Applicants")
        print("8. View Applications for a Specific Job")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            post_job(db_manager)
        elif choice == "2":
            register_company(db_manager)
        elif choice == "3":
            register_applicant(db_manager)
        elif choice == "4":
            apply_for_job(db_manager)
        elif choice == "5":
            view_job_listings(db_manager)
        elif choice == "6":
            view_companies(db_manager)
        elif choice == "7":
            view_applicants(db_manager)
        elif choice == "8":
            view_applications_for_job(db_manager)
        elif choice == "9":
            print("Exiting the application.")
            sys.exit()
        else:
            print("Invalid choice, please try again.")

def post_job(db_manager):
    try:
        company_id = int(input("Enter Company ID: "))
        job_title = input("Enter Job Title: ")
        job_description = input("Enter Job Description: ")
        job_location = input("Enter Job Location: ")
        salary = float(input("Enter Salary: "))
        job_type = input("Enter Job Type (Full-time/Part-time/Contract): ")
        posted_date = datetime.now()

        job_listing = JobListing(
            job_id=None,  
            company_id=company_id,
            job_title=job_title,
            job_description=job_description,
            job_location=job_location,
            salary=salary,
            job_type=job_type,
            posted_date=posted_date
        )

        db_manager.insert_job_listing(job_listing)
        print(f"Job '{job_title}' posted successfully.")
    except Exception as e:
        print(f"Error posting job: {str(e)}")

def register_company(db_manager):
    try:
        company_name = input("Enter Company Name: ")
        location = input("Enter Company Location: ")

        company = Company(
            company_id=None,  
            company_name=company_name,
            location=location
        )

        db_manager.insert_company(company)
        print(f"Company '{company_name}' registered successfully.")
    except Exception as e:
        print(f"Error registering company: {str(e)}")

def register_applicant(db_manager):
    try:
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")
        resume = input("Enter Resume (file path or description): ")

        applicant = Applicant(
            applicant_id=None,  
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            resume=resume
        )

        db_manager.insert_applicant(applicant)
        print(f"Applicant '{first_name} {last_name}' registered successfully.")
    except Exception as e:
        print(f"Error registering applicant: {str(e)}")

def apply_for_job(db_manager):
    try:
        applicant_id = int(input("Enter Applicant ID: "))
        job_id = int(input("Enter Job ID: "))
        cover_letter = input("Enter Cover Letter: ")
        application_date = datetime.now()

        job_application = JobApplication(
            application_id=None,  
            job_id=job_id,
            applicant_id=applicant_id,
            application_date=application_date,
            cover_letter=cover_letter
        )

        db_manager.insert_job_application(job_application)
        print(f"Application submitted for Job ID {job_id} by Applicant ID {applicant_id}.")
    except Exception as e:
        print(f"Error submitting job application: {str(e)}")

def view_job_listings(db_manager):
    try:
        job_listings = db_manager.get_job_listings()
        print("\n--- Job Listings ---")
        for job in job_listings:
            print(f"Job ID: {job.job_id}, Title: {job.job_title}, Company ID: {job.company_id}, Location: {job.job_location}, Salary: {job.salary}, Type: {job.job_type}, Posted Date: {job.posted_date}")
    except Exception as e:
        print(f"Error retrieving job listings: {str(e)}")

def view_companies(db_manager):
    try:
        companies = db_manager.get_companies()
        print("\n--- Companies ---")
        for company in companies:
            print(f"Company ID: {company.company_id}, Name: {company.company_name}, Location: {company.location}")
    except Exception as e:
        print(f"Error retrieving companies: {str(e)}")

def view_applicants(db_manager):
    try:
        applicants = db_manager.get_applicants()
        print("\n--- Applicants ---")
        for applicant in applicants:
            print(f"Applicant ID: {applicant.applicant_id}, Name: {applicant.first_name} {applicant.last_name}, Email: {applicant.email}, Phone: {applicant.phone}")
    except Exception as e:
        print(f"Error retrieving applicants: {str(e)}")

def view_applications_for_job(db_manager):
    try:
        job_id = int(input("Enter Job ID: "))
        applications = db_manager.get_applications_for_job(job_id)
        print(f"\n--- Applications for Job ID {job_id} ---")
        for application in applications:
            print(f"Application ID: {application.application_id}, Applicant ID: {application.applicant_id}, Application Date: {application.application_date}, Cover Letter: {application.cover_letter}")
    except Exception as e:
        print(f"Error retrieving applications for job: {str(e)}")

if __name__ == "__main__":
    main_menu()
