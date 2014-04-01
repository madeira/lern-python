__author__ = 'madeira'
import sys
def iter_lines(fd):
    ch = fd.read(1)
    res = ''
    while ch !='':
        if ch == '\n':
            yield res
            res = ''
        else:
            res += ch
        ch = fd.read(1)
    yield res

def strip_spaces(iter):
    for line in gen:
        yield line.strip()

gen =  iter_lines(open('text.txt'))
gen2 = strip_spaces(gen)

if __name__ == '__main__':
    for line in iter_lines(open('text.txt')):
        print repr(line)


