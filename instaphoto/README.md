Instaphoto - Btc-payable Instagram photo gallery
================================================

Summary: Easy way to sell your private Instagram photo


Create a private Instagram account
----------------------------------
Please create a pricate Instagram account first 


Instagram Access Token Generation
---------------------------------
Please follow the instruction of the article below:
<http://jelled.com/instagram/access-token>


Running the server
------------------
$ python3 server.py


API;

1. Update available Instagram photos
------------------------------------

HTTP URI: /update

Params: None

Result:
	- downloads all the available photos in seller's Instagram account into selected folder




2. Show available photos (In-Progress)
--------------------------------------

HTTP URI: /show

Params: None

Result:
	- show the availble photos in low resolution in a web page




3. List purchasable photos
--------------------------

HTTP URI: /files

Params: None

Result:
	- list the purchasable photos



4. Buy a photo!
---------------

HTTP URI: /buy

Result:
	- Buy a selected photo