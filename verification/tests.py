"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [6, 3, 2],
            "answer": 4.0
        },
        {
            "input": [10, 1, 10],
            "answer": 11.111111111
        },
    ],
    "Edge": [
        {
            "input": [2, 1, 1],
            "answer": 2.0
        },
        {
            "input": [342, 1, 60],
            "answer": 60.175953079
        },
        {
            "input": [342, 341, 1],
            "answer": 342.0
        },
        {
            "input": [342, 341, 60],
            "answer": 20520.0
        },
    ],
    "Extra": [
        {
            "input": [213, 202, 37],
            "answer": 716.454545455
        },
        {
            "input": [330, 150, 57],
            "answer": 104.5
        },
        {
            "input": [26, 13, 59],
            "answer": 118.0
        },
        {
            "input": [106, 101, 16],
            "answer": 339.2
        },
        {
            "input": [15, 13, 56],
            "answer": 420.0
        },
    ]
}
