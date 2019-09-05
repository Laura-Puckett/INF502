# 1. 
## *source code*

     def pythagoreanTheorem(length_a, length_b):
       hypotenuse = (length_a**2 + length_b**2)**(1/2)
       return hypotenuse
    
## *example output*

     >>> pythagoreanTheorem(2,2)
     2.8284271247461903
     
     >>> pythagoreanTheorem(3,4) 
     5.0

     >>> pythagoreanTheorem(11,48)
     49.24428900898052
          

# 2. 

## *approach*

     For each item in the original list, I checked to make the that the item was an integer,
     and then checked if it was even (if not even then I assumed it to be odd). I multiplied 
     by 2 or 3 for even and odd numbers, respectivley, then appended each new number to a list
     of mangled numbers to be returned.

## *source code*

     def list_mangler(list_in):
         new_list = []
         for number in list_in:
             if type(number) == int:
                 if number % 2 == 0:
                     new_number = number * 2
                 else:
                     new_number = number* 3
                 new_list.append(new_number)
         return new_list
    
## *example output*  

     >>> list_mangler([1,2,3,4])
     [3, 4, 9, 8]

     >>> list_mangler([2,3,5,10])
     [4, 9, 15, 20]

     >>> ist_mangler([-2,0,11,5])
     [-4, 0, 33, 15]

# 3. 

## *approach* 

     In order to drop the lowest grades from the list, I first sorted the list from highest 
     to lowest. Then used indexing to take only the elements of the list that weren't to be 
     dropped and took the average of those values. Then I used if/elif/else statements to 
     determine the letter grade to output for the associated average grade.

## *source code*

     def grade_calc(grades_in, to_drop):
         import statistics
         grades_in.sort(reverse = True)
         non_dropped = grades_in[:len(grades_in)-to_drop]
         final_grade = statistics.mean(non_dropped)

         if (final_grade >= 90):
             letter_grade = 'A'
         elif (final_grade >= 80):
             letter_grade = 'B'
         elif (final_grade >= 70):
             letter_grade = 'C'
         elif (final_grade >= 60):
             letter_grade = 'D'
         else:
             letter_grade = 'F'

         return letter_grade

## *example output*  

     >>> grade_calc([100,90,80,95],2)
     'A'

     >>> grade_calc([100,0,0,90,50],1)
     'D'

     >>> grade_calc([70,75,70,65],0)
     'C'

# 4. 
## *approach*

     I made a blank list for even and odd numbers, then iterated through each number in 
     the original list and appended it to the respective list. I output a tuple of both lists.

## *source code*

     def odd_even_filter(numbers):
         even_list = []
         odd_list = []
         for number in numbers:
             if type(number) == int:
                 if number % 2 == 0:
                     even_list.append(number)
                 else:
                     odd_list.append(number)

         return(even_list, odd_list)
    
## *example output*  

     >>> odd_even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
     ([2, 4, 6, 8], [1, 3, 5, 7, 9])

     >>> odd_even_filter([3, 9, 43, 7])
     ([], [3, 9, 43, 7])

     >>> dd_even_filter([71, 39, 98, 79, 5, 89, 50, 90, 2, 56])
     ([98, 50, 90, 2, 56], [71, 39, 79, 5, 89])
