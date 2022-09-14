""" Barrido Parametrico """

# Importamos librerias utiles
import picos
import numpy as np
import matplotlib.pyplot as plt


RUN_FULL_ANALYSIS = True
BARRIDO_COSTOS_OPERACION_PLANTA3 = np.linspace(0.0, 1.3, 14)


def crear_y_resolver_pe(costo_operacion_planta3):
    """"
    Función que resuelve el problema de planificación eléctrica.
    
    @param costo_operacion_planta3: Costo de operación anual de la planta 3.
                                    Parametro a barrer.

    @return punto_optimo: Tupla que contiene el punto óptimo, tanto de 'X', como de 'Y' y de 'Alpha'.
    @return valor_optmo: Valor óptimo.
    """

    # Introduzco todas las constantes
    # Demanda de cada año
    demanda = picos.Constant('demanda', [80, 100, 120, 140, 160])
    # Límite de producción de cada planta
    x_lim = picos.Constant('x_lim', [70, 50, 60, 40])
    # Costo de construcción  de cada planta
    c = picos.Constant('c', [20, 16, 18, 14])
    # Costo de operación anual de cada planta (una vez construída)
    o = picos.Constant('o', [1.5, 0.8, costo_operacion_planta3, 0.6])

    P = picos.Problem()

    x = picos.RealVariable('x', (4,5), lower = 0)
    alpha = picos.BinaryVariable('alpha', (4,5))
    y = picos.BinaryVariable('y', 4)

    # Restricción especial: 
    # Si y_i es 0 entonces la planta i no será construida y la fila x_i será toda 0
    # Si y_i es 1 entonces la planta i es construída en algún momento y 
    # por lo tanto la suma de la energía generada por esa planta será mayor a 0.
    P.add_list_of_constraints([x[i,:].sum <= 1e4*y[i] for i in range(4)])

    # Restricción especial: 
    # Si alpha_ij es 0 entonces x_ij es 0.
    # Si alpha_ij es 1 entonces x_ij va de 0 a lo que pueda producir esa planta
    # en un año.
    P.add_constraint(x <= 1e4*alpha)
    P.add_list_of_constraints([x[i,:] <= x_lim[i] for i in range(4)])

    # Una vez construída, la planta seguirá en operación, entonces si
    # alpha_ij es 1, en consecuencia #alpha_ij+1 también es 1
    P.add_list_of_constraints([alpha[:,j+1] >= alpha[:,j] for j in range(4)])

    # Año a año, la suma de energía generada debe ser igual a la demanda anual.
    P.add_list_of_constraints([x[:,j].sum == demanda[j] for j in range(5)])

    # Función objetivo
    P.set_objective('min', c.T * y + o[0] * alpha[0,:].sum + o[1] * alpha[1,:].sum + o[2] * alpha[2,:].sum + o[3] * alpha[3,:].sum)

    # Buscamos la solucion optima
    P.solve(solver = 'glpk')

    # Devolvemos el punto y valor optimo 
    punto_optimo = (x, alpha, y)
    valor_optmo = P.value
    return punto_optimo, valor_optmo


# Ejemplo de uso de funcion 'crear_y_resolver_pe'
if not RUN_FULL_ANALYSIS:
    print("Ejecutando codigo ejemplo:")
    (x_opt, alpha_opt, y_opt), z_opt = crear_y_resolver_pe(costo_operacion_planta3=1.3)
    print("X:")
    print(x_opt, end="\n\n")
    print("Alpha:")
    print(alpha_opt, end="\n\n")
    print("Y:")
    print(y_opt, end="\n\n")
    print("Z:")
    print(z_opt, end="\n\n")


if RUN_FULL_ANALYSIS:
    print("Ejecutando barrido parametrico:\n")
    print("Parametro a Barrer: Costo de operación de la planta 3")
    print("Valores a evaluar: {}\n".format(BARRIDO_COSTOS_OPERACION_PLANTA3))

    valores_optimos = []
    y_optimos = []
    for costo_op_p3 in BARRIDO_COSTOS_OPERACION_PLANTA3:
        (x_opt, alpha_opt, y_opt), z_opt = crear_y_resolver_pe(costo_operacion_planta3=costo_op_p3)
        y_optimos.append(y_opt)
        valores_optimos.append(z_opt)

    # Graficamos resultados
    # Grafico 1
    plt.figure("Costo Total")
    plt.plot(BARRIDO_COSTOS_OPERACION_PLANTA3, valores_optimos)
    # Activamos la grilla
    plt.grid(True)
    # Steamos titulo y ejes
    plt.title("Barrido Parametrico \n Costo Total vs Costo de Operacion de la planta N°3")
    plt.xlabel("Costo de Operación de la Planta N°3  [Millones $/Año]")
    plt.ylabel("Costo Total  [Millones $]")


    # Grafico 2
    cmap = plt.get_cmap('PiYG')
    plt.matshow(y_optimos, cmap=cmap)
    plantas = ['P1','P2','P3','P4']
    ncols = len(plantas)
    nrows = len(BARRIDO_COSTOS_OPERACION_PLANTA3)
    plt.xticks(np.arange(ncols), labels=plantas)
    plt.yticks(np.arange(nrows), labels=np.array(BARRIDO_COSTOS_OPERACION_PLANTA3).round(1))
    # Steamos titulo y ejes
    plt.title("Barrido Parametrico \n Uso de plantas vs Costo de Operacion de la planta N°3")
    plt.xlabel("Fabrica en uso")
    plt.ylabel("Costo de Operación de la Planta N°3  [Millones $/Año]")
    plt.tight_layout()
    # Add legend
    legends = ["Planta sin uso", "Planta en uso"]
    handles = [plt.Rectangle((0, 0), 0, 0, color=cmap(255 * i), label=legends[i]) for i in range(2)]
    plt.legend(handles=handles, title='Estado de Planta')
    # Activamos la grilla
    ax=plt.gca()
    ax.set_xticks([x-0.5 for x in range(1,ncols)], minor=True )
    ax.set_yticks([y-0.5 for y in range(1,nrows)], minor=True)
    plt.grid(which="minor",ls="-",lw=2)
    plt.show()