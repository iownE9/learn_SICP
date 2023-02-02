# note

scm> (define a '(1))
    a
    scm> a
    (1)
    scm> (define b (cons 2 a))
    b
    scm> b
    (2 1)
    scm> (define c (list 3 b))
    c
    scm> c
    (3 (2 1))
    scm> (car c)
    3
    scm> (cdr c)
    ((2 1))
    scm> (car (car (cdr c)))
    2
    scm> (cdr (car (cdr c)))
    (1)

(= nil ()) ; Error = 仅用于数字
(eq? lst nil)
(null? lst)
