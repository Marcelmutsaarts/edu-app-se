import streamlit as st

# --- Basis Pagina Configuratie ---
# st.set_page_config stelt basisinstellingen voor de pagina in, zoals de titel
# die in het browsertabblad verschijnt en de layout.
# 'wide' layout gebruikt de volledige breedte van het scherm.
st.set_page_config(page_title="Leer Software Engineering", layout="wide")

# --- Functies voor Pagina Inhoud ---
# We definiëren aparte functies voor elke pagina/sectie.
# Dit maakt de code georganiseerd en makkelijker te beheren.

def introductie_pagina():
    """Toont de welkomstpagina en introductie tot Software Engineering."""
    st.title("👋 Welkom bij de Interactieve Software Engineering Gids!")

    st.header("Wat is Software Engineering?")
    # st.write() toont tekst op de pagina. Markdown wordt ondersteund voor opmaak.
    st.write(
        """
        Stel je voor dat je een heel complex bouwpakket hebt, zoals een gigantisch LEGO-kasteel
        of misschien zelfs een echt huis. Je hebt een plan nodig, toch? Je moet weten:
        *   **Wat** je precies gaat bouwen (de eisen).
        *   **Hoe** je het gaat bouwen (het ontwerp, de blauwdruk).
        *   **Welke stappen** je moet volgen (het bouwproces).
        *   **Of het stevig is** en doet wat het moet doen (het testen).
        *   **Hoe je het oplevert** en eventueel later aanpast (onderhoud).

        Software Engineering is eigenlijk precies dat, maar dan voor het bouwen van software (computerprogramma's, apps, websites).
        Het is een **systematische aanpak** om software te ontwerpen, ontwikkelen, testen en onderhouden.
        Het gaat niet alleen om *code schrijven*, maar om het **hele proces** eromheen om ervoor te zorgen
        dat de software werkt, betrouwbaar is en voldoet aan wat de gebruikers nodig hebben.
        """
    )

    st.header("Doel van deze App")
    st.write(
        """
        Deze app is jouw interactieve reisgids door de wereld van software engineering.
        We behandelen de belangrijkste concepten stap voor stap, op een begrijpelijke manier.
        Tegelijkertijd leer je hoe deze Streamlit-app zelf is gebouwd, zodat je zelf ook
        apps kunt leren maken!
        """
    )

def levenscyclus_overzicht_pagina():
    """Toont een overzicht van de software levenscyclus."""
    st.title("🔄 De Levenscyclus van Software: Een Overzicht")
    st.write(
        """
        Net als een product (zoals een auto) of zelfs een levend wezen, heeft software een 'levenscyclus'.
        Dit beschrijft de verschillende fasen die software doorloopt, van het allereerste idee tot het moment
        dat het niet meer gebruikt wordt.

        Denk weer aan het bouwen van een huis:
        1.  **Idee/Behoefte:** Je hebt een plek nodig om te wonen (eis).
        2.  **Plannen/Tekenen:** Een architect maakt een blauwdruk (ontwerp).
        3.  **Bouwen:** Het huis wordt steen voor steen opgebouwd (implementatie/codering).
        4.  **Inspectie:** Controleren of alles veilig en correct is gebouwd (testen).
        5.  **Inhuizen/Gebruik:** Je gaat in het huis wonen (deployment).
        6.  **Onderhoud/Renovatie:** Reparaties uitvoeren of dingen aanpassen (onderhoud).

        De software levenscyclus kent vergelijkbare fasen. We gaan ze nu één voor één bekijken.
        """
    )
    # Placeholder voor toekomstige interactiviteit of visualisatie
    st.markdown("---")
    st.subheader("Reflectie (Placeholder)")
    st.write("Kun je de levenscyclus van een ander product bedenken (bijv. een fiets)? Welke fasen herken je?")
    # Hier kunnen we later een st.text_input of st.radio toevoegen.

def fase_1_eisen_pagina():
    """Pagina voor Fase 1: Eisen Verzamelen."""
    st.title("Fase 1: Eisen Verzamelen")
    st.header("Wat moet de software precies doen?")
    st.write(
        """
        Dit is misschien wel de **allerbelangrijkste fase**. Als je niet precies weet *wat* je moet bouwen,
        hoe kun je dan het *juiste* bouwen? Fouten of misverstanden in deze fase zijn later veel duurder
        om te herstellen dan wanneer je ze meteen aan het begin tackelt. Goed gedefinieerde eisen
        vormen de basis voor het ontwerp, de implementatie en het testen.

        In deze fase praat je met de **stakeholders** (belanghebbenden, zoals de klant, gebruikers)
        om hun wensen, behoeften en problemen te begrijpen. Het doel is om deze te vertalen naar
        duidelijke, ondubbelzinnige en testbare **eisen**.
        """
    )

    st.subheader("Functionele vs. Non-Functionele Eisen")
    st.write(
        """
        Eisen worden vaak opgedeeld in twee hoofdcategorieën:
        """
    )

    # Uitleg Functionele Eisen
    st.markdown("**1. Functionele Eisen:**")
    st.write(
        """
        *   **Wat moet de software DOEN?**
        *   Deze beschrijven de specifieke **functies**, taken of acties die de software moet kunnen uitvoeren.
        *   Ze gaan over de *input* en de verwachte *output* of het gedrag van het systeem.

        ***Voorbeeld (Webshop):***
        *   _"De gebruiker **moet** producten aan een winkelmandje kunnen toevoegen."_
        *   _"Het systeem **moet** een orderbevestiging sturen per e-mail na een aankoop."_
        *   _"Beheerders **moeten** nieuwe producten kunnen toevoegen via een admin-paneel."_
        """
    )

    # Uitleg Non-Functionele Eisen
    st.markdown("**2. Non-Functionele Eisen:**")
    st.write(
        """
        *   **HOE moet de software zijn of presteren?**
        *   Deze beschrijven de **kwaliteiten**, **eigenschappen** of **beperkingen** van de software. Ze gaan niet over specifieke functies, maar over *hoe goed* de software die functies uitvoert of aan welke randvoorwaarden moet worden voldaan.
        *   Categorieën zijn o.a.: prestatie, betrouwbaarheid, bruikbaarheid, veiligheid, onderhoudbaarheid, etc.

        ***Voorbeeld (Webshop):***
        *   _"De webpagina's **moeten** binnen 2 seconden laden."_ (Prestatie)
        *   _"Het systeem **moet** 99.9% van de tijd beschikbaar zijn."_ (Betrouwbaarheid)
        *   _"Alle wachtwoorden **moeten** versleuteld worden opgeslagen."_ (Veiligheid)
        *   _"De huisstijl van het bedrijf **moet** consistent worden toegepast."_ (Bruikbaarheid/Look & Feel)
        *   _"De software **moet** draaien op zowel Windows als macOS."_ (Portabiliteit/Beperking)
        """
    )

    st.info(
        """
        **Klein Scenario:** Stel je voor we maken een simpele **To-Do lijst app**.
        *   Een *functionele eis* zou kunnen zijn: _"De gebruiker moet nieuwe taken kunnen toevoegen aan de lijst."_
        *   Een *non-functionele eis* zou kunnen zijn: _"De app moet ook werken als de gebruiker geen internetverbinding heeft."_ (Offline beschikbaarheid)
        """
    )

    st.subheader("🔑 Sleuteltermen")
    # st.expander maakt een uitklapbaar gedeelte, handig voor definities.
    with st.expander("Eis (Requirement)"):
        st.write(
            """
            Een specifieke beschrijving van wat de software moet kunnen (functioneel) of hoe
            de software moet zijn/presteren (non-functioneel). Goede eisen zijn:
            *   **Duidelijk & Ondubbelzinnig:** Maar op één manier te interpreteren.
            *   **Testbaar:** Je kunt controleren of de software aan de eis voldoet.
            *   **Noodzakelijk:** De eis voegt echt waarde toe.
            *   **Haalbaar:** Het is technisch en binnen budget/tijd mogelijk om te realiseren.
            """
        )
    with st.expander("Stakeholder (Belanghebbende)"):
        st.write(
            """
            Iedereen die een belang heeft bij de software. Dit kunnen zijn:
            *   De **klant** (die betaalt voor de software).
            *   De **eindgebruikers** (die de software gaan gebruiken).
            *   **Ontwikkelaars** (die de software bouwen).
            *   **Managers**, etc.
            """
        )

    st.markdown("---")
    st.subheader("🤔 Test je Kennis!")

    # Definiëren van de vraag en de opties
    vraag = "Welke van de volgende is een typisch voorbeeld van een NON-functionele eis?"
    opties = [
        "De gebruiker moet kunnen inloggen met een e-mailadres en wachtwoord.", # Functioneel
        "Het systeem moet een back-up maken van de data elke 24 uur.", # Functioneel/Operationeel
        "De app moet ook offline beschikbaar zijn op een smartphone.", # Non-functioneel (Correct)
        "De gebruiker moet taken kunnen markeren als voltooid." # Functioneel
    ]
    correct_antwoord = opties[2] # Het derde item in de lijst is het juiste antwoord

    # Tonen van de multiple-choice vraag met st.radio
    # Het label is de vraag. De 'options' parameter krijgt de lijst met opties.
    # De gekozen waarde wordt opgeslagen in 'gekozen_optie'.
    # 'index=None' zorgt ervoor dat er niet standaard al een optie is geselecteerd.
    gekozen_optie = st.radio(
        vraag,
        options=opties,
        index=None, # Geen vooraf geselecteerde optie
        key="f1_vraag" # Een unieke sleutel voor dit radio-element, belangrijk voor state management
    )

    # Feedback geven op basis van de keuze van de gebruiker
    # We controleren of de gebruiker al een keuze heeft gemaakt ('gekozen_optie is not None')
    if gekozen_optie: # Dit is True als een optie is geselecteerd
        if gekozen_optie == correct_antwoord:
            # st.success toont een groene box voor positieve feedback
            st.success(f"Correct! '{gekozen_optie}' is inderdaad een non-functionele eis. Het beschrijft een kwaliteit (beschikbaarheid) van de app, niet een specifieke actie die de gebruiker uitvoert.")
        else:
            # st.error toont een rode box voor incorrecte antwoorden
            st.error(f"Helaas, '{gekozen_optie}' is eerder een functionele eis (het beschrijft *wat* het systeem moet doen). Probeer het nog eens of bekijk de uitleg hierboven opnieuw.")
            # Optioneel: Geef hint naar het juiste antwoord
            st.info("Tip: Non-functionele eisen gaan vaak over *hoe goed*, *hoe snel*, *hoe veilig* of *onder welke voorwaarden* de software werkt.")

    # Placeholder commentaar over data opslag blijft relevant
    # Hier kunnen we later bijhouden of de gebruiker de vraag correct heeft beantwoord.

def fase_2_ontwerp_pagina():
    """Pagina voor Fase 2: Ontwerp."""
    st.title("Fase 2: Ontwerp")
    st.header("Hoe gaan we het bouwen?")
    st.write(
        """
        Nu we weten *wat* we moeten bouwen, is de volgende vraag: *hoe* gaan we dat doen?
        Dit is de ontwerpfase. Hier maken we de **blauwdruk** voor de software.

        Denk aan de architect die de tekeningen voor een huis maakt:
        *   Hoeveel kamers? Waar komen de deuren en ramen? (Structuur)
        *   Waar lopen de waterleidingen en elektriciteitskabels? (Technische details)
        *   Welke materialen worden gebruikt? (Technologiekeuze)

        In software ontwerp beslissen we over:
        *   **Architectuur:** De globale structuur van de software. Hoe werken verschillende onderdelen samen?
        *   **Databases:** Hoe en waar slaan we gegevens op?
        *   **User Interface (UI):** Hoe ziet de app eruit voor de gebruiker? Hoe navigeren ze?
        *   **Algoritmes:** Welke logica gebruiken we voor specifieke taken?
        """
    )

    st.subheader("🔑 Sleuteltermen")
    with st.expander("Architectuur"):
        st.write(
            """
            De hoofdstructuur van het softwaresysteem. Het beschrijft de belangrijkste componenten
            en hoe ze met elkaar communiceren. Vergelijk het met de plattegrond van een gebouw.
            Er zijn verschillende 'stijlen' van architectuur (bijv. client-server, microservices).
            """
        )
    with st.expander("User Interface (UI) / User Experience (UX)"):
        st.write(
            """
            *   **UI (User Interface):** Alles wat de gebruiker ziet en waarmee hij interactie heeft (knoppen, menu's, schermen). Hoe ziet het eruit?
            *   **UX (User Experience):** De *totale ervaring* van de gebruiker bij het gebruiken van de software. Is het makkelijk? Logisch? Prettig?
            Een goed ontwerp houdt rekening met zowel UI als UX.
            """
        )
    with st.expander("Database"):
        st.write(
            """
            Een gestructureerde opslagplaats voor gegevens. Denk aan een digitale archiefkast.
            Software gebruikt databases om informatie te bewaren (bijv. gebruikersaccounts, productinformatie, scores).
            """
        )

    st.markdown("---")
    st.subheader("🤔 Interactieve Oefening (Placeholder)")
    st.write("Denk aan de boodschappenlijstjes-app. Hoe zou je de gegevens opslaan? Gewoon in een tekstbestand, of in iets complexers? Waarom?")
    # Placeholder voor st.radio() of st.text_input().

def fase_3_implementatie_pagina():
    """Pagina voor Fase 3: Implementatie (Coderen)."""
    st.title("Fase 3: Implementatie")
    st.header("Het schrijven van de code")
    st.write(
        """
        Dit is de fase die veel mensen zien als 'het programmeren'. Op basis van het ontwerp
        gaan de ontwikkelaars nu daadwerkelijk de **code schrijven**.

        Vergelijk het met de bouwvakkers die het huis bouwen volgens de blauwdruk van de architect.
        Ze metselen muren, leggen leidingen, installeren ramen, etc.

        Belangrijke aspecten in deze fase:
        *   **Programmeertaal kiezen:** Welke taal is het meest geschikt (Python, Java, C++, etc.)?
        *   **Code schrijven:** De logica en functies implementeren.
        *   **Code kwaliteit:** Schrijven van leesbare, efficiënte en onderhoudbare code. Gebruik van commentaar!
        *   **Versiebeheer:** Tools zoals Git gebruiken om wijzigingen bij te houden en samen te werken.
        """
    )

    st.subheader("🔑 Sleuteltermen")
    with st.expander("Broncode (Source Code)"):
        st.write(
            """
            De instructies geschreven door programmeurs in een specifieke programmeertaal.
            Dit is de 'tekst' die later wordt omgezet in een werkend programma.
            De code die je nu leest in dit `app.py` bestand is broncode.
            """
        )
    with st.expander("Programmeertaal"):
        st.write(
            """
            Een formele taal die mensen gebruiken om instructies te geven aan een computer.
            Voorbeelden: Python (gebruikt voor deze app), Java, JavaScript, C#, PHP, Ruby.
            Elke taal heeft zijn eigen regels (syntax) en sterke/zwakke punten.
            """
        )
    with st.expander("Versiebeheer (Version Control)"):
        st.write(
            """
            Een systeem om wijzigingen in de code (en andere bestanden) bij te houden over tijd.
            Het stelt ontwikkelaars in staat om terug te gaan naar eerdere versies, te zien wie wat
            heeft veranderd, en makkelijker samen te werken aan dezelfde code.
            **Git** is het meest populaire versiebeheersysteem.
            """
        )
    with st.expander("Commentaar (Code Comments)"):
        st.write(
            """
            Tekst in de broncode die *niet* door de computer wordt uitgevoerd, maar bedoeld is
            om uitleg te geven aan menselijke lezers (andere programmeurs, of jezelf later!).
            In Python begint commentaar meestal met een `#`. Goed commentaar is cruciaal!
            *(Zie het commentaar in deze app-code als voorbeeld)*.
            """
        )

    st.markdown("---")
    st.subheader("🤔 Interactieve Oefening (Placeholder)")
    st.write("Waarom is het belangrijk om commentaar in je code te schrijven, zelfs als je de enige bent die eraan werkt?")
    # Placeholder voor st.text_area().

def fase_4_testen_pagina():
    """Pagina voor Fase 4: Testen."""
    st.title("Fase 4: Testen")
    st.header("Werkt het zoals verwacht?")
    st.write(
        """
        Je hebt de software gebouwd, maar doet het ook echt wat het moet doen? En doet het dat *correct*?
        Dat is waar testen om de hoek komt kijken. Het doel is om **fouten (bugs)** te vinden
        voordat de gebruikers dat doen!

        Vergelijk het met de inspectie van het huis:
        *   Werken alle kranen?
        *   Gaan de deuren goed open en dicht?
        *   Zijn er geen lekken?
        *   Is de elektrische installatie veilig?

        Soorten tests in software:
        *   **Unit Tests:** Testen van kleine, geïsoleerde stukjes code (bijv. één functie).
        *   **Integratie Tests:** Testen of verschillende onderdelen goed samenwerken.
        *   **Systeem Tests:** Testen van het complete systeem als geheel.
        *   **Acceptatie Tests:** Controleren of de software voldoet aan de eisen van de klant/gebruiker.
        """
    )

    st.subheader("🔑 Sleuteltermen")
    with st.expander("Bug (Fout)"):
        st.write(
            """
            Een fout of onvolkomenheid in de software waardoor deze niet werkt zoals bedoeld,
            onverwachte resultaten geeft, of crasht. Het vinden en oplossen van bugs (debuggen)
            is een belangrijk onderdeel van software ontwikkeling.
            """
        )
    with st.expander("Test Case"):
        st.write(
            """
            Een specifieke set van acties en verwachte resultaten om te controleren of een bepaald
            onderdeel van de software correct werkt.
            *Voorbeeld (voor inloggen):*
            1.  Voer geldige gebruikersnaam en wachtwoord in. Verwacht resultaat: Succesvol ingelogd.
            2.  Voer ongeldig wachtwoord in. Verwacht resultaat: Foutmelding "Ongeldig wachtwoord".
            """
        )
    with st.expander("Debuggen (Debugging)"):
        st.write(
            """
            Het proces van het vinden, analyseren en oplossen van bugs in de software.
            """
        )

    st.markdown("---")
    st.subheader("🤔 Interactieve Oefening (Placeholder)")
    st.write("Bedenk een simpele 'test case' voor de functie 'item toevoegen' in de boodschappenlijstjes-app. Wat zou je testen?")
    # Placeholder voor st.text_area().

