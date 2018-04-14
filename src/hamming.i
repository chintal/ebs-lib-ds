
 %include "stdint.i"
 
 %module hamming
 %{
 /* Includes the header in the wrapper code */
 #include "config.h"
 #include "hamming.h"
 %}
 
 %include "carrays.i"
%array_class(uint8_t, buffer);
 
 /* Parse the header file to generate wrappers */
 %include "config.h"
 %include "hamming.h"
