from dao.JobBoardDAO import JobBoardDAO
from entity.JobListing import JobListing
from entity.Company import Company
from entity.Applicant import Applicant
from entity.JobApplication import JobApplication
from util.DBConnUtil import DBConnUtil
import pyodbc

class JobBoardDAOImpl(JobBoardDAO):

    def __init__(self):
        self.connection = DBConnUtil.get_db_connection()  


    def insert_job_listing(self, job_listing):
        try:
            with self.connection.cursor() as cursor:
                query = """INSERT INTO JobListing (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
                           VALUES (?, ?, ?, ?, ?, ?, ?);"""
                cursor.execute(query, job_listing.company_id, job_listing.job_title, job_listing.job_description,
                               job_listing.job_location, job_listing.salary, job_listing.job_type, job_listing.posted_date)
                self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error inserting job listing: {str(e)}")

    def insert_company(self, company):
        try:
            with self.connection.cursor() as cursor:
                query = """INSERT INTO Company (CompanyName, Location)
                           VALUES (?, ?);"""
                cursor.execute(query, company.company_name, company.location)
                self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error inserting company: {str(e)}")

    def insert_applicant(self, applicant):
        try:
            with self.connection.cursor() as cursor:
                query = """INSERT INTO Applicant (FirstName, LastName, Email, Phone, Resume)
                           VALUES (?, ?, ?, ?, ?);"""
                cursor.execute(query, applicant.first_name, applicant.last_name, applicant.email,
                               applicant.phone, applicant.resume)
                self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error inserting applicant: {str(e)}")

    def insert_job_application(self, job_application):
        try:
            with self.connection.cursor() as cursor:
                query = """INSERT INTO JobApplication (JobID, ApplicantID, ApplicationDate, CoverLetter)
                           VALUES (?, ?, ?, ?);"""
                cursor.execute(query, job_application.job_id, job_application.applicant_id,
                               job_application.application_date, job_application.cover_letter)
                self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error inserting job application: {str(e)}")

    def get_job_listings(self):
        try:
            with self.connection.cursor() as cursor:
                query = """SELECT * FROM JobListing; """
                cursor.execute(query)
                rows = cursor.fetchall()

                job_listings = []
                for row in rows:
                    job_listing = JobListing(
                        job_id=row.JobID,
                        company_id=row.CompanyID,
                        job_title=row.JobTitle,
                        job_description=row.JobDescription,
                        job_location=row.JobLocation,
                        salary=row.Salary,
                        job_type=row.JobType,
                        posted_date=row.PostedDate
                    )
                    job_listings.append(job_listing)
                return job_listings
        except pyodbc.Error as e:
            print(f"Error retrieving job listings: {str(e)}")
            return []

    def get_companies(self):
        try:
            with self.connection.cursor() as cursor:
                query = """SELECT * FROM company;"""
                cursor.execute(query)
                rows = cursor.fetchall()

                companies = []
                for row in rows:
                    company = Company(
                        company_id=row.CompanyID,
                        company_name=row.CompanyName,
                        location=row.Location
                    )
                    companies.append(company)
                return companies
        except pyodbc.Error as e:
            print(f"Error retrieving companies: {str(e)}")
            return []

    def get_applicants(self):
        try:
            with self.connection.cursor() as cursor:
                query = """SELECT * FROM Applicant; """
                cursor.execute(query)
                rows = cursor.fetchall()

                applicants = []
                for row in rows:
                    applicant = Applicant(
                        applicant_id=row.ApplicantID,
                        first_name=row.FirstName,
                        last_name=row.LastName,
                        email=row.Email,
                        phone=row.Phone,
                        resume=row.Resume
                    )
                    applicants.append(applicant)
                return applicants
        except pyodbc.Error as e:
            print(f"Error retrieving applicants: {str(e)}")
            return []

    def get_applications_for_job(self, job_id):
        try:
            with self.connection.cursor() as cursor:
                query = """SELECT *
                           FROM JobApplication
                           WHERE JobID = ?;"""
                cursor.execute(query, job_id)
                rows = cursor.fetchall()

                applications = []
                for row in rows:
                    job_application = JobApplication(
                        application_id=row.ApplicationID,
                        job_id=row.JobID,
                        applicant_id=row.ApplicantID,
                        application_date=row.ApplicationDate,
                        cover_letter=row.CoverLetter
                    )
                    applications.append(job_application)
                return applications
        except pyodbc.Error as e:
            print(f"Error retrieving applications: {str(e)}")
            return []
