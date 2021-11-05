from objetos import * # clases Path y Nodo

NODOS = { 0: Nodo("Estas en tu habitación, lleno de lujos disfrutando tu delicioso almuerzo. La vida es buena.",
                  [Path(1, "continuar")]),
          1: Nodo("Escuchas gritos provenientes de afuera.",
                  [Path(2, "seguir comiendo"), Path(3, "ir a la ventana")]),
          2: Nodo("Te dispones a seguir comiendo, pero eres interrumpido por la súbita entrada de un guardia.",
                  [Path(4, "Escuchar al guardia")]),
          3: Nodo("Hay un gran alboroto, guardias avanzan por el corredor a paso raudo. Las empleadas tiemblan mientras susurran entre ellas, una te mira de reojo y pronto todas se dispersan.",
                  [Path(4, "Buscar un guardia"), Path(4, "Preguntar qué está pasando")]),
          4: Nodo("Te informan que tu padre, el héroe del reino ha sido asesinado. De alguna forma encuentras las fuerzas para volver a tu cuarto. Sientes que el mundo da vueltas a tu alrededor, la temperatura desciende súbitamente, y la comida que acabas de consumir parece revolverse en tu estómago.",
                  [Path(5, "Te preparas para pelear, quien sea el culpable de esto pagará"), Path(6, "No aguantas la noticia y corres a encerrarte en tu habitación")]),
          5: Nodo("Mientras te preparas escuchas a alguien tocar la puerta",
                  [Path(8, "Abres la puerta"), Path(15, "Ignoras el llamado y sigues preparándote para salir")]),
          6: Nodo("Encerrado en tu cuarto escuchas que llaman a tu puerta",
                  [Path(8, "Abres la puerta"), Path(7, "Crees que aún no es el momento de ver a alguien y permaneces encerrado en tu luto")]),
          7: Nodo("Te tumbas en tu cama y dejas que el sueño se lleve tu pesadumbre. No sabes cuanto tiempo ha pasado, despiertas con el mismo cansancio con el que empezaste a dormir, no tienes energías para poner un pie afuera. Eventualmente se te acaba la comida y mueres de hambre.",
                  []),
          8: Nodo("En el umbral de la puerta aparece una figura con el semblante sombrío, te cuenta que su nombre es Adeltor. Te cuenta que es amigo de tu padre, que lo están persiguiendo y que no tiene mucho tiempo, menciona algo sobre una organización secreta, pero no terminas de entender. Adeltor mira con miedo hacia tu ventana, y corre despavorido. Sientes que te falta el aire, que toda tu habitación es un recordatorio de una gran mentira.",
                  [Path(9, "Tomas un abrigo y sales de tu habitación")]),
          9: Nodo("Sales de tu casa, y de la ciudad que te vio nacer, caminas sin rumbo fijo. Avanzas atormentado por tus pensamientos, ciego al mundo que te rodea. Unas figuras te cortan el paso y te sacan de tu sopor, una pandilla de bandidos, el pueblo más cercano es apenas visible, ¿cómo te defenderás?",
                  [Path(10, "Ataque de fuego"), Path(10, "Ataque de hielo"), Path(11, "Usar tu espada")]),
          10: Nodo("...Este poder no parece funcionar",
                  [Path(9, "Intentar un nuevo ataque")]),
          11: Nodo("Tu espada se rompe y la pandilla te golpea hasta dejarte en el suelo, inconsciente. Un aldeano pasa cerca tuyo, no tienes ninguna de las cosas que traías.",
                  [Path(7, "Los daños no son severos así que buscas descansar donde estás para recuperarte"), Path(12, "Llamas la atención del aldeano")]),
          12: Nodo("Le cuentas que eres el héroe, pero por el estado en el que te ve parece no creerte. Te ayuda a levantarte. \n"
                   "El aldeano te lleva a su casa, durante el camino le diste más detalles de lo que sabes y de lo que pasó, el hombre después de un rato comienza a creer tu historia.\n"
                   "Te cuenta que por estos lugares la vida siempre a sido cruel e injusta, sería bueno que el  héroe les prestara su fuerza...\n"
                   "Luego de contar tu historia al hombre, te das cuenta que no puedes hacer esto solo",
                  [Path(13, "Le cuentas al hombre que necesitas ayuda,")]),
          13: Nodo("El hombre resultó ser el alcalde de la pequeña localidad, decide ayudarte... Pronto se corre la voz entre los necesitados. Luego de unos días se ha reunido un buen pelotón de gente. "
                   "La gente harta de los malos tratos que recibe por parte de la aristocracia decide confiar en ti, ven una pequeña luz de esperanzas de acabar con su sufrimiento.",
                  [Path(14, "Ir con tus nuevos amigos a derrocar a la aristocracia "), Path(26, "Entrenar más antes de atacar")]),
          14: Nodo("Todos los miembros de tu comitiva luchan con ahínco. Sin embargo, la falta de habilidad es notoria.",
                  [Path(15, "seguir luchando contra la gran defensa aristocrática")]),
          15: Nodo("Eres brutalmente superado en fuerza y derrotado",
                  []),
          26: Nodo("Entre los hombres que aparecen se presenta uno particularmente misterioso, Mart, afirma que puede ayudar bastante, "
                   "pues tiene experiencia militar para entrenar a tus seguidores. Mas, nadie sabe de dónde ha salido, parece alguien confiado de sí mismo.\n"
                   "Te pide dejarle dirigir el entrenamiento. No parece dispuesto a irse...",
                   [Path(27, "Le permites ayudarte con el entrenamiento de la gente"), Path(30, "No le confías algo tan importante pero le permites quedarse")]),
          27: Nodo("Han pasado unos meses de arduo entrenamiento, haz compartido, sufrido y superados obstáculos junto a tus camaradas, Mart ha sido"
                   " de gran ayuda, habéis forjado una buena amistad con él, confías en él pero siempre tiene un aire de misterio.\n"
                   "Finalmente se preparan para marchar al palacio, pero Mart te dice que tiene asuntos que hacer y debe marcharse antes,"
                   "te dice que confíes en él y se va con una sonrisa que no termina de agradarte...",
                   [Path(16, "Es hora de partir, inician la marcha.")]),
          16: Nodo("Luego de una larga marcha de días y escaramuzas llegas al palacio con una fuerza"
                   " imparable y crees tener fuerza suficiente para conquistarlo.\n"
                   "Sin embargo en las filas enemigas divisas una figura familiar, es Mart... \n"
                   "Sus miradas se cruzan, él sonríe desafiante y muy confiado...",
                   [Path(28, "Esto parece una trampa, Mart conoce nuestras estrategias debemos retirarnos por hoy..."), Path(29,"Motivas a tus tropas a pesar de esta traición, con gran moral atacan el palacio..")]),
          28: Nodo("Emprendes la retirada, pero tus hombres con esta orden han perdido la moral y retroceden desorganizados, las fuerzas enemigas "
                   "les dan alcance.",
                   [Path(15, " Decides utilizar formaciones que no fueron enseñadas por Mart.")]),
          29: Nodo("Al iniciar la batalla, pierdes de vista a Mart de inmediato, decides concentrarte en la batalla, "
                   "Luego de horas de batallas comienzas a notar la superioridad que tienes, las tropas enemigas luchan pobremente"
                   " en contra de tus formaciones, finalmente luego de una ardua batalla logran asegurar el palacio. Todos cantan por el héroe.",
                  [Path(17, "Rechazar el canto y lideras la exploración del palacio"), Path(19, "El grupo necesita relajarte, asumir la posición de héroe y unirte al festejo")]),
          17: Nodo("Satisfecho con tu decisión, caminas por los grandes pasillos del palacio",
                  [Path(18, "Seguir explorando en busca de fugitivos")]),
          18: Nodo("Ingresas a una habitación oscura ubicada en el extremo del palacio. Con la poca luz ingresando a través de las cortinas vez algo brillante en el suelo",
                  [Path(20, "Recoger objeto brillante"), Path(21, "Ajustar ojos a la oscuridad")]),
          19: Nodo("Te quedas festejando con todos y te unes a la fiesta que estaba formándose",
                  [Path(20, "Continuar")]),
          20: Nodo("Sin notarlo, el héroe del otro reino ha caído en la locura y te ataca con una daga envenenada por la espalda",
                  []),
          21: Nodo("Entre las sombras, vez una silueta. Es el héroe del otro reino quien ha caído en la locura y te ataca. Apenas logras defenderte",
                  [Path(22, "luchar"), Path(23, "llamar por ayuda")]),
          22: Nodo("Sientes que no puedes contra él, repentinamente aparece Mart quien en un ataque suicida hacia el héroe enemigo generando una ventana y permitiéndote contratacar ganando la batalla",
                  [Path(24, "Asistir a Mart")]),
          23: Nodo("Mientras llamas por ayuda los ataques del héroe rival te dejan sin aliento. Por suerte, tus gritos fueron escuchados, es Mart quien se interpone entre tu y el ataque rival recibiendo una herida pero permitiéndote contratacar y ganar la batalla",
                  [Path(24, "Asistir a Mart")]),
          24: Nodo("Con sus últimas palabras, te dice que fue un honor haberte conocido y que ahora si eres un héroe de verdad al haber confiado en él. Te das cuenta de que él interfirió en las formaciones"
                   " del enemigo para que pudiesen ganar... Te despides de él entre lágrimas",
                  [Path(25, "Terminar tu misión")]),
          25: Nodo("Unificas Zarene y Cinait. Ganaste",
                  []),
          ###
          30: Nodo("Han pasado unos meses de arduo entrenamiento, haz compartido, sufrido y superados obstáculos junto a tus camaradas, Mart ha intentado"
                   " interferir varias veces con sus ideas en el entrenamiento, todo ha marchado bien de todas formas, él es bastante hábil pero siempre tiene un aire de misterio.\n"
                   "Finalmente se preparan para marchar al palacio, haz perdido de vista a Mart, parce haber desaparecido aunque no le das importancia.",
                   [Path(31, "Es hora de partir, inician la marcha.")]),
          31: Nodo("Luego de una larga marcha de días y escaramuzas llegas al palacio con una fuerza"
                   " imparable y crees tener fuerza suficiente para conquistarlo.\n"
                   "Sin embargo en las filas enemigas divisas una figura familiar, es Mart... \n"
                   "Sus miradas se cruzan, él sonríe desafiante y muy confiado...",
                   [Path(32, "Esto parece una trampa, Mart conoce nuestras estrategias debemos retirarnos por hoy..."), Path(33,"Motivas a tus tropas a pesar de esta traición, con gran moral atacan el palacio..")]),
          32: Nodo("Emprendes la retirada, pero tus hombres con esta orden han perdido la moral y retroceden desorganizados, las fuerzas enemigas "
                   "les dan alcance.",
                   [Path(15, " Decides utilizar formaciones que no haya visto Mart.")]),
          33: Nodo("Al iniciar la batalla, pierdes de vista a Mart de inmediato, decides concentrarte en la batalla, "
                   "Luego de horas de batallas logran superar con dificultad al enemigo, "
                   " finalmente luego de una ardua batalla logran asegurar el palacio. Todos cantan por el héroe. Estás bastante agotado.",
                  [Path(34, "Rechazar el canto y lideras la exploración del palacio"), Path(19, "El grupo necesita relajarte, asumir la posición de héroe y unirte al festejo")]),
          34: Nodo("Satisfecho con tu decisión, caminas por los grandes pasillos del palacio",
                  [Path(35, "Seguir explorando en busca de fugitivos")]),
          35: Nodo("Ingresas a una habitación oscura ubicada en el extremo del palacio. Con la poca luz ingresando a través de las cortinas vez algo brillante en el suelo",
                  [Path(20, "Recoger objeto brillante"), Path(36, "Ajustar ojos a la oscuridad")]),
          36: Nodo("Entre las sombras, vez una silueta. Es el héroe del otro reino quien ha caído en la locura y te ataca. Apenas logras defenderte",
                  [Path(37, "luchar"), Path(38, "llamar por ayuda")]),
          37: Nodo("Sientes que no puedes contra él, repentinamente aparece Mart quien en un ataque suicida hacia el héroe enemigo generando una ventana y permitiéndote contratacar, "
                   "sin embargo su sincronización contigo no ha sido buena... esto ha sido en vano...",
                  [Path(15, "Continuar luchando.")]),
          38: Nodo("Mientras llamas por ayuda los ataques del héroe rival te dejan sin aliento. Repentinamente aparece Mart!, el maldito logró escabullirse... "
                   "Para tu sorpresa se coloca a tu lado apuntando su espada a tu enemigo.\n"
                   "Luchan contra el héroe enemigo pero tú y Mart no tienen buena sincronización... si tan solo...\n"
                   "Debido a esto y al cansancio el enemigo apuñala a Mart en un descuido.",
                  [Path(39, "Continuar luchando")]),
          39: Nodo("Debido al cansancio acumulado en ti, no eres capaz de super al enemigo, repentinamente eres atravesado por"
                   " su espada...",
                  [Path(15, "Continuar...")]),
          }

