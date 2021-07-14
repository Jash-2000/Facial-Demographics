"""

	In scikit-learn, LDA is implemented using LinearDiscriminantAnalysis includes a parameter, n_components indicating the number of features we want returned. To figure out what argument value to use with n_components (e.g. how many parameters to keep), we can take advantage of the fact that explained_variance_ratio_ tells us the variance explained by each outputted feature and is a sorted array.

Specifically, we can run LinearDiscriminantAnalysis with n_components set to None to return ratio of variance explained by every component feature, then calculate how many components are required to get above some threshold of variance explained (often 0.95 or 0.99).

"""

# Load libraries
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# Load the Iris flower dataset:
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Create and run an LDA
lda = LinearDiscriminantAnalysis(n_components=None)
X_lda = lda.fit(X, y)

# Create array of explained variance ratios
lda_var_ratios = lda.explained_variance_ratio_

# Create a function
def select_n_components(var_ratio, goal_var: float) -> int:
    # Set initial variance explained so far
    total_variance = 0.0
    
    # Set initial number of features
    n_components = 0
    
    # For the explained variance of each feature:
    for explained_variance in var_ratio:
        
        # Add the explained variance to the total
        total_variance += explained_variance
        
        # Add one to the number of components
        n_components += 1
        
        # If we reach our goal level of explained variance
        if total_variance >= goal_var:
            # End the loop
            break
            
    # Return the number of components
    return n_components

# Run function
select_n_components(lda_var_ratios, 0.95)