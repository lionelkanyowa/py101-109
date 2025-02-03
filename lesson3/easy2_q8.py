# 7. Determine whether the following dictionary of people and their age contains an
# entry for 'Spot'

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}
print('Spot' in ages)
print(ages.get('Spot'))

# Using the `in` operator we get a `False` returned.
# The `.get()` method returns a `None` suggesting that the key 'Spot' does
# not exist in the dictionary.

