(if (eq mule-sysdep-version 0)
    (if (string-match "^pl.*" (or (getenv "LANG") "C")) 
	(load "kbd_pl")))