def fase_5_deployment_pagina():
    """Pagina voor Fase 5: Implementatie/Deployment."""
    st.title("Fase 5: Implementatie / Deployment")
    st.header("De software beschikbaar maken")
    st.write(
        """
        De software is gebouwd en getest. Nu is het tijd om deze beschikbaar te maken voor
        de eindgebruikers! Dit proces heet **deployment**.

        Vergelijk het met het moment dat het huis klaar is en je de sleutels krijgt en kunt verhuizen.

        Deployment kan op verschillende manieren:
        *   **Installatie:** Software installeren op de computers van gebruikers.
        *   **Webserver:** Een website of webapplicatie live zetten op het internet.
        *   **App Store:** Een mobiele app publiceren in de Apple App Store of Google Play Store.

        Dit omvat vaak configuratie, opzetten van servers, databases, etc.
        """
    )

    st.subheader("🔑 Sleuteltermen")
    with st.expander("Server"):
        st.write(
            """
            Een krachtige computer die is ontworpen om diensten te verlenen aan andere computers (clients),
            bijvoorbeeld het hosten van websites, databases of applicaties. Als je een website bezoekt,
            maakt jouw computer verbinding met een webserver.
            """
        )
    with st.expander("Productieomgeving (Production Environment)"):
        st.write(
            """
            De 'live' omgeving waar de uiteindelijke software draait en gebruikt wordt door de eindgebruikers.
            Dit is anders dan de ontwikkel- of testomgevingen.
            """
        )
    with st.expander("Release"):
        st.write(
            """
            Een specifieke versie van de software die wordt vrijgegeven aan gebruikers.
            Vaak hebben releases versienummers (bijv. versie 1.0, 1.1, 2.0).
            """
        )

    st.markdown("---")
    st.subheader("🤔 Interactieve Oefening (Placeholder)")
    st.write("Hoe zou je deze Streamlit-app kunnen 'deployen' zodat anderen hem online kunnen gebruiken? (Tip: Streamlit heeft hier een eigen dienst voor!)")
    # Placeholder voor reflectie of link naar Streamlit Cloud documentatie.

def fase_6_onderhoud_pagina():
    """Pagina voor Fase 6: Onderhoud."""
    st.title("Fase 6: Onderhoud")
    st.header("Updates en fixes na de release")
    st.write(
        """
        Software is zelden 'af' na de eerste release. De wereld verandert, gebruikers vinden
        nieuwe bugs, of er ontstaan nieuwe wensen. Onderhoud is het proces van het aanpassen
        en verbeteren van de software *nadat* deze is gedeployed.

        Vergelijk het met het onderhoud aan een huis:
        *   Een lekkende kraan repareren (bug fix).
        *   De keuken renoveren (functionaliteit toevoegen/verbeteren).
        *   Het huis schilderen (uiterlijk aanpassen).
        *   Isolatie verbeteren (prestatieverbetering).

        Soorten onderhoud:
        *   **Correctief:** Fouten (bugs) oplossen die na release worden ontdekt.
        *   **Adaptief:** Software aanpassen aan veranderingen in de omgeving (bijv. nieuw besturingssysteem, nieuwe wetgeving).
        *   **Perfectief:** Bestaande functionaliteit verbeteren (bijv. sneller maken) of nieuwe functies toevoegen op basis van gebruikersfeedback.
        *   **Preventief:** Aanpassingen maken om toekomstige problemen te voorkomen.
        """
    )

    st.subheader("🔑 Sleuteltermen")
    with st.expander("Patch"):
        st.write(
            """
            Een kleine stukje software-update dat bedoeld is om een specifieke bug te repareren
            of een klein probleem op te lossen.
            """
        )
    with st.expander("Update / Upgrade"):
        st.write(
            """
            Een nieuwe versie van de software die verbeteringen, nieuwe functies of bugfixes bevat.
            Een 'upgrade' is vaak een grotere, significantere verandering dan een 'update'.
            """
        )
    with st.expander("Legacy Code"):
        st.write(
            """
            Oudere broncode die nog steeds in gebruik is, maar mogelijk moeilijk te begrijpen
            of aan te passen is (bijv. omdat het verouderde technologie gebruikt of slecht
            gedocumenteerd is). Onderhoud van legacy code kan een uitdaging zijn.
            """
        )

    st.markdown("---")
    st.subheader("🤔 Interactieve Oefening (Placeholder)")
    st.write("Waarom is het belangrijk om software te blijven onderhouden, zelfs als het lijkt te werken?")
    # Placeholder voor st.text_area().

# --- NIEUWE FUNCTIE VOOR ONTWIKKELMETHODES ---
def ontwikkelmethodes_pagina():
    """Pagina over Software Ontwikkelmethodologieën."""
    st.title("🛠️ Ontwikkelmethodes: Hoe werken we?")

    st.header("Waarom verschillende methodes?")
    st.write(
        """
        Je hebt nu een idee van de *fasen* in softwareontwikkeling (eisen, ontwerp, etc.).
        Maar *hoe* doorlopen teams deze fasen? Gaan ze strikt stap voor stap, of werken ze
        meer flexibel en in cirkels? Hiervoor bestaan **ontwikkelmethodes**.

        Een ontwikkelmethode is een **gestructureerde aanpak** voor het plannen, organiseren
        en beheren van het softwareontwikkelingsproces. Het helpt teams om efficiënter
        samen te werken, risico's te beheersen en beter om te gaan met onvermijdelijke
        veranderingen.

        *Analogie:* Denk aan het koken van een complex gerecht. Je kunt een recept **strikt van A tot Z volgen**
        (eerst alle ingrediënten snijden, dan alles mixen, dan bakken). Of je kunt een **flexibeler recept**
        gebruiken dat je toestaat om tijdens het koken te proeven, ingrediënten aan te passen en
        misschien zelfs onderdelen parallel te bereiden. Beide manieren kunnen tot een goed gerecht leiden,
        maar de aanpak verschilt sterk.
        """
    )

    st.markdown("---")
    st.header("1. De Watervalmethode (Waterfall)")
    st.write(
        """
        Dit is een van de oudste en meest traditionele methodes. Zoals de naam suggereert,
        'stroomt' het proces als een waterval van de ene fase naar de volgende, in een **strikt lineaire volgorde**.
        Elke fase moet volledig worden afgerond en goedgekeurd voordat de volgende mag beginnen.
        """
    )

    # Placeholder voor visualisatie
    st.caption("Conceptuele weergave: Eisen → Ontwerp → Implementatie → Testen → Onderhoud (Lineair)")
    # Hier zou je later een st.image("images/waterfall.png") kunnen toevoegen als je een afbeelding hebt.

    st.subheader("Kenmerken van Waterfall:")
    st.markdown(
        """
        *   **Sequentieel:** Strikte volgorde van fasen.
        *   **Veel Documentatie:** Elke fase produceert uitgebreide documenten die de basis vormen voor de volgende fase.
        *   **Rigide:** Het is moeilijk (en duur) om terug te gaan naar een vorige fase als de eisen veranderen.
        *   **Planning Vooraf:** Het hele project wordt in detail gepland aan het begin.
        """
    )

    st.subheader("Wanneer geschikt?")
    st.write("Vooral bij projecten waar de **eisen zeer stabiel en goed begrepen** zijn vanaf het begin, en waar weinig verandering wordt verwacht. Denk aan sommige bouwprojecten of zeer specifieke, goed gedefinieerde software-updates.")

    with st.expander("Definitie: Watervalmethode (Waterfall)"):
        st.write("Een lineaire, sequentiële ontwikkelmethode waarbij elke fase volledig moet zijn afgerond voordat de volgende fase begint.")

    st.markdown("---")
    st.header("2. Agile Methoden (Focus op Flexibiliteit)")
    st.write(
        """
        Als reactie op de rigiditeit van Waterfall ontstonden **Agile** methoden. Agile is geen specifieke methode,
        maar een **filosofie** en set principes die flexibiliteit, samenwerking, snelle oplevering en aanpassing
        aan verandering benadrukken. Er zijn verschillende concrete methoden die Agile principes toepassen,
        waarvan **Scrum** de populairste is.
        """
    )

    st.subheader("Scrum (Een populair Agile framework)")
    st.write(
        """
        Scrum organiseert werk in korte, vaste cycli genaamd **Sprints** (meestal 2-4 weken).
        Aan het begin van elke sprint selecteert het team een aantal taken (items) van de **Product Backlog**
        (een geprioriteerde lijst van al het werk) om in die sprint te voltooien. Aan het einde van de sprint
        levert het team een **werkend stukje software** op en wordt er feedback verzameld.
        Dit proces herhaalt zich.
        """
    )

    # Placeholder voor visualisatie
    st.caption("Conceptuele weergave: Backlog → Sprint Planning → Sprint (Ontwerp/Bouw/Test) → Werkende Software → Review/Feedback (Cyclisch)")
    # Hier zou je later een st.image("images/scrum_cycle.png") kunnen toevoegen.

    st.subheader("Kenmerken van Agile/Scrum:")
    st.markdown(
        """
        *   **Iteratief & Incrementeel:** Werken in korte cycli (iteraties/sprints), waarbij telkens een stukje werkende software wordt toegevoegd (incrementeel).
        *   **Flexibel:** Veranderende eisen zijn welkom, zelfs laat in het proces.
        *   **Samenwerking:** Nauwe samenwerking tussen ontwikkelaars, klant en andere stakeholders.
        *   **Focus op Werkende Software:** Het belangrijkste meetpunt van voortgang is werkende software.
        *   **Zelfsturende Teams:** Teams organiseren hun eigen werk binnen een sprint.
        """
    )

    st.subheader("Wanneer geschikt?")
    st.write("Zeer geschikt voor complexe projecten, projecten waar **eisen onzeker zijn of waarschijnlijk zullen veranderen**, en wanneer snelle feedback en marktintroductie belangrijk zijn.")

    with st.expander("Definities: Agile & Scrum Termen"):
        st.markdown("**Agile:** Een overkoepelende filosofie en set principes voor softwareontwikkeling die flexibiliteit, samenwerking en snelle reactie op verandering benadrukken.")
        st.markdown("**Scrum:** Een specifiek Agile framework dat werk organiseert in iteratieve cycli (Sprints) met gedefinieerde rollen, ceremonies en artefacten (zoals de Backlog).")
        st.markdown("**Sprint/Iteratie:** Een korte, vaste tijdsperiode (bv. 2 weken) waarin een team een afgesproken hoeveelheid werk voltooit en een potentieel bruikbaar product oplevert.")
        st.markdown("**Product Backlog:** Een geprioriteerde lijst van alle gewenste features, functies, eisen, verbeteringen en fixes voor een product.")
        st.markdown("**Sprint Backlog:** De set items van de Product Backlog die het team selecteert om te voltooien tijdens een specifieke Sprint.")

    st.markdown("---")
    st.header("Vergelijking: Waterfall vs. Agile/Scrum")
    st.markdown(
        """
        | Kenmerk              | Waterfall                             | Agile/Scrum                           |
        |----------------------|---------------------------------------|---------------------------------------|
        | **Structuur**        | Lineair, sequentieel                  | Iteratief, cyclisch                   |
        | **Flexibiliteit**    | Laag (moeilijk aan te passen)         | Hoog (verandering is welkom)          |
        | **Planning**         | Gedetailleerd vooraf                  | Globaal vooraf, gedetailleerd per sprint |
        | **Oplevering**       | Aan het einde van het hele project    | Werkende software na elke sprint      |
        | **Klantbetrokkenheid**| Vooral aan begin en eind              | Continu gedurende het project         |
        | **Documentatie**     | Uitgebreid                            | Net genoeg, focus op werkende software |
        """
    )

    st.markdown("---")
    st.subheader("🤔 Test je Kennis!")

    # Definiëren van de vraag en de opties voor ontwikkelmethodes
    methode_vraag = "Je werkt aan een compleet nieuw type social media app. De eisen zijn nog niet 100% duidelijk en zullen waarschijnlijk veranderen na feedback van de eerste gebruikers. Welke ontwikkelmethode past hier waarschijnlijk het beste?"
    methode_opties = [
        "Waterfall (omdat structuur belangrijk is)",
        "Agile/Scrum (omdat flexibiliteit en aanpassing aan verandering cruciaal zijn)", # Correct
        "Geen van beide, je hebt geen methode nodig."
    ]
    methode_correct_antwoord = methode_opties[1]

    # Tonen van de multiple-choice vraag met st.radio
    methode_gekozen_optie = st.radio(
        methode_vraag,
        options=methode_opties,
        index=None, # Geen vooraf geselecteerde optie
        key="methode_vraag" # Unieke sleutel
    )

    # Feedback geven op basis van de keuze
    if methode_gekozen_optie:
        if methode_gekozen_optie == methode_correct_antwoord:
            st.success(f"Correct! '{methode_gekozen_optie}' is de meest geschikte keuze. Agile/Scrum is ontworpen om goed om te gaan met veranderende eisen en onzekerheid, wat typisch is voor nieuwe, innovatieve projecten zoals een social media app.")
        elif methode_gekozen_optie == methode_opties[0]:
            st.error(f"Niet helemaal. Hoewel structuur belangrijk is, is de rigiditeit van Waterfall niet ideaal wanneer eisen waarschijnlijk zullen veranderen. '{methode_correct_antwoord}' past beter bij dit scenario.")
        else:
            st.error("Hoewel je zonder strikte methode *iets* kunt bouwen, helpt een methode zoals Agile/Scrum juist om structuur te bieden in een onzekere omgeving en de kans op succes te vergroten.")

