def mergeDict():
     x = {'Vika' : 'piano',
          'Kate': 'guitar',
          'Lily' : 'violin'}
     y = {'Alex' : 'football',
          'Jack' : 'rugby'}
     z = dict(list(x.items()) + list(y.items()))
     print(z)

mergeDict()