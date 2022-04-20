@ echo off

set SqlRun=runSql.bat
echo "#######################"
echo "   Script  Executing   "
echo "#######################"
echo "Path => "%1
echo "Sub Folder => "%2


FOR /R %1 %%f in (%2"\*.sql") do (
    echo "==>" %%f
    call %SqlRun% "%%f" 1
)

echo "======== DONE ========"