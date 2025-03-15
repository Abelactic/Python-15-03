#Aqui definimos los personajes que usaremos en nuestra historia
define joe = Character("Joe", color="#1c37f5")
define pie = Character("Tío McAllister", color="#4ffa09")
define jugador = Character("Mike", color="#fa0914")

default objeto_lentes = False



#Los labels son las diferentes "escenas" o acontecimientos que suceden en nuestra historia
label start:
    scene escena1 at Transform(size=(1920, 1080))

    play music "musicadefondo.mp3" fadeout 10.0 fadein 10.0

    jugador "Wow, qué fiesta tan épica la de anoche, no recuerdo cómo terminé aquí, jaja."
    "..."
    jugador "Parece que estoy en el baño de Joe."

    label menu_baño:
        menu:
            "Explorar baño":
                call exploracion_wc
                jump menu_baño  # Regresa al menú después de explorar

            "Revisar celular":
                call celular
                jump menu_baño  # Regresa al menú después de revisar el celular

            "Salir del baño":
                call salir_sala  # Avanza en la historia
                return  # Termina la escena

    return

label exploracion_wc:
    jugador "Mmmmmm, Joe solo tiene pasta de dientes en los cajones de su baño."
    jugador "..."
    jugador "¿Qué es esto?"

    stop music
    play sound "efecto1.mp3"
    play music "musicadefondo.mp3" fadeout 10.0 fadein 10.0

    show lentes at Transform(xalign=0.5, yalign=0.5)
    "Has obtenido unos icónicos lentes. Tienen demasiado aumento."
    $ objeto_lentes = True
    hide lentes
    return

label celular:
    jugador "Sin batería, sabía que no debía comprar un iPhone (no es cierto)"
    return

label salir_sala:
    jugador "Creo que saldré de aquí, debo buscar a Joe. Al parecer alguien ha roto el lavabo."
    "Sales del baño"

    scene escena2 at Transform(size=(1920, 1080)) with fade
    "Wow... Realmente fue una fiesta intensa"
    show joe at Transform(xsize=691, ysize=811, xalign=0.5, yalign=0.5)
    joe "¡Hey Mike! Parece que ya despertaste, te quedaste dormido en el baño como en secundaria."
    jugador "¡¿Todas esas botellas son nuestras?!"
    joe "Jajaja, claro que no, es mi icónica colección de botellas verdes."
    jugador "¿Qué sucedió ayer?"
    joe "¿Qué, no recuerdas?"

    menu:
        "Jaja, sí lo recuerdo":
            call recuerdo1
            jump continuar_historia

        "Jaja, no lo recuerdo":
            call recuerdo2
            jump continuar_historia

    return

label recuerdo1:
    jugador "¡Ya lo recordé! Fue una noche loca."
    return

label recuerdo2:
    jugador "No lo logro recordar, ¿puedes ayudarme?"
    joe "¿En serio? ¿No recuerdas el karaoke?"

    hide joe
    scene escena3 at Transform(size=(1920, 1080)) with fade
    stop music
    play music "beatdefiesta.mp3"

    show joe2 at Transform(xsize=691, ysize=811, xalign=0.5, yalign=0.5)
    joe "Mike, dale play a esa canción, amigo."
    jugador "¡El micrófono es todo tuyo!"
    joe "¡De eso estaba hablando!"
    joe "¡Muy bien!"
    joe "Este es un tema dedicado a toda esa gente."
    joe "Que..."
    joe "Ahhh..."
    joe "Sí."

    stop music
    hide joe2
    return

label continuar_historia:
    scene escena2 at Transform(size=(1920, 1080)) with fade
    # Joe centrado al inicio
    show joe at Transform(xsize=691, ysize=811, xalign=0.5, yalign=0.5)
    play music "musicadefondo.mp3" fadeout 10.0 fadein 10.0

    joe "Oye Mike, de casualidad, ¿tú sabes programar en Python? Necesito ayuda con un código de programación."
    jugador "No, pero creo que conozco a un sujeto."

    # Mueve a Joe a la derecha y muestra a Pie a la izquierda
    hide joe  # Esconde a Joe para cambiar su posición
    # Mueve a Joe a la derecha (xalign=1.0)
    show joe at Transform(xsize=691, ysize=811, xalign=1.0, yalign=0.5)
    # Mueve a Pie a la izquierda (xalign=0.0)
    show tm3 at Transform(xsize=691, ysize=811, xalign=0.0, yalign=0.5)

    pie "¡¿QUÉ PASA AQUÍ?!"
    jugador "¡Tío McAllister?!"
    pie "NO FUI A VIETNAM PARA QUE USTEDES NADA MÁS ESTÉN AQUÍ PERDIENDO EL TIEMPO."
    pie "Figurativamente, pues."
    joe "¿Tu tío es un payaso?"
    jugador "Y veterano de Vietnam."

    hide tm3

    show tm1 at Transform(xsize=691, ysize=811, xalign=0.0, yalign=0.5)
    pie "Así es, soy un exmarine."
    pie "Y también catador de malteadas profesional."
    joe "¿Sabes programar en Python, Tío McAllister?"
    pie "Claro, los ayudaría, pero he perdido mis icónicos lentes."

    if objeto_lentes == True:
        "Le entregas los icónicos lentes al Tío McAllister."
        hide tm1
        show tm2 at Transform(xsize=691, ysize=811, xalign=0.0, yalign=0.5)
        pie "¡Mis icónicos lentes! Pensé que los había perdido para siempre."
        pie "Como muestra de mi agradecimiento, les ayudaré con su programa en Python."
        pie "Vamos a verlo."
        scene goodending at Transform(size=(1920, 1080)) with fade
        "GOOD ENDING"

    else:
        joe "¿Sabes dónde los extraviaste, Tío McAllister?"
        pie "Probablemente los haya perdido en la guerra..."
        scene badending at Transform(size=(1920, 1080))
        "BAD ENDING"

    return
