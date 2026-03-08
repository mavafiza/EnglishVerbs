# generate_verbs.py - Versión corregida
import json

# Lista de 100 verbos: (infinitivo, traducción, presente_base, presente_3ra, pasado, participio)
# Para verbos regulares: presente_3ra = presente_base + 's'
# Para irregulares: especificar ambas formas
verbs_list = [
    # Verbos originales con conjugación completa
    ("be", "ser/estar", "am", "is", "was/were", "been", True),  # True = irregular especial
    ("break", "romper", "break", "breaks", "broke", "broken", False),
    ("buy", "comprar", "buy", "buys", "bought", "bought", False),
    ("cook", "cocinar", "cook", "cooks", "cooked", "cooked", False),
    ("do", "hacer", "do", "does", "did", "done", False),
    ("drink", "beber", "drink", "drinks", "drank", "drunk", False),
    ("eat", "comer", "eat", "eats", "ate", "eaten", False),
    ("find", "encontrar", "find", "finds", "found", "found", False),
    ("get", "obtener/llegar", "get", "gets", "got", "got/gotten", False),
    ("go", "ir", "go", "goes", "went", "gone", False),
    ("know", "conocer/saber", "know", "knows", "knew", "known", False),
    ("look", "mirar", "look", "looks", "looked", "looked", False),
    ("make", "hacer/crear", "make", "makes", "made", "made", False),
    ("meet", "conocer", "meet", "meets", "met", "met", False),
    ("play", "jugar", "play", "plays", "played", "played", False),
    ("read", "leer", "read", "reads", "read", "read", False),
    ("see", "ver", "see", "sees", "saw", "seen", False),
    ("speak", "hablar", "speak", "speaks", "spoke", "spoken", False),
    ("spend", "pasar tiempo/gastar", "spend", "spends", "spent", "spent", False),
    ("wake up", "despertarse", "wake up", "wakes up", "woke up", "woken up", False),
    
    # 80 verbos adicionales (regulares en su mayoría)
    ("ask", "preguntar", "ask", "asks", "asked", "asked", False),
    ("call", "llamar", "call", "calls", "called", "called", False),
    ("come", "venir", "come", "comes", "came", "come", False),
    ("give", "dar", "give", "gives", "gave", "given", False),
    ("help", "ayudar", "help", "helps", "helped", "helped", False),
    ("leave", "salir/dejar", "leave", "leaves", "left", "left", False),
    ("live", "vivir", "live", "lives", "lived", "lived", False),
    ("love", "amar", "love", "loves", "loved", "loved", False),
    ("need", "necesitar", "need", "needs", "needed", "needed", False),
    ("open", "abrir", "open", "opens", "opened", "opened", False),
    ("run", "correr", "run", "runs", "ran", "run", False),
    ("say", "decir", "say", "says", "said", "said", False),
    ("take", "tomar", "take", "takes", "took", "taken", False),
    ("think", "pensar", "think", "thinks", "thought", "thought", False),
    ("try", "intentar", "try", "tries", "tried", "tried", False),
    ("use", "usar", "use", "uses", "used", "used", False),
    ("want", "querer", "want", "wants", "wanted", "wanted", False),
    ("work", "trabajar", "work", "works", "worked", "worked", False),
    ("write", "escribir", "write", "writes", "wrote", "written", False),
    ("bring", "traer", "bring", "brings", "brought", "brought", False),
    ("build", "construir", "build", "builds", "built", "built", False),
    ("catch", "atrapar", "catch", "catches", "caught", "caught", False),
    ("choose", "elegir", "choose", "chooses", "chose", "chosen", False),
    ("close", "cerrar", "close", "closes", "closed", "closed", False),
    ("cost", "costar", "cost", "costs", "cost", "cost", False),
    ("cut", "cortar", "cut", "cuts", "cut", "cut", False),
    ("draw", "dibujar", "draw", "draws", "drew", "drawn", False),
    ("drive", "conducir", "drive", "drives", "drove", "driven", False),
    ("fall", "caer", "fall", "falls", "fell", "fallen", False),
    ("feel", "sentir", "feel", "feels", "felt", "felt", False),
    ("fight", "pelear", "fight", "fights", "fought", "fought", False),
    ("fly", "volar", "fly", "flies", "flew", "flown", False),
    ("forget", "olvidar", "forget", "forgets", "forgot", "forgotten", False),
    ("forgive", "perdonar", "forgive", "forgives", "forgave", "forgiven", False),
    ("grow", "crecer", "grow", "grows", "grew", "grown", False),
    ("hear", "oír", "hear", "hears", "heard", "heard", False),
    ("hold", "sostener", "hold", "holds", "held", "held", False),
    ("keep", "mantener", "keep", "keeps", "kept", "kept", False),
    ("learn", "aprender", "learn", "learns", "learned", "learned", False),
    ("let", "dejar/permitir", "let", "lets", "let", "let", False),
    ("lose", "perder", "lose", "loses", "lost", "lost", False),
    ("mean", "significar", "mean", "means", "meant", "meant", False),
    ("pay", "pagar", "pay", "pays", "paid", "paid", False),
    ("put", "poner", "put", "puts", "put", "put", False),
    ("rise", "elevarse", "rise", "rises", "rose", "risen", False),
    ("sell", "vender", "sell", "sells", "sold", "sold", False),
    ("send", "enviar", "send", "sends", "sent", "sent", False),
    ("set", "colocar", "set", "sets", "set", "set", False),
    ("show", "mostrar", "show", "shows", "showed", "shown", False),
    ("sing", "cantar", "sing", "sings", "sang", "sung", False),
    ("sit", "sentarse", "sit", "sits", "sat", "sat", False),
    ("sleep", "dormir", "sleep", "sleeps", "slept", "slept", False),
    ("stand", "estar de pie", "stand", "stands", "stood", "stood", False),
    ("start", "empezar", "start", "starts", "started", "started", False),
    ("stop", "detener", "stop", "stops", "stopped", "stopped", False),
    ("study", "estudiar", "study", "studies", "studied", "studied", False),
    ("swim", "nadar", "swim", "swims", "swam", "swum", False),
    ("teach", "enseñar", "teach", "teaches", "taught", "taught", False),
    ("tell", "contar/decir", "tell", "tells", "told", "told", False),
    ("throw", "lanzar", "throw", "throws", "threw", "thrown", False),
    ("understand", "entender", "understand", "understands", "understood", "understood", False),
    ("wait", "esperar", "wait", "waits", "waited", "waited", False),
    ("walk", "caminar", "walk", "walks", "walked", "walked", False),
    ("watch", "mirar/ver", "watch", "watches", "watched", "watched", False),
    ("win", "ganar", "win", "wins", "won", "won", False),
    ("wish", "desear", "wish", "wishes", "wished", "wished", False),
    ("worry", "preocuparse", "worry", "worries", "worried", "worried", False),
    ("agree", "estar de acuerdo", "agree", "agrees", "agreed", "agreed", False),
    ("answer", "responder", "answer", "answers", "answered", "answered", False),
    ("arrive", "llegar", "arrive", "arrives", "arrived", "arrived", False),
    ("believe", "creer", "believe", "believes", "believed", "believed", False),
    ("carry", "llevar", "carry", "carries", "carried", "carried", False),
    ("change", "cambiar", "change", "changes", "changed", "changed", False),
    ("clean", "limpiar", "clean", "cleans", "cleaned", "cleaned", False),
    ("climb", "escalar", "climb", "climbs", "climbed", "climbed", False),
    ("count", "contar", "count", "counts", "counted", "counted", False),
    ("dance", "bailar", "dance", "dances", "danced", "danced", False),
    ("decide", "decidir", "decide", "decides", "decided", "decided", False),
    ("enjoy", "disfrutar", "enjoy", "enjoys", "enjoyed", "enjoyed", False),
    ("explain", "explicar", "explain", "explains", "explained", "explained", False),
    ("finish", "terminar", "finish", "finishes", "finished", "finished", False),
    ("follow", "seguir", "follow", "follows", "followed", "followed", False),
    ("happen", "suceder", "happen", "happens", "happened", "happened", False),
    ("hope", "esperar/desear", "hope", "hopes", "hoped", "hoped", False),
    ("invite", "invitar", "invite", "invites", "invited", "invited", False),
    ("join", "unirse", "join", "joins", "joined", "joined", False),
    ("jump", "saltar", "jump", "jumps", "jumped", "jumped", False),
    ("kick", "patear", "kick", "kicks", "kicked", "kicked", False),
    ("laugh", "reír", "laugh", "laughs", "laughed", "laughed", False),
    ("listen", "escuchar", "listen", "listens", "listened", "listened", False),
    ("move", "mover/cambiarse", "move", "moves", "moved", "moved", False),
    ("offer", "ofrecer", "offer", "offers", "offered", "offered", False),
    ("plan", "planear", "plan", "plans", "planned", "planned", False),
    ("practice", "practicar", "practice", "practices", "practiced", "practiced", False),
    ("prepare", "preparar", "prepare", "prepares", "prepared", "prepared", False),
    ("receive", "recibir", "receive", "receives", "received", "received", False),
    ("remember", "recordar", "remember", "remembers", "remembered", "remembered", False),
    ("repeat", "repetir", "repeat", "repeats", "repeated", "repeated", False),
    ("return", "regresar/devolver", "return", "returns", "returned", "returned", False),
    ("save", "guardar/ahorrar", "save", "saves", "saved", "saved", False),
    ("search", "buscar", "search", "searches", "searched", "searched", False),
    ("share", "compartir", "share", "shares", "shared", "shared", False),
    ("shout", "gritar", "shout", "shouts", "shouted", "shouted", False),
    ("smile", "sonreír", "smile", "smiles", "smiled", "smiled", False),
    ("solve", "resolver", "solve", "solves", "solved", "solved", False),
    ("stay", "quedarse", "stay", "stays", "stayed", "stayed", False),
    ("talk", "hablar", "talk", "talks", "talked", "talked", False),
    ("touch", "tocar", "touch", "touches", "touched", "touched", False),
    ("travel", "viajar", "travel", "travels", "traveled", "traveled", False),
    ("visit", "visitar", "visit", "visits", "visited", "visited", False),
    ("wash", "lavar", "wash", "washes", "washed", "washed", False),
]

