Create Database CarRentalSystem;

Use CarRentalSystem;

Create Table Vehicle (
    vehicleID Int PRIMARY KEY Identity(101, 1),
    make Varchar(50),
    model Varchar(50),
    year Int,
    dailyRate DECIMAL(10, 2),
    status Varchar(20),  
    passengerCapacity Int,
    engineCapacity Int
);

Create Table Customer (
    customerID Int PRIMARY KEY Identity(1, 1),
    firstName Varchar(50),
    lastName Varchar(50),
    email Varchar(100),
    phoneNumber Varchar(15)
);


Create Table Lease (
    leaseID Int PRIMARY KEY Identity(301, 1),
    vehicleID Int,
    customerID Int,
    startDate Date,
    endDate Date,
    type Varchar(20), 
    Foreign Key (vehicleID) References Vehicle(vehicleID),
    Foreign Key (customerID) References Customer(customerID)
);


Create Table Payment (
    paymentID Int PRIMARY KEY Identity(501, 1),
    leaseID Int,
    paymentDate Date,
    amount Decimal(10, 2),
    Foreign Key (leaseID) References Lease(leaseID)
);

Insert into Vehicle (make, model, year, dailyRate, status, passengerCapacity, engineCapacity)
Values 
    ('Toyota', 'Camry', 2022, 50.00, 'available', 4, 1450),
    ('Honda', 'Civic', 2023, 45.00, 'available', 7, 1500),
    ('Ford', 'Focus', 2022, 48.00, 'notAvailable', 4, 1400),
    ('Nissan', 'Altima', 2023, 52.00, 'available', 7, 1200),
    ('Chevrolet', 'Malibu', 2022, 47.00, 'available', 4, 1800),
    ('Hyundai', 'Sonata', 2023, 49.00, 'notAvailable', 7, 1400),
    ('BMW', '3 Series', 2023, 60.00, 'available', 7, 2499),
    ('Mercedes', 'C-Class', 2022, 58.00, 'available', 8, 2599),
    ('Audi', 'A4', 2022, 55.00, 'notAvailable', 4, 2500),
    ('Lexus', 'ES', 2023, 54.00, 'available', 4, 2500);

Insert into Customer (firstName, lastName, email, phoneNumber) 
Values
('Yash', 'Agrawal', 'sde.yash.agrawal@gmail.com', '6263605498'),
('Khushi', 'Joshi', 'khushijoshi0129@gmail.com', '8765432109'),
('Suresh', 'Patel', 'sureshpatel@gmail.com', '7654321098'),
('Dinesh', 'Verma', 'dineshverma@gmail.com', '6543210987'),
('Rajesh', 'Singh', 'rajeshsingh@gmail.com', '5432109876'),
('Ganesh', 'Kumar', 'ganeshkumar@ gmail.com', '4321098765'),
('Mahesh', 'Tiwari', 'maheshtiwari@ gmail.com', '3210987654'),
('Narendra', 'Mishra', 'narendramishra@ gmail.com', '2109876543'),
('Pradeep', 'Chauhan', 'pradeepchauhan@ gmail.com', '1098765432'),
('Sanjeev', 'Bhatt', 'sanjeevbhatt@ gmail.com', '9876543210');


Insert into Lease (vehicleID, customerID, startDate, endDate, type)
Values 
    (101, 1, '2023-01-01', '2023-01-05', 'Daily'),
    (102, 2, '2023-02-15', '2023-02-28', 'Monthly'),
    (103, 3, '2023-03-10', '2023-03-15', 'Daily'),
    (104, 4, '2023-04-20', '2023-04-30', 'Monthly'),
    (105, 5, '2023-05-05', '2023-05-10', 'Daily'),
    (104, 3, '2023-06-15', '2023-06-30', 'Monthly'),
    (107, 7, '2023-07-01', '2023-07-10', 'Daily'),
    (108, 8, '2023-08-12', '2023-08-15', 'Monthly'),
    (103, 3, '2023-09-07', '2023-09-10', 'Daily'),
    (110, 10, '2023-10-10', '2023-10-31', 'Monthly');

