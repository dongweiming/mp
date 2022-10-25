def task(num):
    raise TypeError(f'Error with {num}')


errors = []
for num in [1, 4, 9]:
    try:
        task(num)
    except TypeError as e:
        e.add_note(f'Note: {num}')
        errors.append(e)

if errors:
    raise ExceptionGroup('Task issues', errors)
