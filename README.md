# Task 1: Create a module similar to `sklearn's` `datasets` module

Create a class called `my_sklearn`, which accepts following parameters

* path: str (path to the csv file)
* is_header: boolean (if the file has header)
* target_variable: str (target variable)
* feature_names: list (Not required if the file already has headers)
* random_state: int (Optional)

Define following methods.

*  **`Representation` in the format:**
    
    `Path: path/to/the/file.csv`
    
    `feature variables: ['your', 'list', 'of', 'features', 'here']`

    `target variable: your_target_variable `
     

*  **`load_data()` with following parameters:**

    * feature_subset: list of features to be selected (Optional)
    * train_size: float, fraction [0, 1] of data to be selected as training set (Optional)
    * CV_subset= "train", "test" or "all"

**Note:** 

* You can use `pandas`, `numpy` and `sklearn`'s `train_test_split` libraries.
* Error handling