Insert into Payment (leaseID, paymentDate, amount)
Values 
    (301, '2023-01-03', 200.00),
    (302, '2023-02-20', 1000.00),
    (303, '2023-03-12', 75.00),
    (304, '2023-04-25', 900.00),
    (305, '2023-05-07', 60.00),
    (306, '2023-06-18', 1200.00),
    (307, '2023-07-03', 40.00),
    (308, '2023-08-14', 1100.00),
    (309, '2023-09-09', 80.00),
    (310, '2023-10-25', 1500.00);


Update Vehicle Set dailyRate = 68.00 Where make = 'Mercedes';


Delete From Payment Where leaseID IN (Select leaseID From Lease Where customerID = 3);
Delete From Lease Where customerID = 3;
Delete From Customer Where customerID = 3;


EXEC sp_rename 'Payment.paymentDate', 'transactionDate', 'COLUMN';


Select * From Customer Where email = 'sde.yash.agrawal@gmail.com';


Declare @currentDate Date = '2023-05-06';
Select Distinct C.customerID, C.firstName, C.lastName, C.email, C.phoneNumber
From Lease L JOIN Customer C ON L.customerID = C.customerID
Where @currentDate BETWEEN L.startDate AND L.endDate;


Declare @phoneNumber Varchar(20) = '6543210987';
Select P.paymentID, P.leaseID, P.transactionDate,
P.amount From Payment P Join Lease L ON P.leaseID
= L.leaseID Join Customer C ON L.customerID = 
C.customerID Where C.phoneNumber = @phoneNumber;


Select AVG(dailyRate) AS averageDailyRate 
From Vehicle Where status = 'available';


Select TOP 1 * From Vehicle Order By dailyRate Desc;


Select V.* From Vehicle V Join Lease L ON V.vehicleID 
= L.vehicleID Join Customer C ON L.customerID = 
C.customerID Where C.phoneNumber = '2109876543';


Select TOP 1 * From Lease Order By endDate Desc;


Select * from Payment Where Year(transactionDate) = 2023;


Select C.* From Customer C Left Join Lease L ON 
C.customerID = L.customerID Left Join Payment P 
ON L.leaseID = P.leaseID WHERE P.paymentID IS Null;


Select V.vehicleID, V.make, V.model, V.year,
V.dailyRate, ISNULL(Sum(P.amount), 0) AS 
totalPayments From Vehicle V Left Join 
Lease L ON V.vehicleID = L.vehicleID 
Left Join Payment P ON L.leaseID = P.leaseID 
Group By V.vehicleID, V.make, V.model, 
V.year, V.dailyRate Order By V.vehicleID;


Select C.customerID, C.firstName, C.lastName, C.email, 
C.phoneNumber, ISNULL(Sum(P.amount), 0) AS totalPayments 
From Customer C Left Join Lease L ON C.customerID = L.customerID
Left Join Payment P ON L.leaseID = P.leaseID Group By 
C.customerID, C.firstName, C.lastName, C.email, C.phoneNumber 
Order By C.customerID;


Select L.leaseID, L.vehicleID, L.customerID, L.startDate, L.endDate, 
L.type AS leaseType, V.make, V.model, V.year, V.dailyRate, V.status, 
V.passengerCapacity, V.engineCapacity From Lease L Join Vehicle V ON 
L.vehicleID = V.vehicleID Order By L.leaseID;


Declare @CurDate Date = '2023-05-06';
Select L.leaseID, L.vehicleID, V.make, V.model, V.year, V.dailyRate, L.customerID, 
C.firstName, C.lastName, C.email, C.phoneNumber, L.startDate, L.endDate, L.type AS 
leaseType From Lease L Join Vehicle V ON L.vehicleID = V.vehicleID Join Customer C 
ON L.customerID = C.customerID Where @CurDate Between L.startDate And L.endDate 
Order By L.leaseID;


Select TOP 1 C.customerID, C.firstName, C.lastName, 
C.email, C.phoneNumber, Sum(P.amount) AS totalSpent 
From Customer C Join Lease L ON C.customerID = 
L.customerID JOIN Payment P ON L.leaseID = P.leaseID 
Group By C.customerID, C.firstName, C.lastName, 
C.email, C.phoneNumber Order By totalSpent Desc;


Declare @date date = '2023-05-06'
Select V.vehicleID, V.make, V.model, V.year, 
V.dailyRate, V.status, L.leaseID, L.customerID, 
L.startDate, L.endDate, L.type AS leaseType From 
Vehicle V Left Join Lease L ON V.vehicleID = 
L.vehicleID And @date Between L.startDate And L.endDate;