'''

NAME
	struct_array.py

VERSION
	[1.1]

AUTHOR
	[Rodelmar Ocampo] <joserodelmar@gmail.com>
	[Other authors]: [Modifications]


DESCRIPTION
	[Structured arrays contain information on induction temperature and cost of production
	for certain genes, this are used to get a cost benefit relation for the gene's
	induction]

CATEGORY
	[numpy usage]

USAGE
	[struct_array.py][-options/arguments]

ARGUMENTS
	[ejer]  [array organised in gene's name, production at 30 degrees C, and at 35 degrees C]
	[cos]  [array organised in gene's name, cost of induction]

INPUT
	[No input required unless data in the corresponding fields is modified]

NOT WORKING INPUT
    [No input required]

OUTPUT
    [Arrays with both temperatures and respective gene's cost of production/induction]

EXAMPLES
    [Program us run
    >Output>
    Beneficio con induccion a 30 grados C [0.7        0.45454545 1.75       2.15      ]
    Beneficio con induccion a 35 grados C [1.16666667 0.71428571 0.77777778 0.71666667]
    ]

GITHUB
    [https://github.com/Rodel-OL/python_class/blob/master/tareas/struct_array.py]

'''

import numpy as np
### data in ejer references two columns of temperature as well as gene's name
ejer = np.array([('gen_1',5,3),('gen_2',11,7),('gen_3',4,9),('gen_4',2,6)],
                dtype=[('Gene', (np.str_, 6)), ('30C', np.int32), ('35C', np.int32)])

### data in cos references gene's name and cost of production
cos = np.array([('gen_1', 3.5), ('gen_2', 5), ('gen_3', 7), ('gen_4', 4.3)],
               dtype=[('Gene', np.str_, 6), ('costo', np.float64)])

### Both columns of temperature and their costs will be printed separately
bene30 = cos['costo'] / ejer['30C']
bene35 = cos['costo'] / ejer['35C']

print("Beneficio con induccion a 30 grados C", bene30)
print("Beneficio con induccion a 35 grados C", bene35)
