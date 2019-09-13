# A1: Systems of Linear Algebraic Equations


## Important note

This assignment must be submitted individually. You are encouraged to 
discuss and exchange solutions during the tutorial sessions or on 
Slack, but you are *not allowed* to share code electronically. 
Plagiarism, unauthorized collaboration and other offences under 
Concordia's [Academic Code of Conduct](http://www.concordia.ca/students/academic-integrity/offences.html) will be firmly handled. 

## Preliminary comments

To submit this assignment, you will have to be familiar with Git and
GitHub. If you have never used these technologies, it is recommended to 
go through the following tutorials:
* [Git](https://rogerdudler.github.io/git-guide)
* [GitHub](https://guides.github.com/)

In particular, you will have to be able to:
1. *Clone* a Git repository from GitHub: find the URL of a GitHub repository
and clone it using `git clone <repo_url>`.
2. *Commit* modifications to a local clone of a Git repository: `git add <file>` and `git commit -m "message"`.
3. *Push* modifications from your local clone to the origin repository on GitHub: `git push`.


## Assignment submission

You have to submit your assignment through GitHub classroom, using the following procedure:
1. Accept the assignment at https://classroom.github.com/a/fKVCmAhq. This will create your own copy
   of the assignment repository, located at http://github.com/tgteacher/COMP-361-A1-F2019-your_github_username.
2. Clone your copy of the assignment repository on your computer, and 
implement the functions in `a1.py`, following the instructions in the 
documentation strings.
3. Commit your solution to your local copy of the assignment repository.
4. Push your solution to your GitHub copy of the assignment repository.

You can repeat steps 3 and 4 as many times as you wish. Your assignment 
will be graded based on a snapshot of your repository taken on the 
submission deadline.

Note that **you are not allowed to use functions from 
`numpy.linalg` to implement this assignment**.


## Evaluation

### Grading

Your assignment will be automatically graded through software tests. 

Half of the tests are already available in directory `tests`. You
may want to run them as you implement your solution, to check that your
code passes them. To do so, you will have to install `pytest` and simply
run `pytest tests` in the base directory of the assignment. 

Half of the tests will remain undisclosed until after the submission deadline.
Undisclosed tests are meant to ensure that your solution doesn't hard code the
specific values used in the tests. Undisclosed tests will look very similar to the
disclosed ones.

Your grade will be determined from the number of passing tests as 
returned by pytest. All tests will contribute equally to the final 
grade. For instance, if 20 tests are evaluated (including disclosed and 
undisclosed ones), and your solution passes 18 tests, then your grade 
will be 90%.

### Test environment and live feedback.

Your code will be tested with Python 3.5 in a Ubuntu environment 
provided by Travis CI. It is your responsibility to ensure that the 
tests will pass in this environment. The following resources will help 
you.

Python 3.5 is available in the computer labs and can be loaded using 
`module load python/3.5.1`. You can check the version of Python that 
you are using by running `python --version`. Computer labs can easily be
accessed remotely, using `ssh`.

It is strongly suggested that you run the disclosed tests before 
submitting your assignment, using `pytest` as explained previously. 

Live feedback on your assignment is provided through Travis CI 
[here](https://travis-ci.com/tgteacher). You will have to sign-in using 
your GitHub account to see your assignment repository. **Your grade will be determined 
from the result of the
tests executed in Travis CI**.