# --- NIEUWE FUNCTIE VOOR FRONTEND & BACKEND ---
def frontend_backend_pagina():
    """Pagina over Frontend en Backend ontwikkeling."""
    st.title("🖼️ Frontend & Backend: De Twee Kanten van de Medaille")

    st.header("Introductie: Het Restaurant Model")
    st.write(
        """
        Moderne webapplicaties (zoals webshops, social media, of zelfs deze educatieve app)
        bestaan meestal uit twee grote delen die nauw samenwerken: de **Frontend** en de **Backend**.
        Om dit te begrijpen, gebruiken we de analogie van een restaurant:

        *   **Frontend (De Eetzaal):** Dit is alles waar jij als klant direct mee te maken hebt.
            De mooi ingerichte eetzaal, de menukaart die je leest, de tafel waaraan je zit,
            en de ober die je bestelling opneemt. Het is de **presentatie** en de **interactie**.

        *   **Backend (De Keuken & Achterkant):** Dit is alles achter de schermen wat nodig is om
            het restaurant te laten draaien. De keuken waar het eten wordt bereid (de logica),
            de voorraadkamer waar ingrediënten worden bewaard (de data), de koks, het kassasysteem,
            het receptenboek. Het is de **motor**, de **logica** en de **dataopslag**.

        Net als in een restaurant, moeten de Frontend en Backend van software goed communiceren om een
        goede ervaring te bieden.
        """
    )

    # --- De Frontend --- #
    st.markdown("---")
    st.header("De Frontend (Client-Side): Wat je Ziet")
    st.write(
        """
        De Frontend is het deel van de applicatie dat **in de browser van de gebruiker draait** (op hun computer, tablet of smartphone).
        Het wordt ook wel **Client-Side** genoemd, omdat de browser de 'client' is die de software gebruikt.
        De focus ligt op de **visuele presentatie** en de **gebruikersinteractie**.
        """
    )
    st.subheader("Verantwoordelijkheden:")
    st.markdown(
        """
        *   **Tonen van informatie:** Data (ontvangen van de Backend) op een begrijpelijke en aantrekkelijke manier weergeven.
        *   **Verwerken van gebruikersinvoer:** Reageren op klikken, toetsaanslagen, formulieren invullen.
        *   **Gebruikerservaring (UX):** Zorgen dat de app makkelijk en prettig is in gebruik (navigatie, layout, feedback).
        *   **Communicatie met Backend:** Verzoeken sturen naar de Backend (bv. om data op te halen of op te slaan) en de antwoorden verwerken.
        """
    )
    st.subheader("Kern Technologieën:")
    st.markdown(
        """
        De drie fundamentele bouwstenen van vrijwel elke web-frontend zijn:
        *   **HTML (HyperText Markup Language):** Bepaalt de **structuur** en de inhoud van een webpagina. Denk aan titels, paragrafen, afbeeldingen, links, lijsten, knoppen.
        *   **CSS (Cascading Style Sheets):** Bepaalt de **styling** en vormgeving. Denk aan kleuren, lettertypen, marges, achtergronden, layout (hoe elementen geplaatst worden).
        *   **JavaScript:** Voegt **interactiviteit** en dynamisch gedrag toe. Hiermee kun je reageren op gebruikersacties zonder de hele pagina opnieuw te laden, animaties maken, formulieren valideren, complexe UI-elementen bouwen en communiceren met de backend.
        """
    )
    st.subheader("Frameworks (Helpers):")
    st.write("Voor complexere applicaties gebruiken ontwikkelaars vaak Frontend **Frameworks** of bibliotheken zoals React, Angular, Vue.js of Svelte. Deze bieden voorgeschreven structuren en tools om efficiënter en georganiseerder complexe interfaces te bouwen.")

    with st.expander("Definities: Frontend Termen"):
        st.markdown("**Frontend:** Het deel van een applicatie waarmee de gebruiker direct interactie heeft, meestal draaiend in de browser. Verantwoordelijk voor presentatie (UI) en gebruikerservaring (UX).")
        st.markdown("**Client-Side:** Code die wordt uitgevoerd op de computer of het apparaat van de eindgebruiker (de 'client'), typisch binnen de webbrowser.")
        st.markdown("**User Interface (UI):** De visuele elementen waarmee een gebruiker interactie heeft (knoppen, menu's, formulieren, etc.). Hoe het eruitziet.")
        st.markdown("**User Experience (UX):** De totale ervaring van de gebruiker tijdens het interactie hebben met de applicatie. Is het makkelijk, efficiënt, logisch, prettig?")
        st.markdown("**HTML (HyperText Markup Language):** De standaard opmaaktaal voor het creëren van de structuur en inhoud van webpagina's.")
        st.markdown("**CSS (Cascading Style Sheets):** Een taal om de presentatie en styling (layout, kleuren, lettertypen) van HTML-documenten te beschrijven.")
        st.markdown("**JavaScript:** Een programmeertaal die wordt gebruikt om webpagina's interactief en dynamisch te maken. Draait meestal in de browser.")
        st.markdown("**Framework (in Frontend):** Een verzameling van vooraf geschreven code, tools en conventies die ontwikkelaars helpt om sneller en gestructureerder complexe (frontend) applicaties te bouwen (bv. React, Angular, Vue).")

    # --- De Backend --- #
    st.markdown("---")
    st.header("De Backend (Server-Side): De Motor")
    st.write(
        """
        De Backend is het deel van de applicatie dat **op een externe computer (een server) draait**. Het is de 'achterkant' die je als gebruiker niet direct ziet, maar die essentieel is voor de werking.
        Het wordt ook wel **Server-Side** genoemd. De focus ligt op **logica**, **dataverwerking** en **opslag**.
        """
    )
    st.subheader("Verantwoordelijkheden:")
    st.markdown(
        """
        *   **Verwerken van verzoeken:** Ontvangen en verwerken van data-aanvragen of acties van de Frontend.
        *   **Bedrijfslogica uitvoeren:** De kernregels en processen van de applicatie implementeren (bv. berekenen van prijzen, verwerken van bestellingen).
        *   **Communicatie met Database:** Gegevens opslaan, bijwerken, verwijderen en ophalen uit een database.
        *   **Authenticatie & Autorisatie:** Controleren wie de gebruiker is (authenticatie) en wat die gebruiker mag doen (autorisatie).
        *   **Veiligheid:** Beschermen van data en de applicatie tegen ongeautoriseerde toegang of aanvallen.
        *   **API's aanbieden:** Interfaces definiëren waarmee de Frontend (en eventueel andere systemen) kan communiceren.
        """
    )
    st.subheader("Kern Technologieën (Voorbeelden):")
    st.markdown(
        """
        *   **Programmeertalen:** Er zijn veel keuzes, afhankelijk van het project. Populaire opties zijn:
            *   **Python:** Met frameworks als Django of Flask (deze Streamlit app gebruikt ook Python!).
            *   **Node.js:** Hiermee kun je JavaScript ook op de server gebruiken.
            *   **Java:** Veel gebruikt in grote bedrijfsapplicaties.
            *   **C# (.NET):** Vooral populair in de Microsoft-wereld.
            *   **PHP:** Al jaren een steunpilaar van het web.
            *   **Ruby:** Bekend van het Ruby on Rails framework.
        *   **Databases:** Systemen voor het gestructureerd opslaan en beheren van gegevens.
            *   **Relationeel (SQL):** Data opgeslagen in tabellen met relaties (bv. gebruikers, producten, bestellingen). Gebruiken **SQL (Structured Query Language)**. Voorbeelden: PostgreSQL, MySQL, SQL Server.
            *   **Niet-Relationeel (NoSQL):** Flexibelere data-modellen (bv. documenten, key-value pairs). Voorbeelden: MongoDB, Cassandra, Redis.
        *   **Servers:** De fysieke of virtuele machines waarop de backend code draait. Vaak gebruikt in combinatie met **Webserver** software (zoals Apache of Nginx) die helpt bij het afhandelen van binnenkomende verzoeken.
        """
    )

    with st.expander("Definities: Backend Termen"):
        st.markdown("**Backend:** Het deel van een applicatie dat op de server draait en verantwoordelijk is voor logica, dataverwerking, opslag en communicatie met de database. Niet direct zichtbaar voor de eindgebruiker.")
        st.markdown("**Server-Side:** Code die wordt uitgevoerd op de server, niet op het apparaat van de gebruiker.")
        st.markdown("**Server:** Een computer (of software op een computer) die bronnen, data, diensten of programma's levert aan andere computers (clients) via een netwerk.")
        st.markdown("**Bedrijfslogica (Business Logic):** De regels en processen die specifiek zijn voor de activiteit die de software ondersteunt (bv. hoe een korting wordt berekend, hoe een lening wordt goedgekeurd).")
        st.markdown("**Database:** Een georganiseerde verzameling van gegevens, elektronisch opgeslagen en toegankelijk. Wordt gebruikt om informatie permanent te bewaren.")
        st.markdown("**Authenticatie:** Het proces van verifiëren wie een gebruiker is (bv. via wachtwoord, biometrie).")
        st.markdown("**Autorisatie:** Het proces van bepalen welke rechten of permissies een geauthenticeerde gebruiker heeft (wat mag de gebruiker zien of doen?).")
        st.markdown("**SQL (Structured Query Language):** De standaardtaal voor het communiceren met en beheren van relationele databases (gegevens opvragen, invoegen, wijzigen, verwijderen).")
        st.markdown("**NoSQL (Not Only SQL):** Een categorie van databases die geen gebruik maken van het traditionele tabel-gebaseerde relationele model. Ze zijn vaak flexibeler en schaalbaarder voor bepaalde soorten data.")

    # --- Communicatie --- #
    st.markdown("---")
    st.header("Communicatie: De Brug via API's")
    st.write(
        """
        Hoe praten de Frontend en Backend met elkaar? Ze staan immers op verschillende computers (de browser van de gebruiker en de server).
        De communicatie verloopt via het **netwerk** (het internet), meestal via een **API (Application Programming Interface)**.

        *Analogie (Restaurant):* De **ober** fungeert als de API. Jij (Frontend) geeft je **bestelling (Request)** aan de ober. De ober brengt dit naar de **keuken (Backend)**. De keuken bereidt het **gerecht (Data)** en geeft dit via de ober (**Response**, vaak in een specifiek formaat zoals **JSON**) terug aan jou.

        De Frontend stuurt een **HTTP Request** naar een specifiek adres (endpoint) van de API op de Backend. De Backend verwerkt dit verzoek, haalt misschien data uit de database, en stuurt een **HTTP Response** terug, vaak met de gevraagde data in **JSON** formaat.
        """
    )

    with st.expander("Definities: Communicatie Termen"):
        st.markdown("**API (Application Programming Interface):** Een set van regels, protocollen en tools die specificeren hoe softwarecomponenten met elkaar moeten communiceren. Voor webapps is dit vaak een web API die Frontend en Backend verbindt.")
        st.markdown("**HTTP (HyperText Transfer Protocol):** Het standaard protocol (set van regels) voor gegevensoverdracht op het World Wide Web. Het definieert hoe berichten (requests en responses) worden geformatteerd en verzonden.")
        st.markdown("**Request (Verzoek):** Een bericht gestuurd van de client (Frontend) naar de server (Backend) om een actie uit te voeren of informatie op te vragen.")
        st.markdown("**Response (Antwoord):** Een bericht gestuurd van de server (Backend) terug naar de client (Frontend) als antwoord op een request, vaak met data of een statuscode.")
        st.markdown("**JSON (JavaScript Object Notation):** Een lichtgewicht, tekstgebaseerd formaat voor gegevensuitwisseling, zeer populair in web API's omdat het makkelijk leesbaar is voor zowel mensen als machines (en direct bruikbaar in JavaScript).")

    # --- Full-Stack --- #
    st.markdown("---")
    st.header("En Full-Stack Dan?")
    st.write(
        """
        Soms hoor je de term **Full-Stack Developer**. Dit is een ontwikkelaar die comfortabel is met
        **zowel Frontend als Backend** technologieën en ontwikkeling. Ze kunnen dus aan de 'hele stack'
        (alle lagen) van een applicatie werken.
        """
    )
    with st.expander("Definitie: Full-Stack Developer"):
        st.markdown("**Full-Stack Developer:** Een softwareontwikkelaar die expertise heeft in zowel frontend- (client-side) als backend- (server-side) technologieën en ontwikkeling.")

    # --- Visueel Overzicht --- #
    st.markdown("---")
    st.header("Visueel Overzicht")
    st.write("Het volgende diagram toont schematisch hoe de onderdelen samenwerken:")

    # Mermaid diagram implementatie
    # We gebruiken st.markdown met unsafe_allow_html=True om de Mermaid JavaScript library (indien beschikbaar) te laten renderen.
    # Let op: Dit werkt mogelijk niet in alle Streamlit omgevingen direct, afhankelijk van de configuratie.
    # Als alternatief zou je een statische afbeelding gebruiken met st.image().
    mermaid_diagram = """
    ```mermaid
    graph LR
        A[Client/Browser <br> (Frontend: HTML, CSS, JS)] -- HTTP Request (API Call) --> B(Server <br> (Backend: Python/Java/Node etc.));
        B -- Database Query --> C{Database <br> (SQL/NoSQL)};
        C -- Data --> B;
        B -- HTTP Response (API, vaak JSON) --> A;
    ```
    """
    st.markdown(mermaid_diagram, unsafe_allow_html=True) # Let op: unsafe_allow_html kan veiligheidsrisico's inhouden bij ongefilterde input.
    st.caption("Diagram: Client (Frontend) communiceert via HTTP requests met de Server (Backend), die op zijn beurt met de Database praat en een HTTP response terugstuurt.")

    # --- Interactieve Oefening --- #
    st.markdown("---")
    st.header("🤔 Oefening: Waar hoort het thuis?")
    st.write("Wijs de volgende technologieën en verantwoordelijkheden toe aan de juiste kant (Frontend of Backend). Selecteer de items die volgens jou bij de Frontend horen en de items die bij de Backend horen.")

    # Definieer de items en hun correcte plaatsing
    alle_items = [
        "HTML", "CSS", "JavaScript (in browser)", "Gebruikersinteractie", "UI Design",
        "Python (op server)", "Database Beheer", "Server Logic", "SQL Queries", "Authenticatie",
        "Node.js", "API Endpoints", "Data Validatie (server-side)"
    ]
    frontend_items_correct = {"HTML", "CSS", "JavaScript (in browser)", "Gebruikersinteractie", "UI Design"}
    backend_items_correct = {
        "Python (op server)", "Database Beheer", "Server Logic", "SQL Queries", "Authenticatie",
        "Node.js", "API Endpoints", "Data Validatie (server-side)"
    }

    # Maak twee kolommen voor de selectievakken
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Frontend Selecties")
        # st.multiselect laat de gebruiker meerdere opties kiezen
        # We geven alle items als opties en slaan de selectie op
        frontend_selecties = st.multiselect(
            "Selecteer Frontend items:",
            options=alle_items,
            key="frontend_multiselect"
        )

    with col2:
        st.subheader("Backend Selecties")
        backend_selecties = st.multiselect(
            "Selecteer Backend items:",
            options=alle_items,
            key="backend_multiselect"
        )

    # Knop om de antwoorden te controleren
    if st.button("Controleer mijn antwoorden", key="check_fb_answers"):
        # Converteer selecties naar sets voor makkelijke vergelijking
        frontend_selecties_set = set(frontend_selecties)
        backend_selecties_set = set(backend_selecties)

        # Controleer Frontend
        correct_frontend = frontend_selecties_set == frontend_items_correct
        # Controleer Backend
        correct_backend = backend_selecties_set == backend_items_correct

        # Geef feedback
        if correct_frontend and correct_backend:
            st.success("Geweldig! Je hebt alle items correct toegewezen aan Frontend en Backend!")
        else:
            st.error("Bijna! Kijk nog eens goed naar de items. Hieronder zie je de juiste verdeling:")
            # Toon de correcte antwoorden ter verduidelijking
            col_correct1, col_correct2 = st.columns(2)
            with col_correct1:
                st.markdown("**Correcte Frontend Items:**")
                for item in frontend_items_correct:
                    st.markdown(f"- {item}")
            with col_correct2:
                st.markdown("**Correcte Backend Items:**")
                for item in backend_items_correct:
                    st.markdown(f"- {item}")

            # Geef specifiekere feedback (optioneel, kan complex worden)
            missing_frontend = frontend_items_correct - frontend_selecties_set
            wrong_frontend = frontend_selecties_set - frontend_items_correct
            missing_backend = backend_items_correct - backend_selecties_set
            wrong_backend = backend_selecties_set - backend_items_correct

            feedback_msgs = []
            if missing_frontend: feedback_msgs.append(f"Frontend mist: {', '.join(missing_frontend)}")
            if wrong_frontend: feedback_msgs.append(f"Onjuist bij Frontend: {', '.join(wrong_frontend)}")
            if missing_backend: feedback_msgs.append(f"Backend mist: {', '.join(missing_backend)}")
            if wrong_backend: feedback_msgs.append(f"Onjuist bij Backend: {', '.join(wrong_backend)}")
            st.warning("Details:\n" + "\n".join(feedback_msgs))

# --- NIEUWE FUNCTIE VOOR BASIS VAN STREAMLIT ---
def streamlit_basis_pagina():
    """Pagina over de basisprincipes van Streamlit."""
    st.title("🚀 Basis van Streamlit: Snel een App Bouwen")

    st.header("Wat is Streamlit?")
    st.write(
        """
        Streamlit is een **Python-bibliotheek** (een verzameling herbruikbare code)
        die speciaal is ontworpen om **snel en eenvoudig interactieve webapplicaties** te maken.
        Het is bijzonder populair in de data science wereld, maar ook geweldig voor projecten zoals deze
        educatieve app, omdat je zonder veel webontwikkelingskennis toch iets visueels en interactiefs
        kunt bouwen.

        De kracht van Streamlit zit in de **eenvoud**: je schrijft een gewoon Python script, en Streamlit
        zorgt voor de magie om dat om te zetten in een werkende web-app.
        """
    )

    st.subheader("Hoe werkt het (conceptueel)?")
    st.write(
        """
        Het kernidee is simpel:
        1.  Je schrijft een Python-script (een `.py` bestand, zoals onze `app.py`).
        2.  In dit script gebruik je speciale Streamlit **commando's** (functies die beginnen met `st.`, zoals `st.title`, `st.write`, `st.button`).
        3.  Wanneer je het script uitvoert met `streamlit run scriptnaam.py`, leest Streamlit je script van boven naar beneden.
        4.  Elk `st.` commando wordt door Streamlit 'vertaald' naar een bijbehorend element (tekst, knop, grafiek, etc.) op een webpagina.
        5.  Als de gebruiker interactie heeft (bv. op een knop klikt), voert Streamlit het script *opnieuw* uit van boven naar beneden, waarbij de nieuwe staat (bv. welke knop is ingedrukt) wordt meegenomen.
        """
    )

    st.subheader("Belangrijke Commando's (Voorbeelden)")
    st.write("Hier zijn een paar basiscommando's die we in deze app gebruiken:")

    st.markdown("**Titels en Tekst:**")
    st.code('''
# Toont een grote titel bovenaan de pagina
st.title("Mijn Fantastische App")

# Toont een iets kleinere kop
st.header("Sectie 1")

# Toont gewone tekst (ondersteunt ook Markdown opmaak)
st.write("Dit is een paragraaf tekst.")
st.markdown("Je kunt **vetgedrukte** of *cursieve* tekst gebruiken met Markdown.")
    ''', language='python')

    st.markdown("**Interactieve Elementen (Widgets):**")
    st.code('''
# Maakt een klikbare knop. Geeft True terug als erop geklikt is.
if st.button("Klik hier!"):
    st.write("Je hebt op de knop geklikt!")

# Maakt een tekstinvoerveld
naam = st.text_input("Voer je naam in")
st.write(f"Hallo, {naam}!")

# Maakt radio buttons voor een keuze
kleur = st.radio("Kies je favoriete kleur:", ["Rood", "Groen", "Blauw"])
st.write(f"Je koos: {kleur}")
    ''', language='python')

    st.markdown("**Layout (Zijbalk):**")
    st.code('''
# Elementen toevoegen aan de zijbalk in plaats van de hoofdpagina
st.sidebar.header("Navigatie")
selectie = st.sidebar.radio("Ga naar:", ["Home", "Instellingen"])
# ... logica op basis van selectie ...
    ''', language='python')

    st.subheader("Hoe voer je het lokaal uit?")
    st.write(
        """
        Om je Streamlit app te bekijken terwijl je eraan werkt, open je een **Terminal**
        (of command prompt) in de map waar je `.py` bestand staat en voer je uit:
        """
    )
    st.code('streamlit run app.py', language='bash')
    st.write(
        """
        Streamlit start dan een kleine lokale webserver en opent de app automatisch in je browser.
        Het adres is meestal `http://localhost:8501` (`localhost` verwijst naar je eigen computer).
        Elke keer als je je script opslaat, zal Streamlit de app in je browser automatisch proberen te vernieuwen!
        """
    )

    st.subheader("Analogie: LEGO voor Web Apps")
    st.write(
        """
        Je kunt Streamlit zien als een doos met speciale, kant-en-klare LEGO-blokjes (de `st.` commando's).
        Elk blokje doet iets specifieks (tekst tonen, een knop maken, een grafiek tekenen).
        Door deze blokjes in je Python-script te combineren, kun je snel een interactieve creatie (je web app)
        bouwen, zonder dat je elk klein plastic nopje (de details van HTML/CSS/JavaScript) zelf hoeft te ontwerpen.
        """
    )

    with st.expander("Definities: Streamlit Termen"):
        st.markdown("**Streamlit:** Een open-source Python bibliotheek voor het snel bouwen en delen van interactieve webapplicaties, vooral voor data science en machine learning projecten.")
        st.markdown("**Bibliotheek (Library):** Een verzameling vooraf geschreven code (functies, klassen) die je in je eigen programma's kunt gebruiken om bepaalde taken uit te voeren zonder de code zelf te hoeven schrijven.")
        st.markdown("**Script:** Een bestand met programmacode (in dit geval een `.py` bestand met Python code) dat stap voor stap wordt uitgevoerd.")
        st.markdown("**Commando (in Streamlit):** Een functie uit de Streamlit bibliotheek (beginnend met `st.`) die een specifiek element of gedrag toevoegt aan de web app.")
        st.markdown("**Widget:** Een interactief element in de gebruikersinterface, zoals een knop, slider, tekstinvoerveld, keuzemenu (`st.button`, `st.slider`, `st.text_input`, `st.radio` zijn voorbeelden van commando's die widgets maken).")
        st.markdown("**localhost:** Een standaardnaam die verwijst naar je eigen computer. Als je een webserver lokaal draait (zoals Streamlit doet), is deze bereikbaar via `http://localhost` (vaak met een poortnummer zoals `:8501`).")
        st.markdown("**Terminal (of Command Prompt/Shell):** Een tekstgebaseerde interface om commando's aan je computer te geven, zoals het starten van programma's (bv. `streamlit run ...`).")

    st.markdown("---")
    st.subheader("🤔 Test je Kennis!")

    streamlit_vraag = "Welk Streamlit commando gebruik je het meest waarschijnlijk om een klikbare knop te maken die een actie start?"
    streamlit_opties = [
        "st.write('Klik hier')",
        "st.markdown('[*Klik*]()')",
        "st.button('Start Actie')", # Correct
        "st.input('Knop')"
    ]
    streamlit_correct = streamlit_opties[2]

    gekozen_streamlit_optie = st.radio(
        streamlit_vraag,
        options=streamlit_opties,
        index=None,
        key="streamlit_vraag"
    )

    if gekozen_streamlit_optie:
        if gekozen_streamlit_optie == streamlit_correct:
            st.success(f"Correct! `{streamlit_correct}` is het commando om een interactieve knop te maken. De `if` statement eromheen controleert of erop geklikt is.")
        else:
            st.error(f"Niet helemaal. `{gekozen_streamlit_optie}` is niet het standaard commando voor een interactieve knop. `{streamlit_correct}` wordt gebruikt om een klikbare knop te genereren.")

