from errors.ReadError import FileNotPL4Error

def readfile(file: str) -> object:
    try:
        
        if '.pl4' in file:
            arq: object = open(file, 'rb')
        else:
            raise FileNotPL4Error
        
    except FileNotFoundError:
       raise FileNotFoundError('File not found!')
   
    except FileNotPL4Error:
        raise FileNotPL4Error('It is not a pl4 file!')
    
    else:
        return arq
