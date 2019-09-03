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
I see a line for the shared history of the two branches, and red lines after the math branch forks off of the master branch


```

3. Use `git diff BRANCH_NAME` to view the differences from a branch and the current branch.
   Summarize the difference from master to the other branch.

```
the calculate_this function has code to caluclate a sum for the master version, but just prints text for the math version. Also, the math version has an extra line of a different file. 

```

4. Write a command sequence to merge the non-master branch into `master`

```
git merge <math>

```


5. Write a command (or sequence) to (i) create a new branch called `math` (from the `master`) 
and (ii) change to this branch

```
git checkout -b <math> <master>

```
   
6. Edit B.py adding the following source code below the content you have there
```
print 'I know math, look:'
print 2+2
```

7. Write a command (or sequence) to commit your changes
```


```

8. Change back to the `master` branch and change B.py adding the following source code (commit your change to `master`):
```
print 'hello world!'
```

9. Write a command sequence to merge the `math` branch into `master` and describe what happened
```


```
   
10. Write a set of commands to abort the merge
```


```
   
11. Now repeat item 10, but proceed with the manual merge (Editing B.py). All implemented methods are needed. Explain your procedure
```


```

12. Write a command (or set of commands) to proceed with the merge and make `master` branch up-to-date
```


```

### Part 2: Using GitHub


4. Report your experience of making this submission, including the steps followed, commands used, and hurdles faced (within the file you created for the **Part 1**.
```


```



