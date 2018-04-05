# CallHubAssignment

## This application is hosted on https://sarvajeetsuman.com
Note : Due to privacy reasons I have not uploaded my settings file. 

This application has been created for the following purpose.

1. To get the fibonacci number between 1 to 999 & time taken to perform the query.
2. To see the history of previous queries
3. Fibonacci Number computation is happening in both Backend & Frontend,
   just for demonstration purpose.

## Frontend - Angular 5.
## Backend - django 1.11 & Django Rest framework 1.11
## Database - mysql
## Hosted on Google Cloud Appengine.

## Details:
Models : HistoryData 
saves input number in integer field & corresponding 
fibonacci number in database with created date & 
modified date.

Views:
HistoryDataViewset performs LIST & Create Operations.
Latest 10 results are listed on the frontend.
If the Number has been queried already, it fetches it from
the database. Otherwise it computes & sends back to the frontend.

## Issues Faced:
 1. Test cases are not working currently.
 

