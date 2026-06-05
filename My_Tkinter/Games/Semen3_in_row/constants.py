COLORS = ["red", "blue", 'orange', 'pink']

DISTANCE_X = 70
DISTANCE_Y = 74

OFFSET_X = {'x2': DISTANCE_X,
            'y2': 0,
            'x3': DISTANCE_X * 2,
            'y3': 0}

OFFSET_Y = {'x2': 0,
            'y2': -DISTANCE_Y,
            'x3': 0,
            'y3': -DISTANCE_Y * 2}

OPTIONS_X_OR_Y = [
    [DISTANCE_X, 0],
    [-DISTANCE_X, 0],
    [0, DISTANCE_Y],
    [0, -DISTANCE_Y]
]
