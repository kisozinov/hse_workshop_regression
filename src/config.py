TARGET_COL = 'SalePrice'
ID_COL = 'Id'
CAT_COLS = ['MSSubClass', 'MSZoning', 'LotShape', 'LandContour',  'Alley',
       'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 
       'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 
       'Exterior1st', 'Exterior2nd', 'MasVnrType', 'Foundation',  'Heating', 
       'Electrical',  'Functional', 'GarageType', 'SaleType', 'SaleCondition', 'MiscFeature',
       'PavedDrive', 'Street', ]
RATE_CAT_COLS = ['FireplaceQu', 'KitchenQual', 'ExterQual', 
       'ExterCond', 'BsmtQual', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 
       'BsmtFinType2', 'HeatingQC',  'GarageFinish','GarageQual', 'GarageCond', 'PoolQC', 'Fence']
RATE_COLS = ['OverallQual', 'OverallCond']
DATE_COLS = ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt', 'MoSold', 'YrSold']
BIN_COLS = ['CentralAir']
DISCRETE_COLS = ['BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 
              'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars']
REAL_COLS = ['LotFrontage', 'LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 
       'BsmtUnfSF', 'TotalBsmtSF', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 
       'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal', 
       '1stFlrSF', 'GrLivArea', '2ndFlrSF', 'LowQualFinSF']

NAN_COLS = ['Alley', 'MiscFeature', 'PoolQC', 'Fence']
CATBOOST_NUM_COLS = ['OverallQual', 'YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'ExterQual',
       'BsmtQual', 'BsmtExposure', 'BsmtFinSF1', 'TotalBsmtSF', 'HeatingQC',
       '1stFlrSF', 'GrLivArea', 'FullBath', 'KitchenQual', 'TotRmsAbvGrd',
       'Fireplaces', 'FireplaceQu', 'GarageFinish', 'GarageCars',
       'GarageArea']

CATBOOST_CAT_COLS = ['MSSubClass', 'MSZoning', 'Street', 'Alley', 'LotShape', 'LandContour',
       'Utilities', 'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
       'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl',
       'Exterior1st', 'Exterior2nd', 'MasVnrType', 'Foundation', 'Heating',
       'Electrical', 'Functional', 'GarageType', 'PavedDrive', 'MiscFeature',
       'SaleType', 'SaleCondition']