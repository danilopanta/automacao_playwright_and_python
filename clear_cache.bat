@echo off

REM Remove a pasta _pycache_ e seu conteúdo
for /d /r . %%d in (__pycache__) do (
    if exist "%%d" (
        echo Removendo a pasta "%%d"
        rmdir /s /q "%%d"
    )
)

REM Remove a pasta .pytest_cache e seu conteúdo
if exist .pytest_cache (
    echo Removendo a pasta .pytest_cache
    rmdir /s /q .pytest_cache
)

echo Limpeza de cache concluída.