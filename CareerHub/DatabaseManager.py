from entity.JobListing import JobListing
from entity.Company import Company
from entity.Applicant import Applicant
from entity.JobApplication import JobApplication
from dao.JobBoardDAOImpl import JobBoardDAOImpl
from exception.DBConnectionException import DBConnectionException

class DatabaseManager:
    def __init__(self):
        
        self.dao = JobBoardDAOImpl()

    def initialize_database(self):
        
        try:
            connection = self.dao.connection
            cursor = connection.cursor()

            
            create_companies_table = '''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Company' and xtype='U')
                CREATE TABLE Company (
                    CompanyID INT PRIMARY KEY IDENTITY(1,1),           
                    CompanyName VARCHAR(255) NOT NULL,   
                    Location VARCHAR(255)                
                );

            '''
            create_jobs_table = '''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='JobListing' and xtype='U')
                CREATE TABLE JobListing (
                    JobID INT PRIMARY KEY IDENTITY(50,1),               
                    CompanyID INT,                       
                    JobTitle VARCHAR(255) NOT NULL,      
                    JobDescription TEXT,                 
                    JobLocation VARCHAR(255),           
                    Salary DECIMAL(15, 2),               
                    JobType VARCHAR(50),                 
                    PostedDate DATETIME,                
                    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
                )
            '''   
            create_applicants_table = '''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Applicant' and xtype='U')
                CREATE TABLE Applicant (
                    ApplicantID INT PRIMARY KEY IDENTITY(100,1),         
                    FirstName VARCHAR(255) NOT NULL,     
                    LastName VARCHAR(255) NOT NULL,      
                    Email VARCHAR(255) NOT NULL,         
                    Phone VARCHAR(20) NOT NULL,                   
                    Resume VARCHAR(255) NOT NULL  
                )
            '''
            create_applications_table = '''
                IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='JobApplication' and xtype='U')
                CREATE TABLE JobApplication (
                    ApplicationID INT PRIMARY KEY IDENTITY(200,1),       
                    JobID INT NOT NULL,                           
                    ApplicantID INT NOT NULL,                     
                    ApplicationDate DATETIME NOT NULL,            
                    CoverLetter TEXT,                    
                    FOREIGN KEY (JobID) REFERENCES JobListing(JobID),   
                    FOREIGN KEY (ApplicantID) REFERENCES Applicant(ApplicantID) 
                )
            '''

            
            cursor.execute(create_jobs_table)
            cursor.execute(create_companies_table)
            cursor.execute(create_applicants_table)
            cursor.execute(create_applications_table)
            connection.commit()

        except Exception as e:
            raise DBConnectionException(f"Failed to initialize the database: {str(e)}")

    def insert_job_listing(self, job_listing: JobListing):
        try:
            self.dao.insert_job_listing(job_listing)
            print(f"Job listing for '{job_listing.job_title}' added successfully.")
        except Exception as e:
            raise DBConnectionException(f"Failed to insert job listing: {str(e)}")

    def insert_company(self, company: Company):
        try:
            self.dao.insert_company(company)
            print(f"Company '{company.company_name}' added successfully.")
        except Exception as e:
            raise DBConnectionException(f"Failed to insert company: {str(e)}")

    def insert_applicant(self, applicant: Applicant):
        try:
            self.dao.insert_applicant(applicant)
            print(f"Applicant '{applicant.first_name} {applicant.last_name}' added successfully.")
        except Exception as e:
            raise DBConnectionException(f"Failed to insert applicant: {str(e)}")

    def insert_job_application(self, job_application: JobApplication):
        try:
            self.dao.insert_job_application(job_application)
            print(f"Job application by applicant ID {job_application.applicant_id} for job ID {job_application.job_id} submitted successfully.")
        except Exception as e:
            raise DBConnectionException(f"Failed to insert job application: {str(e)}")

    def get_job_listings(self):
        try:
            job_listings = self.dao.get_job_listings()
            return job_listings
        except Exception as e:
            raise DBConnectionException(f"Failed to retrieve job listings: {str(e)}")

    def get_companies(self):
        try:
            companies = self.dao.get_companies()
            return companies
        except Exception as e:
            raise DBConnectionException(f"Failed to retrieve companies: {str(e)}")

    def get_applicants(self):
        try:
            applicants = self.dao.get_applicants()
            return applicants
        except Exception as e:
            raise DBConnectionException(f"Failed to retrieve applicants: {str(e)}")

    def get_applications_for_job(self, job_id: int):
        try:
            applications = self.dao.get_applications_for_job(job_id)
            return applications
        except Exception as e:
            raise DBConnectionException(f"Failed to retrieve applications for job ID {job_id}: {str(e)}")
