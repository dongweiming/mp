def go(obj):
    match obj:
        case ['go', direction] if direction in ['east', 'north']:
            print('Right way')
        case direction if direction == 'west':
            print('Wrong way')
        case ['go', _] | _:
            print('Other way')
