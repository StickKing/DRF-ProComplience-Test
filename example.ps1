#------------------------------- Получение токена -------------------------------
$form = @{username = 'root'; password = 'root'}
$url = 'http://127.0.1.1:8000/token/'
$responce = Invoke-RestMethod -Uri $url -Method Post -Form $form
$accessToken = $responce.access
$refreshToken = $responce.refresh

#------------------------------- Вывод данных -------------------------------
$headers = @{Authorization = 'Bearer ' + $accessToken}
#Чтобы вывести информацию о всех файлах
$url = 'http://127.0.1.1:8000/documents/'
#Чтобы вывести информацию о конкретном файле
$url = 'http://127.0.1.1:8000/documents/1/'
#Осуществление запроса
$responce = Invoke-RestMethod -Uri $url -Method Get -Headers $headers

#------------------------------- Загрука файла с данными POST -------------------------------
#Файл для загрузки
$file_name = Get-Item -Path '.\apartment_cost_list.csv'
#Создание формы в которой указывем имя атрибута и файла
$form = @{document_file = $file_name}
$headers = @{Authorization = 'Bearer ' + $accessToken}
$url = 'http://127.0.1.1:8000/documents/'
Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Form $form

#------------------------------- Получение данных из файла POST -------------------------------
#Создание формы в которой указывем имя атрибута и файла
$form = @{sorting_column = 'age (years)'; item_count = '5';
          sort_ascending = $False;}
$headers = @{Authorization = 'Bearer ' + $accessToken}
$url = 'http://127.0.1.1:8000/documents/file/3/'
Invoke-RestMethod -Uri $url -Method Post -Headers $headers -Form $form