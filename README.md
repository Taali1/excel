Instalujesz Git Desktop oraz Doscker Desktop

Uruchamiasz tą komendę
```bash
git clone https://github.com/Taali1/excel.git && cd excel && docker build -t excel-image . && docker run -d -p 3000:3000 --name excel-container excel-image

```


W folderze który się pobrał jest folder OUTPUT. Tam znajdują się wszystkie HTMLe
