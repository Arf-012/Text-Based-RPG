# Untuk map

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examination'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
    'a1': False, 'a2': False, 'a3': False, 'a4': False,
    'b1': False, 'b2': False, 'b3': False, 'b4': False,
    'c1': False, 'c2': False, 'c3': False, 'c4': False,
    'd1': False, 'd2': False, 'd3': False, 'd4': False,
}

zonemap = {
    'a1': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'An entrance to the town, with a large wooden gate and a guard standing watch.',
        EXAMINATION: 'You see a large wooden gate with a guard standing watch. The guard looks stern and vigilant.',
        SOLVED: False,
        UP: None,
        DOWN: 'b1',
        LEFT: None,
        RIGHT: 'a2'
    },
    'a2': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'The Town Square, a plaza with bussling activity, shops, and townsfolk.',
        EXAMINATION: 'the Town Square is filled with people. You can see shops and stalls selling various goods.',
        SOLVED: False,
        UP: None,
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },
    'a3': {
        ZONENAME: 'Town Center',
        DESCRIPTION: 'The Town Center, a large building with a clock tower and a fountain in front.',
        EXAMINATION: 'The Town Center is a large building with a clock tower. The fountain in front is surrounded by flowers.',
        SOLVED: False,
        UP: None,
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'The place where the mayor works, a large building with a grand entrance.',
        EXAMINATION: 'The Town Hall is a large building with a grand entrance. The doors are made of oak and are intricately carved.',
        SOLVED: False,
        UP: None,
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: None
    },
    'b1': {
        ZONENAME: 'b1',
        DESCRIPTION: 'b1 description',
        EXAMINATION: 'b1 examination',
        SOLVED: False,
        UP: 'c1',
        DOWN: 'd1',
        LEFT: None,
        RIGHT: 'b2'
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Your home looks the same - nothing changed',
        SOLVED: False,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
    },
    'b3': {
        ZONENAME: 'b3',
        DESCRIPTION: 'b3 description',
        EXAMINATION: 'b3 examination',
        SOLVED: False,
        UP: 'c3',
        DOWN: 'd3',
        LEFT: 'b2',
        RIGHT: 'b4'
    },
    'b4': {
        ZONENAME: 'b4',
        DESCRIPTION: 'b4 description',
        EXAMINATION: 'b4 examination',
        SOLVED: False,
        UP: 'c4',
        DOWN: 'd4',
        LEFT: 'b3',
        RIGHT: None
    },
    'c1': {
        ZONENAME: 'c1',
        DESCRIPTION: 'c1 description',
        EXAMINATION: 'c1 examination',
        SOLVED: False,
        UP: 'd1',
        DOWN: None,
        LEFT: None,
        RIGHT: 'c2'
    },
    'c2': {
        ZONENAME: 'c2',
        DESCRIPTION: 'c2 description',
        EXAMINATION: 'c2 examination',
        SOLVED: False,
        UP: 'd2',
        DOWN: None,
        LEFT: 'c1',
        RIGHT: 'c3'
    },
    'c3': {
        ZONENAME: 'c3',
        DESCRIPTION: 'c3 description',
        EXAMINATION: 'c3 examination',
        SOLVED: False,
        UP: 'd3',
        DOWN: None,
        LEFT: 'c2',
        RIGHT: 'c4'
    },
    'c4': {
        ZONENAME: 'c4',
        DESCRIPTION: 'c4 description',
        EXAMINATION: 'c4 examination',
        SOLVED: False,
        UP: 'd4',
        DOWN: None,
        LEFT: 'c3',
        RIGHT: None
    },
    'd1': {
        ZONENAME: 'd1',
        DESCRIPTION: 'd1 description',
        EXAMINATION: 'd1 examination',
        SOLVED: False,
        UP: None,
        DOWN: None,
        LEFT: None,
        RIGHT: 'd2'
    },
    'd2': {
        ZONENAME: 'd2',
        DESCRIPTION: 'd2 description',
        EXAMINATION: 'd2 examination',
        SOLVED: False,
        UP: None,
        DOWN: None,
        LEFT: 'd1',
        RIGHT: 'd3'
    },
    'd3': {
        ZONENAME: 'd3',
        DESCRIPTION: 'd3 description',
        EXAMINATION: 'd3 examination',
        SOLVED: False,
        UP: None,
        DOWN: None,
        LEFT: 'd2',
        RIGHT: 'd4'
    },
    'd4': {
        ZONENAME: 'd4',
        DESCRIPTION: 'd4 description',
        EXAMINATION: 'd4 examination',
        SOLVED: False,
        UP: None,
        DOWN: None,
        LEFT: 'd3',
        RIGHT: None
    }
}