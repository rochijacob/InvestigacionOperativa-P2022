"""
Because of excessive pollution on the Momiss River, the state of Momiss is going to build pollution control stations. Three sites (1, 2, and 3) are under consideration. Momiss is interested in controlling the pollution levels of two pollutants (1 and 2). The state legislature requires that at least 80,000 tons of pollutant 1 and at least 50,000 tons of pollutant 2 be removed from the river. The relevant data for this problem are shown in Table 10. Formulate an IP to minimize the cost of meeting the state legislature’s goals.
"""

import picos

P = picos.Problem()

y = picos.BinaryVariable('y', 3) #Construyo o no la estacion

P.set_objective('min', 100000*y[0] + 60000*y[1] + 40000*y[2])