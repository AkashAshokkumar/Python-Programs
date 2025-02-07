def dis(a,b):
    try:
        print('Task Started')
        print(a/b)
    except:
        print('Some Error has Occured')
    else:
        print('Task is Executed without any Error')
    finally:
        print('Task Ended')

dis(10,0)
dis(10,2)
dis(10,5)