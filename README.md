# This Readme File is for Coding Challenge - 2

**Schema Structure**

CREATE DATABASE CareerHub;
USE CareerHub;

CREATE TABLE Company (
    CompanyID INT PRIMARY KEY IDENTITY(1,1),           
    CompanyName VARCHAR(255) NOT NULL,   
    Location VARCHAR(255)                
);


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
);


CREATE TABLE Applicant (
    ApplicantID INT PRIMARY KEY IDENTITY(100,1),         
    FirstName VARCHAR(255) NOT NULL,     
    LastName VARCHAR(255) NOT NULL,      
    Email VARCHAR(255) NOT NULL,         
    Phone VARCHAR(20) NOT NULL,                   
    Resume VARCHAR(255) NOT NULL                  
);


CREATE TABLE JobApplication (
    ApplicationID INT PRIMARY KEY IDENTITY(200,1),       
    JobID INT NOT NULL,                           
    ApplicantID INT NOT NULL,                     
    ApplicationDate DATETIME NOT NULL,            
    CoverLetter TEXT,                    
    FOREIGN KEY (JobID) REFERENCES JobListing(JobID),   
    FOREIGN KEY (ApplicantID) REFERENCES Applicant(ApplicantID) 
);
