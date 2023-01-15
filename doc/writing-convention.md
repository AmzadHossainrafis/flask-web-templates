
* --> aurthor :  @amzadhossainrafis
* ---> date :  2023-01-1
* ----> version :  1.0.0
* -----> email : amzad.rafi@northsouth.edu


# writing convention for the project
---------------------------------------------------------------
Writing conventions are important in Git projects because they help to ensure consistency and clarity in the codebase. This makes it easier for other developers to understand and work with the code, as well as for automated tools to parse and analyze the code. Good writing conventions can also help to prevent errors and bugs from occurring, by providing a clear structure for the code and making it easier to spot potential issues. Additionally, good writing conventions can help to improve the overall maintainability of the codebase, by making it easier to add new features or make changes without introducing new bugs. Overall, writing conventions are essential to ensure that a Git project is well-organized, readable, and maintainable, which will make it easier for developers to collaborate and contribute to the project.






## commit convention :
---------------------------------------------------------------

1. format message in this manner 

    git commit -m "title:  -- body:  what  kind of change  is done , why , any remak or  any  other  thing  you want to  say"
    keep the message in short and simple 

    emxample : 
    git commit -m "title-chng: -- body:  title X to Y  , misleading title"    

2. branch convention
   
    long branch name : master ->  all the  production  code  will be  in this branch including new realease and hotfixes  
    dev branch name : dev -> all the devleopment  will be done in this branch .
    short branch name :  name-of-feature ->  all the  feature  will be  in this branch. Delete the short branch after merging to dev branch 


----------------------------------------------------------------

create separate file for style , script 

    style folder :  all the css files will be  in this folder 
    script folder :  all the js files will be  in this folder


upadet the requirment.txt file after installing any new package 

    commands :  pip freeze > requirment.txt 

    

-----------------------------------------------------------------

test your code before pushing to the remote repo 
you can create your own test cases in the test.py file in the test folder 
    
    commands :  python test.py

or use github action to test your code 

-----------------------------------------------------------------





## contributing to open source 
--------------------------------------------------------------

 1. fork the repo 
 2. clone the repo ( git clone repo-link )
 3. create a branch  ( git checkout -b branch-name )
 4. make changes
 5. commit changes ( git commit -m "title:  -- body:  what  kind of change  is done , why , any remak or  any  other  thing  you want to  say" )
 6. push changes  ( git push origin branch-name )
 7. create pull request ( git pull origin branch-name )
 8. wait for review 
 9. merge the pull request
 10. delete the branch ( git branch -d branch-name)



## For those who are new to git , here are some 
--------------------------------------------------------------

### git commands : 

    git init :  initialize the git repo in the current directory  
    commands : $ git init   

    git status :  check the status of the repo , what files are modified , added , deleted , untracked , etc.
    commands : $ git status

    git add :  add the files to the staging area

    commands : 
    git add .  ( add all the files to the staging area )
    git add filename  ( add the specific file to the staging area )
    git add -A  ( add all the files to the staging area )


    git commit :  commit the changes to the local repo
    commands :  git commit -m "title:  -- body:  what  kind of change  is done , why , any remak or  any  other  thing  you want to  say"


    git push :  push the changes to the remote repo
    commands :  git push origin branch-name



    git pull :  pull the changes from the remote repo to the local repo
    commands :  git pull origin branch-name


    git clone :  clone the repo from the remote repo to the local repo.
    commands :  git clone repo-link


    git branch :  create a new branch
    commands :  git branch branch-name


    git checkout :  switch to a branch
    commands :  git checkout branch-name


    git merge :  merge the changes from one branch to another branch
    commands :  git merge branch-name   


    git log :  check the commit history
    commands :  git log


    git diff :  check the difference between the files
    commands :  git diff


    git remote :  check the remote repo
    commands :  git remote -v  

    git reset :  reset the changes

    commands :  git reset --hard HEAD



