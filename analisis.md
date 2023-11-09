#Anilisis de la calidad del aire 

SELECT *
FROM Cities
INNER JOIN Concentrations USING (City)
ORDER BY Cities."Total Population"  DESC
LIMIT 10;

SELECT *
FROM Cities
INNER JOIN Concentrations USING (City)
ORDER BY Cities."Total Population"  ASC 
LIMIT 10;

SELECT *
FROM Cities
INNER JOIN Concentrations USING (City)
ORDER BY Concentrations.overall_aqi  DESC
LIMIT 10;

SELECT *
FROM Cities
INNER JOIN Concentrations USING (City)
ORDER BY Concentrations.overall_aqi ASC 
LIMIT 10;

para realizar este analisis es primordial comprender en que consiste el indice de calidad del aire o Overall AQI por sus siglas en ingles, de acuerdo a Chat GPT, "el Overall AQI es una medida compuesta que se utiliza para evaluar la calidad general del aire en una región específica. Este índice proporciona una forma resumida de comunicar la calidad del aire a las personas de una manera comprensible y fácil de interpretar."

para poder interpretar los datos del Overall AQI este se divide por rangos o escalas que van desde bueno hasta peligroso para la salud de los seres vivos en ese sector, esta escala puede variar debido a las regulaciones y estandares que establecen las distisntas agencias de proteccion ambiental al rededor del mundo.A continuación, se podra apreciar la escala del Overall AQI:

0-50: Bueno: Cuando el AQI está en este rango, la calidad del aire se considera buena, y no se espera que la población en general experimente efectos adversos para la salud. La calidad del aire es aceptable y no representa un riesgo significativo.

51-100: Moderado: En este rango, la calidad del aire es considerada moderada, lo que significa que la calidad es aceptable; sin embargo, algunas personas sensibles pueden experimentar efectos leves a moderados en su salud. Se recomienda precaución si eres una persona especialmente sensible a la contaminación del aire.

101-150: Insalubre para grupos sensibles: La calidad del aire se considera insalubre para ciertos grupos sensibles, como niños, personas mayores y personas con afecciones médicas preexistentes. Pueden experimentar efectos adversos para la salud. Para la población en general, la calidad del aire aún se considera aceptable.

151-200: Insalubre: La calidad del aire se vuelve insalubre para la población en general. Todos pueden comenzar a experimentar efectos adversos para la salud, y los miembros de grupos sensibles pueden experimentar efectos más graves.

201-300: Muy insalubre: La calidad del aire se vuelve muy insalubre, y la población en general experimentará efectos adversos para la salud más serios. La exposición prolongada a niveles en este rango puede tener efectos graves en la salud.

301-500: Peligroso: La calidad del aire se vuelve peligrosa, y la población en general enfrenta un riesgo significativo para su salud. Se pueden emitir advertencias de salud y se pueden recomendar precauciones, como limitar las actividades al aire libre.

Teniendo en cuenta los resultados de las consultas (Queries), y la informacion suministrada anteriormente, se evidencia que las 10 principales ciudades mas pobladas de Estados Unidos, no son las que tienen peor calidad del aire, ya que en su mayoria entran en un rango moderado de contaminacion y solo representan un riesgo para unos cuantos individuos sensibles a este, por otro lado hay que hacer una excepcion con la ciudad de Los Angeles que ocupa el lugar numero dos dentro de las diez primeras ciudades y se encuentra en un rango insalubre, seria logico especular que al ser una ciudad tan grande, la contaminacion en el aire sea debido a esto mismo, una gran cantidad de personas reunidas en un mismo sitio pero esto tambien aplicaria entonces a la ciudad de Nueva York, que es la numero uno de la lista y tambien a las otras ocho ciudades que tienen rangos de calidad de aire buenos y moderados, una vez comprendido todo esto nos damos cuenta que la contaminacion del aire de Los Angeles, puede que se deba a factores diferentes a la poblacion, como por ejemplo las regulaciones ambientales emitidas, el manejo de residuos solidos generados en esta o sea producto de sus principales actividades economicas que son: la industria del entretenimiento, los negocios internacionales, aeronautica, petroleo y turismo. para nada es un secreto que la industria del entretenimiento, junto con la exploracion de combustibles fosiles son dos de los principales contamienantes actualmente, por un lado tenemos a una industria que se encarga de crear sets de grabacion, grandes insfraestruturas y utilerias que una vez usadas simplemente se desechan o se dejan al olvido, generando grandes cantidades de residuos y por el otro tenemos a un gigante que se encarga de explotar los suelos y generar grandes cantidades de emiciones a la atmosfera.

Analizando las ciudades con la peor calidad del aire de acuerdo al Overall AQI, lo primero que se logra observar, es que son ciudades que no tienen ni el 10%  de la poblacion que tiene New York, por otro lado New York, tiene un Overall AQI que representa el 15% del Overall AQI de la ciudad de Clear Water, que es la ciudad con el aire mas contaminado, lo que descarta la hipotesis de que las ciudades con mayor poblacion son las que peor aire tienen y le agrega bases al argumento de que la calidad del aire, no se ve influenciada por la cantidad de poblacion, sino por factores externos a esta variable, como las principales actividades economicas. Analizando las principales actividades economicas de  cada una de estas ciudades se detecta el patron de que la mayoria estas,  tiene entre sus principales actividades economicas el turismo, seguida de la construccion,bienes raices y mineria junto con aeronautica, lo que permite especular que quizas el sector turismo tenga una leve influencia en la calidad del aire, no seria tan descabellado pensar que los distintos patrones comportacionales de turistas que llegan de todo el mundo sumado con la polucion generada por el sector constructor, la contaminacion generada por la mineria y explotacion de residuos fosiles sea la encargada de que en ciudades con una poblacion relaticamente pequeña sea la culpable de la contaminacion del aire. Por ultimo cabe resaltar que la contaminacion del aire tambien se puede deber a catastrofes o fenomenos naturales tales como incendios forestales o erupciones volcanicas.

En conclusion La calidad del aire no se ve directamente influenciada por la cantidad de poblacion que una ciudad tiene, sino mas bien, está se debe a factores que son distintos a la misma, entre los factores que influyen a la contaminacion del aire pueden estar: las politicas ambientales tomadas por los entes reguladores de la ciudad, medidas de control y desechos de residuos, principales actividades economicas y fenomenos o catstrofes naturales.