# --- NIEUWE FUNCTIE VOOR BASIS VAN GIT & GITHUB ---
def git_github_basis_pagina():
    """Pagina over de basisprincipes van Git en GitHub."""
    st.title("🌳 Basis van Git & GitHub: Code Beheren & Delen")

    st.header("Wat is Git? (Versiebeheer)")
    st.write(
        """
        Stel je voor dat je aan een groot project werkt (zoals deze app!). Je voegt code toe, verwijdert dingen,
        probeert nieuwe ideeën... Hoe houd je bij wat je wanneer hebt veranderd? Wat als je een fout maakt en terug wilt
        naar een vorige versie die wel werkte? Wat als je met meerdere mensen aan hetzelfde project wilt werken?

        Hier komt **Git** om de hoek kijken. Git is een **Versiebeheersysteem (Version Control System - VCS)**.
        Het is software die draait op je computer en die je helpt om **veranderingen in je code (en andere bestanden)
        systematisch bij te houden** over tijd.
        """
    )
    st.subheader("Waarom is versiebeheer belangrijk?")
    st.markdown(
        """
        *   **Geschiedenis:** Je kunt precies zien wie wat heeft veranderd en wanneer.
        *   **Fouten Herstellen:** Makkelijk terugkeren naar een vorige, werkende staat als er iets misgaat.
        *   **Experimenteren (Branching):** Nieuwe features of ideeën uitproberen in een aparte 'tak' (branch) zonder de stabiele hoofdversie te verstoren.
        *   **Samenwerken:** Meerdere ontwikkelaars kunnen tegelijk aan dezelfde codebase werken en hun wijzigingen later samenvoegen.
        *   **Backup:** Je geschiedenis is een vorm van backup (zeker in combinatie met een online platform).
        """
    )
    st.subheader("Analogieën voor Git:")
    st.markdown(
        """
        *   **Track Changes Deluxe:** Vergelijk het met 'Wijzigingen bijhouden' in Word, maar dan veel krachtiger, speciaal voor code, en je beslist zelf wanneer je een 'versie opslaat'.
        *   **Save Points in een Game:** Je maakt bewust 'commits' (opslagpunten) van je project. Gaat het mis? Dan laad je een vorig opslagpunt.
        """
    )

    st.header("Wat is GitHub (GitLab/Bitbucket)? (Online Hosting)")
    st.write(
        """
        Git zelf draait lokaal op jouw computer. Maar wat als je computer crasht? Of als je wilt samenwerken
        met anderen die niet naast je zitten? Daarvoor gebruik je platforms zoals **GitHub**, GitLab of Bitbucket.

        **GitHub** is een **online platform (een website)** dat speciaal is gebouwd om je **Git repositories**
        (je projectmappen met hun Git-geschiedenis) te **hosten** (online op te slaan) en te **delen**.
        Het biedt ook allerlei extra tools voor samenwerking, zoals issue tracking, code reviews, en projectmanagement.
        """
    )
    st.subheader("Analogie voor GitHub:")
    st.markdown("Zie GitHub als een soort **super-powered Google Drive of Dropbox, maar dan speciaal voor code-projecten die Git gebruiken**. Het is de centrale plek online waar je project 'leeft' en waar je kunt synchroniseren met je lokale Git repository.")

    st.header("Kernconcepten van Git (Conceptueel)")
    st.write("Je hoeft de commando's nog niet precies te kennen, maar het is goed om de ideeën te begrijpen:")
    st.markdown(
        """
        *   **Repository (Repo):** Simpel gezegd: je projectmap. Git voegt een verborgen submap (`.git`) toe om alle geschiedenis en informatie bij te houden.
        *   **Commit:** Een 'snapshot' of een opgeslagen versie van je project op een bepaald moment. Elke commit heeft een unieke identificatie en een boodschap die beschrijft wat er is veranderd.
        *   **Branch (Tak):** Een aparte lijn van ontwikkeling. Standaard werk je op de `main` (of `master`) branch. Je kunt nieuwe branches maken om aan features te werken of bugs te fixen, en deze later weer samenvoegen (`merge`) met de `main` branch.
        *   **Push:** Het proces van het uploaden van je lokale commits (jouw opgeslagen veranderingen) van jouw computer naar de online repository (bv. op GitHub).
        *   **Pull:** Het proces van het downloaden van de laatste veranderingen van de online repository naar jouw lokale computer. Dit is nodig als anderen ook wijzigingen hebben gepusht.
        *   **Clone:** Het maken van een volledige lokale kopie van een online repository (inclusief alle geschiedenis) op jouw computer.
        *   **Remote:** Een verwijzing naar een online (of andere externe) repository, zoals die op GitHub. De standaard naam hiervoor is vaak `origin`.
        """
    )

    st.subheader("Simpele Workflow voor Delen (Herhaling):")
    st.write("De basisstappen om je code (zoals deze app) te delen via Git & GitHub zijn vaak:")
    # st.ordered_list([ # VERWIJDERD: st.ordered_list bestaat niet
    #     "Maak wijzigingen in je code lokaal op je computer.",
    #     "Gebruik Git om deze wijzigingen te 'committen' (een snapshot maken met een beschrijving).",
    #     "Gebruik Git om je lokale commits te 'pushen' naar je online repository op GitHub.",
    #     "(Optioneel) Gebruik een platform zoals Streamlit Community Cloud dat je GitHub repository leest om de app online te zetten (deployen)."
    # ])
    # VERVANGEN MET st.markdown:
    st.markdown(
        """
        1. Maak wijzigingen in je code lokaal op je computer.
        2. Gebruik Git om deze wijzigingen te 'committen' (een snapshot maken met een beschrijving).
        3. Gebruik Git om je lokale commits te 'pushen' naar je online repository op GitHub.
        4. (Optioneel) Gebruik een platform zoals Streamlit Community Cloud dat je GitHub repository leest om de app online te zetten (deployen).
        """
    )

    with st.expander("Definities: Git & GitHub Termen"):
        st.markdown("**Git:** Een gedistribueerd versiebeheersysteem (VCS) dat wordt gebruikt om wijzigingen in broncode (en andere bestanden) over tijd bij te houden.")
        st.markdown("**GitHub (GitLab/Bitbucket):** Online platforms die hosting bieden voor Git repositories en samenwerkingsfunctionaliteiten toevoegen.")
        st.markdown("**Versiebeheer (Version Control):** Een systeem dat wijzigingen aan een bestand of set bestanden over tijd vastlegt, zodat je specifieke versies later kunt terughalen.")
        st.markdown("**Repository (Repo):** Een map die alle projectbestanden bevat, inclusief de volledige geschiedenis van wijzigingen (opgeslagen door Git in een `.git` submap).")
        st.markdown("**Commit:** Een opgeslagen 'snapshot' van de staat van je repository op een bepaald moment. Elke commit bevat informatie over de wijzigingen en een beschrijvende boodschap.")
        st.markdown("**Push:** Het uploaden van lokale commits naar een remote repository (zoals op GitHub).")
        st.markdown("**Pull:** Het downloaden en integreren van wijzigingen van een remote repository naar je lokale repository.")
        st.markdown("**Branch:** Een onafhankelijke lijn van ontwikkeling binnen een repository. De standaard branch is vaak `main` of `master`.")
        st.markdown("**Main/Master Branch:** De hoofdbranch van een repository, die meestal de stabiele, productieklare versie van de code bevat.")
        st.markdown("**Clone:** Het maken van een lokale kopie van een bestaande remote repository.")
        st.markdown("**Remote:** Een verwijzing naar een repository die elders wordt gehost (bv. op GitHub).")

    st.markdown("---")
    st.subheader("🤔 Test je Kennis!")

    git_vraag = "Je hebt lokaal belangrijke wijzigingen in je code gemaakt en deze vastgelegd met een Git 'commit'. Wat is de meest logische volgende stap om deze wijzigingen te delen met je team via GitHub?"
    git_opties = [
        "git pull",
        "git clone",
        "git branch new_feature",
        "git push origin main" # Correct (of push naar de branch waar je op werkte)
    ]
    git_correct = git_opties[3]

    gekozen_git_optie = st.radio(
        git_vraag,
        options=git_opties,
        index=None,
        key="git_vraag"
    )

    if gekozen_git_optie:
        if gekozen_git_optie == git_correct:
            st.success(f"Correct! `git push` (vaak naar 'origin' op een specifieke branch zoals 'main') is het commando om je lokale commits naar de gedeelde remote repository op GitHub te sturen.")
        elif gekozen_git_optie == git_opties[0]:
            st.error(f"Niet helemaal. `git pull` haalt juist wijzigingen *van* GitHub *naar* jouw lokale machine. Je wilt jouw wijzigingen *naar* GitHub sturen.")
        elif gekozen_git_optie == git_opties[1]:
            st.error(f"Niet correct. `git clone` gebruik je maar één keer aan het begin om een kopie van een *bestaande* online repo te maken. Je hebt je wijzigingen al lokaal.")
        elif gekozen_git_optie == git_opties[2]:
            st.error(f"Dat is een nuttig commando (`git branch`) om een nieuwe tak te maken, maar het deelt je bestaande commits nog niet met GitHub. Je moet eerst `git push` gebruiken.")

    # --- NIEUWE SECTIE: DEPLOYEN VIA STREAMLIT CLOUD ---
    st.markdown("--- --- ") # Dubbele lijn voor duidelijke scheiding
    st.header("🚀 Stap-voor-stap: Je App Delen via Streamlit Community Cloud")
    st.write(
        """
        Oké, je hebt je app gebouwd met Streamlit en je code staat netjes op GitHub met Git.
        Nu wil je de app delen met de wereld, zodat iedereen hem kan gebruiken via een webadres!
        De makkelijkste manier hiervoor is **Streamlit Community Cloud**, een gratis dienst van Streamlit zelf.

        Hier is hoe je dat doet:
        """
    )

    st.subheader("De Basis Vooraf (Recap)")
    st.markdown(
        """
        Zorg ervoor dat je GitHub **repository** (de map van je project op GitHub) het volgende bevat en dat alles is **gepusht**:
        1.  **Je hoofd app-script:** Meestal `app.py` of `streamlit_app.py`.
        2.  **Een `requirements.txt` bestand:** Hierin staan alle Python-bibliotheken die je app nodig heeft (zoals `streamlit`, maar eventueel ook `pandas`, `numpy`, etc.). Streamlit Cloud gebruikt dit bestand om te weten wat het moet installeren.
        3.  **Alle andere benodigde bestanden:** Afbeeldingen, CSV-bestanden, etc., die je app gebruikt.
        """
    )

    st.subheader("De Stappen voor Deployment:")
    # st.ordered_list([ # VERWIJDERD: st.ordered_list bestaat niet
    #     "**Ga naar Streamlit Community Cloud:** Open je webbrowser en ga naar [share.streamlit.io](https://share.streamlit.io).",
    #     "**Log in of maak een account:** Klik op \"Continue with GitHub\". Het is het makkelijkst om direct in te loggen met het GitHub account waar je code staat. Volg de stappen om je account te autoriseren. *[Hier zou een screenshot passen van de Streamlit Cloud inlogpagina]*",
    #     "**Start een Nieuwe App:** Eenmaal ingelogd in je dashboard, zoek je naar een knop zoals **\"New app\"** en klik je daarop. *[Hier zou een screenshot passen van het dashboard met de 'New app' knop gemarkeerd]*",
    #     "**Koppel en Kies Repository:** Kies de optie om te deployen vanaf GitHub. Selecteer de **repository** waar je app code staat uit de lijst. Geef Streamlit toestemming indien nodig. *[Hier zou een screenshot passen van het scherm waar je een repository selecteert]*",
    #     "**Configureer de Deploy:**\n    *   Kies de juiste **branch** (meestal `main` of `master`). Dit is de 'tak' van je code die je live wilt zetten.\n    *   Controleer het pad naar je hoofd app-bestand (bv. `app.py`). Dit staat vaak al goed.\n    *   Je kunt de app een aangepaste **URL** geven (bv. `mijn-coole-app.streamlit.app`).\n    *   Geavanceerde instellingen zijn meestal niet nodig voor een basis app.",
    #     "**Klik op Deploy!:** Als alles goed is ingesteld, klik je op de grote **\"Deploy!\"** knop. *[Hier zou een screenshot passen van de configuratiepagina met de 'Deploy!' knop gemarkeerd]*",
    #     "**Even Geduld... en Gefeliciteerd!:** Streamlit gaat nu aan de slag! Je ziet logs van het **deployment proces**: het installeren van je requirements en het starten van de app. Dit duurt meestal 1-2 minuten. Zodra het klaar is..."
    # ])
    # VERVANGEN MET st.markdown:
    st.markdown(
        """
        1.  **Ga naar Streamlit Community Cloud:** Open je webbrowser en ga naar [share.streamlit.io](https://share.streamlit.io).
        2.  **Log in of maak een account:** Klik op "Continue with GitHub". Het is het makkelijkst om direct in te loggen met het GitHub account waar je code staat. Volg de stappen om je account te autoriseren. *[Hier zou een screenshot passen van de Streamlit Cloud inlogpagina]*
        3.  **Start een Nieuwe App:** Eenmaal ingelogd in je dashboard, zoek je naar een knop zoals **"New app"** en klik je daarop. *[Hier zou een screenshot passen van het dashboard met de 'New app' knop gemarkeerd]*
        4.  **Koppel en Kies Repository:** Kies de optie om te deployen vanaf GitHub. Selecteer de **repository** waar je app code staat uit de lijst. Geef Streamlit toestemming indien nodig. *[Hier zou een screenshot passen van het scherm waar je een repository selecteert]*
        5.  **Configureer de Deploy:**
            *   Kies de juiste **branch** (meestal `main` of `master`). Dit is de 'tak' van je code die je live wilt zetten.
            *   Controleer het pad naar je hoofd app-bestand (bv. `app.py`). Dit staat vaak al goed.
            *   Je kunt de app een aangepaste **URL** geven (bv. `mijn-coole-app.streamlit.app`).
            *   Geavanceerde instellingen zijn meestal niet nodig voor een basis app.
        6.  **Klik op Deploy!:** Als alles goed is ingesteld, klik je op de grote **"Deploy!"** knop. *[Hier zou een screenshot passen van de configuratiepagina met de 'Deploy!' knop gemarkeerd]*
        7.  **Even Geduld... en Gefeliciteerd!:** Streamlit gaat nu aan de slag! Je ziet logs van het **deployment proces**: het installeren van je requirements en het starten van de app. Dit duurt meestal 1-2 minuten. Zodra het klaar is...
        """
    )
    # Voeg een succesbericht toe
    st.success("🎉 Je app is nu live! Je krijgt een unieke URL (eindigend op `.streamlit.app`) die je kunt delen met iedereen!")
    st.balloons() # Kleine viering!

    st.subheader("Updates aan je App")
    st.write(
        """
        Het mooie is: als je later **wijzigingen maakt** in je code, deze **commit** met Git, en vervolgens **pusht** naar dezelfde branch op GitHub, dan zal Streamlit Community Cloud dit **automatisch detecteren**! Je live app wordt dan vanzelf bijgewerkt met de nieuwste versie. Super handig!
        """
    )

    with st.expander("Definities: Deployment Termen"):
        st.markdown("**Deployen (Deployment):** Het proces van het nemen van je ontwikkelde software (de code, bestanden, etc.) en deze beschikbaar maken voor eindgebruikers op een live omgeving (zoals een webserver of cloud platform).")
        st.markdown("**Streamlit Community Cloud:** Het gratis hosting platform van Streamlit specifiek voor het delen van Streamlit applicaties. Het koppelt direct aan GitHub repositories.")
        st.markdown("**URL (Uniform Resource Locator):** Het unieke webadres waarmee je een specifieke pagina of bron op het internet kunt vinden (bv. `https://jouw-app-naam.streamlit.app`).")
        st.markdown("**Repository (Repo):** (Herhaling) Een map die alle projectbestanden bevat, inclusief de volledige geschiedenis van wijzigingen, vaak gehost op een platform zoals GitHub.")
        st.markdown("**Branch:** (Herhaling) Een onafhankelijke lijn van ontwikkeling binnen een Git repository. `main` of `master` is meestal de hoofdlijn; je deployt vaak vanaf deze branch.")

