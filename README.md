# egn.py
Minimal library for extracting info from Bulgarian national identification numbers (EGN), written in Python

Usage:

    >>> import egn
    
    >>> # Valid EGN
    >>> egn = egn.Egn("2501014540")
    
    >>> Print info encoded in the EGN
    >>> print(egn)
    Year: 1925
    Month: 1
    Day: 01
    Gender: Male
    Region: Plovdiv
    
    >>> # Get individual fields
    >>> egn.year
    '1925'
    >>> egn.month
    1
    >>> egn.day
    '01'
    >>> egn.gender
    'Male'
    >>> egn.region
    'Plovdiv'
    
    >>> # Invalid EGN
    >>> egn = egn.Egn("2502155456")
    >>> Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "egn.py", line 33, in __init__
    self.validate()
    File "egn.py", line 96, in validate
    raise RuntimeError("Invalid EGN")
    RuntimeError: Invalid EGN


Features:
 - Automatic validation as per ESGRAON specification: http://www.grao.bg/esgraon.html
 - Support for EGNs for people born between 1800 and 2100
 - Determine date of birth, sex and region of birth

To do:
 - EGN generation by given criteria
