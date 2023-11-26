<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
<div id="badges">
  <a href="https://www.linkedin.com/in/dastan-ermekov-aa96b4229/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://www.youtube.com/channel/UCrXONS8wjv1LKdgxICTuf9A">
    <img src="https://img.shields.io/badge/YouTube-red?style=for-the-badge&logo=youtube&logoColor=white" alt="Youtube Badge"/>
  </a>
  <a href="your-twitter-URL">
    <img src="https://img.shields.io/badge/Twitter-blue?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter Badge"/>
  </a>
</div>
</div>


<div align="center">
  <img src="https://media.giphy.com/media/dWesBcTLavkZuG35MI/giphy.gif" width="600" height="300"/>
</div>



 Для накатывания миграций, если файла alembic.ini ещё нет, нужно запустить в терминале команду:
```
- alembic init migrations:
 ```

После этого будет создана папка с миграциями и конфигурационный файл для алембика.
- В alembic.ini нужно задать адрес базы данных, в которую будем катать миграции.
- Дальше идём в папку с миграциями и открываем env.py, там вносим изменения в блок, где написано

from myapp import mymodel:
- Дальше вводим: ``` alembic revision --autogenerate -m "comment" ``` - делается при любых изменениях моделей
- Будет создана миграция
- Дальше вводим: ``` alembic upgrade heads ```

Для того, чтобы во время тестов нормально генерировались миграции нужно:
- сначала попробовать запустить тесты обычным образом. с первого раза все должно упасть
- если после падения в папке tests создались алембиковские файлы, то нужно прописать туда данные по миграхам
- если они не создались, то зайти из консоли в папку test и вызвать вручную команды на миграции, чтобы файлы появились


Когда клонируете приложение на сервер надо так же выдать прова на bash скрипт
``` chmod +x run.sh  ```
