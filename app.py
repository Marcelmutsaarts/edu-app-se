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

# --- Placeholder voor Data Opslag ---
# Hier kunnen we later functies toevoegen om bijvoorbeeld gebruikersvoortgang
# op te slaan en te laden. Streamlit heeft 'Session State' voor tijdelijke opslag
# binnen een sessie. Voor permanente opslag zouden we bestanden of een database gebruiken.
# Voorbeeld (nog niet functioneel):
# def laad_voortgang():
#     if 'user_progress' not in st.session_state:
#         st.session_state.user_progress = {} # Initialiseer als leeg dictionary
#     # Hier zou code komen om data uit een bestand/db te laden
#     pass
#
# def sla_voortgang_op():
#     # Hier zou code komen om st.session_state.user_progress op te slaan
#     pass

# --- Navigatie in Sidebar ---
# st.sidebar creëert een zijbalk. Elementen die hieraan worden toegevoegd,
# verschijnen aan de linkerkant van de app.

st.sidebar.title("Navigatie")
# st.sidebar.radio maakt een keuzemenu in de zijbalk.
# Het eerste argument is een label, het tweede is een lijst met opties.
# De gekozen optie wordt opgeslagen in de variabele 'pagina_keuze'.
pagina_keuze = st.sidebar.radio(
    "Kies een onderwerp:",
    [
        "Wat is Software Engineering?",
        "De Levenscyclus van Software (Overzicht)",
        "Fase 1: Eisen Verzamelen",
        "Fase 2: Ontwerp",
        "Fase 3: Implementatie",
        "Fase 4: Testen",
        "Fase 5: Deployment",
        "Fase 6: Onderhoud",
        "Ontwikkelmethodes (Hoe werken we?)",
        "Frontend & Backend (De Twee Kanten)",
        "Basis van Streamlit (App Bouwen)",        # Nieuwe optie
        "Basis van Git & GitHub (Code Beheren & Delen)" # Nieuwe optie
    ]
)

# --- Hoofdlogica: Toon de geselecteerde pagina ---
# Hier gebruiken we if/elif/else statements om te bepalen welke functie
# (en dus welke pagina-inhoud) moet worden aangeroepen op basis van
# de keuze van de gebruiker in de sidebar ('pagina_keuze').

if pagina_keuze == "Wat is Software Engineering?":
    introductie_pagina()
elif pagina_keuze == "De Levenscyclus van Software (Overzicht)":
    levenscyclus_overzicht_pagina()
elif pagina_keuze == "Fase 1: Eisen Verzamelen":
    fase_1_eisen_pagina()
elif pagina_keuze == "Fase 2: Ontwerp":
    fase_2_ontwerp_pagina()
elif pagina_keuze == "Fase 3: Implementatie":
    fase_3_implementatie_pagina()
elif pagina_keuze == "Fase 4: Testen":
    fase_4_testen_pagina()
elif pagina_keuze == "Fase 5: Deployment":
    fase_5_deployment_pagina()
elif pagina_keuze == "Fase 6: Onderhoud":
    fase_6_onderhoud_pagina()
elif pagina_keuze == "Ontwikkelmethodes (Hoe werken we?)":
    ontwikkelmethodes_pagina()
elif pagina_keuze == "Frontend & Backend (De Twee Kanten)":
    frontend_backend_pagina()
elif pagina_keuze == "Basis van Streamlit (App Bouwen)":     # Nieuwe conditie
    streamlit_basis_pagina()
elif pagina_keuze == "Basis van Git & GitHub (Code Beheren & Delen)": # Nieuwe conditie
    git_github_basis_pagina()

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