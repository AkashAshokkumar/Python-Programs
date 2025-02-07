def dis(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print('Zero exception is occured')
    except TypeError:
        print('Type Error has Occured')
    except NameError:
        print('Name Error Has Occured')
    except:
        print('Some Error has Occured')

dis(10,0) # Zero exception is occured
dis(10,'Akash') # Type Error has Occured