;; Funkcje wstawiajace polskie litery

(defun insert-a-ogonek ()
  (interactive "*")
  (insert 305) ;; ±
)

(defun insert-c-acute ()
  (interactive "*")
  (insert 358) ;; æ
)

(defun insert-e-ogonek ()
  (interactive "*")
  (insert 362) ;; ê 
)

(defun insert-l-slash ()
  (interactive "*")
  (insert 307) ;; ³
)

(defun insert-n-acute ()
  (interactive "*")
  (insert 369) ;; ñ
)

(defun insert-o-acute ()
  (interactive "*")
  (insert 371) ;; ó
)

(defun insert-s-acute ()
  (interactive "*")
  (insert 310) ;; ¶
)

(defun insert-z-acute ()
  (interactive "*")
  (insert 316) ;; ¼
)

(defun insert-z-dot ()
  (interactive "*")
  (insert 319) ;; ¿
)

(defun insert-A-ogonek ()
  (interactive "*")
  (insert 289) ;; ¡
)

(defun insert-C-acute ()
  (interactive "*")
  (insert 326) ;; Æ
)

(defun insert-E-ogonek ()
  (interactive "*")
  (insert 330) ;; Ê
)

(defun insert-L-slash ()
  (interactive "*")
  (insert 291) ;; £
)

(defun insert-N-acute ()
  (interactive "*")
  (insert 337) ;; Ñ
)

(defun insert-O-acute ()
  (interactive "*")
  (insert 339) ;; Ó
)

(defun insert-S-acute ()
  (interactive "*")
  (insert 294) ;; ¦
)

(defun insert-Z-acute ()
  (interactive "*")
  (insert 300) ;; ¬
)

(defun insert-Z-dot ()
  (interactive "*")
  (insert 303) ;; ¯
)

(global-set-key (quote [aogonek])   (quote insert-a-ogonek))
(global-set-key (quote [Aogonek])  (quote insert-A-ogonek))
(global-set-key (quote [cacute]) (quote insert-c-acute))
(global-set-key (quote [Cacute]) (quote insert-C-acute))
(global-set-key (quote [eogonek]) (quote insert-e-ogonek))
(global-set-key (quote [Eogonek]) (quote insert-E-ogonek))
(global-set-key (quote [lstroke]) (quote insert-l-slash))
(global-set-key (quote [Lstroke]) (quote insert-L-slash))
(global-set-key (quote [nacute]) (quote insert-n-acute))
(global-set-key (quote [Nacute]) (quote insert-N-acute))
(global-set-key (quote [oacute]) (quote insert-o-acute))
(global-set-key (quote [Oacute]) (quote insert-O-acute))
(global-set-key (quote [sacute]) (quote insert-s-acute))
(global-set-key (quote [Sacute]) (quote insert-S-acute))
(global-set-key (quote [zacute]) (quote insert-z-acute))
(global-set-key (quote [Zacute]) (quote insert-Z-acute))
(global-set-key (quote [zabovedot]) (quote insert-z-dot))
(global-set-key (quote [Zabovedot]) (quote insert-Z-dot))
(global-set-key (quote [?\M-`]) (quote set-justification-left))
