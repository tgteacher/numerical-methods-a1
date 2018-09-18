# A1: Systems of Linear Algebraic Equations


## Note

This assignment must be submitted individually. You are encouraged to 
discuss and exchange solutions during the tutorial sessions or on 
Slack, but you are *not allowed* to share code electronically. 
Plagiarism, unauthorized collaboration and other offences under 
Concordia's [Academic Code of Conduct](http://www.concordia.ca/students/academic-integrity/offences.html) will be firmly handled. 

## Assignment submission

Assignments are submitted through GitHub classroom.

To prepare and submit your assignment, you will:
1. Accept the assignment in GitHub classroom. This will create your own copy
   of the assignment repo, located at http://github.com/tgteacher/COMP-361-A1-F2018-<your_github_username>.
2. Clone your copy on your computer, and implement the functions in `a1.py`, following the instructions in the functions' documentation strings.
3. Commit your solution to your local copy: `git add a1.py` ; `git commit`.
4. Push your solution to your GitHub copy: `git push`.

You can repeat steps 3 and 4 as many times as you wish. A snapshot of 
your repository will be taken on the due date for evaluation.

## Evaluation

### Grading

Your assignment will be automatically graded through software tests. 

Half of the tests are available to you, located in directory `tests`. You
may want to run them before the submission deadline, to check that your
solution complies to them. To do so, you will have to install `pytest` and simply
run `pytest tests` in the base directory. 

Half of the tests will remain undisclosed until after the submission deadline.
Undisclosed tests are meant to ensure that your solution doesn't hard code the
specific values used in the tests. Undisclosed tests will look very similar to the
disclosed ones.

Your grade will be determined from the number of passing tests as
returned by pytest. All tests will contribution equally to the final grade for this 
assignment. For instance, if 20 tests are evaluated (including disclosed and undisclosed ones),
and your solution passes 18 tests, then your grade will be 90%.

### Test environment and live feedback.

Your code will be tested with Python 3.5 in a Ubuntu environment. If 
needed, Python 3.5 is available in the computer labs and can be loaded 
using `module load python/3.5.1`. You can check the version of Python that
you are using by running `python --version`.

It is strongly suggested that you run the disclosed tests before 
submitting your assignment, using `pytest` as explained previously. 

In addition, live feedback on your assignment is provided by Travis CI 
[here](https://travis-ci.com/tgteacher) (you will have to sign-in using your GitHub account to see your 
assignment repository).

