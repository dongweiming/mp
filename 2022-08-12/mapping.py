def mapping(config):
    match config:
        case {'sub': sub_config, **rest}:
            print(f'Sub: {sub_config}')
            print(f'OTHERS: {rest}')
        case {'route': route}:
            print(f'ROUTE: {route}')


mapping({})
mapping({'route': '/auth/login'})
mapping({'route': '/auth/login', 'sub': {'a': 1}})
