1. Which of the following are operators, and which are values?

    *
    'hello'
    -88.8
    -
    /
    +
    5

    Operators: +, -, *, /
    Values: 'hello', -88.8, 5

2. Which of the following is a variable, and which is a string?

    spam
    'spam'

    Variable: spam
    String: 'spam'

3. Name three data types.

    Integers, floating-point numbers, and strings.

4. What is an expression made up of? What do all expressions do?

    An expression is a combination of values and operators. All expressions evaluate to a single value.

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?

    An expression evaluates to a single value. A statement does not.

6. What does the variable bacon contain after the following code runs?

    bacon = 20
    bacon + 1

    The bacon variable is set to 20. The bacon + 1 expression does not reassign the value in bacon.

7. What should the following two expressions evaluate to?

    'spam' + 'spamspam'
    'spam' * 3

    Both expressions evaluate to the string 'spamspamspam'

8. Why is eggs a valid variable name while 100 is invalid?

    Variable names cannot begin with a number.

9. What three functions can be used to get the integer, floating-point number, or string version of a value?

    The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.

10. Why does this expression cause an error? How can you fix it?

    'I have eaten ' + 99 + ' burritos.'

    The expression causes an error because 99 is an integer, and only strings can be concatenated to other strings with the + operator. The correct way is I have eaten ' + str(99) + ' burritos.'.