# --- NIEUWE FUNCTIE VOOR BASIS VAN HTML ---
def html_basis_pagina():
    """Pagina over de basisprincipes van HTML."""
    st.title("🧱 Web Technologie: HTML (HyperText Markup Language)")

    st.header("Wat is HTML? Het Skelet van het Web")
    st.write(
        """
        Als je een website bezoekt, is **HTML** de absolute basis van wat je ziet. Het staat voor
        **HyperText Markup Language**. Denk eraan als het **skelet** of de **blauwdruk** van een webpagina.
        Het definieert de **structuur** en de **inhoud**: welke tekst is een titel, wat is een paragraaf,
        waar staat een afbeelding, welke tekst is een link?

        *   **HyperText:** Verwijst naar de 'links' (hyperlinks) die webpagina's met elkaar verbinden, waardoor je kunt navigeren op het web.
        *   **Markup Language:** Het gebruikt speciale 'markeringen' of **tags** om de browser te vertellen hoe de inhoud moet worden gestructureerd en weergegeven.

        *Analogie:* Als een webpagina een huis is, dan is HTML het fundament, de muren, het dak en de indeling van de kamers. Het bepaalt de basisstructuur, nog voordat er geschilderd wordt (CSS) of er elektrische apparaten worden aangesloten (JavaScript).
        """
    )

    st.subheader("Tags, Elementen en Attributen")
    st.write(
        """
        HTML werkt met **tags**, die meestal in paren komen: een **openingstag** (`<tagnaam>`) en een
        **sluitingstag** (`</tagnaam>`). Alles daartussenin, inclusief de tags zelf, vormt een **HTML-element**.
        """
    )
    st.code('<p>Dit is de inhoud van een paragraaf-element.</p>', language='html')
    st.write(
        """
        Sommige elementen hebben geen inhoud en dus geen sluitingstag, dit zijn 'lege' elementen, zoals `<img>` (afbeelding) of `<br>` (nieuwe regel). Ze worden vaak geschreven met een `/` aan het eind: `<img src=\"logo.png\" />`.

        Tags kunnen ook **attributen** bevatten. Attributen geven **extra informatie** over een element en staan altijd in de openingstag, meestal in de vorm `naam=\"waarde\"`.
        """
    )
    st.code('<a href=\"https://www.google.com\">Klik hier voor Google</a>', language='html')
    st.write("Hier is `href` het attribuut dat aangeeft waar de link naartoe gaat.")

    st.subheader("Basisstructuur van een HTML-document")
    st.code('''
<!DOCTYPE html> <!-- Vertelt de browser dat dit een HTML5 document is -->
<html> <!-- Het root-element, alles staat hierbinnen -->

<head>
    <!-- Bevat meta-informatie over de pagina (niet direct zichtbaar) -->
    <meta charset=\"UTF-8\"> <!-- Tekenset specificatie (belangrijk!) -->
    <title>Titel van de Pagina</title> <!-- Verschijnt in browser tabblad -->
    <!-- Hier kunnen ook links naar CSS bestanden staan -->
</head>

<body>
    <!-- Alle zichtbare inhoud van de pagina komt hier -->
    <h1>Hoofdtitel van de Pagina</h1>
    <p>Dit is een paragraaf met wat tekst.</p>
    <a href=\"about.html\">Over ons</a>
</body>

</html>
    ''', language='html')

    st.subheader("Veelvoorkomende HTML Tags (Voorbeelden)")
    st.markdown("**Koppen (Headings):**")
    st.code("<h1>Grootste Kop</h1>\\n<h2>Subkop</h2>\\n<h6>Kleinste Kop</h6>", language='html')
    st.write("Gebruik `<h1>` t/m `<h6>` om titels en subtitels aan te geven. `<h1>` is de belangrijkste.")

    st.markdown("**Paragrafen:**")
    st.code("<p>Dit is een alinea tekst.</p>\\n<p>Dit is nog een alinea.</p>", language='html')
    st.write("De `<p>` tag wordt gebruikt voor blokken tekst.")

    st.markdown("**Links (Anchors):**")
    st.code("<a href=\\\"https://streamlit.io\\\">Bezoek Streamlit</a>", language='html')
    st.write("De `<a>` tag maakt een hyperlink. Het `href` attribuut bevat de URL.")

    st.markdown("**Afbeeldingen:**")
    st.code("<img src=\\\"pad/naar/afbeelding.jpg\\\" alt=\\\"Beschrijving van afbeelding\\\">", language='html')
    st.write("De `<img>` tag toont een afbeelding. `src` is het pad naar het bestand, `alt` is alternatieve tekst (belangrijk voor toegankelijkheid en als de afbeelding niet laadt). Dit is een leeg element.")

    st.markdown("**Lijsten:**")
    st.markdown("*Ongesorteerde lijst (bolletjes):*", unsafe_allow_html=True)
    st.code("<ul>\\n  <li>Item 1</li>\\n  <li>Item 2</li>\\n</ul>", language='html')
    st.markdown("*Gesorteerde lijst (nummers):*", unsafe_allow_html=True)
    st.code("<ol>\\n  <li>Eerste stap</li>\\n  <li>Tweede stap</li>\\n</ol>", language='html')
    st.write("`<ul>` (unordered list) en `<ol>` (ordered list) maken lijsten. Elk item staat in een `<li>` (list item) tag.")

    st.markdown("**Structuur Elementen:**")
    st.code("<div>Dit is een algemene container.</div>\\n<p>Gebruik <span>dit</span> voor inline styling.</p>", language='html')
    st.write("`<div>` is een blok-niveau container, vaak gebruikt om secties te groeperen voor styling (met CSS). `<span>` is een inline container, vaak gebruikt om een klein stukje tekst binnen een groter blok apart te stijlen.")

    st.subheader("Nesting: Elementen binnen Elementen")
    st.write(
        """
        HTML elementen kunnen in elkaar genest worden. Bijvoorbeeld, een lijstitem (`<li>`) kan een link (`<a>`) bevatten, die weer een afbeelding (`<img>`) bevat.
        Het is belangrijk om tags correct te sluiten in de omgekeerde volgorde waarin je ze opent.
        """
    )
    st.code("<ul>\\n  <li><a href=\\\"#\\\">Link naar <strong>belangrijke</strong> info</a></li>\\n</ul>", language='html')
    st.write("Hier is `<strong>` genest in `<a>`, wat weer genest is in `<li>`.")

    st.subheader("Semantische HTML: Meer dan Alleen Uiterlijk")
    st.write(
        """
        Moderne HTML (HTML5) introduceerde **semantische tags**. Deze tags geven meer *betekenis* aan de structuur van de pagina, niet alleen hoe het eruit moet zien. Voorbeelden zijn:
        *   `<header>`: Voor de kopsectie van een pagina of sectie.
        *   `<footer>`: Voor de voetsectie.
        *   `<nav>`: Voor navigatielinks.
        *   `<article>`: Voor een op zichzelf staand stuk inhoud (bv. blogpost, nieuwsartikel).
        *   `<aside>`: Voor inhoud die losjes gerelateerd is aan de hoofdinhoud (bv. zijbalk).
        *   `<section>`: Voor een thematische groepering van inhoud.

        Het gebruik van deze tags is belangrijk voor:
        *   **Zoekmachines (SEO):** Helpt zoekmachines de structuur van je pagina beter te begrijpen.
        *   **Toegankelijkheid:** Helpt schermlezers en andere hulptechnologieën om de pagina correct te interpreteren voor gebruikers met een beperking.
        *   **Onderhoudbaarheid:** Maakt de code duidelijker en makkelijker te begrijpen voor ontwikkelaars.
        """
    )

    st.subheader("HTML en de Rol van CSS & JavaScript")
    st.info(
        """
        **Onthoud:**
        *   **HTML:** Bepaalt de **structuur** en **inhoud**.
        *   **CSS (Cascading Style Sheets):** Bepaalt de **presentatie** (layout, kleuren, lettertypen). Zorgt ervoor dat het er mooi uitziet.
        *   **JavaScript:** Voegt **interactiviteit** en **dynamisch gedrag** toe (reageren op kliks, animaties, data ophalen zonder herladen). Maakt de pagina levendig.

        Ze werken samen om de moderne webervaring te creëren!
        """
    )

    st.markdown("---")
    st.subheader("🤔 Test je Kennis!")

    html_vraag = "Welke HTML tag gebruik je om de belangrijkste, meest prominente kop op een pagina te maken?"
    html_opties = [
        "<p>",
        "<h6>",
        "<h1>", # Correct
        "<head>"
    ]
    html_correct = html_opties[2]

    gekozen_html_optie = st.radio(
        html_vraag,
        options=html_opties,
        index=None,
        key="html_vraag"
    )

    if gekozen_html_optie:
        if gekozen_html_optie == html_correct:
            st.success(f"Inderdaad! `{html_correct}` is de tag voor de hoofdtitel van een pagina. Het is belangrijk voor zowel de structuur als voor zoekmachines.")
        elif gekozen_html_optie == html_opties[3]:
            st.error(f"Niet helemaal. De `<head>` tag bevat meta-informatie over de pagina, maar niet de zichtbare hoofdtitel. `{html_correct}` is de juiste tag voor de zichtbare hoofdtitel in de `<body>`.")
        else:
            st.error(f"Bijna goed! `{gekozen_html_optie}` is wel een HTML tag, maar `{html_correct}` is specifiek bedoeld voor de belangrijkste kop op de pagina.")

# --- NIEUWE FUNCTIE VOOR BASIS VAN CSS ---
def css_basis_pagina():
    """Pagina over de basisprincipes van CSS."""
    st.title("🎨 Web Technologie: CSS (Cascading Style Sheets)")

    st.header("Wat is CSS? De Stijl van het Web")
    st.write(
        """
        Oké, HTML geeft ons de **structuur** en inhoud (het skelet). Maar hoe zorgen we ervoor
        dat het er mooi en overzichtelijk uitziet? Daarvoor gebruiken we **CSS (Cascading Style Sheets)**.

        CSS is een taal die beschrijft hoe HTML-elementen moeten worden **weergegeven** op het scherm.
        Het bepaalt de **presentatie**: kleuren, lettertypen, marges, afstanden, achtergronden, layout, etc.

        *Analogie:* Als HTML de structuur van het huis is (muren, kamers), dan is CSS de **verf**, het **behang**,
        de **meubels**, en de **decoratie**. Het maakt het huis visueel aantrekkelijk en leefbaar.
        Zonder CSS zouden webpagina's er erg kaal en saai uitzien (alleen zwarte tekst op een witte achtergrond).
        """
    )

    st.subheader("Hoe werkt CSS? Selectors & Declarations")
    st.write(
        """
        CSS werkt door **regels** te definiëren die aangeven welke stijl op welke HTML-elementen moet worden toegepast.
        Een CSS-regel bestaat meestal uit:
        1.  Een **Selector:** Hiermee *selecteer* je de HTML-element(en) die je wilt stijlen (bv. alle paragrafen, een specifiek element met een ID, elementen met een bepaalde class).
        2.  Een **Declaration Block:** Dit staat tussen `{` en `}` en bevat één of meer **declaraties**, gescheiden door puntkomma's `;`.
        3.  Een **Declaration:** Bestaat uit een **Property** (de stijl die je wilt veranderen, bv. `color` of `font-size`) en een **Value** (de waarde die je wilt instellen, bv. `blue` of `16px`), gescheiden door een dubbele punt `:`. 
        """
    )
    st.code('''
/* Dit is een CSS-commentaar */

/* Selector: selecteert alle <p> elementen */
p {
  /* Declaration Block */
  color: blue; /* Property: color, Value: blue */
  font-size: 16px; /* Property: font-size, Value: 16px */
}

/* Selector: selecteert het element met id="intro" */
#intro {
  background-color: lightgray;
}

/* Selector: selecteert alle elementen met class="highlight" */
.highlight {
  font-weight: bold;
}
    ''', language='css')

    st.subheader("CSS Koppelen aan HTML")
    st.write("Er zijn drie manieren om CSS toe te passen op HTML:")
    st.markdown(
        """
        1.  **External Stylesheet (Aanbevolen):** Je schrijft al je CSS-regels in een apart `.css` bestand (bv. `styles.css`) en koppelt dit bestand in de `<head>` van je HTML-document:
            `<link rel="stylesheet" href="styles.css">`
            *Voordeel:* Houdt structuur (HTML) en stijl (CSS) gescheiden, makkelijk te beheren voor grotere sites.
        2.  **Internal Stylesheet:** Je plaatst CSS-regels direct in de `<head>` van je HTML-document, binnen `<style>` tags:
            `<style> p { color: red; } </style>`
            *Voordeel:* Handig voor kleine, specifieke stijlen voor één pagina.
        3.  **Inline Styles:** Je past stijl direct toe op een specifiek HTML-element met het `style` attribuut:
            `<p style="color: green;">Deze paragraaf is groen.</p>`
            *Nadeel:* Maakt HTML onoverzichtelijk, moeilijk te onderhouden, vermijden indien mogelijk.
        """
    )

    st.subheader("Veelvoorkomende CSS Properties")
    st.write("Enkele voorbeelden van wat je met CSS kunt doen:")
    st.markdown(
        """
        *   **Tekst:** `color`, `font-size`, `font-family`, `font-weight` (vet), `text-align` (uitlijning).
        *   **Achtergrond:** `background-color`, `background-image`.
        *   **Box Model:** `margin` (ruimte *buiten* het element), `padding` (ruimte *binnen* het element), `border` (rand).
        *   **Layout:** `display` (bv. `block`, `inline`, `flex`, `grid`), `position`, `width`, `height`.
        """
    )
    # Placeholder voor interactief voorbeeld?

    st.subheader("De 'Cascade' en Specificiteit (Kort)")
    st.write(
        """
        Waarom 'Cascading'? Omdat meerdere CSS-regels van toepassing kunnen zijn op hetzelfde element.
        De browser volgt regels (de cascade) om te bepalen welke stijl uiteindelijk wint:
        1.  **Belangrijkheid:** `!important` wint (maar gebruik spaarzaam!).
        2.  **Specificiteit:** Hoe specifieker de selector (bv. een ID is specifieker dan een class, die weer specifieker is dan een tagnaam), hoe zwaarder deze weegt.
        3.  **Volgorde:** Als de specificiteit gelijk is, wint de regel die *later* in de CSS-code staat.

        Dit klinkt complex, maar het zorgt ervoor dat je basisstijlen kunt definiëren en deze later kunt overschrijven voor specifieke gevallen.
        """
    )

    st.info(
        """
        **Samenhang:**
        *   **HTML:** Levert de inhoud en structuur.
        *   **CSS:** Stijlt die inhoud en structuur.
        *   **JavaScript:** Kan later zowel HTML (inhoud/structuur) als CSS (stijl) dynamisch veranderen.
        """
    )

    st.markdown("---")
    st.subheader("🤔 Test je Kennis!")

    css_vraag = "Je wilt ALLE paragrafen (`<p>`) op je webpagina een blauwe tekstkleur geven. Welke CSS-regel is hiervoor het meest geschikt?"
    css_opties = [
        "p { text-color: blue; }",
        "paragraaf { color: blue; }",
        ".paragraaf { color: blue; }",
        "p { color: blue; }" # Correct
    ]
    css_correct = css_opties[3]

    gekozen_css_optie = st.radio(
        css_vraag,
        options=css_opties,
        index=None,
        key="css_vraag"
    )

    if gekozen_css_optie:
        if gekozen_css_optie == css_correct:
            st.success(f"Correct! `{css_correct}` selecteert alle `<p>` elementen (via de `p` selector) en past de eigenschap `color` toe met de waarde `blue`.")
        elif gekozen_css_optie == css_opties[0]:
            st.error("Bijna! De property voor tekstkleur is `color`, niet `text-color`.")
        elif gekozen_css_optie == css_opties[1]:
            st.error("Niet helemaal. De selector voor een HTML-tag is de tagnaam zelf (`p`), niet het woord 'paragraaf'.")
        elif gekozen_css_optie == css_opties[2]:
            st.error(f'Deze regel zou werken als je aan alle paragrafen de *class* `paragraaf` zou toevoegen (`<p class="paragraaf">`), maar de vraag was om *alle* paragrafen te selecteren, wat je direct met de `p` selector doet.')


# --- NIEUWE FUNCTIE VOOR BASIS VAN JAVASCRIPT ---
def js_basis_pagina():
    """Pagina over de basisprincipes van JavaScript."""
    st.title("⚡ Web Technologie: JavaScript (Interactie)")

    st.header("Wat is JavaScript? Het Leven van het Web")
    st.write(
        """
        We hebben HTML voor de structuur (skelet) en CSS voor de stijl (uiterlijk).
        Maar hoe maken we webpagina's **dynamisch** en **interactief**? Hoe reageren ze op
        gebruikersacties zonder dat de hele pagina opnieuw hoeft te laden?
        Dat is waar **JavaScript (JS)** om de hoek komt kijken.

        JavaScript is een **programmeertaal** die voornamelijk wordt gebruikt om webpagina's
        interactief te maken. Het draait meestal **in de browser van de gebruiker** (net als HTML en CSS).

        *Analogie:* Als HTML het huis en CSS de inrichting is, dan is JavaScript de **elektriciteit**, de **apparaten**,
        en de **bewoners**. Het maakt dingen mogelijk:
        *   De lichten aan/uit doen als je op een knop drukt (reageren op events).
        *   De thermostaat die de temperatuur aanpast (inhoud dynamisch wijzigen).
        *   De deurbel die rinkelt (notificaties tonen).
        *   Apparaten die met elkaar praten (communiceren met de backend via API's).
        """
    )

    st.subheader("Wat kun je met JavaScript doen? (Voorbeelden)")
    st.markdown(
        """
        *   **Reageren op Gebruikersacties:** Iets laten gebeuren als een gebruiker klikt, typt, scrolt, etc. (Events).
        *   **HTML Inhoud Veranderen:** Tekst, afbeeldingen of andere elementen toevoegen, verwijderen of aanpassen *nadat* de pagina is geladen (DOM Manipulatie).
        *   **CSS Stijlen Veranderen:** Het uiterlijk van elementen dynamisch aanpassen.
        *   **Formulieren Valideren:** Controleren of gebruikers de juiste informatie invoeren *voordat* het naar de server wordt gestuurd.
        *   **Animaties Maken:** Elementen laten bewegen of van uiterlijk veranderen.
        *   **Data Ophalen/Versturen:** Communiceren met de backend (via API's) om gegevens op te halen of te verzenden zonder de hele pagina te herladen (AJAX/Fetch).
        *   **Complexe UI Bouwen:** Denk aan interactieve kaarten, drag-and-drop interfaces, etc.
        """
    )

    st.subheader("Basisconcepten (Zeer Eenvoudig)")
    st.write("JavaScript is een volwaardige programmeertaal. Enkele kernideeën:")
    st.markdown(
        """
        *   **Variabelen:** Namen waaronder je data kunt opslaan (bv. `let score = 0;`).
        *   **Data Types:** Soorten gegevens (bv. getallen, tekst (strings), booleans (true/false)).
        *   **Functies:** Blokken herbruikbare code die een specifieke taak uitvoeren.
        *   **Events:** Gebeurtenissen waarop je kunt reageren (bv. `onclick`, `onmouseover`, `onsubmit`).
        *   **DOM (Document Object Model):** Een manier waarop JavaScript de structuur van een HTML-pagina 'ziet' en kan manipuleren (elementen selecteren, aanpassen, toevoegen, verwijderen).
        """
    )

    st.subheader("Simpel Voorbeeld: Knop die Tekst Verandert")
    st.write("Stel je voor, je hebt deze HTML:")
    st.code('<p id="mijnTekst">Hallo!</p>\n<button id="mijnKnop">Verander Tekst</button>', language='html')
    st.write("Met JavaScript kun je dit doen:")
    st.code('''
// Selecteer de knop en de paragraaf
const knop = document.getElementById('mijnKnop');
const tekst = document.getElementById('mijnTekst');

// Voeg een 'event listener' toe aan de knop
// Deze functie wordt uitgevoerd als er op de knop geklikt wordt
knop.addEventListener('click', function() {
  // Verander de inhoud van de paragraaf
  tekst.textContent = 'Tekst is veranderd!';
});
    ''', language='javascript')
    st.write("(Dit JavaScript-fragment zou je meestal in een apart `.js` bestand zetten en koppelen in je HTML, of binnen `<script>` tags plaatsen.)")

    st.subheader("JavaScript Koppelen aan HTML")
    st.write("Net als CSS, kun je JavaScript op een paar manieren toevoegen:")
    st.markdown(
        """
        1.  **External Script (Aanbevolen):** Code in een apart `.js` bestand, gekoppeld met:
            `<script src="mijn_script.js"></script>` (vaak onderaan de `<body>`).
        2.  **Internal Script:** Code direct in de HTML binnen `<script>` tags:
            `<script> alert('Hallo!'); </script>` (kan in `<head>` of `<body>`).
        """
    )

    st.info(
        """
        **De Drie-eenheid:**
        *   **HTML:** Structuur
        *   **CSS:** Stijl
        *   **JavaScript:** Gedrag/Interactie

        Ze vormen samen de basis van moderne webontwikkeling.
        """
    )

    st.markdown("---")
    st.subheader("🤔 Test je Kennis!")

    js_vraag = "Welke taal wordt voornamelijk gebruikt om interactiviteit en dynamisch gedrag toe te voegen aan webpagina's, direct in de browser van de gebruiker?"
    js_opties = [
        "HTML",
        "CSS",
        "Python",
        "JavaScript" # Correct
    ]
    js_correct = js_opties[3]

    gekozen_js_optie = st.radio(
        js_vraag,
        options=js_opties,
        index=None,
        key="js_vraag"
    )

    if gekozen_js_optie:
        if gekozen_js_optie == js_correct:
            st.success(f"Klopt helemaal! {js_correct} is de primaire taal voor client-side scripting en maakt webpagina's levendig.")
        elif gekozen_js_optie == js_opties[0]:
            st.error("HTML definieert de *structuur* en inhoud, maar niet de interactieve logica.")
        elif gekozen_js_optie == js_opties[1]:
            st.error("CSS regelt de *styling* en presentatie, maar voegt geen interactief gedrag toe.")
        elif gekozen_js_optie == js_opties[2]:
            st.error("Python wordt vaak gebruikt voor de *backend* (server-side logica), maar niet typisch voor interactie direct *in* de browser zoals JavaScript dat doet (hoewel er manieren zijn via frameworks zoals Brython of PyScript, is JS de standaard).")

