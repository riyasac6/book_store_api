# book_store_api
Bookstore REST API with CRUD Operations

Clone Git
----------
git clone https://github.com/riyasac6/book_store_api.git

Run Docker 
----------
docker-compose -f docker-compose.yml up -d --build

Restore Database
---------
cd sql/
cat book_store_db.sql | docker exec -i base-postgres psql -U postgres

Down and Up Docker
--------
docker-compose -f docker-compose.yml down && docker-compose -f docker-compose.yml up -d






