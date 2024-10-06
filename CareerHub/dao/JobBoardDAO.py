from abc import ABC, abstractmethod

class JobBoardDAO(ABC):
    
    @abstractmethod
    def insert_job_listing(self, job_listing):
        """Insert a job listing into the database."""
        pass

    @abstractmethod
    def insert_company(self, company):
        """Insert a company into the database."""
        pass

    @abstractmethod
    def insert_applicant(self, applicant):
        """Insert an applicant into the database."""
        pass

    @abstractmethod
    def insert_job_application(self, job_application):
        """Insert a job application into the database."""
        pass

    @abstractmethod
    def get_job_listings(self):
        """Retrieve all job listings from the database."""
        pass

    @abstractmethod
    def get_companies(self):
        """Retrieve all companies from the database."""
        pass

    @abstractmethod
    def get_applicants(self):
        """Retrieve all applicants from the database."""
        pass

    @abstractmethod
    def get_applications_for_job(self, job_id):
        """Retrieve all job applications for a specific job."""
        pass
