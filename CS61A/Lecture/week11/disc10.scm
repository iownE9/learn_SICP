; 3.1
scm> (define a (+ 1 2))
a
scm> a
3
scm> (define b (- (+ (* 3 3) 2) 1))
b
scm> (= (modulo b a) (quotient 5 3))
#t
scm>


; 4.1
scm> (if (or #t (/ 1 0)) 1 (/ 1 0))
1
scm> ((if (< 4 3) + -) 4 100)
-96



; 4.1
(define (factorial x) 
    (if (= x 1)
        x
        (* x (factorial (- x 1)))
    )
)


; 4.2
(define (fib n)
    (if (< n 2)
        n
        (+ (fib (- n 1))   
           (fib (- n 2))
        )
    )
)



; 5.1
(define (my-append a b)
    (if (null? a)
        b
        (cons (car a) 
                (my-append (cdr a) b) 
        )
    )
)


; 5.2
(define (x) (+ 1 2 3))

; 5.3
(define (duplicate lst)
    (if (null? lst)
        lst
        (cons (car lst)
            (cons (car lst)
                (duplicate (cdr lst))
            )
        )
    )
)



; 5.4
(define (insert element lst index)
    (cond 
        ((null? lst) (cons element nil) )
        ((= index 0) (cons element lst) )
        (else (cons (car lst)
                    (insert element (cdr lst) (- index 1))
              )
        )
    )
)







