

CMAKE_MINIMUM_REQUIRED(VERSION 3.1)
CMAKE_POLICY(SET CMP0007 NEW)

SET(LIBRARY_NAME    ds)

PROJECT(${LIBRARY_NAME} C)

SET(PROJECT_DESCRIPTION     "Basic implementations of reusable data structures for use in embedded systems")
SET(PROJECT_AUTHOR_NAME     "Chintalagiri Shashank")
SET(PROJECT_AUTHOR_EMAIL    "shashank.chintalagiri@gmail.com")
SET(PROJECT_LICENSE         "GPLv3")
SET(PROJECT_VERSION_MAJOR   1)
SET(PROJECT_VERSION_MINOR   1)
SET(PROJECT_VERSION_PATCH   0)
SET(PROJECT_VERSION_TWEAK   0)

SET(TOOLCHAINS_PATH           	"/home/chintal/code/toolchains") 
LIST(APPEND CMAKE_MODULE_PATH 	${TOOLCHAINS_PATH})
SET(HAMMING_IMPL   		HAMMING_IMPL_ITER)

INCLUDE(ebs/lib-conf)

FILE(GLOB_RECURSE SOURCES *.c)
FILE(GLOB_RECURSE HEADERS *.h)

IF(CMAKE_TOOLCHAIN_FILE)
    # This is a cross-platform build, and therefore is assumed to be intended for an 
    # embedded target.
    ADD_PLATFORM_LIBRARY(ds STATIC "" ${SOURCES})
    IF(${CMAKE_CURRENT_SOURCE_DIR} STREQUAL ${CMAKE_SOURCE_DIR})
        INSTALL_PLATFORM_LIBRARY(ds ${HEADERS})
        INCLUDE(ebs/lib-doc)
    ENDIF()
    
ELSE(CMAKE_TOOLCHAIN_FILE)
    # This is a native build, and is assumed to be intended for the host. 
    # Libraries and bindings are therefore installed into the appropriate host prefix.
    
    # NOTE: C library is not compiled separately and is not installed.
    
    # Create PYTHON bindings
    SET(LIBRARY_NAME hamming)
    SET(SWIG_SOURCES hamming.i hamming.c)
    INCLUDE(ebs/swig-python)
    
ENDIF(CMAKE_TOOLCHAIN_FILE)

