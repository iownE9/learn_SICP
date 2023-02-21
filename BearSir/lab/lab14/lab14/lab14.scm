(define (split-at lst n)
  ; BearSir's
  (cond
    ((= n 0) (cons nil lst))
    ((> n (length lst)) (cons lst nil))
    (else (let  (
                  (p (split-at (cdr lst) (- n 1)))
                ) 
                (cons (cons (car lst) (car p)) 
                      (cdr p)
                )
          )
    )
  )
)


(define (compose-all funcs)
  (define (func x)
    (if (null? funcs)
        x
        ((compose-all (cdr funcs)) ((car funcs) x))
    )
  )
  func
)

