# README #
  
ШЮП Артезио  
  
### What is this repository for? ###
  
Задания Python для школы  
  
### How do I get set up? ###
  
1. Настройте email и name для Git:   
  `git config --global user.email <your Email>`  
  `git config --global user.name <your First name and Last name>`  
2. Склонируйте свой форк себе на машину (`git clone <repository>`)  
3. Установите основной репозиторий как upstream для вашей копии (в случае использования SSH ссылка на репозиторий будет другая)  
  `git remote add upstream https://<your_username>@bitbucket.org/alexandr_ignatov/python-school.git`  
  
### Contribution guidelines ###
  
1. Сделать форк этого репозитория (как это сделать - https://confluence.atlassian.com/bitbucket/forking-a-repository-221449527.html).  
2. В свой репозиторий (ветку `master`) запулить (`git pull`) последнюю версию проекта с ветки `master`  
  `git pull upstream master --rebase --autostash`  
3. Создать ветку для работы над заданием (например Lesson_1)  
  `git checkout -b Lesson_1`  
4. Выполнить необходимые изменения, закомитить и запушить их в удаленный репозиторий. То есть в вашем форке на bitbucket должна появиться ветка Lesson_1 с вашими изменениями.  
5. На сайте bitbucket.org зайти в своём репозитории в раздел "Pull Request" и создать pull request (вашей ветки) в этот репозиторий (alexandr_ignatov/python-scool).  
    
    Title - FirstName LastName <Email>  
    Description:  
    Описание изменений (E.g. Exercises for the Lesson 1)  
    дополнительные сведения вроде пояснений и т.п.
  
    закрывать `master` не нужно.  
      
6. Написать в Skype в чат ШЮП, что pull request готов к проверке (со ссылкой на него).  
  
### Who do I talk to? ###
  
Если какие-то вопросы, направляйте их в скайп в чат ШЮП или мне лично (live:alexandr.ignatov)  