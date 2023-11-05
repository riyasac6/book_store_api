Bookstore REST API with CRUD Operations

Clone Git
----------
git clone https://github.com/riyasac6/book_store_api.git

Run Docker 
----------
docker-compose -f docker-compose.yml up -d --build

Restore Database
---------
cd sql/ && cat book_store_db.sql | docker exec -i base-postgres psql -U postgres

Down and Up Docker
--------
docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d

Postman Collection
--------
[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/18979185-63aa8f09-9dd1-4bcb-bf30-3a92e90bcdcc?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D18979185-63aa8f09-9dd1-4bcb-bf30-3a92e90bcdcc%26entityType%3Dcollection%26workspaceId%3Df1ce25d2-dc16-40d5-b166-703112d6cf66)


