; simple function to check if (x)emacs is supporting mule
(defun mule? ()
  ""
  (string-match "--with-mule" system-configuration-options)
)
    
(if (string-match "^pl.*" (or (getenv "LC_CTYPE") (getenv "LC_ALL") (getenv "LANG") "C"))
	(if (mule?)
			(load "ogony-mule")
		(load "ogony-nomule")
	)
		
)