# --- NIEUWE SUBPAGINA VOOR PYTHON BACKEND ---
def backend_talen_python_pagina():
    """Subpagina specifiek over Python voor backend ontwikkeling."""
    st.subheader("🐍 Python als Backend Taal")
    st.write(
        """
        Python is extreem populair, en niet alleen voor data science! Het is ook een zeer krachtige en veelgebruikte taal
        voor backend ontwikkeling. De leesbaarheid, grote standaardbibliotheek en enorme community maken het een aantrekkelijke keuze.
        """
    )

    st.markdown("**Voordelen van Python voor Backend:**")
    st.markdown(
        """
        *   **Leesbaarheid & Eenvoud:** Python's syntax is ontworpen om duidelijk en beknopt te zijn, wat ontwikkeling en onderhoud makkelijker maakt.
        *   **Grote Standaardbibliotheek:** Veel ingebouwde modules voor netwerken, bestandsverwerking, data, etc.
        *   **Enorme Package Index (PyPI):** Duizenden externe bibliotheken voor bijna elke denkbare taak (databases, web frameworks, API's, etc.). `pip install ...` is je vriend!
        *   **Actieve Community:** Veel tutorials, documentatie en hulp online beschikbaar.
        *   **Goede Integratie:** Werkt goed samen met andere technologieën en is sterk in dataverwerking (handig als je backend veel data analyseert).
        *   **Schaalbaarheid:** Hoewel soms bekritiseerd, kan Python zeker schalen voor grote applicaties met de juiste architectuur en tools.
        """
    )

    st.markdown("**Populaire Python Backend Frameworks:**")
    st.write("In plaats van alles vanaf nul op te bouwen, gebruiken ontwikkelaars meestal een **framework** dat veelvoorkomende taken vereenvoudigt:")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Django:**")
        st.write(
            """
            *   **"Batteries-included"**: Een full-stack framework dat vrijwel alles biedt wat je nodig hebt (ORM voor databases, admin interface, authenticatie, templating engine, etc.).
            *   **Opinieated:** Heeft een duidelijke structuur en manier van werken ('The Django Way').
            *   **Snel ontwikkelen:** Veel ingebouwde functionaliteit versnelt het bouwproces, vooral voor data-gedreven websites.
            *   **Robuust & Schaalbaar:** Bewezen in productie voor grote sites (bv. Instagram, Pinterest).
            """
        )
        st.code('''
# Voorbeeld (conceptueel - Django view)
from django.http import HttpResponse

def hallo(request):
    return HttpResponse("Hallo vanuit Django!")
        ''', language='python')

    with col2:
        st.markdown("**Flask:**")
        st.write(
            """
            *   **Microframework:** Minimalistisch en flexibel. Geeft je alleen de basis (routing, request handling) en laat jou de rest kiezen.
            *   **Minder Opinieated:** Meer vrijheid in hoe je je project structureert en welke tools je gebruikt.
            *   **Makkelijker te leren (initieel):** Kleiner en minder complex dan Django om mee te beginnen.
            *   **Geweldig voor API's en kleinere apps:** Populair voor het bouwen van REST API's of als je geen behoefte hebt aan alle features van Django.
            """
        )
        st.code('''
# Voorbeeld (conceptueel - Flask route)
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hallo():
    return "Hallo vanuit Flask!"
        ''', language='python')

    st.write("Andere frameworks zoals FastAPI (modern, snel, geweldig voor API's), Pyramid, etc. bestaan ook.")

    st.markdown("**Interactie met Databases (ORM):**")
    st.write(
        """
        Python backends moeten vaak praten met databases. In plaats van direct SQL-queries te schrijven (wat foutgevoelig kan zijn),
        gebruiken veel ontwikkelaars een **Object-Relational Mapper (ORM)**. Een ORM laat je met database tabellen en rijen werken
        alsof het gewone Python objecten en klassen zijn. De ORM vertaalt je Python code naar SQL.
        *   **Django ORM:** Ingebouwd in Django.
        *   **SQLAlchemy:** Een populaire, krachtige en onafhankelijke ORM die met veel frameworks (zoals Flask) kan worden gebruikt.
        """
    )

# --- NIEUWE SUBPAGINA VOOR NODE.JS BACKEND ---
def backend_talen_nodejs_pagina():
    """Subpagina specifiek over Node.js voor backend ontwikkeling."""
    st.subheader("🚀 Node.js (JavaScript op de Server)")
    st.write(
        """
        Traditioneel was JavaScript de taal van de browser (Frontend). Maar met **Node.js** kun je
        JavaScript nu ook gebruiken voor **backend ontwikkeling**! Node.js is geen taal op zich,
        maar een **runtime environment** (uitvoeringsomgeving) gebaseerd op Chrome's V8 JavaScript engine.
        """
    )

    st.markdown("**Voordelen van Node.js voor Backend:**")
    st.markdown(
        """
        *   **JavaScript Overal:** Je kunt dezelfde taal gebruiken voor zowel Frontend als Backend, wat voor sommige teams efficiënt kan zijn.
        *   **Asynchroon & Non-blocking I/O:** Node.js blinkt uit in het afhandelen van veel gelijktijdige verbindingen (zoals bij chat-apps, real-time updates) zonder te 'blokkeren'. Het is zeer efficiënt voor I/O-intensieve taken.
        *   **NPM (Node Package Manager):** Toegang tot een gigantisch ecosysteem van herbruikbare modules en bibliotheken via `npm install`.
        *   **Actieve Community:** Zeer grote en actieve community.
        *   **Snelheid:** De V8 engine is zeer snel in het uitvoeren van JavaScript.
        """
    )

    st.markdown("**Populaire Node.js Backend Frameworks:**")
    st.write("Ook voor Node.js zijn er frameworks om het leven makkelijker te maken:")
    st.markdown(
        """
        *   **Express.js:** Het meest populaire, minimalistische en flexibele framework voor Node.js. Vormt vaak de basis voor andere frameworks. Vergelijkbaar met Flask in Python qua filosofie.
        *   **Koa.js:** Gemaakt door het team achter Express, moderner en gebruikt nieuwere JavaScript features.
        *   **NestJS:** Een meer 'opinionated' framework dat concepten uit Angular (zoals modules, providers) naar de backend brengt. Biedt meer structuur.
        *   **Sails.js:** Een MVC framework dat lijkt op Ruby on Rails.
        """
    )
    st.code('''
// Voorbeeld (conceptueel - Express.js route)
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hallo vanuit Express!');
});

app.listen(3000, () => {
  console.log('Server draait op poort 3000');
});
    ''', language='javascript')

    st.markdown("**Interactie met Databases:**")
    st.write(
        """
        Node.js heeft drivers en bibliotheken voor vrijwel elke database.
        *   Voor **SQL databases** (zoals PostgreSQL, MySQL) gebruik je drivers zoals `pg` of `mysql2`, vaak in combinatie met een query builder (bv. Knex.js) of een ORM (bv. Sequelize, TypeORM).
        *   Voor **NoSQL databases** zoals MongoDB is de `mongodb` driver populair, vaak gebruikt met **Mongoose**, een ODM (Object Document Mapper) die het werken met documenten vergemakkelijkt.
        """
    )

# --- NIEUWE SUBPAGINA VOOR JAVA BACKEND ---
def backend_talen_java_pagina():
    """Subpagina specifiek over Java voor backend ontwikkeling."""
    st.subheader("☕ Java als Backend Taal")
    st.write(
        """
        Java is een van de meest gevestigde en wijdverspreide programmeertalen, en een steunpilaar
        in de wereld van **enterprise (grote bedrijfs-) applicaties**. Het staat bekend om zijn
        robuustheid, performance en het principe van "Write Once, Run Anywhere" (WORA) dankzij de **JVM**.
        """
    )

    st.markdown("**Voordelen van Java voor Backend:**")
    st.markdown(
        """
        *   **Platformonafhankelijkheid (JVM):** Java code wordt gecompileerd naar bytecode, die draait op de **Java Virtual Machine (JVM)**. Er zijn JVM's voor bijna elk besturingssysteem, waardoor Java-applicaties zeer portable zijn.
        *   **Sterk Getypeerd (Statically Typed):** Fouten worden vaak al tijdens het compileren gedetecteerd, wat leidt tot robuustere code (minder runtime fouten).
        *   **Performance:** Moderne JVM's zijn zeer geoptimaliseerd en bieden uitstekende prestaties, zeker voor langlopende applicaties.
        *   **Groot Ecosysteem & Volwassenheid:** Enorme hoeveelheid bibliotheken, frameworks, tools en een zeer grote community. Veel kennis en ondersteuning beschikbaar.
        *   **Schaalbaarheid & Concurrency:** Goede ingebouwde ondersteuning voor multithreading en concurrency, belangrijk voor grote systemen die veel taken tegelijk moeten uitvoeren.
        *   **Objectgeoriënteerd:** Sterk objectgeoriënteerd ontwerp bevordert modulaire en herbruikbare code.
        """
    )

    st.markdown("**Populaire Java Backend Frameworks:**")
    st.write("Java kent een rijk landschap aan frameworks, vooral gericht op enterprise-niveau:")
    st.markdown(
        """
        *   **Spring Framework / Spring Boot:** Veruit het populairste ecosysteem. Spring Boot maakt het zeer eenvoudig om snel standalone, productieklare Spring-applicaties op te zetten. Biedt oplossingen voor dependency injection, web development (Spring MVC/WebFlux), data access, beveiliging, en veel meer.
        *   **Jakarta EE (voorheen Java EE):** Een set van specificaties voor het bouwen van enterprise applicaties. Frameworks zoals WildFly, GlassFish implementeren deze specificaties.
        *   **Quarkus:** Een moderner framework gericht op cloud-native ontwikkeling en snelle opstarttijden (goed voor serverless/containers).
        *   **Micronaut:** Vergelijkbaar met Quarkus, gericht op microservices en cloud.
        """
    )
    st.code('''
// Voorbeeld (conceptueel - Spring Boot Controller)
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping("/")
    public String hello() {
        return "Hallo vanuit Spring Boot!";
    }
}
    ''', language='java')

    st.markdown("**Interactie met Databases:**")
    st.write(
        """
        Java heeft uitgebreide ondersteuning voor database interactie:
        *   **JDBC (Java Database Connectivity):** De standaard API voor het verbinden met SQL databases. Vormt de basis voor veel andere tools.
        *   **JPA (Jakarta Persistence API) / Hibernate:** JPA is een specificatie voor ORM (Object-Relational Mapping) in Java. **Hibernate** is de meest populaire implementatie ervan. Het stelt ontwikkelaars in staat om met Java objecten te werken die automatisch worden gemapt naar database tabellen.
        *   **Spring Data JPA:** Maakt het werken met JPA/Hibernate binnen Spring applicaties nog eenvoudiger.
        *   Drivers voor NoSQL databases zijn ook breed beschikbaar.
        """
    )

# --- NIEUWE SUBPAGINA VOOR C# (.NET) BACKEND ---
def backend_talen_csharp_pagina():
    """Subpagina specifiek over C# (.NET) voor backend ontwikkeling."""
    st.subheader("🔷 C# (.NET) als Backend Taal")
    st.write(
        """
        C# (uitgesproken als 'C Sharp') is een moderne, objectgeoriënteerde programmeertaal ontwikkeld door Microsoft
        als onderdeel van het **.NET platform**. Het is zeer populair voor het bouwen van Windows-applicaties,
        maar met **.NET Core (nu gewoon .NET 5/6/7+ genoemd)** is het ook een krachtige, cross-platform keuze
        geworden voor backend en webontwikkeling.
        """
    )

    st.markdown("**Voordelen van C# (.NET) voor Backend:**")
    st.markdown(
        """
        *   **Sterk Getypeerd & Objectgeoriënteerd:** Vergelijkbaar met Java, helpt dit bij het bouwen van robuuste en onderhoudbare applicaties.
        *   **Uitstekende Performance:** .NET staat bekend om zijn goede prestaties.
        *   **Krachtig Ecosysteem:** Rijke standaardbibliotheken (Base Class Library), uitstekende tooling (Visual Studio, VS Code), en een grote package manager (NuGet).
        *   **Cross-Platform:** Dankzij .NET Core/5+ draaien C# backend applicaties nu native op Windows, macOS en Linux.
        *   **Goede Integratie met Microsoft Azure:** Natuurlijke keuze als je veel gebruik maakt van Microsoft's cloud platform.
        *   **Asynchrone Programmering:** Sterke ingebouwde ondersteuning voor `async/await`.
        """
    )

    st.markdown("**Populair C# Backend Framework:**")
    st.markdown(
        """
        *   **ASP.NET Core:** Het moderne, cross-platform, high-performance framework van Microsoft voor het bouwen van webapplicaties en API's met C#. Het is modulair opgebouwd en biedt opties voor MVC (Model-View-Controller), Razor Pages, en Web API's.
        """
    )
    st.code('''
// Voorbeeld (conceptueel - ASP.NET Core Minimal API)
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hallo vanuit ASP.NET Core!");

app.Run();
    ''', language='csharp')

    st.markdown("**Interactie met Databases:**")
    st.write(
        """
        De meest gebruikte manier om met databases te werken in .NET is via:
        *   **Entity Framework Core (EF Core):** Microsoft's moderne, cross-platform ORM (Object-Relational Mapper). Het maakt database-interactie vanuit C# code eenvoudig en intuïtief.
        *   **Dapper:** Een populaire, lichtgewicht 'micro-ORM' die focust op performance en meer controle geeft over de gegenereerde SQL.
        *   Directe toegang via ADO.NET is ook mogelijk, maar minder gebruikelijk voor nieuwe applicaties.
        """
    )

# --- NIEUWE SUBPAGINA VOOR PHP BACKEND ---
def backend_talen_php_pagina():
    """Subpagina specifiek over PHP voor backend ontwikkeling."""
    st.subheader("🐘 PHP als Backend Taal")
    st.write(
        """
        PHP (Hypertext Preprocessor) is een van de meest gebruikte server-side scripting talen ter wereld,
        vooral bekend van content management systems zoals **WordPress**, Drupal en Joomla.
        Hoewel het soms kritiek krijgt, is modern PHP (versie 7 en 8+) een volwassen en capabele taal
        met een enorm ecosysteem.
        """
    )

    st.markdown("**Voordelen van PHP voor Backend:**")
    st.markdown(
        """
        *   **Wijdverspreid & Goedkoop Hosten:** Bijna elke webhost ondersteunt PHP, vaak tegen lage kosten.
        *   **Grote Community & Veel Resources:** Enorme hoeveelheid tutorials, forums en bestaande code.
        *   **Volwassen Taal & Ecosysteem:** Veel stabiele bibliotheken en frameworks beschikbaar (via **Composer**, de package manager).
        *   **Makkelijker Leercurve (initieel):** Relatief eenvoudig om mee te beginnen voor simpele webpagina's.
        *   **Goede Frameworks:** Moderne frameworks zoals Laravel en Symfony maken gestructureerde en veilige ontwikkeling mogelijk.
        """
    )

    st.markdown("**Populaire PHP Backend Frameworks:**")
    st.markdown(
        """
        *   **Laravel:** Momenteel een van de populairste PHP frameworks, bekend om zijn elegante syntax, uitgebreide featureset ("batteries-included" zoals Eloquent ORM, Blade templating) en focus op developer experience.
        *   **Symfony:** Een zeer robuust en flexibel framework dat bestaat uit herbruikbare componenten. Veel andere frameworks (waaronder Laravel) gebruiken Symfony componenten.
        *   **CodeIgniter:** Een lichtgewicht framework met een focus op eenvoud en snelheid.
        *   **CakePHP:** Een ouder framework dat nog steeds actief wordt ontwikkeld, gebaseerd op Ruby on Rails principes.
        """
    )
    st.code(r'''
<?php
// Voorbeeld (conceptueel - Laravel Route)
use Illuminate\Support\Facades\Route;

Route::get('/', function () {
    return 'Hallo vanuit Laravel!';
});
?>
    ''', language='php')

    st.markdown("**Interactie met Databases:**")
    st.write(
        """
        PHP heeft uitstekende database-ondersteuning:
        *   **PDO (PHP Data Objects):** Een consistente interface voor toegang tot verschillende databases (MySQL, PostgreSQL, SQLite, etc.). Biedt bescherming tegen SQL-injection via prepared statements.
        *   **MySQLi (MySQL Improved):** Een extensie specifiek voor het werken met MySQL databases.
        *   **ORM's:** Frameworks zoals Laravel (Eloquent) en Symfony (Doctrine) bieden krachtige ORM's om interactie met databases te vereenvoudigen.
        """
    )

# --- NIEUWE SUBPAGINA VOOR RUBY BACKEND ---
def backend_talen_ruby_pagina():
    """Subpagina specifiek over Ruby (on Rails) voor backend ontwikkeling."""
    st.subheader("💎 Ruby (on Rails) als Backend Taal")
    st.write(
        """
        Ruby is een dynamische, objectgeoriënteerde taal die bekend staat om zijn elegante syntax en focus
        op productiviteit en 'developer happiness'. Hoewel de taal zelf flexibel is, wordt Ruby in de
        backend wereld bijna synoniem gebruikt met zijn populairste framework: **Ruby on Rails**. 
        """
    )

    st.markdown("**Voordelen van Ruby (on Rails) voor Backend:**")
    st.markdown(
        """
        *   **Ruby on Rails Framework:** Een zeer productief full-stack web framework dat veel conventies volgt ('Convention over Configuration'). Dit maakt snelle ontwikkeling mogelijk als je de conventies volgt.
        *   **Developer Happiness:** De taal en het framework zijn ontworpen om prettig te zijn om mee te werken.
        *   **Groot Ecosysteem (Gems):** Ruby heeft een package manager genaamd RubyGems, waarmee je eenvoudig bibliotheken ('gems') kunt installeren.
        *   **Actieve Community:** Vooral rondom Rails is er een sterke en behulpzame community.
        *   **Elegantie & Expressiviteit:** Code in Ruby is vaak kort en goed leesbaar.
        """
    )

    st.markdown("**Het Ruby on Rails Framework:**")
    st.write("Rails is een 'opinionated' MVC (Model-View-Controller) framework. Kernprincipes zijn:")
    st.markdown(
        """
        *   **Convention over Configuration:** Je hoeft minder configuratie te schrijven als je je aan de standaard naamgeving en structuur houdt.
        *   **Don't Repeat Yourself (DRY):** Vermijd het herhalen van dezelfde code op meerdere plaatsen.
        *   **Active Record:** De ingebouwde ORM die het werken met databases (meestal SQL) sterk vereenvoudigt.
        *   **Ingebouwde Tools:** Veel functionaliteit voor routing, templating (ERB), testing, etc. is standaard aanwezig.
        """
    )
    st.code('''
# Voorbeeld (conceptueel - Ruby on Rails Controller Action)
class PagesController < ApplicationController
  def home
    render plain: "Hallo vanuit Ruby on Rails!"
  end
end

# routes.rb (configuratie)
# Rails.application.routes.draw do
#   root "pages#home"
# end
    ''', language='ruby')

    st.markdown("**Interactie met Databases (Active Record):**")
    st.write(
        """
        **Active Record** is de standaard ORM in Rails. Het volgt sterk het 'Convention over Configuration' principe.
        Als je een databasetabel `products` hebt, maak je een Ruby klasse `Product` (enkelvoud) die erft
        van `ApplicationRecord`, en Rails regelt de rest. Je kunt dan eenvoudig records vinden, maken, bijwerken
        en verwijderen met Ruby methoden.
        """
    )