def get_present_forms(base, third, is_special):
    """Retorna las formas correctas para presente simple"""
    if is_special:
        # Para "be": am/is/are
        return {
            "I": "am", "you": "are", "he/she/it": "is",
            "we": "are", "you_plural": "are", "they": "are"
        }
    else:
        return {
            "I": base, "you": base, "he/she/it": third,
            "we": base, "you_plural": base, "they": base
        }

def get_past_forms(past_value):
    """Maneja past simple con valores como 'was/were' o 'got/gotten'"""
    if '/' in past_value:
        parts = past_value.split('/')
        return {"default": parts[0], "alternative": parts[1] if len(parts) > 1 else parts[0]}
    return {"default": past_value, "alternative": None}

def generate_modal_section(infinitive, past_participle, translation):
    """Genera la sección de modales para un verbo"""
    base = infinitive
    pp = past_participle
    
    # Traducciones base para modales
    t = translation.split('/')[0]  # Tomar primera traducción para simplicidad
    
    return {
        "can": {"form": f"can {base}", "translation": f"puedo/puedes/puede {t}", "note": "Habilidad o posibilidad"},
        "cannot": {"form": f"cannot {base}", "translation": f"no puedo/no puedes/no puede {t}", "note": "Imposibilidad"},
        "could": {"form": f"could {base}", "translation": f"podría {t}", "note": "Posibilidad condicional"},
        "couldn't": {"form": f"couldn't {base}", "translation": f"no podría {t}", "note": "Imposibilidad condicional"},
        "should": {"form": f"should {base}", "translation": f"debería {t}", "note": "Recomendación"},
        "shouldn't": {"form": f"shouldn't {base}", "translation": f"no debería {t}", "note": "Consejo negativo"},
        "must": {"form": f"must {base}", "translation": f"debo/debes/debe {t}", "note": "Obligación"},
        "must_not": {"form": f"must not {base}", "translation": f"no debo/no debes/no debe {t}", "note": "Prohibición"},
        "might": {"form": f"might {base}", "translation": f"podría {t} (quizás)", "note": "Posibilidad remota"},
        "might_not": {"form": f"might not {base}", "translation": f"podría no {t}", "note": "Posibilidad negativa"},
        "could_have": {"form": f"could have {pp}", "translation": f"podría haber {t}", "note": "Posibilidad en el pasado"},
        "should_have": {"form": f"should have {pp}", "translation": f"debería haber {t}", "note": "Arrepentimiento"},
        "must_have": {"form": f"must have {pp}", "translation": f"debe haber {t}", "note": "Deducción sobre el pasado"},
        "might_have": {"form": f"might have {pp}", "translation": f"podría haber {t}", "note": "Posibilidad incierta"}
    }

