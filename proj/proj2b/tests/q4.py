OK_FORMAT = True
test = {   'name': 'q4',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(test_predictions, np.ndarray) # must be ndarray of predictions\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> np.array_equal(np.unique(test_predictions), np.array([0, 1])) # must be binary labels (0 or 1) and not probabilities\nTrue',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> len(test_predictions) == 1000 # must be the right number of predictions\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
