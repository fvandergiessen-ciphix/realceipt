# Realceipt

## About the project

This project uses the Django REST Framework to create a web app where receipts can be uploaded to and retrieved from an SQL database. The user can upload receipts of any file type.

## Requirements

- Python 3.6+
- Django 5.0, 4.2, 4.1, 4.0, 3.2, 3.1, 3.0

## Start the project

Download the project and open it in VS Code. Open the terminal and run the following:

`python manage.py runserver`

Click on the link that is provided in the output. Add '/realceipt/homepage/' to the URL path to go to the Realceipt homepage. 

## URL paths
Follow the URL paths below to reach to project pages. If necessary, change the port path to the port provided in the previous step.

| Page | URL path |
| -------- | -------- |
| Homepage   | http://127.0.0.1:8000/realceipt/homepage/   |
| Uploading a receipt   | http://127.0.0.1:8000/realceipt/newreceipt/   |
| Viewing all receipts   | http://127.0.0.1:8000/realceipt/receipts/   |
| Viewing a specific receipt*   | http://127.0.0.1:8000/realceipt/receipts/receipt_id/    |
| Viewing a specific receipt item*   | http://127.0.0.1:8000/realceipt/receipts/receipt_id/item/item_id/   |

*Replace <receipt_id> with the id of the receipt and <item_id> with the id of the item
You can find the added receipt file in the link provided in the receipt details. 

