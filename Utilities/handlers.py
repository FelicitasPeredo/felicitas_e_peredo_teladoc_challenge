class DatasetHandlers:
    #create a tuple from the dataset dictionary to input the parametrize decorator
    def test_handler(file):
        result = tuple({iteration: data} for iteration, data in file.items())
        return result
        