# --- PLACEHOLDER FUNCTIES VOOR BACKEND SUBPAGINA'S ---
# Deze functies moeten nog worden ingevuld met de daadwerkelijke inhoud.

def backend_frameworks_algemeen_pagina():
    """Pagina over algemene concepten van Backend Frameworks."""
    st.header("🔧 Backend Frameworks: Het Gereedschap van de Ontwikkelaar")
    st.write(
        """
        Hoewel je een backend volledig vanaf nul kunt opbouwen, is dat zelden efficiënt.
        **Backend frameworks** bieden een **gestructureerde basis** en **herbruikbare componenten**
        om de ontwikkeling van webapplicaties en API's te versnellen en te vereenvoudigen.

        Zie het als een **gereedschapskist** en een **bouwplan** voor je backend. In plaats van elke schroef
        en plank zelf te moeten maken en uitvinden hoe ze passen, geeft een framework je kant-en-klare
        onderdelen en een beproefde manier om ze samen te voegen.
        """
    )

    st.subheader("Waarom Frameworks Gebruiken?")
    st.markdown(
        """
        *   **Productiviteit:** Veelvoorkomende taken (zoals request handling, routing, database interactie, templating, beveiliging) zijn al (deels) opgelost.
        *   **Structuur & Organisatie:** Frameworks moedigen een bepaalde projectstructuur en code-organisatie aan (bv. MVC), wat leidt tot beter onderhoudbare code, vooral in teams.
        *   **Best Practices & Beveiliging:** Goede frameworks implementeren vaak beveiligingsmaatregelen (bv. tegen XSS, CSRF) en volgen industriestandaarden.
        *   **Community & Ecosysteem:** Populaire frameworks hebben vaak grote communities voor ondersteuning en een rijk ecosysteem van plug-ins en extensies.
        *   **Schaalbaarheid:** Veel frameworks zijn ontworpen met schaalbaarheid in gedachten.
        """
    )

    st.subheader("Veelvoorkomende Concepten & Patronen")
    st.write("Hoewel frameworks verschillen, zie je vaak dezelfde onderliggende ideeën terugkomen:")

    with st.expander("Routing"):
        st.write("Het proces van het koppelen van inkomende URL's (bv. `/gebruikers/profiel`) aan specifieke stukken code (controllers/functies) die het verzoek moeten afhandelen.")
        st.code('''# Conceptueel voorbeeld (Flask/Express-achtig)
@app.route('/producten/<int:product_id>')
def toon_product(product_id):
    # Code om product met ID op te halen en te tonen
    pass
''', language='python')

    with st.expander("MVC (Model-View-Controller)"):
        st.write(
            """
            Een veelgebruikt architectuurpatroon om de applicatielogica te scheiden in drie onderdelen:
            *   **Model:** Vertegenwoordigt de data en de bedrijfslogica. Communiceert met de database (vaak via een ORM).
            *   **View:** Verantwoordelijk voor de presentatie van de data aan de gebruiker (bv. HTML genereren via templates). Ontvangt data van de Controller.
            *   **Controller:** Ontvangt de input van de gebruiker (HTTP requests), verwerkt deze (roept logica in het Model aan), en bepaalt welke View getoond moet worden met welke data.
            """
        )
        st.caption("Veel frameworks (zoals Ruby on Rails, Django (MVT is vergelijkbaar), ASP.NET MVC, Laravel) zijn gebaseerd op dit patroon.")

    with st.expander("Request/Response Cyclus"):
        st.write("Frameworks beheren de levenscyclus van een HTTP request: het ontvangen, verwerken (routing, controller, model), genereren van een response (vaak via een view/template), en terugsturen naar de client.")

    with st.expander("Templating Engines"):
        st.write(
            """
            Wordt gebruikt door de View om dynamisch HTML (of andere formaten) te genereren.
            Je schrijft templates met placeholders en logica (loops, conditionals) die door de engine worden
            gevuld met data vanuit de controller/model.
            *Voorbeelden:* Jinja2 (Flask/Python), Blade (Laravel/PHP), ERB (Rails/Ruby), Thymeleaf (Java/Spring).
            """
        )
        st.code('''<!-- Jinja2 Template Voorbeeld -->
<h1>Hallo, {{ user.name }}!</h1>
<ul>
{% for item in items %}
  <li>{{ item }}</li>
{% endfor %}
</ul>
''', language='html')

    with st.expander("ORM (Object-Relational Mapper)"):
        st.write("Zoals besproken bij Databases: veel frameworks integreren of faciliteren het gebruik van een ORM om database interactie te vereenvoudigen.")

    st.subheader("Full-Stack vs. Microframeworks")
    st.write("Frameworks variëren sterk in omvang en de hoeveelheid functionaliteit die ze standaard bieden:")

    col_fs, col_mf = st.columns(2)
    with col_fs:
        st.markdown('**Full-Stack Frameworks ("Batteries-included")**')
        st.write(
            """
            *   **Uitgebreid:** Bieden oplossingen voor bijna alle aspecten van webontwikkeling (ORM, authenticatie, admin panel, templating, formulieren, etc.) out-of-the-box.
            *   **Opinieated:** Hebben vaak een sterke mening over hoe dingen gedaan moeten worden.
            *   **Snelle start (voor standaard dingen):** Je kunt snel complexe, data-gedreven applicaties bouwen.
            *   **Voorbeelden:** Django (Python), Ruby on Rails (Ruby), Laravel (PHP), Spring (Java), ASP.NET (C#).
            """
        )
    with col_mf:
        st.markdown("**Microframeworks**")
        st.write(
            """
            *   **Minimalistisch:** Bieden alleen de kernfunctionaliteit (vaak routing en request/response handling).
            *   **Flexibel:** Laten de ontwikkelaar vrij om zelf componenten (ORM, templating engine, etc.) te kiezen en te integreren.
            *   **Eenvoudiger (initieel):** Makkelijker te begrijpen en mee te starten voor kleine projecten of API's.
            *   **Meer configuratie/setup:** Vereisen meer werk om dezelfde functionaliteit als een full-stack framework te krijgen.
            *   **Voorbeelden:** Flask (Python), Express.js (Node.js), Sinatra (Ruby), Spark (Java).
            """
        )

    st.info("De keuze tussen full-stack en micro hangt af van het project, de teamvoorkeuren en de benodigde flexibiliteit.")

    st.markdown("---")
    st.write("Specifieke populaire frameworks per taal worden behandeld onder het 'Programmeertalen' onderwerp.")

def backend_databases_pagina():
    """Pagina over Databases voor de Backend."""
    st.header("💾 Databases: Het Geheugen van de Applicatie")
    st.write(
        """
        Bijna elke serieuze webapplicatie moet gegevens **opslaan** en weer **ophalen**. Denk aan gebruikersprofielen,
        productcatalogi, blogposts, scores, etc. De backend is verantwoordelijk voor deze interactie met
        een **database**, een gestructureerde opslagplaats voor data.
        """
    )

    st.subheader("Waarom een Database?")
    st.markdown(
        """
        *   **Persistentie:** Data blijft bewaard, ook als de applicatie stopt en opnieuw start.
        *   **Efficiëntie:** Databases zijn geoptimaliseerd voor het snel opslaan, opzoeken en bijwerken van grote hoeveelheden data.
        *   **Dataintegrititeit:** Helpen bij het afdwingen van regels om te zorgen dat data correct en consistent is.
        *   **Gelijktijdigheid (Concurrency):** Meerdere gebruikers of processen kunnen tegelijkertijd (op een gecontroleerde manier) toegang krijgen tot de data.
        """
    )

    st.subheader("SQL (Relationeel) vs. NoSQL (Niet-Relationeel)")
    st.write("De twee belangrijkste categorieën databases zijn:")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**1. SQL / Relationele Databases**")
        st.write(
            """
            *   **Structuur:** Data wordt opgeslagen in **tabellen** met vooraf gedefinieerde kolommen en datatypes (zoals in een spreadsheet).
            *   **Relaties:** Tabellen kunnen aan elkaar gekoppeld worden via relaties (bv. een `users` tabel en een `orders` tabel, waarbij elke order een link heeft naar een gebruiker).
            *   **Taal:** Gebruiken **SQL (Structured Query Language)** voor het definiëren en manipuleren van data (data opvragen, toevoegen, wijzigen, verwijderen).
            *   **Schema:** Vereisen een vast schema dat bepaalt hoe de data gestructureerd is.
            *   **Consistentie:** Sterk gericht op dataconsistentie (ACID principes).
            *   **Voorbeelden:** PostgreSQL, MySQL, MariaDB, SQL Server, Oracle, SQLite.
            """
        )
        st.code('''-- Simpel SQL voorbeeld:
SELECT name, email FROM users WHERE country = 'Nederland';
''', language='sql')

    with col2:
        st.markdown("**2. NoSQL / Niet-Relationele Databases**")
        st.write(
            """
            *   **Structuur:** Flexibeler, geen vaste tabellen. Data kan op verschillende manieren worden opgeslagen:
                *   **Document:** Data opgeslagen in JSON-achtige documenten (bv. MongoDB).
                *   **Key-Value:** Simpele paren van een sleutel en een waarde (bv. Redis, DynamoDB).
                *   **Wide-Column:** Tabellen met flexibele kolommen (bv. Cassandra, HBase).
                *   **Graph:** Focust op relaties tussen data-entiteiten (bv. Neo4j).
            *   **Schema:** Vaak schema-loos of met een flexibel schema.
            *   **Schaalbaarheid:** Vaak ontworpen voor horizontale schaalbaarheid (makkelijk uit te breiden over meerdere servers).
            *   **Flexibiliteit:** Makkelijker om data structuren te veranderen.
            *   **Voorbeelden:** MongoDB, Redis, Cassandra, Neo4j, Couchbase.
            """
        )
        st.code('''// Simpel MongoDB document voorbeeld:
{
  "_id": "123",
  "name": "Alice",
  "email": "alice@example.com",
  "tags": ["active", "premium"]
}
''', language='json')

    st.subheader("ORM (Object-Relational Mapper)")
    st.write(
        """
        Direct SQL schrijven kan krachtig zijn, maar ook repetitief en foutgevoelig (denk aan SQL injection!).
        Veel backend frameworks gebruiken daarom een **ORM (Object-Relational Mapper)**.

        Een ORM is een bibliotheek die een laag vormt tussen jouw **objectgeoriënteerde code** (bv. Python klassen)
        en de **relationele database** (tabellen). Het 'mapt' database tabellen naar klassen en rijen naar objecten.
        """
    )
    st.markdown(
        """
        **Voordelen van ORM:**
        *   **Minder SQL:** Je schrijft code in de programmeertaal van je backend (bv. Python) om data te bevragen en te manipuleren.
        *   **Abstraction:** Verbergt de details van de specifieke database dialecten.
        *   **Productiviteit:** Vaak sneller ontwikkelen omdat je minder boilerplate SQL hoeft te schrijven.
        *   **Beveiliging:** Helpt vaak automatisch beschermen tegen SQL injection door correct gebruik van parameters.
        *   **Database Onafhankelijkheid (deels):** Makkelijker wisselen van database (bv. van SQLite naar PostgreSQL) met minimale codewijzigingen (in theorie).
        """
    )
    st.write("**Voorbeelden:** SQLAlchemy (Python), Django ORM (Python), Hibernate (Java), Entity Framework Core (.NET), Sequelize/TypeORM (Node.js), Eloquent (PHP), Active Record (Ruby).")

    st.code('''# Conceptueel Python voorbeeld met een ORM (bv. SQLAlchemy-achtig)

# Definieer een User klasse die mapt naar de 'users' tabel
class User:
    id: int
    name: str
    email: str

# Haal een gebruiker op met ID 5 (ORM genereert SQL)
user = session.query(User).get(5)

# Maak een nieuwe gebruiker aan (ORM genereert INSERT SQL)
new_user = User(name="Bob", email="bob@example.com")
session.add(new_user)
session.commit()
    ''', language='python')

    st.subheader("ACID Principes (Kort)")
    st.write("Relationele databases leggen vaak de nadruk op ACID-garanties voor transacties (een reeks operaties die als één geheel slagen of falen):")
    with st.expander("Wat betekent ACID?"):
        st.markdown(
            """
            *   **Atomicity (Atomiciteit):** Een transactie is ondeelbaar. Of *alle* operaties slagen, of *geen enkele* (alles wordt teruggedraaid bij een fout).
            *   **Consistency (Consistentie):** Een transactie brengt de database van de ene geldige staat naar de andere. Regels (constraints) worden niet geschonden.
            *   **Isolation (Isolatie):** Gelijktijdige transacties beïnvloeden elkaar niet op een onvoorspelbare manier. Het lijkt alsof ze na elkaar worden uitgevoerd.
            *   **Durability (Duurzaamheid):** Zodra een transactie succesvol is afgerond (commit), zijn de wijzigingen permanent, zelfs bij een systeemcrash.
            """
        )
    st.write("NoSQL databases hebben vaak een flexibelere benadering van consistentie (soms 'BASE' genoemd: Basically Available, Soft state, Eventually consistent) ten gunste van beschikbaarheid en schaalbaarheid.")

    st.markdown("---")
    # Placeholder voor interactieve oefening of kennisvraag
    # st.subheader("🤔 Test je Kennis!")

