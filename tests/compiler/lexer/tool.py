
with open('test.hapdl', 'w', encoding='u8') as f:
    for i in range(100000):
        f.write(f'# {i}\n')