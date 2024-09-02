import os

def get_model_path():
    my_path = __file__
    dir_name = os.path.dirname(my_path)
    model_path = os.path.join(dir_name, "model.pkl")
    
    return model_path
