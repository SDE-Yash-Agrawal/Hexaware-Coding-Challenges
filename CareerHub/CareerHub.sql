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

INSERT INTO Company (CompanyName, Location)
VALUES 
('Tata Consultancy Services', 'Mumbai, Maharashtra'),
('Infosys', 'Bengaluru, Karnataka'),
('Wipro', 'Bengaluru, Karnataka'),
('HCL Technologies', 'Noida, Uttar Pradesh'),
('Reliance Industries', 'Mumbai, Maharashtra'),
('Flipkart', 'Bengaluru, Karnataka'),
('Zomato', 'Gurgaon, Haryana'),
('Swiggy', 'Bengaluru, Karnataka'),
('Paytm', 'Noida, Uttar Pradesh'),
('Hexaware', 'Chennai, Tamil Nadu');

select * from Company;


INSERT INTO JobListing (CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
VALUES 
(1, 'Software Engineer', 'Develop and maintain software applications.', 'Mumbai, Maharashtra', 600000.00, 'Full-time', '2024-09-15'),
(2, 'Data Analyst', 'Analyze business data to generate insights.', 'Bengaluru, Karnataka', 450000.00, 'Full-time', '2024-09-16'),
(3, 'DevOps Engineer', 'Manage infrastructure and deployments.', 'Bengaluru, Karnataka', 700000.00, 'Full-time', '2024-09-17'),
(4, 'Network Engineer', 'Maintain company network systems.', 'Noida, Uttar Pradesh', 550000.00, 'Full-time', '2024-09-18'),
(5, 'Project Manager', 'Lead and manage software development projects.', 'Mumbai, Maharashtra', 900000.00, 'Full-time', '2024-09-19'),
(6, 'Marketing Manager', 'Plan and execute marketing campaigns.', 'Bengaluru, Karnataka', 800000.00, 'Full-time', '2024-09-20'),
(7, 'UI/UX Designer', 'Design user-friendly interfaces for apps.', 'Gurgaon, Haryana', 500000.00, 'Full-time', '2024-09-21'),
(8, 'Content Writer', 'Write and edit educational content.', 'Bengaluru, Karnataka', 400000.00, 'Part-time', '2024-09-22'),
(9, 'Finance Analyst', 'Analyze financial data for decision making.', 'Noida, Uttar Pradesh', 600000.00, 'Full-time', '2024-09-23'),
(10, 'Data Engineer', 'Work on the data gathering and pipelining.', 'Mumbai, Maharashtra', 750000.00, 'Full-time', '2024-09-24');

select * from JobListing;


INSERT INTO Applicant (FirstName, LastName, Email, Phone, Resume)
VALUES
('Sarthak', 'Londhey', 'sarthak.londhey@gmail.com', '9826996450', 'sarthak_resume.pdf'),
('Yash', 'Agrawal', 'sde.yash.agrawal@gmail.com', '6263605492', 'yash_resume.pdf'),
('Khushi', 'Joshi', 'khushijoshi0129@gmail.com', '8770108629', 'khushi_resume.pdf'),
('Sneha', 'Verma', 'sneha.verma@gmail.com', '9876543200', 'sneha_resume.pdf'),
('Rohit', 'Singh', 'rohit.singh@gmail.com', '8876543214', 'rohit_resume.pdf'),
('Neha', 'Kapoor', 'neha.kapoor@gmail.com', '6876543215', 'neha_resume.pdf'),
('Arjun', 'Kumar', 'arjun.kumar@gmail.com', '9876543944', 'arjun_resume.pdf'),
('Sakshi', 'Desai', 'sakshi.desai@gmail.com', '9876543217', 'sakshi_resume.pdf'),
('Vikram', 'Rao', 'vikram.rao@gmail.com', '6876543218', 'vikram_resume.pdf'),
('Anjali', 'Jain', 'anjali.jain@gmail.com', '7876543219', 'anjali_resume.pdf');

select * from Applicant;


INSERT INTO JobApplication (JobID, ApplicantID, ApplicationDate, CoverLetter)
VALUES
(50, 100, '2024-09-25 10:00:00', 'I am excited to apply for the Software Engineer position.'),
(51, 101, '2024-09-26 11:00:00', 'Looking forward to contributing as a Data Analyst at Infosys.'),
(52, 102, '2024-09-27 12:00:00', 'I have experience in DevOps and would love to join Wipro.'),
(53, 103, '2024-09-28 13:00:00', 'My skills in networking will be a good fit at HCL Technologies.'),
(54, 104, '2024-09-29 14:00:00', 'I have led successful projects and can bring value to Reliance Industries.'),
(55, 105, '2024-09-30 15:00:00', 'Excited about the opportunity to manage marketing campaigns at Flipkart.'),
(56, 106, '2024-10-01 16:00:00', 'I am passionate about UI/UX design and can enhance the user experience at Zomato.'),
(57, 107, '2024-10-02 17:00:00', 'Food is my love language, and I would love to contribute as a Content Writer at Swiggy.'),
(58, 108, '2024-10-03 18:00:00', 'My experience in finance will help Paytm make informed decisions.'),
(59, 109, '2024-10-04 19:00:00', 'I have expertise in Data engineering and ETL so would be thrilled to join Hexaware.');

select * from JobApplication;






