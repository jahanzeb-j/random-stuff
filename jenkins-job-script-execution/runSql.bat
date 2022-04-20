@ echo off

echo %1
docker cp %1 Postgres10:/check.sql
docker exec Postgres10 psql -U postgres -d postgres -f check.sql