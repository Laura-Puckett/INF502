### Part 1: Dealing with git

1. Draw a diagram of the commits and branches in repository.

    - Use `git branch` to list the branches in this repository.
    - Use `git checkout` to explore each branch.
    - Use `git log --decorate` to explore the structure of commits.

```
                                                - "Making a small change here" (MASTER branch)
"create all files" - "Added a draft of A"  -< 
                                                -  "Adding some more knowledge to the function" (Math branch)

```

2. Try `git log --graph --all` to see the commit tree. What do you see?
```
A commit tree with a fork.

* commit 18931d12a8be7cac049b73c6bc8136e9482f3371 (master)
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:15:28 2019 -0700
| 
|     Making a small change here
|   
| * commit e3c629dd524712aedea96d7dbaad1c50d12b5b5e (HEAD -> math)
|/  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
|   Date:   Wed Aug 14 23:13:48 2019 -0700
|   
|       Adding some more knowledge to the function
| 
* commit 654b490a181dedf82dd6deda5f9848d6cca05918
| Author: Igor Steinmacher <igorsteinmacher@gmail.com>
| Date:   Wed Aug 14 23:12:14 2019 -0700
| 
|     Added a draft of A.py
| 
* commit 2dfb02c3f9383d6c3b2695c99e175d8b85f594a1
  Author: Igor Steinmacher <igorsteinmacher@gmail.com>
  Date:   Wed Aug 14 23:08:47 2019 -0700
  
       Creating all files (all empty)

```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch.
   Summarize the difference from master to the other branch.

```
the calculate_this function has code to caluclate a sum in the master branch, but just prints text in the math branch Also, in the math branch, it has an extra line of a different file. 

```

4. Write a command sequence to merge the non-master branch into `master`

```
git commit -all -m "commiting changes before merging math branch into master"
git merge math
git branch -d math

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) 
and (ii) change to this branch

```
git checkout -b math master

```
   
6. Edit B.py adding the following source code below the content you have there
```
print 'I know math, look:'
print 2+2

```

7. Write a command (or sequence) to commit your changes
```
git commit --all -m "added lines to B.py"

```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened
```
The merge failed because there was a merge conflict in B.py (since it had been edited in both branches, there's a merge conflict)

```
   
10. Write a set of commands to abort the merge
```
git merge --abort
git reset

```
   
11. Now repeat item 10, but proceed with the manual merge (Editing B.py). All implemented methods are needed. Explain your procedure
```
I tried to merge, and got an error. Then I opened the B.py file (using sudo open -e B.py) and saw this:
<<<<<<< HEAD
# Another file that will receive a line of code... at least.
print 'hello world!'

=======
print 'I know math, look:'
print 2+2
>>>>>>> math

I then I incorporated both changes by editing the file to the following:
# Another file that will receive a line of code... at least.
print 'hello world!'
print 'I know math, look:'
print 2+2

then I added the new file to the commit by using: git add B.py, then I comitted using: git commit -all -m 'resolved conflicts in B.py"

```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date
```
git checkout master
git merge math

```

### Part 2: Using GitHub


4. Report your experience of making this submission, including the steps followed, commands used, and hurdles faced (within the file you created for the **Part 1**.
```



```



