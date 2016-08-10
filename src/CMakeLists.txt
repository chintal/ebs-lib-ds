
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)
CMAKE_POLICY(SET CMP0007 NEW)

PROJECT(ds C)
SET(PROJECT_VERSION 1.0.0.0)

SET(TMP_PROJECT_DESCRIPTION 
    "Basic implementations of standard data structures for use in embedded systems"
    CACHE STRING "Project Description")

FILE(GLOB SOURCES *.c)
FILE(GLOB_RECURSE HEADERS *.h)

# This is a cross-platform build, and therefore is assumed to be intended for an 
# embedded target.
SET(CMAKE_INSTALL_PREFIX ${PLATFORM_PACKAGES_PATH})
SET(PUBLIC_INCLUDE_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR})
                
ADD_PLATFORM_LIBRARY(ds STATIC "" ${SOURCES})
INSTALL_PLATFORM_LIBRARY(ds ${HEADERS})
    