def create_verb_object(infinitive, translation, present_base, present_third, past_value, past_participle, is_special):
    """Crea un objeto verbo completo"""
    
    # Presente simple
    present_forms = get_present_forms(present_base, present_third, is_special)
    present_simple = {
        person: {"form": form, "translation": f"{['yo','tú','él/ella','nosotros','ustedes','ellos/ellas'][i]} {translation.split('/')[0]}"}
        for i, (person, form) in enumerate(present_forms.items())
    }
    
    # Pasado simple
    past_info = get_past_forms(past_value)
    past_form = past_info["alternative"] if past_info["alternative"] and infinitive in ["be", "get"] else past_info["default"]
    past_simple = {
        person: {"form": past_form, "translation": f"{['yo','tú','él/ella','nosotros','ustedes','ellos/ellas'][i]} {translation.split('/')[0]} (pasado)"}
        for i, person in enumerate(["I", "you", "he/she/it", "we", "you_plural", "they"])
    }
    
    # Participio para perfectos
    pp_form = past_participle.split('/')[0] if '/' in past_participle else past_participle
    
    # Present Perfect
    present_perfect = {
        person: {
            "form": f"{'has' if person == 'he/she/it' else 'have'} {pp_form}",
            "translation": f"{['yo he','tú has','él/ella ha','nosotros hemos','ustedes han','ellos/ellas han'][i]} {translation.split('/')[0]}"
        }
        for i, person in enumerate(["I", "you", "he/she/it", "we", "you_plural", "they"])
    }
    
    # Past Perfect
    past_perfect = {
        person: {
            "form": f"had {pp_form}",
            "translation": f"{['yo había','tú habías','él/ella había','nosotros habíamos','ustedes habían','ellos/ellas habían'][i]} {translation.split('/')[0]}"
        }
        for i, person in enumerate(["I", "you", "he/she/it", "we", "you_plural", "they"])
    }
    
    return {
        "infinitive": infinitive,
        "translation": translation,
        "presentSimple": present_simple,
        "pastSimple": past_simple,
        "presentPerfect": present_perfect,
        "pastPerfect": past_perfect,
        "modals": generate_modal_section(infinitive, pp_form, translation)
    }

# Generar JSON completo
print("🔄 Generando 100 verbos con conjugaciones y modales...")
verbs_json = {"verbs": [create_verb_object(*v) for v in verbs_list]}

# Guardar archivo
with open('verbs.json', 'w', encoding='utf-8') as f:
    json.dump(verbs_json, f, indent=2, ensure_ascii=False)

print(f"✅ verbs.json generado exitosamente con {len(verbs_json['verbs'])} verbos")
print(f"📁 Tamaño del archivo: {len(json.dumps(verbs_json, ensure_ascii=False)) / 1024:.1f} KB")