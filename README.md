# CM500292_Flight_Management_Database_App_Projet

To run the application type in a bash Python main.py 


The main file initialize the db_init that load all the DDL and DML and perform the insert to mock the data for testing purpose. 

Pattern applied 

MVC - Repository 
The MVC repository pattern has been applied. Queries to be executed are stored in the various repositories (folder repository); 
the controller performs input sanitization, query recall, and any data formatting. 
The application entities are defined in the model folder.
The display logic of the menus which includes the graphical part is delegated to the main.py