def backend_apis_pagina():
    """Pagina over API's (Application Programming Interfaces)."""
    st.header("🔌 API's: De Brug tussen Systemen")
    st.write(
        """
        Je hebt nu gezien hoe de Frontend (wat de gebruiker ziet) en de Backend (de motor) de twee
        hoofdonderdelen van een webapplicatie vormen. Maar hoe communiceren ze met elkaar,
        vooral als ze vaak op compleet verschillende machines draaien (de browser van de gebruiker vs. de server)?
        Het antwoord is: via **API's (Application Programming Interfaces)**.

        Een API fungeert als een **contract** of een set **spelregels** die definieert hoe
        verschillende softwarecomponenten met elkaar kunnen praten. Het is de **interface**
        waardoor ze verzoeken kunnen sturen en antwoorden kunnen ontvangen, zonder dat ze
        precies hoeven te weten *hoe* de andere component intern werkt.
        """
    )

    st.subheader("Analogie: Het Restaurant (Opnieuw)")
    st.write(
        """
        Denk weer aan het restaurant:
        *   **Jij (Frontend):** Je wilt eten bestellen.
        *   **Keuken (Backend):** Bereidt het eten.
        *   **De Menukaart & De Ober (API):** De menukaart (API-documentatie) vertelt je welke gerechten (operaties) beschikbaar zijn en welke informatie (parameters) je moet geven. De ober (API-endpoint/interface) neemt jouw specifieke bestelling (request) aan, geeft deze door aan de keuken, en brengt het bereide gerecht (response) terug.

        Je hoeft niet te weten hoe de keuken precies werkt om eten te bestellen via de ober. De API (ober & menu) vormt de gestandaardiseerde manier van communiceren.
        """
    )

    st.subheader("Waarom zijn API's zo belangrijk?")
    st.markdown(
        """
        *   **Scheiding van Zorgen (Separation of Concerns):** Frontend en Backend teams kunnen onafhankelijk van elkaar werken, zolang ze zich aan het API-contract houden.
        *   **Herbruikbaarheid:** Een backend API kan data en functionaliteit leveren aan meerdere frontends (web, mobiel) of zelfs aan andere systemen/partners.
        *   **Microservices Architectuur:** Moderne applicaties worden vaak opgedeeld in kleinere, onafhankelijke 'microservices'. API's zijn cruciaal voor de communicatie *tussen* deze services.
        *   **Integratie van Externe Diensten:** API's stellen je in staat om functionaliteit van derden te gebruiken (bv. betalingen via Stripe, kaarten via Google Maps, social login).
        """
    )

    st.subheader("Web API's: Communicatie via HTTP")
    st.write(
        """
        In de context van webontwikkeling praten we meestal over **Web API's**. Deze gebruiken het
        **HTTP protocol** (dezelfde basis als voor het ophalen van webpagina's) als communicatiemiddel.
        De Frontend stuurt een HTTP **Request** naar een specifieke URL (een **endpoint**) van de API op de Backend.
        De Backend verwerkt dit request en stuurt een HTTP **Response** terug, vaak met data in **JSON** formaat.

        Er zijn verschillende stijlen of architecturen voor het ontwerpen van web API's:
        """
    )

    # --- REST ---
    st.markdown("**1. REST (Representational State Transfer)**")
    st.write(
        """
        REST is veruit de meest populaire architectuurstijl voor web API's. Het is geen strikt protocol,
        maar een set van principes en beperkingen. Kernideeën zijn:
        *   **Resources:** Alles wordt gezien als een 'resource' (bv. gebruikers, producten, bestellingen). Elke resource heeft een unieke URL (endpoint).
            *   `/users` (collectie van alle gebruikers)
            *   `/users/123` (specifieke gebruiker met ID 123)
        *   **HTTP Methoden (Verbs):** Standaard HTTP methoden worden gebruikt om acties op resources uit te voeren:
            *   `GET`: Haal data op (bv. `GET /users/123` om gebruiker 123 op te halen).
            *   `POST`: Creëer een nieuwe resource (bv. `POST /users` om een nieuwe gebruiker aan te maken, data in request body).
            *   `PUT` / `PATCH`: Werk een bestaande resource bij (bv. `PUT /users/123` om gebruiker 123 volledig te vervangen, `PATCH` voor gedeeltelijke update).
            *   `DELETE`: Verwijder een resource (bv. `DELETE /users/123`).
        *   **Representaties:** Resources worden uitgewisseld in een bepaald formaat, meestal **JSON**. De client kan via headers aangeven welk formaat het accepteert (`Accept` header).
        *   **Stateless:** Elk request van de client naar de server moet alle informatie bevatten die nodig is om het request te begrijpen en te verwerken. De server slaat geen client-specifieke sessie-informatie op tussen requests.
        """
    )
    with st.expander("REST Voorbeeld Interactie (Gebruiker ophalen)"):
        st.code('''
Frontend (Client)                     Backend (Server - REST API)
-----------------                     ---------------------------
1. Stuurt HTTP Request:
   GET /api/users/123
   Host: example.com
   Accept: application/json
                                  --->

                                      2. Ontvangt request.
                                      3. Zoekt gebruiker met ID 123 in database.
                                      4. Formatteert gebruikersdata als JSON.
                                      5. Stuurt HTTP Response:
   <---                                  Status: 200 OK
                                         Content-Type: application/json

                                         {
                                           "id": 123,
                                           "name": "Alice",
                                           "email": "alice@example.com"
                                         }

6. Ontvangt response.
7. Verwerkt JSON data en toont deze in de UI.
        ''', language='text')
    st.markdown(
        """
        *   **Voordelen:** Eenvoudig te begrijpen, schaalbaar, maakt gebruik van bestaande HTTP-infrastructuur (caching, etc.), wijdverspreid.
        *   **Nadelen:** Kan leiden tot *over-fetching* (je krijgt meer data dan nodig) of *under-fetching* (je moet meerdere requests doen om alle benodigde data te verzamelen voor een complexe view).
        """
    )

    # --- GraphQL ---
    st.markdown("**2. GraphQL**")
    st.write(
        """
        GraphQL is een **query language** (vraagtaal) voor API's, ontwikkeld door Facebook als alternatief voor REST.
        Het pakt de problemen van over/under-fetching aan.
        *   **Client Specificeert Data:** De client stuurt een query waarin precies wordt aangegeven welke velden van welke resources nodig zijn.
        *   **Eén Endpoint:** GraphQL API's hebben meestal maar één endpoint (bv. `/graphql`) waar alle queries naartoe worden gestuurd (via POST requests).
        *   **Sterk Getypeerd Schema:** De API definieert een duidelijk schema van beschikbare data types en relaties.
        """
    )
    with st.expander("GraphQL Voorbeeld Query"):
        st.write("Client vraagt specifiek om naam en email van gebruiker 123, en de titels van hun laatste 5 posts:")
        st.code('''
query {
  user(id: "123") {
    name
    email
    posts(last: 5) {
      title
    }
  }
}
        ''', language='graphql')
        st.write("De response bevat alleen de gevraagde data:")
        st.code('''
{
  "data": {
    "user": {
      "name": "Alice",
      "email": "alice@example.com",
      "posts": [
        { "title": "Mijn eerste post" },
        { "title": "GraphQL is cool" }
        // ... tot 5 posts ...
      ]
    }
  }
}
        ''', language='json')
    st.markdown(
        """
        *   **Voordelen:** Efficiënte data-fetching (geen over/under-fetching), sterk getypeerd, introspectief (schema kan opgevraagd worden).
        *   **Nadelen:** Complexer om te implementeren aan de serverkant, caching is lastiger dan bij REST, minder volwassen ecosysteem dan REST.
        """
    )

    # --- Andere Types (Kort) ---
    st.markdown("**Andere API Types (kort genoemd):**")
    st.write(
        """
        *   **RPC (Remote Procedure Call):** Ouder model waarbij de client direct een functie/procedure op de server aanroept (bv. gRPC van Google, gebruikt HTTP/2 en Protocol Buffers voor efficiëntie).
        *   **WebSockets:** Protocol voor bi-directionele, real-time communicatie tussen client en server (goed voor chat, live updates), anders dan het request-response model van HTTP.
        """
    )

    # --- Authenticatie & Autorisatie ---
    st.subheader("Authenticatie & Autorisatie in API's")
    st.write(
        """
        Vaak wil je niet dat *iedereen* zomaar je API kan gebruiken of alle data kan zien/wijzigen.
        *   **Authenticatie:** Wie ben jij? (Identiteit vaststellen).
        *   **Autorisatie:** Wat mag jij doen? (Rechten controleren).

        Veelgebruikte methoden voor API authenticatie:
        """
    )
    with st.expander("Methoden voor API Authenticatie"):
        st.markdown(
            """
            *   **API Keys:** Een simpele geheime sleutel die de client meestuurt in een header. Geschikt voor simpele toegang, maar minder veilig (kan lekken).
            *   **Basic Authentication:** Gebruikersnaam/wachtwoord gecodeerd meegestuurd in de `Authorization` header. **Niet aanbevolen** zonder HTTPS, omdat het makkelijk te onderscheppen is.
            *   **Token-Based Authenticatie (bv. JWT):**
                1.  Client logt in met credentials.
                2.  Server valideert en stuurt een **token** (bv. een JSON Web Token - JWT) terug.
                3.  Client stuurt dit token mee in de `Authorization: Bearer <token>` header bij elk volgend request.
                4.  Server valideert het token (vaak zonder database lookup nodig) om de gebruiker te authenticeren. Tokens hebben meestal een beperkte geldigheidsduur.
            *   **OAuth 2.0:** Een complexer protocol, vooral gebruikt voor **gedelegeerde autorisatie**. Hiermee kan een gebruiker een applicatie toestemming geven om namens hem toegang te krijgen tot data op een andere service (bv. "Login met Google" of een app toegang geven tot je Twitter feed), zonder je wachtwoord aan die app te geven.
            """
        )

    # --- Design Best Practices ---
    st.subheader("API Design Best Practices")
    st.write("Een goed ontworpen API is makkelijk te begrijpen, te gebruiken en te onderhouden:")
    with st.expander("Tips voor Goed API Ontwerp"):
        st.markdown(
            """
            *   **Consistentie:** Gebruik consistente naamgeving voor endpoints, parameters en response structuren.
            *   **Gebruik Standaard HTTP Methoden correct (voor REST):** Gebruik `GET` voor ophalen, `POST` voor aanmaken, etc.
            *   **Gebruik Standaard HTTP Status Codes:** Geef duidelijke feedback over het resultaat van een request (bv. `200 OK`, `201 Created`, `400 Bad Request`, `401 Unauthorized`, `404 Not Found`, `500 Internal Server Error`).
            *   **Versioning:** Plan voor toekomstige wijzigingen. Zet versie-informatie in de URL (bv. `/api/v1/users`) of een header.
            *   **Documentatie:** Zorg voor duidelijke en up-to-date documentatie (bv. met tools als Swagger/OpenAPI). Dit is het 'contract' voor de gebruikers van je API.
            *   **Beveiliging:** Denk altijd aan beveiliging (authenticatie, autorisatie, input validatie, rate limiting).
            *   **Performance:** Optimaliseer queries en processen om de API snel te laten reageren.
            """
        )

    st.info("Het ontwerpen en bouwen van goede API's is een essentieel onderdeel van moderne backend ontwikkeling, dat de basis legt voor flexibele en schaalbare applicaties.")

def backend_servers_deployment_pagina():
    """Pagina over Servers & Deployment."""
    st.header("🚀 Servers & Deployment: Je Applicatie Live Brengen")
    st.write(
        """
        Je hebt je fantastische applicatie gebouwd – de frontend ziet er gelikt uit, de backend logica werkt perfect.
        Maar nu draait alles nog lokaal op jouw computer. Hoe zorg je ervoor dat de rest van de wereld jouw applicatie
        kan gebruiken via het internet? Dat is waar **servers** en **deployment** om de hoek komen kijken.

        **Deployment** is het proces van het nemen van je ontwikkelde software (code, bestanden, configuraties) en
        deze te plaatsen op een **server** zodat deze toegankelijk en bruikbaar wordt voor je eindgebruikers.
        """
    )

    st.subheader("Wat is een Server?")
    st.write(
        """
        In de context van webapplicaties is een server in essentie een **krachtige computer** die (bijna) altijd aan staat
        en verbonden is met het internet. Zijn primaire taak is om **verzoeken** (requests) van clients (zoals browsers)
        te ontvangen, deze te verwerken (vaak door je backend code uit te voeren), en een **antwoord** (response) terug
        te sturen (bv. HTML, CSS, JS voor de frontend, of JSON data van een API).

        *Analogie:* Denk aan een bibliotheek die 24/7 open is. De server is het gebouw en de bibliothecarissen
        die klaarstaan om verzoeken voor boeken (webpagina's/data) te verwerken en uit te lenen.

        Servers kunnen verschillende vormen aannemen:
        """
    )
    st.markdown(
        """
        *   **Fysieke Server:** Een daadwerkelijke machine in een datacenter (of zelfs in een kantoorkast, hoewel minder gebruikelijk voor publieke apps). Je bent zelf verantwoordelijk voor hardware, onderhoud, koeling, etc.
        *   **Virtuele Machine (VM):** Softwarematige emulatie van een fysieke computer die draait op een fysieke host. Meerdere VM's kunnen op één fysieke machine draaien. Biedt meer flexibiliteit dan fysieke servers. Aanbieders zoals DigitalOcean, Linode, Vultr bieden VM's aan.
        *   **Cloud Server/Instance:** VM's die draaien op de infrastructuur van grote cloud providers zoals AWS (EC2), Google Cloud (Compute Engine) of Microsoft Azure (Virtual Machines). Biedt enorme schaalbaarheid, flexibiliteit en een breed scala aan beheerde diensten.
        *   **Serverless Computing:** Een abstracter model waarbij je je code uitvoert zonder je zorgen te hoeven maken over de onderliggende servers. De cloud provider beheert de infrastructuur volledig en schaalt automatisch. Voorbeelden: AWS Lambda, Google Cloud Functions, Azure Functions.
        """
    )

    st.subheader("De Rol van Webservers (Software)")
    st.write(
        """
        Naast de fysieke/virtuele machine heb je ook **webserver software** nodig die luistert naar inkomende HTTP-verzoeken
        en deze correct doorstuurt of afhandelt. Twee zeer populaire keuzes zijn:
        *   **Nginx (uitgesproken als 'Engine-X'):** Bekend om zijn hoge performance, stabiliteit, en efficiëntie, vooral bij het afhandelen van veel gelijktijdige verbindingen en statische bestanden. Wordt vaak gebruikt als **reverse proxy**, **load balancer** en voor het serveren van statische content.
        *   **Apache HTTP Server:** Een van de oudste en meest gebruikte webservers. Zeer flexibel en configureerbaar via `.htaccess` bestanden.

        Vaak zie je een setup waarbij Nginx fungeert als de 'voordeur' (reverse proxy). Het vangt alle requests op, serveert snel statische bestanden (CSS, JS, afbeeldingen), en stuurt dynamische requests (die je backend code vereisen) door naar je applicatieserver (bv. een Python server die draait met Gunicorn/uWSGI, een Node.js server, een Java Tomcat server, etc.).
        """
    )
    with st.expander("Definities: Webserver Termen"):
        st.markdown("**Webserver Software:** Programma dat HTTP(S) requests afhandelt, zoals Nginx of Apache.")
        st.markdown("**Applicatieserver:** Software die de backend code van je applicatie uitvoert (bv. Gunicorn voor Python, Tomcat voor Java). Wordt vaak *achter* een webserver geplaatst.")
        st.markdown("**Reverse Proxy:** Een server (vaak Nginx) die requests van clients ontvangt en doorstuurt naar een of meer backend/applicatieservers. Verbergt de backend infrastructuur en kan extra taken uitvoeren zoals load balancing, SSL encryptie, en caching.")
        st.markdown("**Load Balancer:** Verdeelt inkomende requests over meerdere backend servers om de werklast te spreiden en de beschikbaarheid te verhogen.")

    st.subheader("Cloud Platforms (IaaS, PaaS, SaaS)")
    st.write(
        """
        Moderne deployment gebeurt steeds vaker op **cloud platforms**. Deze bieden verschillende servicemodellen:
        *   **IaaS (Infrastructure as a Service):** Je huurt de basis infrastructuur (VM's, opslag, netwerk). Je bent zelf verantwoordelijk voor het besturingssysteem, middleware en de applicatie. (Bv. AWS EC2, Google Compute Engine, Azure VMs).
        *   **PaaS (Platform as a Service):** Je beheert alleen je applicatiecode en data. De provider beheert het besturingssysteem, middleware, schaling, en infrastructuur. (Bv. Heroku, Google App Engine, AWS Elastic Beanstalk, Azure App Service, Streamlit Community Cloud!).
        *   **SaaS (Software as a Service):** Je gebruikt kant-en-klare software via het internet. Je beheert niets van de onderliggende infrastructuur of applicatie. (Bv. Gmail, Dropbox, Salesforce).

        PaaS-oplossingen maken deployment vaak veel eenvoudiger, omdat veel van de complexe infrastructuurtaken worden overgenomen.
        """
    )

    st.subheader("Containers: Docker & Kubernetes")
    st.write(
        """
        Een revolutionaire technologie in deployment is **containerisatie**, met **Docker** als de populairste tool.
        *   **Docker:** Stelt je in staat om je applicatie en *al* zijn afhankelijkheden (bibliotheken, runtime, systeentools) samen te verpakken in een gestandaardiseerde eenheid: een **container image**. Deze image kan vervolgens consistent worden uitgevoerd op elke machine waarop Docker draait (jouw laptop, een testserver, een cloud VM).
            *   *Voordeel:* Lost het "het werkt wel op mijn machine" probleem op. Zorgt voor consistente omgevingen van ontwikkeling tot productie. Containers zijn lichtgewicht en starten snel.
        *   **Kubernetes (K8s):** Als je veel containers hebt draaien (bv. voor een microservices architectuur), heb je een tool nodig om deze te **beheren en orkestreren**: automatisch deployen, schalen, load balancing, health checks, rollbacks, etc. Kubernetes is de de-facto standaard voor container orchestratie. Cloud providers bieden beheerde Kubernetes diensten (AWS EKS, Google GKE, Azure AKS).

        *Analogie:* Een Docker container is als een scheepscontainer: de inhoud (je app en dependencies) is netjes verpakt, en de buitenkant (de container) is gestandaardiseerd, waardoor hij makkelijk te verplaatsen en te beheren is op verschillende schepen en kranen (verschillende machines/omgevingen). Kubernetes is de havenmeester die bepaalt welke container waarheen gaat en hoeveel kranen er nodig zijn.
        """
    )
    with st.expander("Definities: Container Termen"):
        st.markdown("**Container Image:** Een lichtgewicht, standalone, uitvoerbaar pakket dat alles bevat wat nodig is om een stuk software te draaien: code, runtime, systeemtools, systeembibliotheken, instellingen.")
        st.markdown("**Container:** Een draaiende instantie van een container image.")
        st.markdown("**Dockerfile:** Een tekstbestand dat de instructies bevat om een Docker image te bouwen.")
        st.markdown("**Container Orchestration:** Het automatiseren van de deployment, schaling, en beheer van containerized applicaties.")

    st.subheader("Deployment Strategieën")
    st.write("Hoe breng je een nieuwe versie van je app live zonder (veel) downtime of problemen?")
    with st.expander("Veelgebruikte Strategieën"):
        st.markdown(
            """
            *   **Big Bang / Recreate:** Stop de oude versie, deploy de nieuwe. Simpel, maar veroorzaakt downtime.
            *   **Rolling Update:** Vervang servers/instances één voor één of in batches door de nieuwe versie. Minder downtime, maar tijdelijk draaien er twee versies naast elkaar.
            *   **Blue/Green Deployment:** Zet een identieke 'groene' omgeving op naast de live 'blauwe' omgeving. Test de groene omgeving. Schakel vervolgens de routering om van blauw naar groen. Bij problemen kun je snel terugschakelen. Vereist dubbele infrastructuur.
            *   **Canary Release:** Rol de nieuwe versie uit naar een klein percentage van de gebruikers. Monitor de resultaten. Als alles goed gaat, rol verder uit. Als er problemen zijn, rol terug. Minimaliseert risico.
            """
        )

    st.subheader("CI/CD: Automatisering is Koning")
    st.write(
        """
        Moderne softwareontwikkeling streeft naar **snelle en betrouwbare** releases. **CI/CD** is een set praktijken en tools die dit automatiseren:
        *   **Continuous Integration (CI):** Ontwikkelaars voegen hun code regelmatig (minstens dagelijks) samen in een gedeelde repository (bv. via Git). Elke samenvoeging triggert een **automatische build** en **automatische tests**. Dit helpt om integratieproblemen vroegtijdig te ontdekken.
        *   **Continuous Delivery (CD):** Gaat een stap verder dan CI. Na een succesvolle build en test wordt de code **automatisch** klaargezet voor deployment naar een (test- of productie-) omgeving. De daadwerkelijke deployment naar productie vereist vaak nog een handmatige goedkeuring.
        *   **Continuous Deployment (CD - andere betekenis):** De meest geavanceerde vorm. Elke wijziging die alle CI-stappen succesvol doorloopt, wordt **automatisch** gedeployed naar productie.

        Tools zoals Jenkins, GitLab CI/CD, GitHub Actions, CircleCI helpen bij het implementeren van CI/CD pipelines.
        """
    )
    st.info(
        """
        Servers en deployment vormen de brug tussen ontwikkeling en de eindgebruiker. Het kiezen van de juiste
        serverinfrastructuur, deployment strategie en het automatiseren via containers en CI/CD zijn cruciaal
        voor het leveren van betrouwbare en schaalbare applicaties.
        """
    )
# --- End of Function ---

# Placeholder aanroepen (nog niet functioneel)
# laad_voortgang() # Laad voortgang aan het begin (hypothetisch)
# ... aan het einde van interactieve elementen:
# sla_voortgang_op() # Sla voortgang op na interactie (hypothetisch)

# --- Extra informatie in de sidebar ---
st.sidebar.markdown("---") # Voegt een horizontale lijn toe
st.sidebar.info(
    """
    **Over deze app:**
    Gebouwd met [Streamlit](https://streamlit.io).
    Broncode beschikbaar op [GitHub](link-naar-jouw-repo) (TODO: link toevoegen).
    """
)
# TODO: Vervang 'link-naar-jouw-repo' door de daadwerkelijke link zodra je het op GitHub zet.

# --- Hoe de app te draaien (Instructie voor de gebruiker) ---
# Dit deel is commentaar en wordt niet getoond in de app, maar is voor jou:
# 1. Zorg dat je Python hebt geïnstalleerd.
# 2. Open een terminal of command prompt.
# 3. Navigeer naar de map waar dit bestand (`app.py`) en `requirements.txt` staan.
# 4. Installeer de benodigde bibliotheek: `pip install -r requirements.txt`
# 5. Start de app: `streamlit run app.py`
#    Er opent automatisch een tabblad in je browser met de app. 
#    Er opent automatisch een tabblad in je browser met de app. 

