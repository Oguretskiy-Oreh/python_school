# README #
  
ШЮП Артезио

Автор заданий - Александр Игнатов

Материалы для обучения - https://drive.google.com/drive/u/1/folders/1jUBrSJauBKdfnc4SVye5GJMfvrIERNuc
  
### How do I get set up? ###
  
1. Настройте email и name для Git:   
  `git config --global user.email <your Email>`  
  `git config --global user.name <your First name and Last name>`  
2. Склонируйте свой форк себе на машину (`git clone <repository>`)  
3. Установите основной репозиторий как upstream для вашей копии (в случае использования SSH ссылка на репозиторий будет другая)  
  
### Contribution guidelines ###
  
1. Сделать форк этого репозитория (как это сделать - https://confluence.atlassian.com/bitbucket/forking-a-repository-221449527.html).  
2. В свой репозиторий (ветку `master`) запулить (`git pull`) последнюю версию проекта с ветки `master`  
  `git pull upstream master --rebase --autostash`  
3. Создать ветку для работы над заданием (например Lesson_1)  
  `git checkout -b Lesson_1`  
4. Выполнить необходимые изменения, закомитить и запушить их в удаленный репозиторий. То есть в вашем форке на bitbucket должна появиться ветка Lesson_1 с вашими изменениями.  
5. На сайте bitbucket.org зайти в своём репозитории в раздел "Pull Request" и создать pull request (вашей ветки) в этот репозиторий.  
    
    Title - FirstName LastName <Email>: Lesson Number(E.g. Lesson 1)
    Description:  
    Описание изменений (E.g. Exercises for the Lesson 1)  
    дополнительные сведения вроде пояснений и т.п.
  
    закрывать `master` не нужно.  
